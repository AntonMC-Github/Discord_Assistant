import discord


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*UNTERDRÜCKTE ARGUMENTE: %s*" % args.__str__()[1:-1].replace("'", "")
    embed = discord.Embed(
        title="",
        color=0xe67e22,
        description="Pong! Gemessene Zeit(in ms): 7ms"
    )
    embed.set_author(
        name="Assistant",
        icon_url="",
        url="http://antonmc.de/"
    )
    embed.set_footer(
        text="Assistant Bot Server Unit |",
        icon_url="http://antonmc.de"
    )
    yield from client.send_message(message.channel, embed=embed)
