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

@pytest.fixture
def text():
    return 'test'
