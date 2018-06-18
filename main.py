import asyncio as asyncio
import discord
from discord import Game, Server, Member, Embed

import SECRETS
import STATICS
from commands import cmd_ping, cmd_help, cmd_dieantwort, cmd_baum, cmd_paperfreddie, cmd_pokemon, cmd_lol, \
    cmd_eisen, cmd_afd, cmd_trump, cmd_gold, cmd_bismut, cmd_add, cmd_Schokolade, cmd_tjc_magazin, cmd_kick, \
    cmd_abstimmung, cmd_bewerbung, cmd_mir_reichts, cmd_lock, cmd_unlock
from admincmd import admin_game

client = discord.Client()

players = {}

commands = {

    "ping": cmd_ping,
    "help": cmd_help,
    "die-antwort": cmd_dieantwort,
    "antwort": cmd_dieantwort,
    "paperfreddie": cmd_paperfreddie,
    "pokemon": cmd_pokemon,
    "lol": cmd_lol,
    "eisen": cmd_eisen,
    "afd": cmd_afd,
    "trump": cmd_trump,
    "gold": cmd_gold,
    "bismut": cmd_bismut,
    "add": cmd_add,
    "abstimmung": cmd_abstimmung,
    "bewerbung": cmd_bewerbung,
    "mir-reichts": cmd_mir_reichts,
    "lock": cmd_lock,
    "unlock": cmd_unlock,

}

selfmade = {

    "schokolade": cmd_Schokolade,
    "tjc-magazin": cmd_tjc_magazin,
    "kick": cmd_kick,
    "baum": cmd_baum,

}

admin_cmd = {

    "game": admin_game,

}


@client.event
@asyncio.coroutine
def on_ready():
    print("Bot hat sich erfolgreich einngeloggt, der Bot laeuft derzeit auf folgenden Servern:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name="Assistant Bot Ps: Hilft dir gerne xD"))



@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(STATICS.PREFIX):

        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]

        if commands.__contains__(invoke):

            yield from commands.get(invoke).ex(args, message, client, invoke)

        elif selfmade.__contains__(invoke):

            yield from client.send_message(message.channel, selfmade.get(invoke).MESSAGE)

        elif admin_cmd.__contains__(invoke):

            yield from commands.get(invoke).ex(args, message, client, invoke)

        else:

            yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(),
                                                                        description=("Tut mir leid, diesen #Befehl gibt es nicht! Techniker sind halt von Natur aus faul ;)")))

client.run(SECRETS.TOKEN)
