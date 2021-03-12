import discord
from discord.ext import commands, tasks
import random
import urllib.request

# REDDIT PRAW API IMPORT
import praw

reddit = praw.Reddit(client_id='Your Reddit ID',
                     client_secret='Your Reddit Secret',
                     user_agent='Your Reddit Agent')

memespic = reddit.subreddit('quotes')

hot_posts = reddit.subreddit('quotes').new(limit=50)

client = commands.Bot(command_prefix='.')

ROLE = "New Comer"


# CODE FOR WATCHING IF THE BOT IS READY OR NOT
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Watching Your Server'))
    print("Bot Is Ready")


# clear command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    if amount == 0:
        await ctx.send("OH ! Please Enter The Amount More Than 0")
    else:
        await ctx.channel.purge(limit=amount)


# Code For Sending Memes
@client.command()
async def memes(ctx):
    url = []
    for submission in reddit.subreddit('memes').new(limit=30):
        if not submission.stickied:
            url.append(submission.url)
            image = random.choice(url)
            name = 'memes' + '.jpg'
    urllib.request.urlretrieve(image, name)
    await ctx.send(file=discord.File('memes.jpg'))


# Code For Sending Valorant Memes
@client.command()
async def valomemes(ctx):
    url = []
    for submission in reddit.subreddit('ValorantMemes').top(limit=30):
        if not submission.stickied:
            url.append(submission.url)
            image = random.choice(url)
            name = 'valomemes' + '.jpg'
    urllib.request.urlretrieve(image, name)
    await ctx.send(file=discord.File('valomemes.jpg'))


# Code For Sending Artworks
@client.command()
async def art(ctx):
    url = []
    for submission in reddit.subreddit('Art').new(limit=30):
        if not submission.stickied:
            url.append(submission.url)
            image = random.choice(url)
            name = 'art' + '.jpg'
    urllib.request.urlretrieve(image, name)
    await ctx.send(file=discord.File('art.jpg'))


# Code For Sending Sketches
@client.command()
async def sketch(ctx):
    url = []
    for submission in reddit.subreddit('sketches').new(limit=30):
        if not submission.stickied:
            url.append(submission.url)
            image = random.choice(url)
            name = 'sketches' + '.jpg'
    urllib.request.urlretrieve(image, name)
    await ctx.send(file=discord.File('sketches.jpg'))


# Code For Sending NSFW
@client.command()
async def nsfw(ctx):
    url = []
    for submission in reddit.subreddit('PetiteGoneWild').new(limit=30):
        if not submission.stickied:
            url.append(submission.url)
            image = random.choice(url)
            name = 'PetiteGoneWild' + '.jpg'
    urllib.request.urlretrieve(image, name)
    await ctx.send(file=discord.File('PetiteGoneWild.jpg'))


# CODE FOR SENDING THE QUOTE
quoteList = []


@client.command(aliases=['quotes'])
async def quote(ctx):
    for post in hot_posts:
        quoteList.append(post.title)
    await ctx.send(random.choice(quoteList))


# SEND AVATAR COMMAND
@client.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(color=discord.Color.dark_blue())
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)


client.run('Your Discord Token')
