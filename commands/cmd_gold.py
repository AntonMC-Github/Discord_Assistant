import discord


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*UNTERDRÜCKTE ARGUMENTE: %s*" % args.__str__()[1:-1].replace("'", "")
    yield from client.send_message(message.channel, "Gold (bereits althochdeutsch gold, zu einer indogermanischen Wurzel *ghel: glänzend, gelb[11]) ist ein chemisches Element mit dem Elementsymbol Au (lateinisch Aurum) und der Ordnungszahl 79. Es ist ein Übergangsmetall und steht im Periodensystem in der 1. Nebengruppe (Gruppe 11), die auch als Kupfergruppe bezeichnet wird. Diese Gruppe enthält Kupfer und die Edelmetalle Silber und Gold. Die drei Metalle werden in der Chemie auch als „Münzmetalle“ bezeichnet. Des Weiteren enthält die Gruppe noch das künstlich erzeugte, radioaktive und extrem kurzlebige Roentgenium, welches bisher keine Anwendungen hat. \n https://de.wikipedia.org/wiki/Gold" + args_out)
