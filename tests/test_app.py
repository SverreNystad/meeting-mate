from langchain_core.messages import AIMessage
from src.summarizer import summarize


def test_summarize():
    text = "Meeting notes for Q1"
    result = summarize(text)

    assert result is not None
    assert isinstance(result, AIMessage)
    assert len(result.content) > 0
