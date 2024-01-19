import langchain
import openai
from langchain_community import document_loaders
from langchain_community import vectorstores
from langchain.embeddings import OpenAIEmbeddings
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = ' '

class GeneratePrompts():
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def generate_prompts(self):
        pass