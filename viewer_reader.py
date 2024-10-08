import discord
from discord.ext import commands

# Вставьте сюда токен вашего бота
TOKEN = ''

# ID каналов (можно найти, включив режим разработчика в Discord)
SOURCE_CHANNEL_IDS = {
    1293295122406047898: [1293297199152758904],  # Источник 1 и его каналы-получатели
    1293297542158749830: [1293288260877025370]   # Источник 2 и его каналы-получатели
}

# Создание объекта intents с включёнными нужными событиями
intents = discord.Intents.default()
intents.message_content = True  # Чтобы бот мог считывать содержание сообщений

# Инициализация бота
# Инициализация бота с intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно подключён и работает!')

@bot.event
async def on_message(message):
    # Проверка, что сообщение не от бота и пришло из одного из источников
    if message.channel.id in SOURCE_CHANNEL_IDS and not message.author.bot:
        # Получаем список каналов-получателей для данного источника
        target_channel_ids = SOURCE_CHANNEL_IDS[message.channel.id]
        
        # Проходим по всем каналам-получателям
        for target_channel_id in target_channel_ids:
            # Найдём канал-получатель
            target_channel = bot.get_channel(target_channel_id)
            if target_channel is not None:
                # Отправим сообщение в канал-получатель
                await target_channel.send(f'{message.content}')
            else:
                print(f'Канал-получатель с ID {target_channel_id} не найден.')

# Запуск бота
bot.run(TOKEN)