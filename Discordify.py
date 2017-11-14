import asyncio #for await, async events

import discord #discord.py for controlling the self-bot
from discord.ext import commands

import win32gui #for capturing window details from Spotify
import win32api

import tkinter #drawing error & warning windows
from tkinter import messagebox

import sys

def main():
    
    longstring = """\
    ___ _                       _ _  __       
   /   (_)___  ___ ___  _ __ __| (_)/ _|_   _ 
  / /\ / / __|/ __/ _ \| '__/ _` | | |_| | | |
 / /_//| \__ \ (_| (_) | | | (_| | |  _| |_| |
/___,' |_|___/\___\___/|_|  \__,_|_|_|  \__, |
                                        |___/ 
                                        """
    print(longstring)

    try: 
        token = read_token()
        bot = commands.Bot(command_prefix=['m.'], self_bot=True)
        bot.remove_command('help')
        bot.loop.create_task(music_loop(bot))
        bot.run(token, bot=False)
        
    except discord.errors.LoginFailure as e:
        root = tkinter.Tk()
        root.withdraw()
        root.iconbitmap('icon.ico')
        messagebox.showwarning("Discordify",e)
        sys.exit()
        


def read_token():

    token = open('token.txt','r')
    token = token.read()

    if token == '':
        root = tkinter.Tk()
        root.withdraw()
        root.iconbitmap('icon.ico')
        messagebox.showerror("Discordify", "Error, Your Token.txt file is empty.")
        
    else:
        return token


async def music_loop(bot):

    print('Awaiting bot until ready')
    print(bot.wait_until_ready())
    await bot.wait_until_ready()
    
    
    await asyncio.sleep(1)
    previousSong = ""
    
    while not bot.is_closed:
        
        currentSong = ''
        windowID = win32gui.FindWindow("SpotifyMainWindow", None)
        currentlyPlaying = win32gui.GetWindowText(windowID)
        
        
        if currentlyPlaying != previousSong:
            previousSong = currentlyPlaying

            if currentlyPlaying == "" or currentlyPlaying == "Spotify":
                await bot.change_presence(afk=True, status=discord.Status.invisible, game=None)
                print('No Song is Currently Playing')
            else:
                print("Now Playing:",currentlyPlaying)
                await bot.change_presence(afk=True,status=discord.Status.invisible,game=discord.Game(name=currentlyPlaying, type=2))

        await asyncio.sleep(2)

main()
