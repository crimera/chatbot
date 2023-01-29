import openai
from api import generate_response
from utils import to_message
from models import Conversation, Prompt, Message
from config import CHANNEL, INSTRUCTIONS, EXAMPLE_CONVERSATIONS, DISCORD_TOKEN
from discord import Intents, app_commands, Client, Interaction, Message as DiscordMessage

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)
tree = app_commands.tree.CommandTree(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await tree.sync()
    print("Commands are synced")

@client.event
async def on_message(message: DiscordMessage):
    channel = message.channel
    BOT_NAME = client.user.name
    if channel.name != CHANNEL:
        return
    if message.author.name == BOT_NAME:
        return
    
    messages = [
            to_message(message)
            async for message in channel.history(limit=1500)
        ]
    messages = [x for x in messages if x is not None]
    messages.reverse()

    conversation = Conversation(messages)
    

    prompt = Prompt(
            header=Message("System", f"Instructions to {BOT_NAME}: {INSTRUCTIONS}"),
            name=BOT_NAME,
            example_conversations=EXAMPLE_CONVERSATIONS,
            conversation=conversation
        )
        
    async with channel.typing():
            response = await generate_response(prompt)
        
    await channel.send(response)
    
@tree.command(name="chat", description="Starts a new chat thread")
async def chat_command(interaction: Interaction, message: str):
    print(f"{interaction.user.name} used the chat command with the message: {message}") 

client.run(DISCORD_TOKEN)