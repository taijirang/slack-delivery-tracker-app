from logging import Logger

from slack_bolt import BoltContext, Say

def delivery_message_callback(context: BoltContext, say: Say, logger: Logger):
    try:
        delivery_id = context["matches"][0]
        say(blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Delivery ID *{delivery_id}* was submitted, is this correct?"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Accept",
                            "emoji": True
                        },
                        "value": "accept_delivery",
                        "action_id": "accept_delivery",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Deny",
                            "emoji": True
                        },
                        "value": "deny_delivery",
                        "action_id": "deny_delivery",
                        "style": "danger"
                    }
                ]
            }
        ])
    except Exception as e:
        logger.error(e)