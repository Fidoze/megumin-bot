import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

bot = commands.Bot('m ')

@bot.event
async def on_ready():
    print("ready for explosions!")
    await bot.change_presence(game=discord.Game(name='z Fidoze <3'))

@bot.command(
    help='BOOM',
    description='...'
)
async def explosion():
    await bot.say("EXPLOOOOSION\n http://gifimage.net/wp-content/uploads/2017/08/megumin-explosion-gif-5.gif")

@bot.command(
	help='Dont',
    description='...'
 )
async def lewd():
    await bot.say("Don't lewd lolis!")

@bot.command(
	help="<3",
	description=""
)
async def waifu():
    await bot.say("http://megumin.love")

@bot.command()
async def dog():
    await bot.say("http://random.dog")


@bot.event
async def on_member_join(member):
    await bot.send_message(discord.Object(id="439060856542593036"), "Welcome and get ready for explosions {}!".format(member.mention))

@bot.event
async def on_member_remove(member):
    await bot.send_message(discord.Object(id="439060856542593036"), "Bye, have a good day {}!".format(member.mention))

bot.run("NDQyOTY4MzMxNzU5Mzg2NjI1.DdG2rw.0DIGsRXOEJ1lcYp-QBTIDJAkSlY")
