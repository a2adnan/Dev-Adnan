import asyncio
import karbo

# التوكن الموثق مالتك
TOKEN = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4"
# آيدي الكروب مالتك
CHAT_ID = "c495857a-a042-4750-8b64-845185df3607"

async def main():
    async with karbo.KarboBot(TOKEN) as bot:
        ws = karbo.KarboBotWS(TOKEN)

        me = await bot.get_me()
        print(f"🤖 تم تشغيل البوت بنجاح! اسم البوت: {me.name}")

        @ws.on_message
        async def on_message(msg: karbo.Message):
            if msg.user_id == me.bot_id:
                return

            # الترحيب العراقي عند انضمام عضو جديد للدردشة المحددة
            if msg.chat_id == CHAT_ID and msg.type == "user_joined":
                username = msg.author.nickname if msg.author else "العضو الجديد"
                welcome_text = f"أهلاً وسهلاً بنخبتنا! نورت المجموعة يا غالي {username}، نتشرف بوجودك ويانا لتبادل الخبرات والتعاون."
                await bot.send_message(CHAT_ID, content=welcome_text)

        await ws.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
