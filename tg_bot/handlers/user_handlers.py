from aiogram import Router
from aiogram.filters import Command, Text, CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state

from lexicon.lexicon import CommandsLexicon, UserMessagesLexicon
from keyboards.keyboards import UserKeyboards, AdminKeyboards
from config_data.config import Config, load_config, get_channel_link
from services import services
from services.redis_logic import get_from_redis


router: Router = Router()
router.message.filter(StateFilter(default_state))


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=CommandsLexicon.start_and_help_command,
                         reply_markup=UserKeyboards.start_keyboard)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Выбери нужное",
                         reply_markup=services.get_start_keyboard_by_role(message=message))


@router.message(Text(text='Получить ссылку'))
async def get_link(message: Message):
    await message.answer(text='Выбери канал',
                         reply_markup=UserKeyboards.channel_chosing_keyboard)


@router.message(Text(text='Ссылка на основной канал'))
async def get_main_channel_link(message: Message):
    await message.answer(text=await get_from_redis('main_link'),
                         reply_markup=UserKeyboards.channel_chosing_keyboard,
                         disable_web_page_preview=True)


@router.message(Text(text='Помощь'))
async def get_help(message: Message):
    await message.answer(text="Какая помощь тебе нужна?",
                         reply_markup=UserKeyboards.help_keyboard)


@router.message(Text(text='Как зайти на порно канал'))
async def get_guide(message: Message):
    await message.answer(text=UserMessagesLexicon.help_message,
                         reply_markup=UserKeyboards.help_keyboard)


@router.message(Text(text='Связаться с админом'))
async def message_to_admin(message: Message):
    await message.answer(text="Держи: https://t.me/BlackTheo",
                         reply_markup=UserKeyboards.help_keyboard,
                         disable_web_page_preview=True)


@router.message(Text(text='Ссылка на канал 18+'))
async def get_second_channel_link(message: Message):
    await message.answer(text=await get_from_redis('second_link'),
                         reply_markup=UserKeyboards.channel_chosing_keyboard,
                         disable_web_page_preview=True)


@router.message(Text(text='Назад'))
async def get_back(message: Message):
    await message.answer(text="Выбери нужное",
                         reply_markup=services.get_start_keyboard_by_role(message=message))
