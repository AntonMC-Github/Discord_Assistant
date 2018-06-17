import discord


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*UNTERDRÜCKTE ARGUMENTE: %s*" % args.__str__()[1:-1].replace("'", "")
    embed = discord.Embed(
        title="",
        color=0xe67e22,
        description="Hier kannst du dich bewerben:\n"
                    "https://goo.gl/forms/G8ugLQL7x4OsjU1r1"
    )
    embed.set_author(
        name="Bewerbung",
        icon_url="",
        url="http://tjcmagazin.de/"
    )
    embed.set_footer(
        text="© McT-Magazin - 2018 - Command by Marius",
        icon_url=""
    )
    yield from client.send_message(message.channel, embed=embed)
