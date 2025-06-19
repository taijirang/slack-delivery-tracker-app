from logging import Logger

def deny_delivery_callback(ack, body, client, logger: Logger):
    try:
        ack()

        delivery_id = body['message']['text'].split('*')[1]
        # Update the original message so you can't press it twice.
        client.chat_update(
            channel=body["container"]["channel_id"],
            ts=body["container"]["message_ts"],
            blocks=[
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"This is not the correct delivery ID {delivery_id}."
			}
		}
	]
)
    except Exception as e:
        logger.error(e)

def approve_delivery_callback(ack, body, client, logger: Logger):
    try:
        ack()

        delivery_id = body['message']['text'].split('*')[1]
        client.views_open(
            trigger_id=body["trigger_id"],
            view={
	"type": "modal",
    "callback_id": "approve_delivery_view",
    "private_metadata": f"{delivery_id}|{body['container']['channel_id']}",
	"title": {
		"type": "plain_text",
		"text": "Approve Delivery",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": True
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"Approving Delivery ID *{delivery_id}*"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "delivery_notes_input",
                "placeholder": {
					"type": "plain_text",
					"text": "Enter any special instructions or notes about this delivery..."
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Delivery Notes",
				"emoji": True
			},
            "block_id": "delivery_notes",
            "optional": True
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "delivery_location_input",
                "placeholder": {
					"type": "plain_text",
					"text": "Enter the delivery address or location details..."
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Delivery Locations",
				"emoji": True
			},
            "block_id": "delivery_location",
            "optional": True
		}
	]
})
    except Exception as e:
        logger.error(e)