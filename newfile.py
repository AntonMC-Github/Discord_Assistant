if my_dir.is_dir():
    my_dir = Path("/commands")
    my_file = Path("/path/to/file")
    invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
    args = message.content.split(" ")[1:]

    if my_file.is_file():
        yield from commands.get(invoke).ex(args, message, client, invoke)

    else:
        yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(),
                                                        description=("Error 304 | Command cant found.")))
"""
    elif:
        yield form command_send.message.get.(invoke).ex(args, message, client, invoke)
        import newfile as newfile.py
        my_dir = Path("/path/to/dir")
        args_out COMMIT_EDITMSG
        packed-refs as remotes_heads
        fetch_head tags objects remotes_heads
"""
else:
    print:("Error 301 | directory does not exist!")
