from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import CommandsLexicon


router: Router = Router()

@router.message(Command(commands=['help', 'start']))
async def process_help_command(message: Message):
    await message.answer(text=CommandsLexicon.start_and_help_command)
