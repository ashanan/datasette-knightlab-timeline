from datetime import datetime
import pytest

from datasette_knightlab_timeline.timeline_slide import TimelineSlide

@pytest.mark.asyncio
async def test_set_start_date():
    today = datetime.now()
    slide = TimelineSlide({'start_date': today, 'text': ''})
    assert slide.start_date == today
