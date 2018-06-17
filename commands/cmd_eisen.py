import discord


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*UNTERDRÜCKTE ARGUMENTE: %s*" % args.__str__()[1:-1].replace("'", "")
    yield from client.send_message(message.channel, "https://www.youtube.com/watch?v=noSUZfjq3f4 \n Eisen (von ahd. īsa(r)n; aus urgerm. *īsarnan, wie gall. īsarnon wahrscheinlich entlehnt aus dem Illyrischen und in Bezug auf das im Gegensatz zur weicheren Bronze starke, kräftige Metall verwandt mit lateinisch ira, ‚Zorn, Heftigkeit‘)[10][11] ist ein chemisches Element mit dem Elementsymbol Fe (lateinisch ferrum, ‚Eisen‘) und der Ordnungszahl 26. Es zählt zu den Übergangsmetallen, im Periodensystem steht es in der 8. Nebengruppe (Eisen-Platin-Gruppe), nach der neuen Zählung in der Gruppe 8 oder Eisengruppe. Es ist, auf den Massenanteil (ppmw) bezogen, nach Sauerstoff, Silicium und Aluminium das vierthäufigste Element in der Erdkruste und nach Aluminium das häufigste Metall. Copyright: https://de.wikipedia.org/wiki/Eisen" + args_out)
