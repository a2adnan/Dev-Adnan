import asyncio
import karbo

TOKEN = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4"
BOT_ID = "c495857a-a042-4750-8faf-1179db1cfa2d"
CHAT_ID = "c495857a-a042-4750-8b64-845185df3607"

async def main():
    async with karbo.KarboBot(TOKEN) as bot:
        ws = karbo.KarboBotWS(TOKEN)

        print("🤖 رادار النخبة المطور شغال سحابياً ومستعد لقراءة الدردشة...")

        @ws.on_message
        async def on_message(msg: karbo.Message):
            # تجاهل رسايل البوت نفسه
            if msg.user_id == BOT_ID:
                return

            # التأكد أن الرسالة داخل كروب النخبة المحدود
            if msg.chat_id == CHAT_ID:
                text = msg.content.strip() if msg.content else ""
                username = msg.author.nickname if msg.author else "العضو"

                # 1. قسم الردود الذكية على الكلمات
                if text in ["السلام عليكم", "سلام عليكم", "السلام عليكم ورحمة الله"]:
                    await bot.send_message(CHAT_ID, content=f"وعليكم السلام ورحمة الله وبركاته، مية هلا بيك يا غالي بنخبتنا! 🌹")
                    return

                elif any(word in text for word in ["شلونك", "شلونكم", "شخباركم"]):
                    await bot.send_message(CHAT_ID, content=f"الحمد لله بنعمة وفضل من الله، أنت شلونك حجي يا طيب؟ إن شاء الله بخير.")
                    return

                elif any(word in text for word in ["هلا", "هلاو", "مرحبا", "نورت"]):
                    await bot.send_message(CHAT_ID, content=f"يا مية هلا ونورتنا بحضورك الغالي! كلك ذوق.")
                    return

                # 2. قسم الرادار النظامي (إذا كان الدخول أو الخروج يرسل رسالة نظامية type تختلف عن 0)
                if msg.type != 0:
                    # بما أن السيستم يرسل إشعار نظامي، البوت سيفحص الاسم ويرحب فوراً
                    welcome_text = f"👑 نورت الكروب يا غالي {username}! أهلاً وسهلاً بيك في مجموعة النخبة، نتشرف بوجودك ويانا."
                    await bot.send_message(CHAT_ID, content=welcome_text)

        await ws.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
