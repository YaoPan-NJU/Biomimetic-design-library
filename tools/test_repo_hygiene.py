#!/usr/bin/env python3
"""Regression tests for repository hygiene rules."""

import os
import tempfile
import unittest
from pathlib import Path

from check_repo_hygiene import check_root_directory


class RootDirectoryRulesTest(unittest.TestCase):
    def test_allows_claude_project_instructions(self):
        original_cwd = os.getcwd()
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                Path(temp_dir, "README.md").touch()
                Path(temp_dir, "CLAUDE.md").touch()
                os.chdir(temp_dir)

                self.assertEqual([], check_root_directory())
        finally:
            os.chdir(original_cwd)


if __name__ == "__main__":
    unittest.main()
