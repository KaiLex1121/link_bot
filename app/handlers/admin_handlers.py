from aiogram import Router, F, Bot
from aiogram.filters import Text, StateFilter
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import Redis

from keyboards.inline_keyboards import InlineAdminKeyboards
from keyboards.keyboards import AdminKeyboards
from lexicon.messages import AdminMessages
from filters import admin_filters, common_filters

from states.admin_states import EditLinkState, MakeBroadcastState
from app.dao.holder import HolderDAO
from services.broadcaster import broadcast


router: Router = Router()
router.message.filter(admin_filters.AdminFilter())


@router.callback_query(
    StateFilter(default_state),
    F.data == 'create_broadcast_button_pressed'
)
async def create_broadcast(callback: CallbackQuery, state: FSMContext):

    await callback.message.delete()

    message_to_delete = await callback.message.answer(
        text="Пришли сообщение, которое хочешь отправить",
        reply_markup=AdminKeyboards.cancel_editing_keyboard,
    )

    await state.update_data({
        'message_to_delete': message_to_delete.message_id
    })

    await state.set_state(MakeBroadcastState.MESSAGE_TEXT_WRITING)


@router.message(
    StateFilter(MakeBroadcastState.MESSAGE_TEXT_WRITING),
    F.content_type == ContentType.TEXT,
    F.text != "Отменить редактирование"

)
async def broadcast_text_preview(
    message: Message,
    bot: Bot,
    state: FSMContext
):

    message_text = message.text

    msg_cor = await state.get_data()
    message_to_delete = msg_cor['message_to_delete']

    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message_to_delete
    )

    message_to_delete = await message.answer(
        text=message_text,
        reply_markup=InlineAdminKeyboards.broadcast_preview_keyboard
    )

    await state.update_data({
        'message_to_delete': message_to_delete.message_id
    })

    await state.update_data({
        'broadcast_text': message_text
    })

    await state.set_state(MakeBroadcastState.BROADCAST_PREVIEW)


@router.callback_query(
    StateFilter(MakeBroadcastState.BROADCAST_PREVIEW),
    F.data == 'cancel_broadcast_button_pressed'
)
async def cancel_broadcast(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()

    await callback.message.answer(
        text="Создание рассылки отменено",
        reply_markup=AdminKeyboards.start_keyboard
    )

    await state.clear()


@router.callback_query(
    StateFilter(MakeBroadcastState.BROADCAST_PREVIEW),
    F.data == 'confirm_broadcast_button_pressed'
)
async def confirm_broadcast(
    callback: CallbackQuery,
    bot: Bot, state: FSMContext,
    dao: HolderDAO
):
    users = await dao.user.get_all()

    fsm_data = await state.get_data()
    broadcast_text = fsm_data['broadcast_text']

    users_count = await broadcast(
        bot,
        users,
        text=broadcast_text
    )

    await callback.message.delete()

    await callback.message.answer(
        text=f"Сообщение доставлено {users_count} подпищекам",
        reply_markup=AdminKeyboards.start_keyboard
    )

    await state.clear()


@router.message(StateFilter(default_state), Text(text="Модерация бота"))
async def admin_command_handler(message: Message):
    await message.answer(
        text="Модерация бота",
        reply_markup=InlineAdminKeyboards.initial_keyboard
    )


@router.callback_query(
    StateFilter(default_state),
    F.data == 'get_links_button_pressed'
)
async def get_links(callback: CallbackQuery, redis: Redis):

    main = (await redis.get(name="main_link")).decode("utf-8")
    second = (await redis.get(name="second_link")).decode("utf-8")
    links_message = AdminMessages.get_links_message(main, second)

    if callback.message.text.strip("\n") != links_message.strip("\n"):
        await callback.message.edit_text(
            text=links_message,
            reply_markup=callback.message.reply_markup,
            disable_web_page_preview=True,
        )
    await callback.answer()


@router.callback_query(
    StateFilter(default_state),
    F.data == "edit_links_button_pressed"
)
async def edit_links(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Выбери канал",
        reply_markup=InlineAdminKeyboards.edit_links_keyboard
    )
    await callback.answer()


@router.callback_query(
    StateFilter(default_state),
    F.data == "get_back_button_pressed"
)
async def get_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Модерация бота",
        reply_markup=InlineAdminKeyboards.initial_keyboard
    )
    await callback.answer()


@router.callback_query(
    StateFilter(default_state),
    F.data == 'main_link_button_pressed'
)
@router.callback_query(
    StateFilter(default_state),
    F.data == "second_link_button_pressed"
)
async def edit_main_link_process(callback: CallbackQuery, state: FSMContext):

    CHANNEL = "Основной"
    STATE = EditLinkState.FILL_MAIN_LINK

    if callback.data == "second_link_button_pressed":
        CHANNEL = "Порно"
        STATE = EditLinkState.FILL_SECOND_LINK

    await callback.message.delete()
    await callback.message.answer(
        text=f"Пришли ссылку на {CHANNEL} канал",
        reply_markup=AdminKeyboards.cancel_editing_keyboard,
    )
    await state.set_state(STATE)


@router.message(
    StateFilter(EditLinkState.FILL_MAIN_LINK),
    F.content_type == ContentType.TEXT,
    common_filters.IsLink(),
)
@router.message(
    StateFilter(EditLinkState.FILL_SECOND_LINK),
    F.content_type == ContentType.TEXT,
    common_filters.IsLink(),
)
async def fill_link_process(message: Message, state: FSMContext, redis: Redis):
    if await state.get_state() == EditLinkState.FILL_MAIN_LINK:
        await redis.set(name="main_link", value=message.text)
    else:
        await redis.set(name="second_link", value=message.text)

    await message.answer(
        text=f"Ссылка изменена на «{message.text}»",
        reply_markup=AdminKeyboards.start_keyboard,
        disable_web_page_preview=True,
    )
    await state.clear()


@router.message(
    StateFilter(EditLinkState.FILL_MAIN_LINK),
    F.content_type == ContentType.TEXT,
    Text(text="Отменить редактирование"),
)
@router.message(
    StateFilter(EditLinkState.FILL_SECOND_LINK),
    F.content_type == ContentType.TEXT,
    Text(text="Отменить редактирование"),
)
@router.message(
    StateFilter(MakeBroadcastState.MESSAGE_TEXT_WRITING),
    F.content_type == ContentType.TEXT,
    Text(text="Отменить редактирование")
)
async def cancel_link_editing(message: Message, bot: Bot, state: FSMContext):

    await message.answer(
        text="Редактирование отменено",
        reply_markup=AdminKeyboards.start_keyboard
    )

    await state.clear()


@router.message(
    StateFilter(EditLinkState.FILL_MAIN_LINK),
    F.content_type == ContentType.TEXT
)
@router.message(
    StateFilter(EditLinkState.FILL_SECOND_LINK),
    F.content_type == ContentType.TEXT
)
async def warning_not_link(message: Message, state: FSMContext):
    await message.answer(
        text="Ты прислал не ссылку!",
        reply_markup=AdminKeyboards.cancel_editing_keyboard,
    )


async def message_echo(message: Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(text=f"Message попал сюда c состоянием {state}")


async def callback_echo(callback: CallbackQuery, state: FSMContext):
    state = await state.get_state()
    await callback.answer(text=f"Callback попал сюда c состоянием {state}")
