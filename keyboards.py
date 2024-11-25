from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🍋купить🍋')],
                                     [KeyboardButton(text='🍐Корзина🍐')],
                                     [KeyboardButton(text='💸баланс💸')],
                                     [KeyboardButton(text='🪙монета🪙')],
                                     [KeyboardButton(text='⚙️настройки⚙️'),
                                     KeyboardButton(text='ℹ️профильℹ️')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🍌банан🍌', callback_data='t-shirt')],
    [InlineKeyboardButton(text='🍏яблоко🍏', callback_data='sneakers')],
    [InlineKeyboardButton(text='🍐груша🍐', callback_data='cap')]])
referal = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='👨мои рефералы👨', callback_data='moiref')],
    [InlineKeyboardButton(text='🏆конкурс рефералов🏆', callback_data='refi')]])
obmen = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💳пополнение баланса💳', callback_data='vvod')],
    [InlineKeyboardButton(text='💰вывод средств💰', callback_data='vivod')]])
kodrefa = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ввести код реферала', callback_data='refcod')]])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)