from aiogram import Router
from aiogram.filters import Command, Text, CommandStart
from aiogram.types import Message
from lexicon.lexicon import CommandsLexicon
from keyboards import keyboards
from config_data import config

router: Router = Router()


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=CommandsLexicon.start_and_help_command,
                         reply_markup=keyboards.start_keyboard)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Нажми на кнопку и получи ссылку',
                         reply_markup=keyboards.start_keyboard)


@router.message(Text(text='Получить ссылку'))
async def get_link(message: Message):
    await message.answer(text='Выбери канал',
                         reply_markup=keyboards.channel_chosing_keyboard)


@router.message(Text(text='Ссылка на основной канал'))
async def get_main_channel_link(message: Message):
    await message.answer(text=f"{config.get_main_channel_link()}",
                         reply_markup=keyboards.start_keyboard)


@router.message(Text(text='Ссылка на канал 18+'))
async def get_second_channel_link(message: Message):
    await message.answer(text=f'{config.get_second_channel_link()}',
                         reply_markup=keyboards.start_keyboard)



@router.message(Text(text='Назад'))
async def get_back(message: Message):
    await message.answer(text='Нажми на кнопку и получишь ссылку',
                         reply_markup=keyboards.start_keyboard)
