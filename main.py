import aiogram
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import KeyboardButton,ReplyKeyboardRemove,ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import filters
import sqlite3 as sq
import re
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage



TOKEN_API = ""

with sq.connect("oiscit.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Monoblock(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    room INTEGER,
    brand TEXT,
    model TEXT,
    number INTEGER)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Printer(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        room INTEGER,
        brand TEXT,
        seria TEXT,
        model TEXT,
        number INTEGER)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS PC(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        room INTEGER,
        brand TEXT,
        model TEXT,
        number INTEGER)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Screen(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            room INTEGER,
            brand TEXT,
            model TEXT,
            number INTEGER)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS NoteBook(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            room INTEGER,
            brand TEXT,
            model TEXT,
            number INTEGER)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS MiniPC(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            room INTEGER,
            brand TEXT,
            model TEXT,
            number INTEGER)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Proector(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            room INTEGER,
            brand TEXT,
            model TEXT,
            number INTEGER)
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS Teacher(
            user_id TEXT NOT NULL PRIMARY KEY,
            surname TEXT,
            name TEXT,
            patronymic TEXT,
            login TEXT,
            password TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Admin(
                user_id TEXT NOT NULL PRIMARY KEY,
                surname TEXT,
                name TEXT,
                patronymic TEXT,
                login TEXT,
                password TEXT )""")
    cur.executescript("""
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438712);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438734);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438776);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438735);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438709);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438761);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438123);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438823);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438711);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438722);
    insert into Monoblock (room, brand,model,number) values (321,"HP","22-df0097ur",222067438733);
    insert into Monoblock (room, brand,model,number) values (204,"DEPO","Neos MF724",222067438744);
    insert into Monoblock (room, brand,model,number) values (204,"DEPO","Neos MF724",222067438554);
    insert into Monoblock (room, brand,model,number) values (204,"DEPO","Neos MF724",222067438576);
    insert into Monoblock (room, brand,model,number) values (205,"DEPO","Neos MF724",222067438798);
    insert into Monoblock (room, brand,model,number) values (205,"DEPO","Neos MF724",222067438555);
    insert into Monoblock (room, brand,model,number) values (402,"DEPO","Neos MF524",222067438777);
    insert into Monoblock (room, brand,model,number) values (402,"DEPO","Neos MF524",222067438778);


    insert into Printer (room, brand,seria,model,number) values (204,"Kyocera","Ecosys","M2040dn",222067438152);
    insert into Printer (room, brand,seria,model,number) values (205,"Kyocera","Ecosys","M2040dn",222067438152);
    insert into Printer (room, brand,seria,model,number) values (205,"Kyocera","TaskAlfa","M2135dn",222067438188);
    insert into Printer (room, brand,seria,model,number) values (402,"Kyocera","Ecosys","M2335dw",222067438170);
    insert into Printer (room, brand,seria,model,number) values (402,"HP","LaserJet","107w",222067438199);


    insert into Proector (room, brand,model,number) values (407,"Epson" ,"E20",222067438312);
    insert into Proector (room, brand,model,number) values (221,"Epson" ,"982W",222067438333);
    insert into Proector (room, brand,model,number) values (221,"Epson" ,"982W",222067438345);
    insert into Proector (room, brand,model,number) values (119,"Epson" ,"982W",222067438345);


    insert into NoteBook (room, brand,model,number) values (211,"HP","15s-eq1129ur",01361212);
    insert into NoteBook (room, brand,model,number) values (211,"HP","15s-eq1129ur",01361222);
    insert into NoteBook (room, brand,model,number) values (103,"HP","15s-eq1129ur",01361212);


    insert into Pc (room, brand,model,number) values (112,"DEXP","XC-830",01361233);
    insert into Pc (room, brand,model,number) values (112,"DEXP","XC-830",01361234);
    insert into Pc (room, brand,model,number) values (112,"DEXP","XC-850",01361235);
    insert into Pc (room, brand,model,number) values (117,"DEXP","XC-830",01361236);
    insert into Pc (room, brand,model,number) values (117,"DEXP","XC-850",01361237);
    insert into Pc (room, brand,model,number) values (118,"DEXP","XC-830",01361238);
    insert into Pc (room, brand,model,number) values (115,"DEXP","XC-830",01361239);
    insert into Pc (room, brand,model,number) values (108,"DEXP","XC-850",01361230);
    insert into Pc (room, brand,model,number) values (108,"DEXP","XC-830",01361231);
    insert into Pc (room, brand,model,number) values (108,"DEXP","XC-830",01361232);


    insert into Screen (room, brand,model,number) values (112,"Acer","V206HQLAb",01361241);
    insert into Screen (room, brand,model,number) values (112,"Acer","V206HQLAb",01361242);
    insert into Screen (room, brand,model,number) values (112,"Acer","V206HQLAb",01361243);
    insert into Screen (room, brand,model,number) values (117,"Acer","V206HQLAb",01361244);
    insert into Screen (room, brand,model,number) values (117,"Acer","223V5LSB2",01361245);
    insert into Screen (room, brand,model,number) values (118,"Acer","223V5LSB2",01361246);
    insert into Screen (room, brand,model,number) values (115,"Acer","223V5LSB2",01361247);
    insert into Screen (room, brand,model,number) values (108,"ViewSonic","E2422HN",01361248);
    insert into Screen (room, brand,model,number) values (108,"ViewSonic","E2422HN",01361249);
    insert into Screen (room, brand,model,number) values (108,"ViewSonic","E2422HN",01361240);

    insert into MiniPC (room, brand,model,number) values (119,"Acer","PN41-BBC086MV",01361234);
    insert into MiniPC (room, brand,model,number) values (202,"Acer","PN41-BBC086MV",01361235);
    insert into MiniPC (room, brand,model,number) values (102,"Acer","PN41-BBC086MV",01361236);
    insert into MiniPC (room, brand,model,number) values (102,"Acer","PN41-BBC086MV",01361237);
    insert into MiniPC (room, brand,model,number) values (301,"Acer","PN41-BBC086MV",01361238);

    """)

con.commit()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot,storage=MemoryStorage())

class ProfileStateGroup(StatesGroup):
    surname = State()
    name = State()
    patronymic = State()
    login = State()
    password = State()
    room = State()
    model = State()
    seria = State()
    brand = State()
    number = State()

class BrokenCall(StatesGroup):
    thing = State()
    auditoria = State()

ikbInventory = InlineKeyboardMarkup(row_width=2)
ibInventory1 = InlineKeyboardButton(text="Принтеры",callback_data="Printers")
ibInventory2 = InlineKeyboardButton(text="Моноблоки",callback_data="Mono-blocks")
ibInventory3 = InlineKeyboardButton(text="ПК",callback_data="PCs")
ibInventory4 = InlineKeyboardButton(text="Ноутбуки",callback_data="Notebooks")
ibInventory5 = InlineKeyboardButton(text="Проекторы",callback_data="Proectors")
ibInventory6 = InlineKeyboardButton(text="МиниПК",callback_data="MiniPCs")
ibInventory7 = InlineKeyboardButton(text="Мониторы",callback_data="Screens")

ikbInventory.add(ibInventory1, ibInventory2,ibInventory3,ibInventory4,ibInventory5,ibInventory6,ibInventory7)
kbGuest = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
kbUser = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
kbAdmin = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
kbGuest.add((KeyboardButton("/регистрация")))
kbUser.add(KeyboardButton("/SOS"))
kbAdmin.add((KeyboardButton("/inventory")))

@dp.message_handler(commands=['регистрация'])
async def reg_command(message: types.Message):
     await message.answer("Введите Вашу фамилию")
     await ProfileStateGroup.next()
@dp.message_handler(state=ProfileStateGroup.surname)
async def surname_load(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await message.reply('Введите Ваше имя')
    await ProfileStateGroup.name.set()  # ожидание ботом ответа
@dp.message_handler(state=ProfileStateGroup.name)
async def name_load(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.reply('Введите Ваше отчество')
    await ProfileStateGroup.next()
@dp.message_handler(state=ProfileStateGroup.patronymic)
async def patronymic_load(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text
    await message.reply('Введите Ваш логин')
    await ProfileStateGroup.next()
@dp.message_handler(state=ProfileStateGroup.login)
async def login_load(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text
        await message.reply('Введите Ваш пароль')
        await ProfileStateGroup.next()
@dp.message_handler(state=ProfileStateGroup.password)
async def password_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
    print(data)
    if data['password'] == "q1w2":
        await create_admin(user_id=message.from_user.id)
        await edit_adminLogin(state,user_id=message.from_user.id)
        await message.answer(text = "Поздравляю, Вы зарегестрированны как Админ", reply_markup=kbAdmin)
    else:
        await create_teacher(user_id=message.from_user.id)
        await edit_teacherLogin(state, user_id=message.from_user.id)
        await message.reply("Поздравляю, Ваш профиль успешно создан!",reply_markup=kbUser)
    await state.finish()
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в чат-бот технического отдела", reply_markup=kbGuest)
@dp.message_handler(commands=['SOS'])
async def sos_command(message: types.Message):
    await message.answer("Опишите вкратце поломку")
    await BrokenCall.next()
@dp.message_handler(state=BrokenCall.thing)
async def thing_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['thing'] = message.text
    await message.reply('Введите № аудитории')
    await BrokenCall.next()  # ожидание ботом ответа
@dp.message_handler(state=BrokenCall.auditoria)
async def auditoria_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['auditoria'] = message.text
        await state.finish()
        print(data)
        admins = get_admins()
        for row in admins:
            await bot.send_message(row[0], data['thing'])
            await bot.send_message(row[0], data['auditoria'])
        await bot.send_message(message.from_user.id, text="Заявка принята, специалист уже в пути")
def get_admins():
    return cur.execute('select user_id from Admin').fetchall()
@dp.message_handler(commands=['inventory'])
async def inventory_command(message: types.Message):
    users_id = str(message.from_user.id)
    cur.execute(
      "SELECT count(*) FROM Admin WHERE user_id = ?", (users_id,))
    info = cur.fetchone()[0]
    if info == 0:
        await message.answer("У вас нет доступа")
    else:
        await message.answer(text="Выберите категорию", reply_markup=ikbInventory)
def get_monoblocks():
        zapros = cur.execute("SELECT room, brand, model, number from Monoblock order by room")
        data = zapros.fetchall()

        m = []

        for i in data:
            m.append(i)

        l = len(data)
        g = []

        for i in range(l):
            a = re.sub("|\(|\'|\,|\)","",str(m[i]))
            g.append(a)
        c = []

        for i in g:

            q = i + "\n"
            c.append(q)

        v = "\n".join(c)
        return v
def get_printers():
    zapros = cur.execute("SELECT room, brand, seria, model, number from Printer order by room")
    data = zapros.fetchall()

    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub("|\(|\'|\,|\)", "", str(m[i]))
        g.append(a)
    c = []

    for i in g:
        q = i + "\n"
        c.append(q)

    v = "\n".join(c)
    return v
def get_proectors():
    zapros = cur.execute("SELECT room, brand, model, number from Proector order by room")
    data = zapros.fetchall()

    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub("|\(|\'|\,|\)", "", str(m[i]))
        g.append(a)
    c = []

    for i in g:
        q = i + "\n"
        c.append(q)

    v = "\n".join(c)
    return v
def get_notebooks():
    zapros = cur.execute("SELECT room, brand, model, number from NoteBook order by room")
    data = zapros.fetchall()
    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub("|\(|\'|\,|\)", "", str(m[i]))
        g.append(a)
    c = []

    for i in g:
        q = i + "\n"
        c.append(q)

    v = "\n".join(c)
    return v
def get_pc():
    zapros = cur.execute("SELECT room, brand, model, number from PC order by room")
    data = zapros.fetchall()

    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub("|\(|\'|\,|\)", "", str(m[i]))
        g.append(a)
    c = []

    for i in g:
        q = i + "\n"
        c.append(q)

    v = "\n".join(c)
    return v
def get_minipc():
    zapros = cur.execute("SELECT room, brand, model, number from MiniPC order by room")
    data = zapros.fetchall()

    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub("|\(|\'|\,|\)", "", str(m[i]))
        g.append(a)
    c = []

    for i in g:
        q = i + "\n"
        c.append(q)

    v = "\n".join(c)
    return v
def get_screens():
    zapros = cur.execute("SELECT room, brand, model, number from Screen order by room")
    data = zapros.fetchall()

    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub("|\(|\'|\,|\)", "", str(m[i]))
        g.append(a)
    c = []

    for i in g:
        q = i + "\n"
        c.append(q)

    v = "\n".join(c)
    return v

@dp.callback_query_handler()
async def category_callback(callback: types.CallbackQuery):
    if callback.data == "Mono-blocks":
        await callback.message.answer("Моноблоки")
        await callback.message.answer(get_monoblocks())
    if callback.data == "Printers":
        await callback.message.answer("Принтеры")
        await callback.message.answer(get_printers())
    if callback.data == "Proectors":
       await callback.message.answer("Проекторы")
       await callback.message.answer(get_proectors())
    if callback.data == "Notebooks":
        await callback.message.answer("Ноутбуки")
        await callback.message.answer(get_notebooks())
    if callback.data == "PCs":
        await callback.message.answer("ПК")
        await callback.message.answer(get_pc())
    if callback.data == "MiniPCs":
        await callback.message.answer("МиниПК")
        await callback.message.answer(get_minipc())
    if callback.data == "Screens":
        await callback.message.answer("Мониторы")
        await callback.message.answer(get_screens())
async def create_admin(user_id):
    user = cur.execute("select 1 from Admin where user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("insert into Admin values(?,?,?,?,?,?) ",(user_id,'','','','',''))
        con.commit()
async def edit_adminLogin(state,user_id):
    async with state.proxy() as data:
        cur.execute("update Admin set surname ='{}', name='{}', patronymic = '{}', login='{}', password = '{}' where user_id =='{}'".format(
            data['surname'],data['name'],data['patronymic'],data['login'],data['password'],user_id))
        con.commit()

async def create_teacher(user_id):
    user = cur.execute("select 1 from Teacher where user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("insert into Teacher values(?,?,?,?,?,?) ", (user_id, '', '', '', '',''))
        con.commit()
async def edit_teacherLogin(state,user_id):
    async with state.proxy() as data:
        cur.execute("update Teacher set surname ='{}', name='{}', patronymic = '{}', login='{}', password = '{}' where user_id =='{}'".format(
            data['surname'],data['name'],data['patronymic'],data['login'],data['password'],user_id))
        con.commit()
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
