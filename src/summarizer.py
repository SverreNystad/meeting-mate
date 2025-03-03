from langchain_ollama import ChatOllama

llm = ChatOllama(model="mistral")


def summarize(text: str):
    prompt = f"Summarize the following meeting:\n\n{text}"
    return llm.invoke(prompt)
