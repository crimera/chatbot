from models import Message
from discord import Message as DiscordMessage

def to_message(message: DiscordMessage) -> Message:
    return Message(message.author.name, message.content)

def process_response(response: str, bot_name: str) -> str:
    return response