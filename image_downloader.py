import discord
import aiohttp


intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.attachments and "keyword" in message.content:
        async with aiohttp.ClientSession() as session:
            async with session.get(message.attachments[0].url) as resp:
                if resp.status == 200:
                    with open(message.attachments[0].filename, 'wb') as f:
                        f.write(await resp.read())
                        print(f"Downloaded {message.attachments[0].filename}")

client.run('')

