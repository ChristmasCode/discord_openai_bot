from dotenv import load_dotenv
import discord
import os

from app.chatgpt_ai.openai import chatgpt_response

# Load environment variables from .env file
load_dotenv()

# Load discord token from environment variable
discord_token = os.getenv("DISCORD_TOKEN")


class MyClient(discord.Client):
    async def on_message(self, message):
        # Called whenever a message is received by the bot
        if message.author == self.user:
            # Ignore messages sent by the bot itself
            return
        command, user_message = None, None

        for text in ["/ai", "/bot", "/chatgpt"]:
            # Check if the message is a command
            if message.content.startswith(text):
                command = message.content.split(" ")[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)

        if command == "/ai" or command == "/bot" or command == "/chatgpt":
            # If it is a command, get the response from the chatbot and send it back to the user
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")


# Set up the intents and create a new instance of our custom client class
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
