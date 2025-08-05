
        [KeyboardButton(text="💰 Баланс"), KeyboardButton(text="🎯 Цели")],
        [KeyboardButton(text="📊 Установить бюджет"), KeyboardButton(text="💡 Совет")]
    ],
    resize_keyboard=True
)
kb_cancel = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="❌ Отмена")]],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    uid = str(message.from_user.id)
    users = load()
    if uid not in users:
        users[uid] = {"balance": 0, "history": [], "goals": {}, "budget": 0}
        save(users)
    await message.answer(
        f"👋 Привет, <b>{message.from_user.full_name}</b>!
"
        "Я твой личный финансовый аналитик. Выбирай нужный пункт в меню ниже 👇",
        reply_markup=kb_main
    )

# ... (оставшиеся обработчики и функции добавим в следующем шаге)
