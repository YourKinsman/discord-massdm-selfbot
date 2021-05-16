import discord
import os
import colorama
from colorama import Fore, Style
import requests
import time
import termcolor 
from termcolor import colored
from colorama import Fore
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

def Cls():
    os.system('cls')
Cls()
b = Style.BRIGHT
print(colored('Created by', 'red'), colored('https://github.com/YourKinsman', 'green'))
print(colored('Please be sure to put your token in message.py', 'cyan'), colored('IT WONT WORK OTHERWISE!', 'red'))
print(" ")
message = input("What would you like to message everyone?")
Cls() 

# Put your token inbetween the quotations below.
token = ""

Cls()


b = Style.BRIGHT
print(f"""
{b+Fore.GREEN}
Test



{b+Fore.GREEN} > {Fore.RESET}Discord Mass DM Tool.
{b+Fore.WHITE} > {Fore.RESET}Created by Kinsman.
{b+Fore.ORANGE} > {Fore.RESET}https://github.com/YourKinsman
""")

watch = discord.Client()


@watch.event
async def on_connect():
  for user in watch.user.friends:
    try:
      
      watchy = discord.Embed(color= discord.Color(0x2f3136))
      watchy.set_author(name="Check out my Github https://github.com/YourKinsman ")
      watchy.add_field(name="Mass-DM Tool created by Kinsman.",value=message)
      watchy.set_image(url="https://i.redd.it/vhxb1zykzmv41.jpg")
      # To decrease your chances of being banned/detected turn "time.sleep(.5)" up.
      # it'll slow down how quick it gets sent but it'll be more safe. How it is right now should work fine.
      time.sleep(.5)
      await user.send(embed=watchy)
      await user.send("")
      # To decrease your chances of being banned/detected turn "time.sleep(.5)" up.
      # it'll slow down how quick it gets sent but it'll be more safe. How it is right now should work fine.
      time.sleep(.5)
      print(f'messaged:' + Fore.GREEN + f' {user.name}')
    except:
       print(f"Could not send message to : {user.name}")
       print(f"Directed messaged all users friends")


watch.run(token, bot=False)
