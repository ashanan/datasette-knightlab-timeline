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
        (r"^/-/timeline$", timeline)
    ]

async def timeline(request, datasette):
    return Response.html(
        await datasette.render_template(
        "timeline.html",
        {
            "text": "template test"
        },
        request=request,
        )
    )
