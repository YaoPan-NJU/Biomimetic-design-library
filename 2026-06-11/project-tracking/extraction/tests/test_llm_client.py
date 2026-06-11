# extraction/tests/test_llm_client.py
import pytest
from unittest.mock import patch, MagicMock
from llm_client import LLMClient


class TestLLMClient:
    def test_init_loads_provider_config(self):
        client = LLMClient(provider="coding_plan")
        assert client.model == "qwen3.6-plus"
        assert "coding.dashscope" in client.base_url

    def test_route_task_returns_correct_provider(self):
        assert LLMClient.route_task("coarse_scan") == "coding_plan"
        assert LLMClient.route_task("deep_read") == "coding_plan"  # now load-balanced list
        assert LLMClient.route_task("multimodal_extract") == "mimo"
        assert LLMClient.route_task("weight_assign") == "dashscope"  # still single

    def test_chat_calls_openai_api(self):
        client = LLMClient(provider="coding_plan")
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = '{"result": "ok"}'
        with patch.object(client.client.chat.completions, "create", return_value=mock_response) as mock_create:
            result = client.chat("Extract data from this abstract: ...")
            mock_create.assert_called_once()
            assert result == '{"result": "ok"}'

    def test_chat_json_parses_structured_output(self):
        client = LLMClient(provider="coding_plan")
        with patch.object(client, "chat", return_value='{"pollutants": ["Pb", "Cd"], "qmax": "120 mg/g"}'):
            result = client.chat_json("test prompt")
            assert result == {"pollutants": ["Pb", "Cd"], "qmax": "120 mg/g"}

    def test_chat_json_handles_markdown_fences(self):
        client = LLMClient(provider="coding_plan")
        raw = '```json\n{"key": "value"}\n```'
        with patch.object(client, "chat", return_value=raw):
            result = client.chat_json("test prompt")
            assert result == {"key": "value"}

    def test_from_task_type_creates_routed_client(self):
        # biomimetic_extract is now load-balanced across 3 providers
        client = LLMClient.from_task_type("biomimetic_extract")
        assert client.provider in ["coding_plan", "dashscope", "mimo"]
        # weight_assign is still single-provider
        client2 = LLMClient.from_task_type("weight_assign")
        assert client2.provider == "dashscope"
        assert client2.model == "qwen3.7-max"

    def test_exclude_provider_for_retry(self):
        # When excluding a provider, should pick from remaining
        client = LLMClient.from_task_type("coarse_scan", exclude_provider="coding_plan")
        assert client.provider in ["dashscope", "mimo"]
