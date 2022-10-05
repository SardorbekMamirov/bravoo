
import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,CallbackQuery
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram .types import ReplyKeyboardMarkup, KeyboardButton,Message, Location
import sqlite3

URL = 'https://api.telegram.org/bot'

API_TOKEN = '5731140088:AAFuHbzkFir8uE6xCCjRHA19JLuszgXMTik'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# 😊✔️⬅️👇👉☺️📬💵💸💰💳🪟🪄🪄






asosiy = ReplyKeyboardMarkup(
 keyboard = [

   [
       KeyboardButton(text="ALFRAGANUS UNIVERSITY"),
 KeyboardButton(text="MA'MUN UNIVERSITETI"),
   ],
   [
       KeyboardButton(text="ISFT INSTITUTI"),
 KeyboardButton(text="TMC INSTITUTE"),
   ],
   [
       KeyboardButton(text="AL-BUKHARI UNIVERSITY"),
 KeyboardButton(text="TURON ZARMED UNIVERSITETI"),
   ],
  [
 KeyboardButton(text="TOSHKENT AMALIY FANLAR UNIVERSITETI"),
 KeyboardButton(text="NAVOIY INNOVATSIYALAR INSTITUTI"),
 ],
  [
 KeyboardButton(text="PROFI"),
  KeyboardButton(text="TURAN INTERNATIONAL UNIVERSITY"),
 ],
  [
 KeyboardButton(text="⬅️Ortga"),
   ],
 
 ],
 
 resize_keyboard=True
)


asosiy0 = ReplyKeyboardMarkup(
 keyboard = [
   [
       KeyboardButton(text="📬Biz bilan bog'lanish uchun"),
 KeyboardButton(text="📃Universitetlar haqida ma'lumot")],
   [
 KeyboardButton(text="📞Telefon nomerni yuborish" , request_contact=True),
 KeyboardButton(text="📬Fikr va mulohaza bildirish"),
 
 
   ] 
 ],
 
 resize_keyboard=True
)

# phone = ReplyKeyboardMarkup(
#  keyboard = [
#   [

#  KeyboardButton(text="📱 Telefon nomerini yuborish" , request_contact=True)
#  ],
#   [
#  KeyboardButton(text="⬅️ Ortga",)
#  ],
#  ],
 
#  resize_keyboard=True
# )

Alfraganus = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya", callback_data="Litsenziya"),
    InlineKeyboardButton(text="Yo'nalishlar", callback_data="Yo'nalishlar"),
    InlineKeyboardButton(text="Ma'lumot", callback_data="Ma'lumot")
    ],
  ]
)

@dp.message_handler(text=["ALFRAGANUS UNIVERSITY"])
async def send_settings(message: Message):
    photo = open('files/alfraganus.jpg', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali Alfraganus Universityda imtihonsiz talaba bo'ling""", reply_markup=Alfraganus)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")


Mamun = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya2", callback_data="Litsenziya2"),
    InlineKeyboardButton(text="Yo'nalishlar2", callback_data="Yo'nalishlar2"),
    InlineKeyboardButton(text="Ma'lumot", callback_data="Ma'lumot")
    ],
  ]
)


@dp.message_handler(content_types=['contact'])
async def send_phone(message: Message):
    print(message.contact)
    await bot.send_message(message.from_user.id, "Yuborilgan nomer qabul qilindi")
    

@dp.message_handler(text=["MA'MUN UNIVERSITETI"])
async def send_settings(message: Message):
    photo = open('files/bukhari.jpg', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali MA'MUN UNIVERSITETIda imtihonsiz talaba bo'ling""", reply_markup=Mamun)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")


isft = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya3", callback_data="Litsenziya3"),
    InlineKeyboardButton(text="Yo'nalishlar3", callback_data="Yo'nalishlar3"),
    InlineKeyboardButton(text="Ma'lumot3", callback_data="Ma'lumot3")
    ],
  ]
)

@dp.message_handler(text=["ISFT INSTITUTI"])
async def send_settings(message: Message):
    photo = open('files/isft.jpg', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali ISFT INSTITUTIda imtihonsiz talaba bo'ling""", reply_markup=isft)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")


tmc = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya4", callback_data="Litsenziya4"),
    InlineKeyboardButton(text="Yo'nalishlar4", callback_data="Yo'nalishlar4"),
    InlineKeyboardButton(text="Ma'lumot4", callback_data="Ma'lumot4")
    ],
  ]
)

@dp.message_handler(text=["TMC INSTITUTE"])
async def send_settings(message: Message):
    photo = open('files/tmc.jpg', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali TMC INSTITUTEda imtihonsiz talaba bo'ling""", reply_markup=tmc)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")


bukhary = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya5", callback_data="Litsenziya5"),
    InlineKeyboardButton(text="Yo'nalishlar5", callback_data="Yo'nalishlar5"),
    InlineKeyboardButton(text="Ma'lumot5", callback_data="Ma'lumot5")
    ],
  ]
)

@dp.message_handler(text=["AL-BUKHARI UNIVERSITY"])
async def send_settings(message: Message):
    photo = open('files/bukhari.jpg', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali AL-BUKHARI UNIVERSITYda imtihonsiz talaba bo'ling""", reply_markup=bukhary)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")


turon = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya6", callback_data="Litsenziya6"),
    InlineKeyboardButton(text="Yo'nalishlar6", callback_data="Yo'nalishlar6"),
    InlineKeyboardButton(text="Ma'lumot6", callback_data="Ma'lumot6")
    ],
  ]
)

@dp.message_handler(text=["TURON ZARMED UNIVERSITETI"])
async def send_settings(message: Message):
    photo = open('files/turon.jpg', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali TURON ZARMED UNIVERSITETIda imtihonsiz talaba bo'ling""", reply_markup=turon)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")







amaliy = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya7", callback_data="Litsenziya7"),
    InlineKeyboardButton(text="Yo'nalishlar7", callback_data="Yo'nalishlar7"),
    InlineKeyboardButton(text="Ma'lumot7", callback_data="Ma'lumot7")
    ],
  ]
)

@dp.message_handler(text=["TOSHKENT AMALIY FANLAR UNIVERSITETI"])
async def send_settings(message: Message):
    photo = open('files/amaliy.png', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali TOSHKENT AMALIY FANLAR UNIVERSITETIda imtihonsiz talaba bo'ling""", reply_markup=amaliy)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")


navoiy = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya8", callback_data="Litsenziya8"),
    InlineKeyboardButton(text="Yo'nalishlar8", callback_data="Yo'nalishlar8"),
    InlineKeyboardButton(text="Ma'lumot8", callback_data="Ma'lumot8")
    ],
  ]
)

@dp.message_handler(text=["NAVOIY INNOVATSIYALAR INSTITUTI"])
async def send_settings(message: Message):
    photo = open('files/navoiy.jpg', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali NAVOIY INNOVATSIYALAR INSTITUTIda imtihonsiz talaba bo'ling""", reply_markup=navoiy)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")


profi = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya9", callback_data="Litsenziya9"),
    InlineKeyboardButton(text="Yo'nalishlar9", callback_data="Yo'nalishlar9"),
    InlineKeyboardButton(text="Ma'lumot9", callback_data="Ma'lumot9")
    ],
  ]
)

@dp.message_handler(text=["PROFI"])
async def send_settings(message: Message):
    photo = open('files/profi4.png', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali PROFI Universityda imtihonsiz talaba bo'ling""", reply_markup=profi)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")



turonino = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="Litsenziya10", callback_data="Litsenziya10"),
    InlineKeyboardButton(text="Yo'nalishlar10", callback_data="Yo'nalishlar10"),
    InlineKeyboardButton(text="Ma'lumot10", callback_data="Ma'lumot10")
    ],
  ]
)

@dp.message_handler(text=["TURAN INTERNATIONAL UNIVERSITY"])
async def send_settings(message: Message):
    photo = open('files/turanint.png', 'rb')
    # await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Firmamiz orqali TURAN INTERNATIONAL UNIVERSITYda imtihonsiz talaba bo'ling""", reply_markup=turonino)
    # await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!")



@dp.message_handler(text=["⬅️Ortga"])
async def send_asosiy0(message: Message):
    await bot.send_message(message.from_user.id, "Eslatib o'tamiz❗️❗️❗️ Firmamiz orqali Litsenziyaga ega Xususiy Universitetlarga imtihonsiz talaba bo'lasiz 💯", reply_markup=asosiy0)




@dp.message_handler(text=["📬Biz bilan bog'lanish uchun"])
async def send_asosiy0(message: Message):
    await bot.send_message(message.from_user.id, "+998975320234 >>>> Sardor\n +00898888999 >>>> Javohir\n +09898998998 Kimdur\n t.me/@Sardor_B_Mamirov \n chanel>>>> t.me/bravoo_consult")



@dp.message_handler(text=["📬Fikr va mulohaza bildirish"])
async def send_idea(message: Message):
    # print(message.reply_location)
    await bot.send_message(message.from_user.id, "Hozirda ishlab chiqilmoqda")



                  #YO'NALISHLAR
                  
                  
                  
                  
@dp.callback_query_handler(text=["Yo'nalishlar"])
async def mac(call:CallbackQuery):
    photo = open('files/alfraganusfak.jpg', 'rb')
    await call.message.answer_photo(photo)


@dp.callback_query_handler(text=["Yo'nalishlar2"])
async def mac(call:CallbackQuery):
    photo = open('files/mamunfak2.png', 'rb')
    await call.message.answer_photo(photo)
    
    
@dp.callback_query_handler(text=["Yo'nalishlar3"])
async def mac(call:CallbackQuery):
    photo = open('files/isftfak.png', 'rb')
    await call.message.answer_photo(photo)



@dp.callback_query_handler(text=["Yo'nalishlar4"])
async def mac(call:CallbackQuery):
    photo = open('files/tmcfak.png', 'rb')
    await call.message.answer_photo(photo)


@dp.callback_query_handler(text=["Yo'nalishlar5"])
async def mac(call:CallbackQuery):
    photo = open('files/buhoriyfak.png', 'rb')
    await call.message.answer_photo(photo)
    
    
@dp.callback_query_handler(text=["Yo'nalishlar6"])
async def mac(call:CallbackQuery):
    photo = open('files/turonzarmedfak.png', 'rb')
    await call.message.answer_photo(photo)  
    
    
@dp.callback_query_handler(text=["Yo'nalishlar7"])
async def mac(call:CallbackQuery):
    photo = open('files/amaliyfak.jpg', 'rb')
    await call.message.answer_photo(photo)  
        
    
@dp.callback_query_handler(text=["Yo'nalishlar8"])
async def mac(call:CallbackQuery):
    photo = open('files/navoiyfak.png', 'rb')
    await call.message.answer_photo(photo)  
        
    
@dp.callback_query_handler(text=["Yo'nalishlar9"])
async def mac(call:CallbackQuery):
    photo = open('files/profifak.jpg', 'rb')
    await call.message.answer_photo(photo)  
        

@dp.callback_query_handler(text=["Yo'nalishlar10"])
async def mac(call:CallbackQuery):
    photo = open('files/turonfak.jpg', 'rb')
    await call.message.answer_photo(photo)  
            
    
      
                    #LITSENZIYALAR

@dp.callback_query_handler(text=["Litsenziya"])
async def mac(call:CallbackQuery):
    photo = open('files/alfraganuslit.jpg', 'rb')
    await call.message.answer_photo(photo)


@dp.callback_query_handler(text=["Litsenziya2"])
async def mac(call:CallbackQuery):
    photo = open('files/mamunlit.jpg', 'rb')
    await call.message.answer_photo(photo)

@dp.callback_query_handler(text=["Litsenziya3"])
async def mac(call:CallbackQuery):
    photo = open('files/isftlit.jpg', 'rb')
    await call.message.answer_photo(photo)
    
@dp.callback_query_handler(text=["Litsenziya4"])
async def mac(call:CallbackQuery):
    photo = open('files/tmclit.jpg', 'rb')
    await call.message.answer_photo(photo)
    
@dp.callback_query_handler(text=["Litsenziya5"])
async def mac(call:CallbackQuery):
    photo = open('files/buhoriylit.jpg', 'rb')
    await call.message.answer_photo(photo)
    
@dp.callback_query_handler(text=["Litsenziya6"])
async def mac(call:CallbackQuery):
    photo = open('files/turon.jpg', 'rb')
    await call.message.answer_photo(photo)
    

@dp.callback_query_handler(text=["Litsenziya7"])
async def mac(call:CallbackQuery):
    photo = open('files/amaliylit.jpg', 'rb')
    # photo2 = open('files/amaliylit2.jpg', 'rb')
    await call.message.answer_photo(photo)


@dp.callback_query_handler(text=["Litsenziya8"])
async def mac(call:CallbackQuery):
    photo = open('files/navoiylit.jpg', 'rb')
    # photo2 = open('files/amaliylit2.jpg', 'rb')
    await call.message.answer_photo(photo)



@dp.callback_query_handler(text=["Litsenziya9"])
async def mac(call:CallbackQuery):
    photo = open('files/profilit.jpg', 'rb')
    # photo2 = open('files/amaliylit2.jpg', 'rb')
    await call.message.answer_photo(photo)


@dp.callback_query_handler(text=["Litsenziya10"])
async def mac(call:CallbackQuery):
    photo = open('files/.jpg', 'rb')
    # photo2 = open('files/amaliylit2.jpg', 'rb')
    await call.message.answer_photo(photo)

@dp.message_handler(text=["📃Universitetlar haqida ma'lumot"])
async def send_asosiy(message: Message):
    await bot.send_message(message.from_user.id, "Universitetni tanlang", reply_markup=asosiy)


@dp.message_handler(commands=["start"])
async def send_basic(message: Message):
    await bot.send_message(message.from_user.id, "Assalomu Alekum messaga.from_user.username BRAVOO-CONSULT Firmasining botiga hush kelibsiz!!!\n bu bot orqali siz biz bilan hakorlik qiladigan Universitetlarning ma'lumotlarini olishingiz mumkin", reply_markup=asosiy0)


@dp.message_handler(commands=["help"])
async def send_basic(message: Message):
    await bot.send_message(message.from_user.id, "Assalomu Alekum BRAVOO-CONSULT Firmasining botiga hush kelibsiz siz help buyrug'ini tanladingiz agarda botda xatolik bo'lsa /start  tugmasini bosib ko'ring yangilanish kiritilgan bo'lishi mumkin!!!", reply_markup=asosiy0)








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)