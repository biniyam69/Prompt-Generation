import langchain
import openai
from openai import OpenAI
from langchain_community import document_loaders
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
import os, sys
import dotenv
from dotenv import load_dotenv
from utils.load_data import embed_context

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from load_data import embed_context

load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)


class GeneratePrompts():
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def generate_prompts(initial_prompt, context, question):
        """Return the completion of the prompt."""
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": initial_prompt.replace("{Context}", context).replace("{Question}", question)}
        ]

        params = {
            "messages": messages,
            "model": "gpt-3.5-turbo",
            "max_tokens": 500,
            "temperature": 0,
            "stop": None,
            "seed": 123,
            "logprobs": None
        }

        completion = client.chat.completions.create(**params)
        # return completion.choices[0].message['content']
    
        generated_content = completion['choices'][0]['message']

        return generated_content
    
    # def get_completion(
    #     messages: list[dict[str, str]],
    #     model: str = env_manager['vectordb_keys']['VECTORDB_MODEL'],
    #     max_tokens=500,
    #     temperature=0,
    #     stop=None,
    #     seed=123,
    #     tools=None,
    #     logprobs=None,
    #     top_logprobs=None,
    # ) -> str:
    #     """Return the completion of the prompt.
    #     @parameter messages: list of dictionaries with keys 'role' and 'content'.
    #     @parameter model: the model to use for completion. Defaults to 'davinci'.
    #     @parameter max_tokens: max tokens to use for each prompt completion.
    #     @parameter temperature: the higher the temperature, the crazier the text
    #     @parameter stop: token at which text generation is stopped
    #     @parameter seed: random seed for text generation
    #     @parameter tools: list of tools to use for post-processing the output.
    #     @parameter logprobs: whether to return log probabilities of the output tokens or not.
    #     @returns completion: the completion of the prompt.
    #     """

    #     params = {
    #         "model": model,
    #         "messages": messages,
    #         "max_tokens": max_tokens,
    #         "temperature": temperature,
    #         "stop": stop,
    #         "seed": seed,
    #         "logprobs": logprobs,
    #         "top_logprobs": top_logprobs,
    #     }
    #     if tools:
    #         params["tools"] = tools

    #     completion = client.chat.completions.create(**params)
    #     return completion