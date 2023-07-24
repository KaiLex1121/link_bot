from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon import UserKeyboardsLexicon

link_giving_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.link_giving_button)
back_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.back_button)
main_channel_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.main_channel_button)
second_channel_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.second_channel_button)

start_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[link_giving_button]],
                                                          resize_keyboard=True)

channel_chosing_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[main_channel_button, second_channel_button], [back_button]],
                                                                    resize_keyboard=True)
