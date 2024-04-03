from datetime import datetime
from pyrogram import Client

data = []

def main():
	api_id = 25261182
	api_hash = 'fd7039bceb96000b2cd6b844aa51e555'

	channel_ids = [-1001280770128, -1001758115439, ]

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
