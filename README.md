# O'z12E moylash nazorati — kompyuter ilovasi (Windows 10/11)

## Variant 1: tayyor .exe yasash (bir marta)
1. Python 3.10+ o'rnating (python.org, "Add to PATH" belgisini qo'ying).
2. `build.bat` ni ikki marta bosing. Tugagach `dist\Oz12E_Moylash.exe` hosil bo'ladi — shu faylni istalgan kompyuterga ko'chirib, Python o'rnatmasdan ishlatish mumkin.

## Variant 2: yasamasdan ishga tushirish
`start.bat` ni ikki marta bosing.

## Birinchi ishga tushirish
Oynada admin paroli chiqadi. Kirgach "Hisob" bo'limida parolni o'zgartiring va foydalanuvchilar qo'shing.
Yangi foydalanuvchi qo'shishda "Oddiy foydalanuvchi (faqat kuzatish)" rolini tanlasangiz, u elektrovozlar va moylash holatlarini ko'radi, lekin ma'lumotlarni o'zgartira olmaydi.
Ma'lumotlar: `%APPDATA%\Oz12E_Moylash\moylash.db` (zaxira uchun shu faylni nusxalang).

## Bir nechta kompyuterda umumiy ishlash (admin va xodimlar bir vaqtda)
1. Bitta doimiy yoqiq kompyuterda `server.bat` ni ishga tushiring (oyna ochiq tursin). U manzilni ko'rsatadi, masalan `http://192.168.1.10:8000`. Birinchi marta chiqqan admin parolini yozib oling. Windows xavfsizlik oynasi chiqsa, "Ruxsat berish" ni bosing.
2. Boshqa kompyuterlarda oddiy brauzerda shu manzilni oching YOKI ilovani bir marta `Oz12E_Moylash.exe --server http://192.168.1.10:8000` bilan ishga tushiring (keyin oddiy ochaveradi; mahalliy rejimga qaytish: `--local`).
3. Birovning o'zgarishi boshqalarda 3 soniya ichida avtomatik ko'rinadi.
