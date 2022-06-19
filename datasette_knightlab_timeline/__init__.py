from datasette import hookimpl, Response
import dateutil.parser

from datasette_knightlab_timeline.timeline_slide import TimelineSlide

@hookimpl
def extra_js_urls(datasette):
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
    databases = plugin_config['databases']
    slides_by_day = {}
    for database_config in databases:
        database = datasette.databases[database_config['database']]
        results = await database.execute(database_config['query'])
        for row in results:
            start_date = dateutil.parser.isoparse(row['start_date'])
            key = start_date.strftime('%m-%d-%y')
            text = '%s%s' %(database_config['text'], row[database_config['text_column']])
            if key in slides_by_day:
                slides_by_day[key].addText(text)
            else:
                slides_by_day[key] = TimelineSlide({'start_date': start_date, 'text': text})

    return [await buildTimelineSlideView(datasette, slide) for slide in slides_by_day.values()]

async def buildTimelineSlideView(datasette, slide):
    view = slide.toDict()
    view['text']['text'] = await renderTimelineText(datasette, slide)
    return view

async def renderTimelineText(datasette, slide):
    return await datasette.render_template("text.html", {'text_entries': slide.text})
