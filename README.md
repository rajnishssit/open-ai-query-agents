# open-ai-query-agents

Connecting to the LLM Ecosystem
This notebook demonstrates how to programmatically connect to the world's leading Large Language Models (LLMs). We cover two distinct strategies for integration:

Direct Provider SDKs: Connecting directly to OpenAI, Anthropic, and Google using their official Python libraries.

Unified Aggregators: Using OpenRouter to access any model (Llama 3, Mistral, Claude, GPT) using a single, standardized API format.

This notebook requires you to set the keys in the colab secrets denoted by the key icon on the left sidebar of your screen.

You'll need to set the following API KEYS using Colab Secrets

OPENAI_API_KEY
OPENROUTER_API_KEY
Strategy 1: The "Siloed" Approach (Official SDKs)
Each major AI lab releases its own Python software development kit (SDK).

OpenAI (openai)

The Standard: OpenAI's format (chat.completions.create) has effectively become the industry standard.

Key Features: Simple message history list [{"role": "user", "content": "..."}].

Best For: Accessing GPT-4o, GPT-4-Turbo, and legacy models directly.
