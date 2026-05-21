const { KarboBot, KarboBotWS } = require('karboai');

// التوكن الخاص بك تم وضعه هنا بأمان
const token = "9588878f62c6d982f37c79730ca11bcb8725ad20c19f6d869c834b9e7e206c191e70ee72b718e5a158e0587f0bfccc79b8f0f9c59edf4e85dc3b5f6ac99351b4";

async function main() {
    // ربط البوت بالخدمة
    const bot = new KarboBot(token);
    const ws = new KarboBotWS(token);

    // جلب معلومات البوت للتأكد من الاتصال
    try {
        const me = await bot.getMe();
        console.log(` تم تشغيل البوت بنجاح! اسم البوت: (${me.name})`);
    } catch (error) {
        console.error(" خطأ في التوكن أو الاتصال بالسيرفر:", error.message);
        return;
    }

    // الاستماع للرسائل القادمة في المجموعات أو الخاص
    ws.on('new_message', async (msg) => {
        // تجنب رد البوت على نفسه لحمايته من التكرار اللانهائي
        if (msg.user_id === msg.author?.user_id) return; 

        console.log(`رسالة جديدة من ${msg.author?.nickname || 'مستخدم'}: ${msg.content}`);

        // مثال الرد التلقائي (Echo): البوت يعيد إرسال نفس النص الذي وصله
        if (msg.content) {
            await bot.sendMessage(msg.chat_id, `أهلاً بك! لقد استلمت رسالتك: ${msg.content}`);
        }
    });

    // تشغيل الاتصال الدائم
    await ws.runForever();
}

main().catch(console.error);
