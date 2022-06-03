from datasette import hookimpl, Response

@hookimpl
def extra_body_script():
    return {
        "module": True,
        "script": "console.log('hello datasette world!')"
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

async def timeline(request):
    return Response.html("Hello world")