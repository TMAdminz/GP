from os import environ
import aiohttp
from pyrogram import Client, Filters


API_ID = environ.get('API_ID','1782843')
API_HASH = environ.get('API_HASH','957019557cd7f7a6c1e10a09ce0f83f2')
BOT_TOKEN = environ.get('BOT_TOKEN','1289913030:AAHPMlrRyWGwMBUV0enlNbNu83SHm2YGeP8')
API_KEY = environ.get('API_KEY','465c8ce5f5ab0049da6147655dc5d6b2cb0d1762')


bot = Client('gplink bot', 
             api_id=API_ID, 
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)


@bot.on_message(Filters.command('start') & Filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm GPlink bot.\n"
        "**Just send me link and get short link**\n\n"
        "__ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ɢʀᴏᴜᴘ:__\n"
        "**• [@TM_Moviez](https://t.me/joinchat/AAAAAFIN2ibGFWeYBNj2Xg)**\n"
        "**• [@Tamil_BiggBoss](https://telegram.dog/joinchat/AAAAAEbnj7Sa0YPARrnXUA)**\n"
        "**• @Plethro_Movies**\n"
        "**• @TM_Group_1**\n")
        
@bot.on_message(Filters.regex(r'https?://[^\s]+') & Filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'__Generated Links__.....\n\n**{short_link}**\n\n__ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ɢʀᴏᴜᴘ:\n__**• [@TM_Moviez](https://t.me/joinchat/AAAAAFIN2ibGFWeYBNj2Xg)**\n**• [@Tamil_BiggBoss](https://telegram.dog/joinchat/AAAAAEbnj7Sa0YPARrnXUA)**\n**• @Plethro_Movies**\n**• @TM_Group_1**', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)
    
    
async def get_shortlink(link): 
    urls = 'https://gplinks.in/ https://gplinks.in/api?api=apikey&url='
    params = {'apikey': API_KEY, 'urls': link}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
            
        
bot.run()
