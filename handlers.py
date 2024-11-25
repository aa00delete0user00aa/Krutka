from aiogram import F, Router , Bot , types , Dispatcher
import datetime
import asyncio
import time
import random
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
bot = Bot(token='7669581824:AAHgxatHQ1Dv0oJnHJeGemo--1c1O0haEkw')
import app.keyboards as kb
router = Router()
class Register(StatesGroup):
    name = State()
    age = State()
    number = State()
@router.message(CommandStart())
async def cmd_start(message: Message):
    await bot.send_photo(message.chat.id, photo='https://api.neuro-holst.ru/api/v1/image/share/render/bONO9K99L86K', caption='')
    await message.answer('🏹🏹Привет!Ищешь понятный проект для инвестиций?Тогда знакомься , Wild Hunt - это доступный для всех способ заработка и инвистиций.Удачи!!🏹🏹', reply_markup=kb.main)
    await message.reply('💵💵Ты можешь покупать  охотников и получать с них стабильный доход , также ты можешь зарабатывать , учавствуя в различных конкурсах.Удачи!!!💵💵')
    global idi
    idi = str(message.from_user.id )
    global kiku
    kiku = idi
    print(idi)
    proverka_balance(idi)
def proverka_balance(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'w') as file:
        h = 0
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal = line.strip().split(',')
            file.write(f'{user},{balance},{banan},{apple},{grug},{refcod},{referal}\n')
            if user == username:
                h = 1
        if h == 0 :
            user = username
            balance = 1000
            banan = 0
            apple = 0
            grug = 0
            refcod = round(random.uniform(1, 10000000), 2)
            referal = 0
            file.write(f'{user},{balance},{banan},{apple},{grug},{refcod},{referal}\n')
def update_balance(username, new_balance):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'w') as file:
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal= line.strip().split(',')
            if user == username:
                new_balance = int(new_balance)
                balance = int(balance)
                balance = balance + new_balance
                balance = str(balance)
            file.write(f'{user},{balance},{banan},{apple},{grug},{refcod},{referal}\n')
def smotr_balance(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'r') as file:
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal = line.strip().split(',')
            if user == username:
                return balance
def smotr_refcod(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'r') as file:
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal = line.strip().split(',')
            if user == username:
                return refcod
def update_referal(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'w') as file:
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal = line.strip().split(',')
            if refcod == username:
                referal += 1
            file.write(f'{user},{balance},{banan},{apple},{grug},{refcod},{referal}\n')
def smotr_referal(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'r') as file:
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal = line.strip().split(',')
            if user == username:
                return referal
                
            

def smotr_banan(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'r') as file:
        kik = 0
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal= line.strip().split(',')
            if user == username:
                kik = 1
        if kik == 1 :
            return banan
        
def smotr_apple(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'r') as file:
        kik = 0
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal = line.strip().split(',')
            if user == username:
                kik = 1
        if kik == 1 :
            return apple
        
def smotr_grug(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'r') as file:
        kik = 0
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal = line.strip().split(',')
            if user == username:
                kik = 1
        if kik == 1 :
            return grug
print(id)      

def update_banan(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'w') as file:
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal = line.strip().split(',')
            if user == username:
                banan = int(banan)
                banan += 1
                banan = str(banan)
            print(balance)
            file.write(f'{user},{balance},{banan},{apple},{grug},{refcod},{referal}\n')

def update_apple(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'w') as file:
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal = line.strip().split(',')
            if user == username:
                apple = int(apple)
                apple += 1
                apple = str(apple)
            print(balance)
            file.write(f'{user},{balance},{banan},{apple},{grug},{refcod},{referal}\n')

def update_grug(username):
    with open('balances.txt', 'r') as file:
        lines = file.readlines()
    
    with open('balances.txt', 'w') as file:
        for line in lines:
            user, balance , banan , apple , grug , refcod , referal= line.strip().split(',')
            if user == username:
                grug = int(grug)
                grug += 1
                grug = str(grug)
            print(balance)
            file.write(f'{user},{balance},{banan},{apple},{grug},{refcod},{referal}\n')
print(id)
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')


@router.message(F.text == '🍋купить🍋')
async def catalog(message: Message):
    await message.answer('Разные фрукты приносят разное количество доходов , вот подробная информация о них:\nБанан - стоит 50 монет , приносит 2 монеты в день , работает 30 дней \nЯблоко - стоит 150 монет , приносит 5 монет в день , работает 30 дней \nГруша - стоит 300 монет , приносит 5 монеты в день , работает 90 дней\nОни перестанут работать после истечения срока учитывайте это при покупке', reply_markup=kb.catalog)
    await message.answer('Выберите нужный товар')


@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    global idi
    if int(smotr_balance(idi)) >= 50:
        await callback.message.answer('Вы купили банан')
        balance1 = -50
        print(str(idi))
        update_banan(idi)
        balance1 = int(balance1)
        update_balance(idi, str(balance1))
        await callback.message.answer('у вас осталось ' + str(smotr_balance(idi) + 'монет'))
    else:
        await callback.message.answer('у вас недостаточно средст, пополните баланс')
        

@router.callback_query(F.data == 'sneakers')
async def t_shirt(callback: CallbackQuery):
    global idi
    if int(smotr_balance(idi)) >= 150:
        await callback.message.answer('Вы купили яблоко')
        balance1 = -150
        update_apple(idi)
        update_balance(idi, str(balance1))
        await callback.message.answer('у вас осталось ' + str(smotr_balance(idi) + 'монет'))
    else:
        await callback.message.answer('у вас недостаточно средст, пополните баланс')

@router.callback_query(F.data == 'cap')
async def t_shirt(callback: CallbackQuery):
    global idi
    if int(smotr_balance(idi)) >= 300:
        await callback.message.answer('Вы купили грушу')
        balance1 = -300
        update_grug(idi)
        update_balance(idi, str(balance1))
        await callback.message.answer('у вас осталось ' + str(smotr_balance(idi) + 'монет'))
    else:
        await callback.message.answer('у вас недостаточно средст, пополните баланс')

@router.message(F.text == '🍐Корзина🍐')
async def cmd_start(message: Message):
    global idi
    idi = str(message.from_user.id )
    await message.answer('ваша корзина: \nбананов - '+ str(smotr_banan(idi)) + ' ,яблок - '+ str(smotr_apple(idi)) + ' ,груш - ' + str(smotr_banan(idi)))
@router.message(F.text == '⚙️настройки⚙️')
async def cmd_start(message: Message):
    await message.answer('Вы можете выбрать нужные настройки:\nЧтобы поменять язык введите команду /change launguage')
@router.message(F.text == '🪙монета🪙')
async def cmd_start(message: Message):
    global idi
    idi = str(message.from_user.id )
    await message.answer('Монета WHK - одна из самых конкурентоспособных монет в данный момент.Вы можете покупать и продовать ее когда захотите.\nМинимальное пополнение средств - 2 доллара💲.Минимальный вывод средств - 5 долларов💲.\nХорошая новость,в этом месяце проходит акция:\nПри пополнении от 3 долларов💲 - бонус 1 обычный охотник\nПри пополнении от 8 долларов💲 - бонус 50 монет\nПри пополнении от 20 долларов💲 - бонус 2 элитных охотника\n💱\nКурс валюты в данный момент - '+ str(round(random.uniform(1.0, 3.0), 2)), reply_markup=kb.obmen)
suma = 5
suma3 = 150
suma4 = 10
@router.callback_query(F.data == 'vvod')
async def t_shirt(callback: CallbackQuery):
    global idi , suma
    await callback.message.answer('введите сумму в долларах ,на которую вы хотите пополнить баланс')
    async def echo(message: types.Message): 
        global suma
        suma = message
    await callback.message.answer('пополните баланс на ' + str(suma) + 'долларов💲 в валюте ton по криптокошельку xn34-2/2_xzc_325ncvn , баланс пополнится автоматически')
    update_balance(idi, int(-1 * (int(suma) / round(random.uniform(1.0, 3.0), 2))))
@router.callback_query(F.data == 'vivod')
async def t_shirt(callback: CallbackQuery):
    global idi
    global price
    global suma3 
    global suma4
    await callback.message.answer('введите сумму в долларах , которуя вы хотите вывести')
    await callback.message.answer('введите номер вашего криптокошелька')
    update_balance(idi, int(int(suma3) / round(random.uniform(1.0, 3.0), 2)))
    
@router.message(F.text == '💸баланс💸')
async def cmd_start(message: Message):
    global idi
    global price
    idi = str(message.from_user.id )
    sis = smotr_balance(idi)
    await message.answer('📊')
    await message.answer('ваш баланс сейчас равен ' + str(sis))
    suma = int(smotr_banan(idi)) + int(smotr_apple(idi)) + int(smotr_banan(idi))
    await message.answer('у вас сейчас есть ' + str(suma) + ' охотников')
    price = round(random.uniform(1.0, 3.0), 2)
    await message.answer('курс монеты на данный момент - ' + str(price)+'💲', reply_markup=kb.referal)
@router.callback_query(F.data == 'moiref')
async def t_shirt(callback: CallbackQuery):
    global idi
    await callback.message.answer('у вас на данный момент ' + smotr_referal(idi) + ' рефералов😔')
    await callback.message.answer('ваш код реферала ' + str(smotr_refcod(idi)),  reply_markup=kb.kodrefa)
@router.callback_query(F.data == 'refcod')
async def t_shirt(callback: CallbackQuery):
    await callback.message.answer('Введите код реферала')
    bot = Bot(token='7669581824:AAHgxatHQ1Dv0oJnHJeGemo--1c1O0haEkw')
    dp = Dispatcher(bot)
    @dp.message_handler(content_types=types.ContentTypes.TEXT)  
    async def send_message(message: types.Message):  
        await message.reply(f'Вы написали: {message.text}') 
        global kodik
        kodik = message.text
        update_referal(kodik)
        return
    


async def t_shirt(callback: CallbackQuery):
    global idi
    await callback.message.answer('🏆 Осенний конкурс рефералов\nДрузья! Мы стартуем новый конкурс рефералов, который позволит вам получить много ценных призов и подарков.💡 В этот раз конкурс будет проводиться по двум номинациям, каждая из которых будет иметь свой список лидеров.\n1️⃣ Пользователи которые пригласят наибольшее количество активных рефералов.\n2️⃣ Пользователи чьи рефералы внесут наибольшее количество депозитов.\nВ качестве призов вы сможете получить уникальных охотников:Священный охотник , Великий охотник солнца , Безумный охотник\nваша текущая позиция - 128')
async def increase_balance(x,y,z):  
    global idi
    balanc = 50 * x
    balanc = balanc + 50 * y
    balanc = balanc + 50 * z
    update_balance(idi, balanc)
@router.callback_query(F.data == 'refi')
async def t_shirt(callback: CallbackQuery):
    global idi
    await callback.message.answer('🏆 Осенний конкурс рефералов\nДрузья! Мы стартуем новый конкурс рефералов, который позволит вам получить много ценных призов и подарков.💡 В этот раз конкурс будет проводиться по двум номинациям, каждая из которых будет иметь свой список лидеров.\n1️⃣ Пользователи которые пригласят наибольшее количество активных рефералов.\n2️⃣ Пользователи чьи рефералы внесут наибольшее количество депозитов.\nВ качестве призов вы сможете получить уникальных охотников:Священный охотник , Великий охотник солнца , Безумный охотник\nваша текущая позиция - 128')
async def increase_balance(x,y,z):  
    global idi
    balanc = 50 * x
    balanc = balanc + 50 * y
    balanc = balanc + 50 * z
    update_balance(idi, balanc)
     
    

# Функция для проверки дня и выполнения задачи  
async def daily_task(x,y,z):  
    while True:  
        current_time = datetime.datetime.now()  
        if current_time.hour == 0 and current_time.minute == 0:  # Проверьте, есть ли полночь  
            await increase_balance(x,y,z)  
        await asyncio.sleep(60)  # Проверяйте каждую минуту  

# Функция для запуска задачи  
async def on_startup(dp):  
    asyncio.create_task(daily_task(smotr_banan(idi),smotr_apple(idi),smotr_grug(idi)))  