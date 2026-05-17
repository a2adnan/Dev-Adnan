import asyncio
import karbo
import socketio

TOKEN = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4"
BOT_ID = "c495857a-a042-4750-8faf-1179db1cfa2d"
CHAT_ID = "c495857a-a042-4750-8b64-845185df3607"

async def start_bot():
    async with karbo.KarboBot(TOKEN) as bot:
        ws = karbo.KarboBotWS(TOKEN)

        print("🤖 بوت النخبة المطور شغال الآن...")

        @ws.on_message
        async def on_message(msg: karbo.Message):
            if msg.user_id == BOT_ID:
                return

            if msg.chat_id == CHAT_ID:
                if msg.type == "user_joined" or msg.type == 1:
                    username = msg.author.nickname if msg.author else "العضو الجديد"
                    welcome_text = f"أهلاً وسهلاً بنخبتنا! نورت المجموعة يا غالي {username}، نتشرف بوجودك ويانا لتبادل الخبرات والتعاون."
                    await bot.send_message(CHAT_ID, content=welcome_text)
                    return

                if msg.content:
                    text = msg.content.strip()
                    username = msg.author.nickname if msg.author else "يا غالي"

                    if any(word in text for word in ["هلاو", "هلو", "هلا", "مرحبا"]):
                        await bot.send_message(CHAT_ID, content=f"يا مية هلا بيك {username}! نورتنا عيني.")
                    elif any(word in text for word in ["شلونكم", "شلونج", "شلونك"]):
                        await bot.send_message(CHAT_ID, content=f"الحمد لله بخير ونشكر الله {username}، أنت شلونك؟")
                    elif any(word in text for word in ["السلام عليكم", "سلام عليكم"]):
                        await bot.send_message(CHAT_ID, content=f"وعليكم السلام والرحمة والإكرام يا مية هلا بيك {username}.")

        await ws.run_forever()

async def main():
    while True:
        try:
            await start_bot()
        except (socketio.exceptions.ConnectionError, Exception) as e:
            print("⚠️ سيرفر تطبيق KarboAI واگع هسة (خطأ 502 صيانة).. راح أنتظر 10 ثواني وأرجع أتصل تلقائياً...")
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
