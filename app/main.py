from app.context.context import AppContext


def start():
    context = AppContext()
    context.on_startup()
    app = context.appl
    context.on_shutdown()

    return app


app = start()

if __name__ == '__main__':
    pass
