from discord.ext import commands
import discord
import requests
import os

token = "MTQ4ODY4MDQ1OTUzMjUwNTIzNA.GcezsN.OTwBkDHfUP0REo4jbAaEfulWm20DaLpc876_EM"

bot = commands.Bot(command_prefix='!')

@bot.command()
async def saytca(ctx, message: str):
    if str(ctx.message.author) == "kinz_gamer":
        MAIN_GUILD = bot.get_guild(1469749041163272233)
        channel = MAIN_GUILD.get_channel(1487473577107263588)
        await channel.send(message)

@bot.command()
async def dnd(ctx, status: str):
    if str(ctx.message.author) == "kinz_gamer":
        status = discord.CustomActivity(name=status)
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=status)

@bot.command()
async def online(ctx, status: str):
    if str(ctx.message.author) == "kinz_gamer":
        status = discord.CustomActivity(name=status)
        await bot.change_presence(status=discord.Status.online, activity=status)

@bot.command()
async def offline(ctx):
    if str(ctx.message.author) == "kinz_gamer":
        await bot.change_presence(status=discord.Status.offline)

@bot.command()
async def shutdown(ctx):
    if str(ctx.message.author) == "kinz_gamer":
        os._exit(0)

from flask import Flask
import threading

app = Flask(__name__)


run = False


@app.route("/")
def main():
    global run
    if run == False:
        threading.Thread(
            target=bot.run,
            args=(
                token,
            ),
        ).start()
        run = True
    return "Running"


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
