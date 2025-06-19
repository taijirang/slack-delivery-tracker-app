import os
import logging
import argparse

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from listeners import register_listeners

logging.basicConfig(level=logging.DEBUG)

def parse_args():
    parser = argparse.ArgumentParser(description='Slack Delivery Tracker App')
    parser.add_argument('--bot-token', required=True, help='Slack Bot User OAuth Token')
    parser.add_argument('--app-token', required=True, help='Slack App-Level Token')
    return parser.parse_args()

# Initialization
args = parse_args()
app = App(token=args.bot_token)

# Register Listeners
register_listeners(app)

# Start Bolt app
if __name__ == "__main__":
    SocketModeHandler(app, args.app_token).start()
