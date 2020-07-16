import discord
import random
import datetime
import time
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(['Made by Reven8e', '<3'])
client.remove_command('help')
ROLE = "Cool"

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# member joins

@client.event
async def on_member_join(member : discord.member):
    channel = client.get_channel(732548393024618506)
    await channel.send(f'{member.mention} has **joined the server** {(str(member.created_at))}')

# member leaves

@client.event
async def on_member_remove(member : discord.member):
    channel = client.get_channel(732548393024618506)
    await channel.send(f'{member} has **left the server**')

# help

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.set_author(name='Help- Command List')
    embed.add_field(name='.ping', value='Pong! and ms', inline=False)
    embed.add_field(name='.howgay {Tag}',value='gay %', inline=False)
    embed.add_field(name='.ball {Question}',value='Bot answers', inline=False)
    embed.add_field(name='.purge {Amount}',value='purging amount of messages', inline=False)
    embed.add_field(name='.kick {Mention}',value='kick a member', inline=False)
    embed.add_field(name='.ban {Mention}',value='ban a member', inline=False)
    embed.add_field(name='.unban{Uname}',value='unban a user', inline=False)
    embed.add_field(name='.nuke', value='nuke a channel', inline=False)
    embed.add_field(name='.svf', value='Server Info', inline=False)
    embed.add_field(name='.say', value='Say or ask something', inline=False)

    embed.set_footer(text="Made by Reven8e with <3")

    await ctx.send(embed=embed)

# ping

@client.command()
async def ping(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.add_field(name='Pong!', value=f'my ms is {round(client.latency *1000)}', inline=False)
    embed.set_footer(text="Made by Reven8e with <3")
    await ctx.send(embed=embed)

# howgay

@client.command(aliases=['howgay', 'gay'])
async def _howgay (ctx, *, question):
    responses = ['50%',
                 '75$',
                 '100$',
                 '150%',
                 '1000%']
    if "703409174096117771" in question:
        await ctx.send(f'Why you even try he will never be gay')
    elif "641515058060460044" in question:
        await ctx.send(f'Why you even try he is my owner he is not gay')
    elif "650087046106447914" in question:
        await ctx.send(f' He is the sexiest being in the all planet')
    elif "312980623910371328" in question:
        await ctx.send(f'999$')
    else:
        await ctx.send(f'{question} is {random.choice(responses)} gay')

@_howgay.error
async def _howgay_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('``.howgay {mention}``')

# ball

@client.command(aliases=['ball', 'question'])
async def _8ball (ctx, *, question):
    responses = ['yes',
                 'no',
                 'yep',
                 'nah',
                 'frick no',
                 'fuck yeah',
                 'idk']
    await ctx.send(f'Question:{question} \n Answer: {random.choice(responses)}')

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('``.ball {question}``')

# purge

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('``.Purge {Amount}``')

# kick member

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member , * , reason=None):
    embed = discord.Embed(colour=discord.Colour.green())
    embed.add_field(name=f'kicked- {member}', value=f'Reason: {reason}', inline=False)
    embed.set_footer(text="Made with <3 by Reven8e")
    await member.kick(reason=reason)
    await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name='.Kick {mention}', value='Reason: {Enter your reason}', inline=False)
        embed.set_footer(text="Made with <3 by Reven8e")
        await ctx.send(embed=embed)

# ban member

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member : discord.Member , * , reason=None):
    embed = discord.Embed(colour=discord.Colour.green())
    embed.add_field(name=f'Banned- {member}', value=f'Reason: {reason}', inline=False)
    embed.set_footer(text="Made with <3 by Reven8e")
    await member.ban(reason=reason)
    await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name='.Ban {mention}', value='Reason: {Enter your reason}', inline=False)
        embed.set_footer(text="Made with <3 by Reven8e")
        await ctx.send(embed=embed)

# unban member

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            embed = discord.Embed(colour=discord.Colour.green())
            embed.description = f'**Unbanned- {user} **'
            embed.set_footer(text="Made with <3 by Reven8e")
            await ctx.guild.unban(user)
            await ctx.send(embed=embed)
            return

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.description = ".unban {Uname#}"
        embed.set_footer(text="Made with <3 by Reven8e")

        await ctx.send(embed=embed)

# say

@client.command()
async def say(ctx, *, say):
    embed= discord.Embed(colour=discord.Colour.green())
    embed.description = f"{say}"
    embed.set_footer(text="Made with <3 by Reven8e")
    await ctx.send(embed=embed)

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name='.say {Something/Question}', value= 'Bot answers', inline=False)
        await ctx.send(embed=embed)

# nuke channel

@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx):
    await ctx.send("Nuking this channel")
    time.sleep(1)
    channel_id = ctx.channel.id
    channel = client.get_channel(channel_id)
    new_channel = await ctx.guild.create_text_channel(name=channel.name, topic=channel.topic, overwrites=channel.overwrites, nsfw=channel.nsfw, category=channel.category, slowmode_delay=channel.slowmode_delay, position=channel.position)
    await channel.delete()
    await new_channel.send("Nuked this channel.\nhttps://imgur.com/LIyGeCR")

@client.command(aliases=['srvinfo', 'svf'])
async def _svf(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",colour = discord.Colour.green())
    embed.add_field(name=f"Server Created At:", value=f"{ctx.guild.created_at}", inline=False)
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}", inline=False)
    embed.add_field(name="Member Count", value=f"{ctx.guild.member_count}", inline=False)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.set_footer(text="Made by Reven8e with <3")
    await ctx.send(embed=embed)

client.run("NjQ1OTQyNDQzNzUzMzQwOTQ3.Xwy8QQ.x5e2cOFKoGuYLb53tpqf9YXjH_A")