# from app.context_app.context import AppContext
import uvicorn

import context_app as test


def create_ctx() -> test.context.AppContext:
    ctx = test.context.AppContext()
    ctx.appl.add_event_handler('startup', ctx.on_startup)
    ctx.appl.add_event_handler('shutdown', ctx.on_shutdown)
    return ctx


context = create_ctx()
app = context.appl


if __name__ == '__main__':
    # for debug in IDE
    uvicorn.run(app, host='0.0.0.0', port=8000)

# TODO req.txt
# TODO Dockerfile
