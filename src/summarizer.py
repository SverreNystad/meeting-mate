from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

llm = ChatOllama(model="mistral")


def summarize(text: str) -> AIMessage:
    prompt = f"Summarize the following meeting:\n\n{text}"
    return llm.invoke(prompt)


