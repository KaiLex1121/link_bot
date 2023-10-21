from aiogram import Router
from aiogram.filters import Command, Text, CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state

from lexicon.ru_lexicon import CommandsLexicon, UserMessagesLexicon
from keyboards.keyboards import UserKeyboards, AdminKeyboards
from config_data.config import Config, load_config
from services import services
from services.redis_logic import get_from_redis


router: Router = Router()
router.message.filter(StateFilter(default_state))


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=CommandsLexicon.start_and_help_command,
                         reply_markup=UserKeyboards.start_keyboard)


@router.message(CommandStart())
async def process_start_command(message: Message, config):
    await message.answer(text=UserMessagesLexicon.start_text,
                         reply_markup=services.get_start_keyboard_by_role(message=message, config=config))


@router.message(Text(text='Получить ссылку | Get a link'))
async def get_link(message: Message):
    await message.answer(text=UserMessagesLexicon.get_link,
                         reply_markup=UserKeyboards.channel_chosing_keyboard)


@router.message(Text(text='Основа | Gore'))
async def get_main_channel_link(message: Message):
    await message.answer(text=await get_from_redis('main_link'),
                         reply_markup=UserKeyboards.channel_chosing_keyboard,
                         disable_web_page_preview=True)


@router.message(Text(text='18+ | Porn'))
async def get_second_channel_link(message: Message):
    await message.answer(text=await get_from_redis('second_link'),
                         reply_markup=UserKeyboards.channel_chosing_keyboard,
                         disable_web_page_preview=True)


@router.message(Text(text='Помощь | Help'))
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


@router.message(Text(text='Назад | Back'))
async def get_back(message: Message, config):
    await message.answer(text=UserMessagesLexicon.start_text,
                         reply_markup=services.get_start_keyboard_by_role(message=message, config=config))
