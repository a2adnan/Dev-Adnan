--[[ 
▀▄ ▄▀▀▄▄▀▀▄▄▀▀▄▄▀▀▄▄▀▀▄▄▀▀▄▄▀▀▄▀▄▄▀▀▄▄▀▀▄▄▀▀▄▄▀▀          
▀▄ ▄▀            help2  : مساعدة2            ▀▄ ▄▀ 
▀▄▀▀▄▄▀▀▄▄▀▄▄▀▀▄▄▀▀▄▄▀▄▄▀▀▄▄▀▀▄▄▀▄▄▀▀▄▄▀▀▄▄▀▄▄▀▀
--]]
do

function run(msg, matches)
  return [[ 
✔️تعمل جميع الاوامر بدون وضع / او !
ا🔸➖🔹➖🔸➖🔹➖🔸
🔰 ترقيه سوبر : لترقيه المجموعه سوبر
 🔰 تفعيل  : لتفعيل البوت ب المجموعه
 🔰 تعطيل  : لتعطيل البوت ب المجموعه
 🔰 رفع المدير : لرفع مدير للمجموعه
 
 🔰 اذاعه : لنشر كلمه ب جميع مجموعات البوت
 🔰 تشغيل البوت : لتشغيل البوت ب المجموعه معينه
 🔰 اطفاء البوت :  لاطفاء البوت ب المجموعه معينه
 🔰 اضف مطور : لاضافه مطور
 🔰 طرد البوت : لطرد البوت من المجموعه
 🔰 جلب ملف : لجلب الملف من السيرفر
🔰 فحص السيرفر : لفحص السيرفر كل 5 دقايق
🔰 اصدار : لعرض سورس البوت
🔰مطور البوت : لمعرفه مطور البوت
🔰 صوره  : بالرد للملصق المراد تحويله صوره
🔰زخرفه+ النص : لزخرفه بالعربيه
🔰زخرف+ النص: لزخرفه بالنكليزيه
🔰 ملصق: بالرد للصوره المراد تحويلها ملصق
☯-لرؤيه قائمه الاوامر الرئيسيه :اكتب مساعدة♻️

 ]]

end

return {
description = "Help list", 
usage = "Help list",
patterns = {
"(الاوامر)"
},
run = run 
}
end
