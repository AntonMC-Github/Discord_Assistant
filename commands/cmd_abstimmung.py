import discord


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*UNTERDRÜCKTE ARGUMENTE: %s*" % args.__str__()[1:-1].replace("'", "")
    yield from client.add_reaction(message, ':thumbsup:')
    yield from client.add_reaction(message, ':thumbsdown:')
    yield from client.add_reaction(message, ':thinking:')