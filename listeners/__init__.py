from listeners import messages, actions, views


def register_listeners(app):
    messages.register(app)
    actions.register(app)
    views.register(app)
