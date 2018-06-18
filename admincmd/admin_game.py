    if message.content.startswith('!game') and message.author.id == ImXemm:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game), status='online')
        await client.send_message(message.channel, "Ich habe meinen Status zu {0} geandert.".format(game))
