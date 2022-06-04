from datasette import hookimpl, Response


# @hookimpl
# def extra_js_urls(database, table, columns, view_name, datasette):
#     timeline_url = datasette.urls.static_plugins(
#         "datasette-knightlab-timeline", "timeline.js"
#     )
#     print(timeline_url)

#     return [
#         {
#             "url": datasette.urls.static_plugins(
#                 "datasette-knightlab-timeline", "timeline.js"
#             ),
#             "module": True,
#         }
#     ]

@hookimpl
def extra_body_script(datasette):
    timeline_url = datasette.urls.static_plugins(
        "datasette-knightlab-timeline", "timeline.js"
    )

    return {
        "module": True,
        "script": "console.log('hello datasette world!', '%s')" %(timeline_url)
    }

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
    # return Response.html("Hello world")