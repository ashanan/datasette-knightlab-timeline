from datasette import hookimpl, Response

@hookimpl
def extra_js_urls(database, table, columns, view_name, datasette):
    return [
        {
            "url": datasette.urls.static_plugins(
                "datasette-knightlab-timeline", "timeline.js"
            ),
            "module": True,
        },
        {
            "url": "https://cdn.knightlab.com/libs/timeline3/latest/js/timeline.js"
        }
    ]

@hookimpl
def extra_css_urls():
    return [
        {
            "url": "https://cdn.knightlab.com/libs/timeline3/latest/css/timeline.css"
        }
    ]

@hookimpl
def menu_links(datasette):
    return [
        {"href": datasette.urls.path("/-/timeline"), "label": "Timeline"}
    ]

@hookimpl
def register_routes():
    return [
        (r"^/-/(timeline|timeline.json)$", timeline)
    ]

async def timeline(request, datasette):
    if request.path == '/-/timeline.json':
        return Response.json({
            'events': await build_events(datasette),
            'title': {
                'text': {'text': 'Hardcoded timeline!'}
            }
        })
    else:
        return Response.html(
            await datasette.render_template(
                "timeline.html",
                {
                    "text": "template test"
                },
                request=request,
            )
        )

async def build_events(datasette):
    plugin_config = datasette.plugin_config(
        "datasette-knightlab-timeline"
    )
    database = datasette.databases[plugin_config['database']]

    results = await database.execute(plugin_config['query'])
    events_array = []
    for row in results:
        text = '%s%s' %(plugin_config['text'], row[plugin_config['text_column']])
        events_array.append({
            'start_date': {
                'year': 2022
            },
            'text': {
                'text': text
            }
        })

    return events_array
