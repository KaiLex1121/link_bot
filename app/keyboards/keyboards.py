from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.ru_lexicon import UserKeyboardsLexicon, AdminKeyboardsLexicon


class UserButtons:
    link_giving_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.link_giving_button)
    back_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.back_button)
    main_channel_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.main_channel_button)
    second_channel_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.second_channel_button)
    help_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.help_button)
    how_to_join_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.how_to_join_button)
    message_to_admin_button: KeyboardButton = KeyboardButton(text=UserKeyboardsLexicon.message_to_admin_button)


class AdminButtons:
    administer_button: KeyboardButton = KeyboardButton(text=AdminKeyboardsLexicon.administer_button)
    cancel_editing_button: KeyboardButton = KeyboardButton(text=AdminKeyboardsLexicon.cancel_editing_button)


class UserKeyboards:
    start_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[UserButtons.link_giving_button], [UserButtons.help_button]],
                                                                        resize_keyboard=True)

    channel_chosing_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[UserButtons.main_channel_button, UserButtons.second_channel_button],
                                                                                  [UserButtons.back_button]],
                                                                        resize_keyboard=True)

    help_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[UserButtons.how_to_join_button, UserButtons.message_to_admin_button],
                                                                       [UserButtons.back_button]],
                                                                        resize_keyboard=True)


class AdminKeyboards:
    admin_start_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[UserButtons.link_giving_button, UserButtons.help_button], [AdminButtons.administer_button]],
                                                                        resize_keyboard=True)
    admin_cancel_editing_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[AdminButtons.cancel_editing_button]],
                                                                        resize_keyboard=True,
                                                                        is_persistent=True)