import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
    model_provider="openai",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
)
