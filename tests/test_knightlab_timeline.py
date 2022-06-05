from datasette.app import Datasette
import pytest


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
