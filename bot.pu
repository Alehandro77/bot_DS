import discord
from bot_logic import gen_pass
from coin import coin

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('gen_pass'):
        password = await gen_pass(10)
        await message.channel.send(password)

    elif message.content.startswith('coin'):
        otvet = await coin()
        await message.channel.send(otvet)

    elif message.content.startswith('$привет'):
        await message.channel.send("Привет!")

    elif message.content.startswith('$как дела'):
        await message.channel.send("Очень хорошо, всё время разговарию с людьми и учусь у них, очень интересно) А у Вас как дела?")

    elif message.content.startswith('$плохо'):
        await message.channel.send("Как так?( чтоже у вас такого случилось?")

    elif message.content.startswith('$хорошо'):
        await message.channel.send("Это очень замечательно) Давайте оставайтесь в таком настроение всегда! Можем для  этого ещё немного поболтать, что хотите обсудить?")

    elif message.content.startswith('$Какая сегодня погода'):
        await message.channel.send("[Например в москве егодня](https://www.gismeteo.ru/weather-moscow-4368/)")

    elif message.content.startswith('$как тебя зовут'):
        await message.channel.send("Моё имя пока держится в строжайшей тайне, но когда-нибудь вы его узнаете)!")

    elif message.content.startswith('$что ты умеешь'):
        await message.channel.send("[Здесь есть перечень моих функций](https://www.youtube.com/watch?v=xvFZjo5PgG0)")

    elif message.content.startswith('$бу'):
        await message.channel.send("[АААААААААА](https://avatars.mds.yandex.net/i?id=9def1cb3a1d4482b587e20965f39df2d8a17ee7d-12895285-images-thumbs&n=13)")

    elif message.content.startswith('$пока'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("Token")
