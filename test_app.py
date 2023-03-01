from app import text_summary


def test_summarizer(text):
    summary = text_summary(text)
    assert len(summary) > 0
