import discord


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = " %s*" % args.__str__()[1:-1].replace("'", "")
        yield from client.send_message(message.channel, "Du hast ein neues " + args_out + " gefunden")
    else:
        yield from client.send_message(message.channel, "Du kannst dich nicht selbst finden :D")