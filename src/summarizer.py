from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage

llm = ChatOllama(model="mistral")


def summarize(text: str) -> BaseMessage:
    prompt = f"Summarize the following meeting:\n\n{text}"
    return llm.invoke(prompt)
