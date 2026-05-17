import asyncio
import karbo

# 1. التوكن الجدييييد الموثق مالتك جاهز هنا
TOKEN = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4"

# 2. آيدي البوت الجديد الصحيح (Bot ID)
BOT_ID = "c495857a-a042-4750-8faf-1179db1cfa2d"

# 3. آيدي الكروب مالتك (Chat ID)
CHAT_ID = "c495857a-a042-4750-8b64-845185df3607"

async def main():
    # الاتصال بالسيرفر الرسمي عبر مكتبة karbo بالتوكن الجديد
    async with karbo.KarboBot(TOKEN) as bot:
        ws = karbo.KarboBotWS(TOKEN)

        print(f"🤖 تم ربط البوت بالتوكن والآيدي الجديد بنجاح!")
        print("⚡ الرادار السحابي شغال الآن ومستعد لاستقبال الأعضاء الجدد...")

        @ws.on_message
        async def on_message(msg: karbo.Message):
            # إذا الرسالة جاية من البوت نفسه (باستخدام الآيدي الجديد)، يتجاهلها فوراً
            if msg.user_id == BOT_ID:
                return

            # الترحيب العراقي المعدل عند انضمام عضو جديد للكروب مالتك
            if msg.chat_id == CHAT_ID and msg.type == "user_joined":
                username = msg.author.nickname if msg.author else "العضو الجديد"
                
                welcome_text = f"أهلاً وسهلاً بنخبتنا! نورت المجموعة يا غالي {username}، نتشرف بوجودك ويانا لتبادل الخبرات والتعاون."
                
                await bot.send_message(CHAT_ID, content=welcome_text)
                print(f"✅ تم الترحيب بنجاح بالعضو: {username}")

        # تشغيل الاتصال المستمر 24 ساعة على السيرفر
        await ws.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
