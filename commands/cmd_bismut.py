import discord


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*UNTERDRÜCKTE ARGUMENTE: %s*" % args.__str__()[1:-1].replace("'", "")
    yield from client.send_message(message.channel, "Bismut oder Wismut (veraltet auch: Wismuth) ist ein chemisches Element mit dem Elementsymbol Bi und der Ordnungszahl 83. Im Periodensystem steht es in der 5. Hauptgruppe oder Stickstoffgruppe. \n https://de.wikipedia.org/wiki/Bismut" + args_out)
