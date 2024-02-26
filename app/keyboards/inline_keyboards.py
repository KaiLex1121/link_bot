from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class InlineAdminButtons:

    get_links_button = InlineKeyboardButton(
        text="Посмотреть ссылки", callback_data="get_links_button_pressed"
    )

    edit_links_button = InlineKeyboardButton(
        text="Изменить ссылки", callback_data="edit_links_button_pressed"
    )

    edit_main_link_button = InlineKeyboardButton(
        text="Основной канал", callback_data="main_link_button_pressed"
    )

    edit_second_link_button = InlineKeyboardButton(
        text="Порно канал", callback_data="second_link_button_pressed"
    )

    get_back_button = InlineKeyboardButton(
        text="Назад", callback_data="get_back_button_pressed"
    )

    make_broadcast_button = InlineKeyboardButton(
        text="Создать рассылку",
        callback_data="create_broadcast_button_pressed"
    )

    cancel_broadcast_button = InlineKeyboardButton(
        text="❌ ОТМЕНИТЬ ❌",
        callback_data="cancel_broadcast_button_pressed"
    )

    confirm_broadcast_button = InlineKeyboardButton(
        text="✅ ОТПРАВИТЬ ✅",
        callback_data="confirm_broadcast_button_pressed"
    )


class InlineAdminKeyboards:

    initial_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineAdminButtons.get_links_button,
                InlineAdminButtons.edit_links_button
            ],
            [
                InlineAdminButtons.make_broadcast_button
            ],
        ]
    )

    edit_links_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineAdminButtons.edit_main_link_button,
                InlineAdminButtons.edit_second_link_button,
            ],
            [
                InlineAdminButtons.get_back_button
            ],
        ]
    )

    broadcast_preview_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineAdminButtons.confirm_broadcast_button,
                InlineAdminButtons.cancel_broadcast_button

            ],
        ]
    )
