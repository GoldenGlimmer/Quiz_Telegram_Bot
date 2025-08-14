from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from db import update_quiz_index, get_quiz_index, update_user_score

# Структура квиза
quiz_data = [
    {
        "question": "Что такое Python?",
        "options": [
            "Язык программирования",
            "Тип данных",
            "Музыкальный инструмент",
            "Змея на английском",
        ],
        "correct_option": 0,
    },
    {
        "question": "Какой тип данных используется для хранения целых чисел?",
        "options": ["int", "float", "str", "natural"],
        "correct_option": 0,
    },
    {
        "question": "Какая из перечисленных библиотек используется для построения графиков?",
        "options": ["NumPy", "TensorFlow", "Matplotlib", "Requests"],
        "correct_option": 2,
    },
    {
        "question": "Какой тип данных принимает только два значения: True(Истина) или False(Ложь)?",
        "options": ["str", "bool", "float", "list"],
        "correct_option": 1,
    },
    {
        "question": "Какая библиотека предназначена для работы с многомерными массивами и выполнения математических операций над ними?",
        "options": ["Pandas", "scikit-learn", "Seaborn", "NumPy"],
        "correct_option": 3,
    },
    {
        "question": "Какая функция используется для запроса данных от пользователя?",
        "options": ["print()", "input()", "ReadLine()", "Нет правильного ответа"],
        "correct_option": 1,
    },
    {
        "question": "Какой оператор прерывает выполнение цикла?",
        "options": ["stop", "exit", "continue", "break"],
        "correct_option": 3,
    },
    {
        "question": "Каким образом можно импортировать модуль в Python?",
        "options": ["import", "load", "install", "read"],
        "correct_option": 0,
    },
    {
        "question": "Какие условные операторы используются в синтаксисе Python?",
        "options": ["if", "else", "elif", "Всё перечисленное"],
        "correct_option": 3,
    },
    {
        "question": "Какой метод используется для удаления последнего элемента из списка?",
        "options": ["delete()", "except()", "pop()", "remove()"],
        "correct_option": 2,
    },
]


def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()

    for option in answer_options:
        builder.add(
            types.InlineKeyboardButton(
                text=option,
                callback_data=(
                    "right_answer" if option == right_answer else "wrong_answer"
                ),
            )
        )

    builder.adjust(1)
    return builder.as_markup()


async def get_question(message, user_id):

    # Получение текущего вопроса из словаря состояний пользователя
    current_question_index = await get_quiz_index(user_id)
    correct_index = quiz_data[current_question_index]["correct_option"]
    opts = quiz_data[current_question_index]["options"]
    kb = generate_options_keyboard(opts, opts[correct_index])
    await message.answer(
        f"{quiz_data[current_question_index]['question']}", reply_markup=kb
    )


async def new_quiz(message):
    user_id = message.from_user.id
    current_question_index = 0
    new_score = 0
    await update_quiz_index(user_id, current_question_index)
    await update_user_score(user_id, new_score)
    await get_question(message, user_id)
