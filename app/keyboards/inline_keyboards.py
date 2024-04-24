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
    edit_porn_link_button = InlineKeyboardButton(
        text="Порно канал", callback_data="porn_link_button_pressed"
    )
    edit_animal_link_button = InlineKeyboardButton(
        text="Animal gore", callback_data="animal_link_button_pressed"
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
    get_statistic_button = InlineKeyboardButton(
        text="Статистика",
        callback_data="get_statistic_button"
    )
    users_count_button = InlineKeyboardButton(
        text="Все пользователи",
        callback_data="users_count_button"
    )
    yesterday_new_users = InlineKeyboardButton(
        text="Новые пользователи за вчера",
        callback_data="yesterday_new_users_button"
    )
    yesterday_active_users = InlineKeyboardButton(
        text="Активные пользователи за вчера",
        callback_data="yestarday_active_users_button"
    )
    week_active_users = InlineKeyboardButton(
        text="Активные пользователи за вчера",
        callback_data="week_active_users_button"
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
            [
                InlineAdminButtons.get_statistic_button
            ]
        ]
    )
    edit_links_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineAdminButtons.edit_main_link_button,
                InlineAdminButtons.edit_porn_link_button,
                InlineAdminButtons.edit_animal_link_button
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
    statistic_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineAdminButtons.users_count_button,
                InlineAdminButtons.yesterday_new_users
            ],
            [
                InlineAdminButtons.week_active_users,
                InlineAdminButtons.yesterday_active_users
            ],
            [
                InlineAdminButtons.get_back_button
            ]
        ]
    )