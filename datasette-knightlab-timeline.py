from datasette import hookimpl

@hookimpl
def extra_body_script():
    return {
        "module": True,
        "script": "console.log('hello datasette world!')"
    }