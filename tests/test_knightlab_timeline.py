from datasette.app import Datasette

from datetime import datetime, timedelta
from unittest import TestCase
import pytest
import sqlite_utils
import textwrap
import yaml

@pytest.mark.asyncio
async def test_plugin_is_installed():
    datasette = Datasette(memory=True)
    response = await datasette.client.get("/-/plugins.json")
    assert response.status_code == 200
    installed_plugins = {p["name"] for p in response.json()}
    assert "datasette-knightlab-timeline" in installed_plugins

@pytest.mark.asyncio
async def test_timeline_route_reachable():
    datasette = Datasette(memory=True)
    response = await datasette.client.get("/-/timeline")
    assert response.status_code == 200
    assert 'id=\'timeline-embed\'' in response.text

@pytest.mark.asyncio
async def test_timeline_json_reachable(ds):
    response = await ds.client.get("/-/timeline.json")
    assert response.status_code == 200

    payload = response.json()
    assert len(payload['events']) > 0

@pytest.mark.asyncio
async def test_timeline_json_conforms_to_contract(ds):
    response = await ds.client.get("/-/timeline.json")
    assert response.status_code == 200

    payload = response.json()
    assert len(payload['events']) > 0

    today = datetime.now()
    expected_dict = {
        'year': today.year,
        'month': today.month,
        'day': today.day
    }
    slide = payload['events'][0]
    TestCase().assertDictEqual(expected_dict, slide['start_date'])

@pytest.fixture
def ds(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("dbs") / "timeline-test.db"
    other_db_path = tmp_path_factory.mktemp("dbs") / "another-timeline-test.db"
    for path in [db_path, other_db_path]:
        database = sqlite_utils.Database(path)

        today = datetime.now()
        yesterday = today - timedelta(days=1)

        # Create a simple timeline table for test data
        database["timeline"].insert_all([{
            "id": 1,
            "start_date": today.isoformat(),
            "text": "High temp: ",
            "text_column": "89°F"
        }, {
            "id": 2,
            "start_date": yesterday.isoformat(),
            "text": "High temp: ",
            "text_column": "95°F"
        }])

    return Datasette(
        [str(db_path), str(other_db_path)],
        metadata=METADATA,
    )

METADATA = yaml.safe_load(textwrap.dedent(
        """
    plugins:
        datasette-knightlab-timeline:
            databases:
                - database: timeline-test
                  query: SELECT * FROM timeline;
                  text: text-goes-here
                  text_column: text_column
                - database: another-timeline-test
                  query: SELECT * FROM timeline;
                  text: text-goes-here
                  text_column: text_column
    """
    ))
