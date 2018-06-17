import discord


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = args.__str__()[1:-1].replace("'", "")

    person = message.author
    print(person)

    for role in message.author.roles:
        if role.id == "448428748908396544":
            person = "282250702842101770"

            yield from client.send_message(message.channel, "Okay, wie du willst! ich veranlasse alles nötige ;)")
            yield from client.start_private_message(discord.Server.get_member(client.get_server("440450305591738369"), person))
            yield from client.send_message(discord.Server.get_member(client.get_server("440450305591738369"), person), "Dein Ausschluss aus dem Team wurde jetzt eingereicht. Die Admins wurden informiert und werden darüber abstimmen. Da es in diesem Prozess um dich geht, wurde dir dein Stimmrecht enthoben. Du darfst bei der Abstimmung in einem Talk gerne dabei sein. https://discord.gg/UkDt95Z Falls die Admins sich gegen einen Ausschluss  entscheiden sollten, bekommst du alle Rechte wieder. MCT-Magazin")
            yield from client.kick(discord.Server.get_member(client.get_server("440450305591738369"), person))
            yield from client.send_message(message.channel, "Fertig, dein Auftrag wurde ausgeführt!")
