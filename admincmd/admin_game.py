import discord


<<<<<<< HEAD



    if message.content.startswith('!game') and message.author.id == ImXemm:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game), status='online')
        await client.send_message(message.channel, "Ich habe meinen Status zu {0} geandert.".format(game))
=======
def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*UNTERDRÜCKTE ARGUMENTE: %s*" % args.__str__()[1:-1].replace("'", "")
    yield from client.send_message(message.channel, "Wie ihr wünscht!" + args_out)
    game = message.content[6:]
    yield from client.change_presence(game=discord.Game(name=game), status='online')
    yield from client.send_message(message.channel, "Ich habe meinen Status zu {0} geandert.".format(game))
>>>>>>> acb704d4bd9f59f707e1bd4a410885a2e88a0475
