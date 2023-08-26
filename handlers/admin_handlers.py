from aiogram import Router, F
from aiogram.filters import Command, Text, CommandStart
from aiogram.types import Message
from lexicon.lexicon import CommandsLexicon
from keyboards import keyboards
from config_data.config import load_config, Config
from filters import admin


router: Router = Router()
router.message.filter(admin.AdminFilter())


@router.message(Text(text="Модерация бота"))
async def admin_command_handler(message: Message):
    await message.answer(text='Модерация бота')