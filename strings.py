MAIN_MENU = """
🏠 Вы можете сделать следующее

- Изменить свой профиль
- Добавить путешествие
"""

WELCOME = """
👋 Привет, {}!
Я помогу тебе зарегистрироваться в Travel Agent!

Введи свой *логин*, он будет использоваться для взаимодействия с другими пользователями 🌏

✨ Длина логина: *5-32* символа
✨ Допустимые символы: *a-z, A-Z, 0-9, _*
*Пример*: `Oleg8`

P.S. Все данные ты всегда сможешь изменить после регистрации
"""

LOGIN_IS_SET_TO = """
👤 Отлично, твой *логин*: `{}`

Теперь введи свой *возраст*

✨ Допустимый возраст: *6-130* лет
✨ *Например*: `20`
"""

AGE_IS_SET_TO = """👤 Отлично, твой возраст: `{}`

Теперь введи свой *пол*

✨ *Мужской* или *Женский*
Ты можешь воспользоваться кнопками ниже 💯
"""

SEX_IS_SET_TO = """
👤 Отлично, твой пол: `{}`

Теперь введи *место проживания* в формате "Город, Страна" или нажми на кнопку ниже (доступно только на мобильной версии Telegram)

✨ *Например*: `Москва, Россия`
"""

LOCATION_IS_SET_TO = """
👤 Отлично, ты выбрал: `{} - {}`

Теперь введи немного *о себе*

✨ Максимальная длина: *120* символов
✨ *Например*: `Меня зовут Олег, у меня много денег`

Это действие можно пропустить /skip
"""

BIO_SKIPPED = """
Хорошо. Теперь введи свои *интересы* через запятую

✨ *Например*: `футбол, программирование, музыка`

Это действие можно пропустить /skip
"""

BIO_IS_SET_TO = """
👤 Отлично, твое био: `{}`

Теперь введи свои *интересы* через запятую

✨ *Например*: `футбол, программирование, музыка`

Это действие можно пропустить /skip
"""

INTERESTS_IS_SET_TO = """
👤 Отлично, я провалидировал данные, твои интересы: `{}`

Добро пожаловать в Travel Agent! 🌏
"""

ENTER_NEW_TRAVEL = """
🗺 Введите название нового путешествия

✨ Максимальная длина: *32* символа
"""

TRAVEL_NAME_IS_SET_TO = """
🗺 Имя путешествия: {}

Теперь введите описание

✨ Максимальная длина: *120* символов
✨ *Например*: `Очень красивое путешествие`

Это действие можно пропустить /skip
"""

SHOW_TRAVEL = """
🗺 Путешествие: `{}`
Описание:
`{}`

Участники: `{}`

Чтобы построить маршрут нужно добавить минимум *две* локации
"""

SHOW_PROFILE = """
*Логин:* `{login}`
*Возраст:* `{age}`
*Пол:* `{sex}`
*Страна:* `{country}`
*Город:* `{city}`
*Интересы:* `{interests}`

*Био:*
`{bio}`

✨ Ты можешь изменить основные данные с помощью кнопок.
"""

ENTER_NEW_LOGIN = """
👤 Твой текущий логин: {login}

✨ Длина логина: *5-32* символа
✨ Допустимые символы: *a-z, A-Z, 0-9, _*
"""
ENTER_NEW_AGE = """
👤 Твой текущий возраст: {age}

✨ Допустимый возраст: *6-130* лет
"""
ENTER_NEW_SEX = """
👤 Твой текущий пол: {sex}
"""
ENTER_NEW_LOCATION = """
👤 Твой текущий город: {city}, {country}

✨ Формат ввода: *Страна*, *Город*
"""
ENTER_NEW_BIO = """
👤 Твой текущее био: {bio}

✨ Максимальная длина: *120* символов
"""
ENTER_NEW_INTERESTS = """
👤 Твой текущие интересы: {interests}

✨ Формат ввода: *Интерес1, интерес2, интерес3*
✨ Максимальное количество интересов: *10*
"""

CREATE_TRAVEL = '🚩 Создать путешествие'

ENTER_LOCATION_NAME = """
📍 Введите название локации

✨ Максимальная длина: *32* символа
Например: `Краснодар`
"""
LOCATION_NAME_IS_SET_TO = """
Название локации установлено как: {name}

Введите время начала путешествия в формате `23:59 31.12.2024`
"""
LOCATION_START_IS_SET_TO = """
Время начала установлено как: {start}

Введите время окончания путешествия в формате `23:59 31.12.2024`
"""
LOCATION_END_IS_SET_TO = """
Время окончания установлено как: {end}

✨ Все готово
"""

SHOW_LOCATION = """
📍 {name}

🚀 {start}
🏁 {end}
"""

LOCATIONS_LIST = """
📍 Список локаций для выбранного путешествия
"""

TRAVELS = """
🚩 Список твоих путешествий

Ты можешь:
- Создать путешествие
- Изменить путешествие
- Удалить путешествие
- Добавить локации
- Построить маршруты через локации
"""

BACK = '↩️ Назад'
ADD = '➕ Добавить'
EDIT = '✏️ Изменить'
DELETE = '❌ Удалить'
YES = '✅ Да'
NO = '❌ Нет'
PROFILE = '👤 Профиль'
LOGIN = '👤 Логин'
SEX = '👤 Пол'
AGE = '📆 Возраст'
CITY = '🗺️ Город'
LOCATIONS = '📍 Локации'
COUNTRY = '🌍 Страна'
BIO = '📝 Био'
INTERESTS = '👤 Интересы'
SHOW = '👁️ Показать'
WOMAN = 'Женский'
MAN = 'Мужской'
CANCEL = '↩️ Отмена'
LOCATION = '🌍 Локация'
LOADING = '☁️ Обработка данных...'
TIMEOUT_ERROR = '☁️ Превышено время ожидания, попробуйте ещё раз'
LOCATION_CANCELED = '☁️ Хорошо, попробуй уточнить данные ещё раз'
I_DONT_UNDERSTAND = 'К сожалению, я не понимаю тебя 😥'

LOGIN_ALREADY_EXISTS_ERROR = '❌ Такой логин уже существует'

LOGIN_TOO_LONG_ERROR = '❌ Логин должен содержать не более 32 символов'
LOGIN_TOO_SHORT_ERROR = '❌ Логин должен содержать не менее 5 символов'
LOGIN_INCORRECT_ERROR = '❌ Логин должен содержать только латинские буквы, цифры и нижнее подчеркивание'

AGE_TOO_HIGH_ERROR = '❌ Возраст должен быть не более 130 лет'
AGE_TOO_LOW_ERROR = '❌ Возраст должен быть не менее 6 лет'
AGE_INCORRECT_ERROR = '❌ Возраст должен быть целым положительным числом'

LOCATION_INPUT_ERROR = '❌ Проверь, что страна и город разделены запятой'
LOCATION_INCORRECT_ERROR = '❌ Введены некорректные данные'

BIO_TOO_LONG_ERROR = '❌ Био должно быть не более 120 символов'
BIO_INCORRECT_ERROR = '❌ Био должно быть строкой'

INTERESTS_INCORRECT_ERROR = '❌ Проверь, что интересы разделены запятыми'
INTERESTS_TOO_MANY_ERROR = '❌ Интересов не может быть больше 10'

DESCRIPTION_TOO_LONG_ERROR = '❌ Описание должно быть не более 120 символов'

SEX_INCORRECT_INPUT = (
    '❌ Пол введен некорректно. Возможные значения: "Мужской" или "Женский"'
)

START_INCORRECT_ERROR = '❌ Некорректное время начала'
END_INCORRECT_ERROR = '❌ Некорректное время окончания'
END_LAST_DAY_ERROR = '❌ Нельзя установить время окончания ранее, чем время начала'

NAME_TOO_LONG_ERROR = '❌ Название должно быть не более 32 символов'

EDIT_TRAVEL = '✏️ Изменить путешествие'

EDIT_TRAVEL_NAME = '✏️ Название'
EDIT_TRAVEL_DESCRIPTION = '✏️ Описание'

ENTER_TRAVEL_NAME = '📝 Введите новое название путешествия'
ENTER_TRAVEL_DESCRIPTION = '📝 Введите новое описание путешествия'

MAP = '🗺️ Маршруты'
MAPS = '🗺️ Выбери нужный тип карты, чтобы посмотреть её'
