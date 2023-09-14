import discord

dir = "/".join(discord.__path__[0].replace("\\", "/").split("/")[:-1])

try:
    code = open(f"{dir}/discord/ext/commands/bot.py","r",encoding="utf_8").read()
    delete = "if self._skip_check(message.author.id, self.user.id):  # type: ignore" + code.split("if self._skip_check(message.author.id, self.user.id):  # type: ignore")[1].split("return ctx")[0] + "return ctx"
    open(f"{dir}/discord/ext/commands/bot.py","w",encoding="utf_8").write(code.replace(delete, ""))
except:
    pass
