import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
from discord.ext.commands import Bot, guild_only
import asyncio
import json

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("че?")
    
@bot.command()
async def хелп(ctx, member: discord.Member, time: int, about, amount=2):          
    await ctx.send(
        embed=discord.Embed(title=f"Ввести хелп?", color = 0xdad2a0, description=f""),
        components=[[
            Button(style=ButtonStyle.green, label="Да"),
            Button(style=ButtonStyle.red, label="нит")
        ]]
    )
    
    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Да":
            
            Banrole = discord.utils.get(ctx.guild.roles, id = 782860339342737408)
            await member.add_roles(Banrole)
            
            embed = discord.Embed(color = 0xdad2a0, title=":closed_book: Основные команды :closed_book:", description=f"Общие команды, помогающие делать мир лучше!\nСпециально для **Всех**!\n \n \n**Пользовательские команды** :speech_balloon:\n \n`!sendmember` < - Отправить сообщение участнику в лс\n \n`!send` < - Написать сообщение от имени бота\n \n`!report` < - Написать жалобу на участника.\n \n \n**Модерация** :crystal_ball:\n \n`!роль` < - Выдать роль\n \n`!бан` < - Забанить участника\n \n`!разбан` < - Разбанить участника\n \n`!мут` < - Замьютить участника\n \n`!размут` < - Размьютить участника\n \n \nПодробее об команде: `!help_команда`\n \n")
            await ctx.send(embed = embed)
            
            await ctx.channel.purge(limit=amount)
        
        else:
            await ctx.channel.purge(limit=amount)
            
            
@bot.command()
async def репорт(ctx):
    await ctx.send(
        "Hello, World!",
        components=[
            Select(
                placeholder="select something!",
                options=[SelectOption(label="a", value="A"), SelectOption(label="b", value="B")],
                disabled=False,
            )
        ],
    )

    interaction = await bot.wait_for("select_option")
    await interaction.respond(content=f"{interaction.component[0].label} selected!")
    

bot.run("ODYzMjk1MzE1MTI1NDY5MjE0.YOk0ag.vSVpoP6--F-VawuVawHGx-NpuGY")
