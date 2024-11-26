from datetime import datetime
from pyrogram import Client

data = []

def main():
	# api_id = 
	# api_hash = 

	# channel_ids = []

	client = Client('my_session', api_id=api_id, api_hash=api_hash)
	client.start()

	for channel_id in channel_ids:
		tg_posts = client.get_chat_history(channel_id, limit=10)

		for post in tg_posts:
			timestamp = post.date
			current_dt = datetime.now()
			time_diff = current_dt - timestamp

			if time_diff.total_seconds() < 24 * 3600 and post.caption:
				data.append(post.caption)

	return data


if __name__ == 'main':
	main()
