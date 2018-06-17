import discord


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = args.__str__()[1:-1].replace("'", "")

    person = message.author
    print(person)

    for role in message.author.roles:
        if role.id == "448428748908396544":
            person = "322068124704964609"

            yield from client.send_message(message.channel, "Der #team-chat wird nun gesperrt")

            rolle = discord.utils.find(lambda r: r.name == "Mitarbeiter", message.server.roles)
            rolle2 = discord.utils.find(lambda r: r.name == "Techniker", message.server.roles)

            overwrite = discord.PermissionOverwrite()
            overwrite.write_messages = False
            yield from client.edit_channel_permissions(client.get_channel("440957321435283466"), rolle, overwrite)
            yield from client.edit_channel_permissions(client.get_channel("440957321435283466"), rolle2, overwrite)

            yield from client.send_message(message.channel, "Der #team-chat wurde nun erfolgreich gesperrt!")
