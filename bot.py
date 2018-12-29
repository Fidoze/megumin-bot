import discord
import random
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import json
from random import randint

bot = commands.Bot('m ')
explosions = ["https://vignette.wikia.nocookie.net/powerlisting/images/b/b6/Explosion_Megumin.gif","https://tenor.com/view/explosion-megumin-konusoba-gif-7559841", "https://media1.tenor.com/images/3197441d730ffde04b00fe169431ee89/tenor.gif?itemid=8587771", "https://media1.tenor.com/images/88c9891f89eb13e66a414d65dd6a31f7/tenor.gif?itemid=8899533"]
facts = ["Raw horse meat is a popular food in Japan.", "There's over 5.5 million vending machines in Japan!", "You need to wear face masks when you are ill" "The unemployment rate in Japan is only 4%.", "Crime rate in Japan is one of the lowest in the world.", "Japanese can say “Sorry” in 20 different ways.", "Japan's literacy rate is almost 100%.", "Japanese people can't speak english very well.", "There are 4 writing systems in Japan!", "Tokyo is the second most expensive city in the world to live in.", "Over 1 thousand tremors hits Japan every year."]
#Komendy_z_prefixem

@bot.event
async def on_ready():
    print("ready for explosions!")
    await bot.change_presence(game=discord.Game(name='z Fidoze <3'))
    global hajs
    try:
        with open('hajs.json') as test:             
            hajs = json.load(test)
    except FileNotFoundError:
        print("ni ma")
        hajs = {}

@bot.command(pass_context=True)
async def create(ctx):
    global hajs
    id = ctx.message.author.id
    if id in hajs:
        await bot.say("You arleady have an account!")
    else:
        hajs[id] = 50
        await bot.say("Account created!")
        zapisz()

@bot.command(pass_context=True)
async def stan(ctx):
    id = ctx.message.author.id
    if id in hajs:
        await bot.say("💰 You have {} money! 💰".format(hajs[id]))
    else:
        print("dunno")

@bot.command(pass_context=True)
@commands.cooldown(1, 60*60*24, commands.BucketType.user)
async def daily(ctx):
    id = ctx.message.author.id
    if id in hajs:
        hajs[id] += 50
        await bot.say("{} +50!".format(ctx.message.author.mention))
        zapisz()
    else:
        await bot.say("Make an account first!")

@bot.command(pass_context=True)
async def work(ctx):
    RanHajs = random.randint(1, 20)
    id = ctx.message.author.id
    if id in hajs:
        hajs[id] += RanHajs
        await bot.say("You have earned {} money!".format(RanHajs))
        zapisz()
    else:
        await bot.say("That shouldn't even happen")

def zapisz():
    with open('hajs.json', 'w+') as test:
        json.dump(hajs, test)

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


def has_pings():
    def predicate(Ship):
        if Ship.message.mentions:
            return True
        else:
            return False
    return commands.check(predicate)

@has_pings()
@bot.command(pass_context = True)
async def ship(Ship):
    author_mention = Ship.message.author.mention
    param_mention = Ship.message.mentions[0].mention
    Percent = random.randint(1, 100)
    if Percent >= 60:
    	await bot.say("{} x {} l {}\n True Love <3".format(author_mention, param_mention, Percent))
    if Percent < 60:
    	await bot.say("{} x {} l {}\n This is so sad...".format(author_mention, param_mention, Percent))





#Komendy_bez_prefixu

@bot.event 
async def on_message(msg):
    if msg.author == bot.user:
        return
    if msg.content.upper().startswith("UR MOM GAY"):
        await bot.send_message(msg.channel, "no u")

    if msg.content.upper().startswith("GOOD NIGHT"):
        await bot.send_message(msg.channel, "Good night :3")

    if msg.content.startswith("-rule34 tags Megumin"):
        await bot.send_message(msg.channel, ">:l")

    if msg.content.upper().startswith("YOS"):
        await bot.send_message(msg.channel, "https://cdn.discordapp.com/attachments/439060856542593036/444454725803311105/9k.png")

    if msg.content.upper().startswith("LIAM"):
        await bot.send_message(msg.channel, "to morderca piesków :c")

    if msg.content.upper().startswith("THIS IS SO SAD"):
        await bot.send_message(msg.channel, "Here's your despacito\n https://www.youtube.com/watch?v=W3GrSMYbkBE")

    await bot.process_commands(msg)



#powitania_pożegnania

@bot.event
async def on_member_join(member):
    await bot.send_message(discord.Object(id="439060856542593036"), "Welcome and get ready for explosions {}!".format(member.mention))

@bot.event
async def on_member_remove(member):
    await bot.send_message(discord.Object(id="439060856542593036"), "Bye, have a good day {}!".format(member.mention))


bot.run("")
