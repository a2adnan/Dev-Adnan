import asyncio
import karbo

# 1. التوكن والآيديات الموثقة مالتك
TOKEN = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4"
BOT_ID = "c495857a-a042-4750-8faf-1179db1cfa2d"
CHAT_ID = "c495857a-a042-4750-8b64-845185df3607"

async def main():
    # الاتصال بالسيرفر الرسمي
    async with karbo.KarboBot(TOKEN) as bot:
        ws = karbo.KarboBotWS(TOKEN)

        print("🤖 بوت النخبة شغال ومحدث بميزة الردود التلقائية!")
        print("⚡ الرادار شغال ويراقب الكروب 24 ساعة...")

        @ws.on_message
        async def on_message(msg: karbo.Message):
            # إذا الرسالة من البوت نفسه، نتجاهلها
            if msg.user_id == BOT_ID:
                return

            # نتأكد إن الرسالة جاية بداخل الكروب مالتنا
            if msg.chat_id == CHAT_ID:
                
                # أولاً: ميزة الترحيب بالعضو الجديد عند الانضمام
                if msg.type == "user_joined":
                    username = msg.author.nickname if msg.author else "العضو الجديد"
                    welcome_text = f"أهلاً وسهلاً بنخبتنا! نورت المجموعة يا غالي {username}، نتشرف بوجودك ويانا لتبادل الخبرات والتعاون."
                    await bot.send_message(CHAT_ID, content=welcome_text)
                    print(f"✅ تم الترحيب بالعضو الجديد: {username}")
                    return

                # ثانياً: ميزة الردود التلقائية على الكلمات (الدردشة)
                if msg.content:
                    text = msg.content.strip().lower()
                    username = msg.author.nickname if msg.author else "يا غالي"

                    # الرد على: هلاو أو هلا
                    if "هلاو" in text or text == "هلا":
                        reply = f"يا مية هلا بيك {username}! نورتنا عيني، شلون الصبحة؟"
                        await bot.send_message(CHAT_ID, content=reply)
                        print(f"💬 رد البوت على هلاو من: {username}")

                    # الرد على: مرحبا
                    elif "مرحبا" in text:
                        reply = f"مراحب يا غالي {username}! نورت الكروب بوجودك."
                        await bot.send_message(CHAT_ID, content=reply)
                        print(f"💬 رد البوت على مرحبا من: {username}")

                    # الرد على: شلونكم
                    elif "شلونكم" in text or "شلونج" in text:
                        reply = f"الحمد لله بنعمة ونشكر الله، إحنا بخير إذا أنتوا بخير وعافية {username}. أنت شلونك؟"
                        await bot.send_message(CHAT_ID, content=reply)
                        print(f"💬 رد البوت على شلونكم من: {username}")

                    # الرد على: السلام عليكم
                    elif "السلام عليكم" in text:
                        reply = f"وعليكم السلام والرحمة والإكرام! يا مية هلا بيك {username} وبجيتك."
                        await bot.send_message(CHAT_ID, content=reply)
                        print(f"💬 رد البوت على السلام عليكم من: {username}")

        # تشغيل الاتصال المستمر
        await ws.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
