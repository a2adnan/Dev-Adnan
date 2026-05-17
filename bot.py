import asyncio
import karbo
from replies import WORDS_REPLIES  # استدعاء ملف الردود الـ 216 الجديد

# إعدادات البوت الرسمية مالتك حجي
TOKEN = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4"
BOT_ID = "c495857a-a042-4750-8faf-1179db1cfa2d"
CHAT_ID = "c495857a-a042-4750-8b64-845185df3607"

async def main():
    async with karbo.KarboBot(TOKEN) as bot:
        ws = karbo.KarboBotWS(TOKEN)

        print("🤖 تم تشغيل الرادار والردود الـ 216 التلقائية بنجاح!")

        @ws.on_message
        async def on_message(msg: karbo.Message):
            # تجاهل رسائل البوت نفسه
            if msg.user_id == BOT_ID:
                return

            # في حال دخول عضو جديد للجروب
            if msg.chat_id == CHAT_ID and msg.type == "user_joined":
                username = msg.author.nickname if msg.author else "العضو الجديد"
                welcome_text = f"أهلاً وسهلاً بنخبتنا! نورت المجموعة يا غالي {username}، نتشرف بوجودك ويانا لتبادل الخبرات والتعاون."
                await bot.send_message(CHAT_ID, content=welcome_text)
                return

            # فحص الردود التلقائية لجميع الرسائل داخل الجروب
            if msg.chat_id == CHAT_ID and msg.content:
                text_clean = msg.content.strip() # تنظيف الفراغات
                
                # إذا كانت الكلمة موجودة في قاموس الردود
                if text_clean in WORDS_REPLIES:
                    reply_text = WORDS_REPLIES[text_clean]
                    # إرسال الرد للجروب
                    await bot.send_message(CHAT_ID, content=reply_text)
                    print(f"💬 تم الرد تلقائياً على كلمة: ({text_clean})")

        await ws.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
