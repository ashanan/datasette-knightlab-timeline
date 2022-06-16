from datetime import datetime
import pytest

from datasette_knightlab_timeline.timeline_slide import TimelineSlide

@pytest.mark.asyncio
async def test_set_start_date(text):
    today = datetime.now()
    slide = TimelineSlide({'start_date': today, 'text': text})
    assert slide.start_date == today

@pytest.mark.asyncio
async def test_set_text(text):
    today = datetime.now()
    slide = TimelineSlide({'start_date': today, 'text': text})
    assert slide.text == [text]

@pytest.mark.asyncio
async def test_add_text(text):
    today = datetime.now()
    slide = TimelineSlide({'start_date': today, 'text': text})
    addedText = "test text added in test_add_text"
    slide.addText(addedText)
    assert slide.text == [text, addedText]

@pytest.fixture
def text():
    return 'test'
