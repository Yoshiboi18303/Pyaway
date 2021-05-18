import discord
from discord.ext import commands
import datetime
import asyncio
import random


client = commands.Bot(command_prefix = "p/")
bot_name = "Pyaway"

@client.command()
@commands.has_role("Giveaways")
async def gstart(ctx, mins : int, * , prize: str):
    embed = discord.Embed(title = "<:Pyaway_gstart:844318196822441996> Giveaway! <:Pyaway_gstart:844318196822441996>", description = f"Giveaway Prize is: {prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

    embed.add_field(name = "<:Pyaway_giveaway_endsat:844319765933719613> Ends At:", value = f"{end} UTC")
    embed.add_field(name = "<:Pyaway_giveaway_enter:844324555463983145> Enter", value = "React with <:Pyaway_gstart:844318196822441996> to enter!")
    embed.set_footer(text = f"Ends {mins} minutes from now!")

    my_msg = await ctx.send(embed = embed)


    await my_msg.add_reaction("<:Pyaway_gstart:844318196822441996>")


    await asyncio.sleep(mins*60)


    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations {winner.mention}, you've won the Prize of {prize}!")


@client.event
async def on_ready():
  print(f"{bot_name} is ready!")





client.run(YOUR_TOKEN_HERE)
