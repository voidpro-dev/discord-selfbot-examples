import discord, random

client = discord.Client()

@client.event
async def on_guild_channel_create(channel):
	print(channel)
	if channel.name == "🇨🇳│荒ʖ‘し𝖢𝖧𝖠𝖳":
		if channel.guild.id == 1054247482332303360:
			await channel.send("1")

client.run("token")