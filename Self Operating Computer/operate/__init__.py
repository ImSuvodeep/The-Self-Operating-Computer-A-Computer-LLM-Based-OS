"""
Self-Operating Computer (AIOS) - Operate Module
================================================

A comprehensive AI-powered module that orchestrates desktop automation 
with multi-model LLM support (OpenAI, Google, Anthropic).

Submodules:
-----------
- config: Configuration management for API keys and settings
- main: CLI entry point and argument parsing
- operate: Core orchestration engine
- exceptions: Custom exception classes
- models: Prompt templates and API interfaces
- utils: Utility functions for OS interaction, vision, and styling

Example:
    Basic usage::

        from operate.operate import main
        main(model="gpt-4-with-ocr", terminal_prompt="Visit GitHub.com")

    Or via command line::

        $ operate --model gpt-4-vision --prompt "Take a screenshot"

Version: 1.4.5
License: Apache 2.0
"""

__version__ = "1.4.5"
__author__ = "ImSuvodeep"
__license__ = "Apache 2.0"

from operate.config import Config
from operate.exceptions import ModelNotRecognizedException

__all__ = [
    "Config",
    "ModelNotRecognizedException",
]
