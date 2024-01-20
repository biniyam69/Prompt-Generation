import pytest
import os, sys, dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.generate_prompts import GeneratePrompts

def test_generate_prompts():
    initial_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. {Context} {Question}"
    context = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
    question = "What is human life expectancy in the United States?"
    assert GeneratePrompts.generate_prompts(initial_prompt, context, question) == "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. What is human life expectancy in the United States? The average life expectancy in the United States is 78.6 years."

test_generate_prompts()