from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_community.chat_models import ChatOllama
from prompt import input_prompt
from dotenv import load_dotenv
import os

load_dotenv()

class LLM():
    def __init__(self, provider_name, model_name ):
        self.provider_name = provider_name
        self.model_name = model_name

        self.llm = self.initialize_llm()

    def initialize_llm(self):
        if self.provider_name == "Groq":
            GROQ_API_KEY = os.getenv("GROQ_API_KEY")
            return ChatGroq(model=self.model_name, temperature=0).with_structured_output(method="json_mode")
        elif self.provider_name == "OpenAI":
            OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
            return ChatOpenAI(model=self.model_name, temperature=0).with_structured_output({"type": "json"})
        elif self.provider_name == "Anthropic":
            ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
            return ChatAnthropic(model=self.model_name, temperature=0).with_structured_output({"type": "json"})
        elif self.provider_name == "Ollama":
            return ChatOllama(model=self.model_name, temperature=0)
        else:
            raise ValueError(f"Unsupported provider: {self.provider_name}")

    def generate_response(self, user_input):
        prompt = input_prompt(user_input)
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        response = self.llm.invoke(messages)
        return response

    def test_connection(self):
        try:
            test_prompt = "Hello, how are you?"
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": test_prompt}
            ]
            self.llm.invoke(messages)
            return True
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False
