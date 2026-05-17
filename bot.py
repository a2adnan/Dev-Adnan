import asyncio
import requests

# 1. التوكن الجديد الموثق والآيدي
TOKEN = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4"
BOT_ID = "c495857a-a042-4750-8faf-1179db1cfa2d"
CHAT_ID = "c495857a-a042-4750-8b64-845185df3607"

# العناوين الرسمية حسب الوثائق مالتهم
BASE_URL = "https://api.karboai.com/bot"
HEADERS = {
    "Bot-Token": TOKEN,
    "Content-Type": "application/json"
}

async def send_welcome(username):
    url = f"{BASE_URL}/send-message"
    welcome_text = f"أهلاً وسهلاً بنخبتنا! نورت المجموعة يا غالي {username}، نتشرف بوجودك ويانا لتبادل الخبرات والتعاون."
    payload = {
        "chat_id": CHAT_ID,
        "content": welcome_text
    }
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        if response.status_code == 200:
            print(f"✅ تم إرسال الترحيب بنجاح لـ {username}")
        else:
            print(f"❌ فشل الإرسال. كود الحالة: {response.status_code} | الرد: {response.text}")
    except Exception as e:
        print(f"⚠️ خطأ أثناء الإرسال: {e}")

async def main():
    print("🚀 تم تشغيل نظام الفحص المستقر والآمن...")
    print("👀 البوت جاي يفحص الأعضاء كل ثانيتين هسة بدون رادار الـ WebSocket...")
    
    # مصفوفة لحفظ الأعضاء اللي رحبنا بيهم حتى لا نكرر الترحيب
    welcomed_users = set()
    first_run = True

    while True:
        try:
            # جلب قائمة أعضاء الجروب الحالية حسب نقاط النهاية بالوثائق
            url = f"{BASE_URL}/chat/{CHAT_ID}/members?limit=200"
            response = requests.get(url, headers=HEADERS)
            
            if response.status_code == 200:
                data = response.json()
                members = data.get("items", [])
                
                for member in members:
                    user_id = member.get("user_id")
                    username = member.get("nickname", "العضو الجديد")
                    is_bot = member.get("is_api_bot", False)
                    status = member.get("member_status") # "joined" أو غيرها

                    # تجاهل البوت نفسه
                    if user_id == BOT_ID or is_bot:
                        continue

                    # إذا العضو منضم وجديد ولم يتم الترحيب به من قبل
                    if status == "joined" and user_id not in welcomed_users:
                        welcomed_users.add(user_id)
                        
                        # في أول تشغيل للكود، نضيف الأعضاء القدامى للمصفوفة بدون ترحيب حتى لا يرحب بالكل مرة وحدة
                        if not first_run:
                            await send_welcome(username)
                
                # بعد أول فحص، نلغي حالة التشغيل الأول حتى يرحب باللي يدخلون وراها
                if first_run:
                    print(f"📊 تم حصر الأعضاء الحاليين بنجاح (العدد: {len(welcomed_users)}). البوت جاهز تماماً هسة لأي عضو جديد!")
                    first_run = False
                    
        except Exception as e:
            print(f"⚠️ خطأ في الاتصال بالسيرفر: {e}")
            
        # فحص كل ثانيتين
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
