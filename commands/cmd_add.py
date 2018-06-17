import discord


def ex(args, message, client, invoke):
    args_out = ""

    yield from client.send_message(message.channel, "Dieser Befehl wurde aus Sicherheitsgründen deaktiviert um Codeinjektion vorzubeugen :D")

    """
    if len(args) > 0:
        cmd_name = args[0]
        cmd_inhalt = ""

        for i in args:
            cmd_inhalt = cmd_inhalt + str(i) + " "

        cmd_inhalt = cmd_inhalt.split(' ', 1)[1]

        write(cmd_name, cmd_inhalt)
    else:
        yield from client.send_message(message.channel, "Das darf doch wohl nicht wahr sein wie blöd ist die Menschheit denn gewordn weiß sie mitlerweile schon nicht mehr wofür ein add Befehl zuständig ist? Sehr traurig :( ")
    yield from client.send_message(message.channel, "Datei wurde erfolgreich erstellt!" + args_out)
    """


def write(name, text):
    f = open('commands/cmd_' + name + '.py', 'w')
    f.write("MESSAGE = '" + text + "' \n")
    f.close()
