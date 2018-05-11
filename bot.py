import discord
import random
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

bot = commands.Bot('m ')
explosions = ["https://vignette.wikia.nocookie.net/powerlisting/images/b/b6/Explosion_Megumin.gif","https://tenor.com/view/explosion-megumin-konusoba-gif-7559841", "https://media1.tenor.com/images/3197441d730ffde04b00fe169431ee89/tenor.gif?itemid=8587771", "https://media1.tenor.com/images/88c9891f89eb13e66a414d65dd6a31f7/tenor.gif?itemid=8899533"]
facts = ["Raw horse meat is a popular food in Japan.", "There's over 5.5 million vending machines in Japan!", "You need to wear face masks when you are ill" "The unemployment rate in Japan is only 4%.", "Crime rate in Japan is one of the lowest in the world.", "Japanese can say “Sorry” in 20 different ways.", "Japan's literacy rate is almost 100%.", "Japanese people can't speak english very well.", "There are 4 writing systems in Japan!", "Tokyo is the second most expensive city in the world to live in.", "Over 1 thousand tremors hits Japan every year."]
#Komendy_z_prefixem

@bot.event
async def on_ready():
    print("ready for explosions!")
    await bot.change_presence(game=discord.Game(name='z Fidoze <3'))

@bot.command(
    help='- BOOM',
    description='...'
)
async def explosion():
    await bot.say("EXPLOSION\n" + random.choice(explosions))


@bot.command(
    help='- Random fact about Japan',
    description='...'
)
async def J_fact():
    await bot.say("Here's your random fact! Enjoy\n" + random.choice(facts))

@bot.command(
    help='- Dont',
    description=''
 )
async def lewd():
    await bot.say("Don't lewd lolis!")

@bot.command(
    help="- <3",
    description=""
)
async def waifu():
    await bot.say("http://megumin.love")

@bot.command()
async def dog():
    await bot.say("http://random.dog")

@bot.command(pass_context=True)
async def rip(message):
    await bot.say(f"{message.message.author.mention} pays respect")

@bot.command(
    help='- Flips coin',
    description=''
 )
async def flipcoin():
    choice = random.choice(['Head', 'Tail'])
    await bot.say(f'You flipped {choice}')

@bot.command(
    help="- Give someone a cookie",
    description="",
    pass_context = True
)
async def cookie(Cookie):
    mentions = [i.name for i in Cookie.message.mentions]
    await bot.say("{} gives {} :cookie:".format(Cookie.message.author.mention, "".join(mentions)))

@bot.command(
    help="- Info about you",
    description="",
    pass_context = True
)
async def user(User):
    Name = User.message.author.name
    Nickname = User.message.author.nick
    Id = User.message.author.id
    await bot.say("{}'s\n Name: {}\n Nickname: {}\n id: {}\n Avatar: {}".format(User.message.author.mention, Name, Nickname, Id, User.message.author.avatar_url))





#Komendy_bez_prefixu

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    if msg.content.upper().startswith("UR MOM GAY"):
        await bot.send_message(msg.channel, "no u")

    if msg.content.upper().startswith("KAZUMA"):
        await bot.send_message(msg.channel, "KAZUMA KAZUMA KAZUMA")

    if msg.content.upper().startswith("GOOD NIGHT"):
        await bot.send_message(msg.channel, "Good night :3")

    if msg.content.startswith("-rule34 tags megumin"):
        await bot.send_message(msg.channel, ">:l")

    if msg.content.upper().startswith("YOS"):
        await bot.send_message(msg.channel, "https://cdn.discordapp.com/attachments/439060856542593036/444454725803311105/9k.png")
    await bot.process_commands(msg)



#powitania_pożegnania

@bot.event
async def on_member_join(member):
    await bot.send_message(discord.Object(id="439060856542593036"), "Welcome and get ready for explosions {}!".format(member.mention))

@bot.event
async def on_member_remove(member):
    await bot.send_message(discord.Object(id="439060856542593036"), "Bye, have a good day {}!".format(member.mention))

bot.run("NDQyOTY4MzMxNzU5Mzg2NjI1.DdG2rw.0DIGsRXOEJ1lcYp-QBTIDJAkSlY")
