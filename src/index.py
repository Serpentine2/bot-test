import importlib
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl
from urllib import parse, request


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-') #prefijo del bot

@bot.command(name='suma') #@bot.command(name=) función para que el bot haga cosas
async def suma(ctx, num1,num2):
   response = int(num1)+int(num2)
   await ctx.send(response)

#no se escucha la musica tengo que mirarlo.
@bot.command(name='play')
async def play (ctx, url: str):
   song_there = os.path.isfile("song.mp3")
   try:
      if song_there:
         os.remove("song.mp3")
   except PermissionError:
      await ctx.send("Espera a que la canción acabe o usa el comando 'stop'")
      return

   voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
   await voiceChannel.connect()
   voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

   ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }



@bot.command(name='leave')
async def leave(ctx):
      voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
      if voice.is_connected():
            await voice.disconnect()
      else:
            await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='pause')
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@bot.command(name='resume')
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@bot.command(name='stop')
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()




bot.run(TOKEN)
