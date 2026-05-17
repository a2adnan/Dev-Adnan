import asyncio
import karbo

# البيانات الخاصة بك الموثقة
TOKEN = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4"
CHAT_ID = "c495857a-a042-4750-8b64-845185df3607"

async def main():
    # فتح الاتصال عبر الـ API والـ WebSocket الرسمي
    async with karbo.KarboBot(TOKEN) as bot:
        ws = karbo.KarboBotWS(TOKEN)

        # جلب معلومات البوت وتخزين الـ bot_id لفلترة الرسائل
        me = await bot.get_me()
        print(f"🤖 تم الاتصال بنجاح! اسم البوت: {me.name} | معرف البوت: {me.bot_id}")
        print("⚡ رادار النخبة السحابي شغال الآن ومستعد لاستلام الرسائل...")

        # التسمية الصحيحة للحدث حسب الوثائق الرسمية مالتهم
        @ws.on_message
        async def on_message(msg: karbo.Message):
            # 1. فلترة وتجاهل رسائل البوت نفسه حسب نصيحة الموقع (Filter out your own messages)
            if msg.user_id == me.bot_id:
                return

            # 2. التأكد أن الرسالة قادمة من كروب النخبة المحدد
            if msg.chat_id == CHAT_ID:
                # جلب اسم الشخص المرسل
                username = msg.author.nickname if msg.author else "عضو النخبة"
                
                # فحص إذا كانت الرسالة نظامية (انضمام أو مغادرة عضو جديد type != 0)
                if msg.type != 0:
                    welcome_text = f"👑 أهلاً وسهلاً بنخبتنا الطيبين! نورت الكروب يا غالي {username}، نتشرف بوجودك ويانا لتبادل الخبرات."
                    await bot.send_message(CHAT_ID, content=welcome_text)
                    print(f"✅ تم الترحيب بالعضو النظامي الجديد: {username}")
                    return

                # جلب النص إذا كانت رسالة عادية
                text = msg.content.strip() if msg.content else ""

                # 3. قسم الردود الذكية على الكلمات
                if "السلام عليكم" in text or "سلام عليكم" in text:
                    await bot.send_message(CHAT_ID, content="وعليكم السلام ورحمة الله وبركاته، مية هلا بيك يا غالي بنخبتنا! 🌹")
                    print("✅ رد البوت: السلام")

                elif any(word in text for word in ["شلونك", "شلونكم", "شخباركم"]):
                    await bot.send_message(CHAT_ID, content="الحمد لله بنعمة وفضل من الله، أنت شلونك حجي يا طيب؟ إن شاء الله بخير وعافية.")
                    print("✅ رد البوت: شلونك")

                elif any(word in text for word in ["هلا", "هلاو", "مرحبا", "نورت"]):
                    await bot.send_message(CHAT_ID, content=f"يا مية هلا ونورتنا بحضورك الغالي يا {username}! كلك ذوق.")
                    print("✅ رد البوت: الترحيب")

        # تشغيل الرادار بشكل مستمر
        await ws.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
