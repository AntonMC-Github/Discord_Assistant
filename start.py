
import asyncio as asyncio
import discord

client = discord.Client()

@client.event
@asyncio.coroutine
def start():
    print("Bot hat sich erfolgreich einngeloggt, der Bot laeuft derzeit auf folgenden Servern:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name="Assistant Bot Ps: Hilft dir gerne xD"))
