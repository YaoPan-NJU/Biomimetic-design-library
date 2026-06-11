# extraction/llm_client.py
"""Unified LLM client supporting three API providers via OpenAI-compatible interface.

Supports load-balanced routing: when a task type maps to a list of providers,
calls are distributed round-robin across them for maximum throughput.
"""

from __future__ import annotations

import json
import re
import threading
from openai import OpenAI
from config import PROVIDERS, MODEL_ROUTING


class LLMClient:
    """A unified client for calling LLMs across three providers."""

    # Thread-safe round-robin counters per task type
    _rr_counters: dict[str, int] = {}
    _rr_lock = threading.Lock()

    def __init__(self, provider: str):
        if provider not in PROVIDERS:
            raise ValueError(f"Unknown provider: {provider}. Must be one of {list(PROVIDERS.keys())}")

        self.provider = provider
        cfg = PROVIDERS[provider]
        self.model = cfg["model"]
        self.base_url = cfg["base_url"]

        api_key = cfg["api_key"] or "sk-placeholder"

        self.client = OpenAI(
            api_key=api_key,
            base_url=cfg["base_url"],
        )

    @classmethod
    def from_task_type(cls, task_type: str, exclude_provider: str = None) -> "LLMClient":
        """Create a client for a task type. If routing is a list, round-robin across providers.

        Args:
            task_type: The task type to route.
            exclude_provider: If set, skip this provider (useful for 429 retry to switch APIs).
        """
        if task_type not in MODEL_ROUTING:
            raise ValueError(f"Unknown task type: {task_type}. Must be one of {list(MODEL_ROUTING.keys())}")

        routing = MODEL_ROUTING[task_type]

        if isinstance(routing, list):
            candidates = [p for p in routing if p != exclude_provider] or routing
            with cls._rr_lock:
                idx = cls._rr_counters.get(task_type, 0)
                cls._rr_counters[task_type] = idx + 1
            provider = candidates[idx % len(candidates)]
        else:
            provider = routing

        return cls(provider=provider)

    @staticmethod
    def route_task(task_type: str) -> str:
        """Return the primary provider name for a task type."""
        if task_type not in MODEL_ROUTING:
            raise ValueError(f"Unknown task type: {task_type}")
        routing = MODEL_ROUTING[task_type]
        if isinstance(routing, list):
            return routing[0]
        return routing

    def chat(
        self,
        prompt: str,
        system_prompt: str = "You are a scientific literature analysis assistant. Respond in the language of the input.",
        temperature: float = 0.1,
        max_tokens: int = 4096,
    ) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    def chat_json(
        self,
        prompt: str,
        system_prompt: str = "You are a scientific literature analysis assistant. Always respond with valid JSON.",
        temperature: float = 0.1,
        max_tokens: int = 4096,
    ) -> dict:
        raw = self.chat(prompt, system_prompt=system_prompt, temperature=temperature, max_tokens=max_tokens)
        cleaned = re.sub(r"```(?:json)?\s*\n?", "", raw).strip()
        return json.loads(cleaned)
