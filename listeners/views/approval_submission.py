from logging import Logger

def handle_approve_delivery_view(ack, client, view, logger: Logger):
    try:
        ack()
        
        delivery_id, update_channel = view["private_metadata"].split("|")
        delivery_notes = view["state"]["values"]["delivery_notes"]["delivery_notes_input"]["value"]
        delivery_location = view["state"]["values"]["delivery_location"]["delivery_location_input"]["value"]

        client.chat_postMessage(
            channel=update_channel,
            blocks=[
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"✅ Delivery *{delivery_id}* has been approved."
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"*Delivery notes*\n{delivery_notes}"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"*Delivery location*\n{delivery_location}"
			}
		}
	])

    except Exception as e:
        logger.error(f"Error in approve_delivery_view: {e}")