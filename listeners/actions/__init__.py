from slack_bolt import App
from .approve_deny_buttons import deny_delivery_callback, approve_delivery_callback

def register(app: App):
    app.action("deny_delivery")(deny_delivery_callback)
    app.action("accept_delivery")(approve_delivery_callback)