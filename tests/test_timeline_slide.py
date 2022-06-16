from datetime import datetime
import json
import pytest

from datasette_knightlab_timeline.timeline_slide import TimelineSlide

@pytest.mark.asyncio
async def test_set_start_date(today, slide):
    assert slide.start_date == today

@pytest.mark.asyncio
async def test_set_text(text, slide):
    assert slide.text == [text]

@pytest.mark.asyncio
async def test_add_text(text, slide):
    addedText = "test text added in test_add_text"
    slide.addText(addedText)
    assert slide.text == [text, addedText]

@pytest.mark.asyncio
async def test_to_json(text, today, slide):
    expected_json = {
                        'start_date': {
                            'year': today.year,
                            'month': today.month,
                            'day': today.day
                        },
                        'text': {
                            'text': text
                        }
                    }
    assert slide.toJson() == json.dumps(expected_json)

@pytest.fixture
def text():
    return 'test'

@pytest.fixture
def today():
    return datetime.now()

@pytest.fixture
def slide(today, text):
    return TimelineSlide({'start_date': today, 'text': text})
