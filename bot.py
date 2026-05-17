import asyncio
import karbo

TOKEN = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4"
BOT_ID = "c495857a-a042-4750-8faf-1179db1cfa2d"
CHAT_ID = "c495857a-a042-4750-8b64-845185df3607"

async def main():
    async with karbo.KarboBot(TOKEN) as bot:
        ws = karbo.KarboBotWS(TOKEN)

        print("🔍 رادار الفحص الشامل شغال... اكتب أي شي بالكروب هسة أو خلي أحد يدخل")

        @ws.on_message
        async def on_message(msg: karbo.Message):
            # راح نطبع كل البيانات اللي تجي من السيرفر حتى نشوفها بعيننا
            print(f"📥 جتي رسالة! من دردشة: {msg.chat_id} | النوع: {msg.type} | النص: {msg.content}")
            
            # تجربة إرسال رسالة ترحيبية فورية لأي شي يصير بالكروب للتأكد من الصلاحية
            if msg.chat_id == CHAT_ID and msg.user_id != BOT_ID:
                try:
                    await bot.send_message(CHAT_ID, content="فحص: الرادار لقط الحركة وجاي يرسل بنجاح! ✅")
                except Exception as e:
                    print("❌ خطأ أثناء محاولة الإرسال للكروب:", e)

        await ws.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
