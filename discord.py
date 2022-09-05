from discord_webhook import DiscordWebhook
from os import environ as env


def send_message(content):
    webhook = DiscordWebhook(url=env.get('DISCORD_URL'), content=content)
    return webhook.execute()
