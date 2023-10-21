from aiogram import Router, F, Dispatcher
from aiogram.filters import Text, StateFilter, Command
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import Redis

from keyboards.inline_keyboards import InlineAdminKeyboards
from keyboards.keyboards import AdminKeyboards
from filters import admin_filters, common_filters
from services.redis_logic import get_from_redis
from states.admin_states import EditLinkState


redis: Redis = Redis()
router: Router = Router()
router.message.filter(admin_filters.AdminFilter())


@router.message(StateFilter(default_state), Text(text="Модерация бота"))
async def admin_command_handler(message: Message):
    await message.answer(text='Модерация бота',
                         reply_markup=InlineAdminKeyboards.initial_admin_keyboard)


@router.callback_query(StateFilter(default_state), F.data == "get_links_button_pressed")
async def get_link_handler(callback: CallbackQuery):

    links_message= f"""
Ссылка на основной канал: {await get_from_redis('main_link')}

Ссылка на порно канал: {await get_from_redis('second_link')}"""

    if callback.message.text.strip('\n') != links_message.strip('\n'):

        await callback.message.edit_text(text=links_message,
                                    reply_markup=callback.message.reply_markup,
                                    disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(StateFilter(default_state), F.data == "edit_links_button_pressed")
async def edit_links_handler(callback: CallbackQuery):
    await callback.message.edit_text(text="Выбери канал",
                                    reply_markup=InlineAdminKeyboards.edit_links_keyboard)
    await callback.answer()


@router.callback_query(StateFilter(default_state), F.data == "get_back_button_pressed")
async def get_back_handler(callback: CallbackQuery):
    await callback.message.edit_text(text='Модерация бота',
                         reply_markup=InlineAdminKeyboards.initial_admin_keyboard)
    await callback.answer()


@router.callback_query(StateFilter(default_state), F.data == "main_link_button_pressed")
@router.callback_query(StateFilter(default_state), F.data == "second_link_button_pressed")
async def edit_main_link_process(callback: CallbackQuery, state: FSMContext):

    CHANNEL = 'Основной'
    STATE = EditLinkState.FILL_MAIN_LINK

    if callback.data == 'second_link_button_pressed':
        CHANNEL = 'Порно'
        STATE = EditLinkState.FILL_SECOND_LINK

    await callback.message.delete()
    await callback.message.answer(text=f"Пришли ссылку на {CHANNEL} канал",
                                  reply_markup=AdminKeyboards.admin_cancel_editing_keyboard)
    await state.set_state(STATE)


@router.message(StateFilter(EditLinkState.FILL_MAIN_LINK), F.content_type == ContentType.TEXT, common_filters.IsLink())
@router.message(StateFilter(EditLinkState.FILL_SECOND_LINK), F.content_type == ContentType.TEXT, common_filters.IsLink())
async def fill_link_process(message: Message, state: FSMContext):
    if await state.get_state() == EditLinkState.FILL_MAIN_LINK:
        await redis.set(name='main_link', value=message.text)
    else:
        await redis.set(name='second_link', value=message.text)

    await message.answer(text=f'Ссылка изменена на «{message.text}»',
                         reply_markup=AdminKeyboards.admin_start_keyboard,
                         disable_web_page_preview=True)
    await state.clear()


@router.message(StateFilter(EditLinkState.FILL_MAIN_LINK), F.content_type == ContentType.TEXT, Text(text="Отменить редактирование"))
@router.message(StateFilter(EditLinkState.FILL_SECOND_LINK), F.content_type == ContentType.TEXT, Text(text="Отменить редактирование"))
async def cancel_link_editing(message: Message, state: FSMContext):
    await message.answer(text="Редактирование отменено",
                         reply_markup=AdminKeyboards.admin_start_keyboard)
    await state.clear()


@router.message(StateFilter(EditLinkState.FILL_MAIN_LINK), F.content_type == ContentType.TEXT)
@router.message(StateFilter(EditLinkState.FILL_SECOND_LINK), F.content_type == ContentType.TEXT)
async def warning_not_link(message: Message, state: FSMContext):
    await message.answer(text="Ты прислал не ссылку!",
                         reply_markup=AdminKeyboards.admin_cancel_editing_keyboard)


@router.message(~StateFilter(default_state))
async def message_echo(message: Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(text=f"Апдейт попал сюда c состоянием {state}")


@router.message(~StateFilter(default_state))
async def callback_echo(message: Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(text=f"Апдейт попал сюда c состоянием {state}")
