from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class UserButtons:
    link_giving_button = KeyboardButton(text="Получить ссылку | Get a link")
    back_button = KeyboardButton(text="Назад | Back")
    main_channel_button = KeyboardButton(text="Основа | Gore")
    porn_channel_button = KeyboardButton(text="18+ | Porn")
    animal_channel_button = KeyboardButton(
        text="Animal gore (animal vs animal)"
        )
    help_button = KeyboardButton(text="Помощь | Help")
    how_to_join_button = KeyboardButton(text="Как зайти на порно канал")
    message_to_admin_button = KeyboardButton(text="Связаться с админом")


class AdminButtons:
    administer_button = KeyboardButton(text="Модерация бота")
    cancel_link_editing_button = KeyboardButton(text="Отменить редактирование")


class UserKeyboards:
    start_keyboard = ReplyKeyboardMarkup(
        keyboard=[[UserButtons.link_giving_button], [UserButtons.help_button]],
        resize_keyboard=True,
    )
    channel_chosing_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                UserButtons.animal_channel_button
            ],
            [
                UserButtons.main_channel_button,
                UserButtons.porn_channel_button,
            ],
            [
                UserButtons.back_button
            ],
        ],
        resize_keyboard=True,
    )
    help_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                UserButtons.how_to_join_button,
                UserButtons.message_to_admin_button
            ],
            [
                UserButtons.back_button
            ],
        ],
        resize_keyboard=True,
    )


class AdminKeyboards:
    start_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [UserButtons.link_giving_button, UserButtons.help_button],
            [AdminButtons.administer_button],
        ],
        resize_keyboard=True,
    )
    cancel_editing_keyboard = ReplyKeyboardMarkup(
        keyboard=[[AdminButtons.cancel_link_editing_button]],
        resize_keyboard=True,
        is_persistent=True,
    )
