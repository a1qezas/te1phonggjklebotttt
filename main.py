import telebot
from telebot.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

bot = telebot.TeleBot('8033205744:AAHlgCbMmACpWiD5ohJJdO__ijjK7t_pzME')

# Клавиатура выбора языка
language_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
language_keyboard.add(
    KeyboardButton("Русский🇷🇺"),
    KeyboardButton("English🇬🇧")
)

# Клавиатура классов для русского
rus_class_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
rus_class_keyboard.add(
    KeyboardButton("Блондинки💋"),
    KeyboardButton("Брюнетки / шатенки🔞"),
    KeyboardButton("Рыжие🍓")
)

# Клавиатура классов для английского
eng_class_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
eng_class_keyboard.add(
    KeyboardButton("Blondes💋"),
    KeyboardButton("Brunettes / shades🔞"),
    KeyboardButton("Redheads🍓")
)

# ========== КОНФИГУРАЦИЯ ДАННЫХ ==========
MODELS = {
    'rus': {
        'Блондинки💋': ['Фитнесс / Стройные девушки', 'ББВ / Пышки', 'Мастурбация', 'Ноги / Фетиш контент',
                       'ФемДом / Доминация',
                       'Милфы / Мамочки', 'Косплей / Е-Герл / Альт Герл', 'Молоденькие', 'Европейки', 'Азиатки',
                       'Русские'],
        'Брюнетки / шатенки🔞': ['Фитнесс / Стройные девушки', 'ББВ / Пышки', 'Мастурбация', 'Ноги / Фетиш контент',
                       'ФемДом / Доминация',
                       'Милфы / Мамочки', 'Косплей / Е-Герл / Альт Герл', 'Молоденькие', 'Европейки', 'Азиатки',
                       'Русские'],
        'Рыжие🍓': ['Фитнесс / Стройные девушки', 'ББВ / Пышки', 'Мастурбация', 'Ноги / Фетиш контент',
                       'ФемДом / Доминация',
                       'Милфы / Мамочки', 'Косплей / Е-Герл / Альт Герл', 'Молоденькие', 'Европейки', 'Азиатки',
                       'Русские']
    },
    'eng': {
        'Blondes💋': ['Fitness / Gym girls', 'BBW / Curvy Queens', 'Masturbation content', 'Feet / Fetish content',
                     'FemDom / Domination',
                     'MILFS / Moms', 'Cosplay / E-girls / Alt girls', 'Young girls', 'Asian', 'Europeans', 'Russian'],
        'Brunettes / shades🔞': ['Fitness / Gym girls', 'BBW / Curvy Queens', 'Masturbation content', 'Feet / Fetish content',
                     'FemDom / Domination',
                     'MILFS / Moms', 'Cosplay / E-girls / Alt girls', 'Young girls', 'Asian', 'Europeans', 'Russian'],
        'Redheads🍓': ['Fitness / Gym girls', 'BBW / Curvy Queens', 'Masturbation content', 'Feet / Fetish content',
                     'FemDom / Domination',
                     'MILFS / Moms', 'Cosplay / E-girls / Alt girls', 'Young girls', 'Asian', 'Europeans', 'Russian']
    }
}

# ID для callback_data (максимально короткие)
model_ids = {
    'rus': {

        'Мастурбация': 'mast',
        'Ноги / Фетиш контент': 'fetish',  # Add this line
        'ФемДом / Доминация': 'dom',  # Add this line
        'Фитнесс / Стройные девушки': 'slim',
        'ББВ / Пышки': 'bbw',
        'Милфы / Мамочки': 'mom',
        'Косплей / Е-Герл / Альт Герл': 'cospl',
        'Молоденькие': 'youn',
        'Европейки': 'eur',
        'Азиатки': 'ais',
        'Русские': 'rus'
    },
#'Fitness / Gym girls+', 'BBW / Curvy Queens+', 'Masturbation content+', 'Feet / Fetish content+',
                     #'FemDom / Domination+',
                     #'MILFS+', 'Cosplay / E-girls / Alt girls+', 'Young girls+', 'Asian+', 'Europeans+', 'Russian'
    'eng': {
        'Feet / Fetish content': 'fetish',
        'Masturbation content': 'mast',
        'Fitness / Gym girls': 'slim',
        'BBW / Curvy Queens': 'bbw',
        'FemDom / Domination': 'dom',
        'MILFS / Moms': 'mom',
        'Cosplay / E-girls / Alt girls': 'cospl',
        'Young girls': 'youn',
        'Asian': 'ais',
        'Europeans': 'eur',
        'Russian': 'rus'
    }
}

class_ids = {
    'rus': {
        'Блондинки💋': 'wh', 'Брюнетки / шатенки🔞': 'bl', 'Рыжие🍓': 'red'
    },
    'eng': {
        'Blondes💋': 'wh', 'Brunettes / shades🔞': 'bl', 'Redheads🍓': 'red'
    }
}

# Галерея для каждой фото
GALLERIES = {
    'rus': {
        'Блондинки💋': {
            'Фитнесс / Стройные девушки': [
                {
                    'photo': 'photos/blondes/Fitness/low1.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/blondes/Fitness/low2.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/blondes/Fitness/low3.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/blondes/Fitness/low4.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                }
            ],
            'ББВ / Пышки': [
                {
                    'photo': 'photos/blondes/BBW/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Мастурбация': [
                {
                    'photo': 'photos/blondes/Mastur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Ноги / Фетиш контент': [
                {
                    'photo': 'photos/blondes/Fetish/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'ФемДом / Доминация': [
                {
                    'photo': 'photos/blondes/FemDom/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Милфы / Мамочки': [
                {
                    'photo': 'photos/blondes/MILFS/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Косплей / Е-Герл / Альт Герл': [
                {
                    'photo': 'photos/blondes/Cospl/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Молоденькие': [
                {
                    'photo': 'photos/blondes/Young/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Европейки': [
                {
                    'photo': 'photos/blondes/Eur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Азиатки': [
                {
                    'photo': 'photos/blondes/Asian/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Русские': [
                {
                    'photo': 'photos/blondes/Ru/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ]

        },
        'Брюнетки / шатенки🔞': {
            'Фитнесс / Стройные девушки': [
                {
                    'photo': 'photos/blackHair/fit1.jpg',
                    'text': "Ольга, 24 года\nБрюнетка-атлет 💪"
                }
            ],
            'ББВ / Пышки': [
                {
                    'photo': 'photos/blackHair/BBW/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Мастурбация': [
                {
                    'photo': 'photos/blackHair/Mastur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Ноги / Фетиш контент': [
                {
                    'photo': 'photos/blackHair/Fetish/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'ФемДом / Доминация': [
                {
                    'photo': 'photos/blackHair/FemDom/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Милфы / Мамочки': [
                {
                    'photo': 'photos/blackHair/MILFS/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Косплей / Е-Герл / Альт Герл': [
                {
                    'photo': 'photos/blackHair/Cospl/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Молоденькие': [
                {
                    'photo': 'photos/blackHair/Young/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Европейки': [
                {
                    'photo': 'photos/blackHair/Eur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Азиатки': [
                {
                    'photo': 'photos/blackHair/Asian/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Русские': [
                {
                    'photo': 'photos/blackHair/Ru/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ]
        },
        'Рыжие🍓':{
            'Фитнесс / Стройные девушки': [
                {
                    'photo': 'photos/blackHair/fit1.jpg',
                    'text': "Ольга, 24 года\nБрюнетка-атлет 💪"
                }
            ],
            'ББВ / Пышки': [
                {
                    'photo': 'photos/blackHair/BBW/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Мастурбация': [
                {
                    'photo': 'photos/blackHair/Mastur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Ноги / Фетиш контент': [
                {
                    'photo': 'photos/blackHair/Fetish/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'ФемДом / Доминация': [
                {
                    'photo': 'photos/blackHair/FemDom/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Милфы / Мамочки': [
                {
                    'photo': 'photos/blackHair/MILFS/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Косплей / Е-Герл / Альт Герл': [
                {
                    'photo': 'photos/blackHair/Cospl/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Молоденькие': [
                {
                    'photo': 'photos/blackHair/Young/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Европейки': [
                {
                    'photo': 'photos/blackHair/Eur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Азиатки': [
                {
                    'photo': 'photos/blackHair/Asian/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Русские': [
                {
                    'photo': 'photos/blackHair/Ru/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ]
        }
#'Fitness / Gym girls+', 'BBW / Curvy Queens+', 'Masturbation content+', 'Feet / Fetish content+',
                     #'FemDom / Domination+',
                     #'MILFS+', 'Cosplay / E-girls / Alt girls+', 'Young girls+', 'Asian+', 'Europeans+', 'Russian'
    },
    'eng': {
        'Blondes💋': {
            'Fitness / Gym girls': [
                {
                    'photo': 'photos/blondes/Fitness/low1.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/blondes/Fitness/low2.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/blondes/Fitness/low3.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/blondes/Fitnesslow4.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                }
            ],
            'BBW / Curvy Queens': [
                {
                    'photo': 'photos/blondes/BBW/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Masturbation content': [
                {
                    'photo': 'photos/blondes/Mastur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Feet / Fetish content': [
                {
                    'photo': 'photos/blondes/Fetish/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'FemDom / Domination': [
                {
                    'photo': 'photos/blondes/FemDom/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'MILFS / Moms': [
                {
                    'photo': 'photos/blondes/MILFS/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Cosplay / E-girls / Alt girls': [
                {
                    'photo': 'photos/blondes/Cospl/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Young girls': [
                {
                    'photo': 'photos/blondes/Young/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Europeans': [
                {
                    'photo': 'photos/blondes/Eur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Asian': [
                {
                    'photo': 'photos/blondes/Asian/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Russian': [
                {
                    'photo': 'photos/blondes/Ru/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ]

        },
        'Brunettes / shades🔞': {
            'Fitness / Gym girls': [
                {
                    'photo': 'photos/blackHair/Fitness/low1.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/blackHair/Fitness/low2.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/blackHair/Fitness/low3.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/blackHair/Fitness/low4.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                }
            ],
            'BBW / Curvy Queens': [
                {
                    'photo': 'photos/blackHair/BBW/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Masturbation content': [
                {
                    'photo': 'photos/blackHair/Mastur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Feet / Fetish content': [
                {
                    'photo': 'photos/blackHair/Fetish/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'FemDom / Domination': [
                {
                    'photo': 'photos/blackHair/FemDom/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'MILFS / Moms': [
                {
                    'photo': 'photos/blackHair/MILFS/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Cosplay / E-girls / Alt girls': [
                {
                    'photo': 'photos/blackHair/Cospl/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Young girls': [
                {
                    'photo': 'photos/blackHair/Young/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Europeans': [
                {
                    'photo': 'photos/blackHair/Eur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Asian': [
                {
                    'photo': 'photos/blackHair/Asian/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Russian': [
                {
                    'photo': 'photos/blackHair/Ru/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ]
        },
        'Redheads🍓': {
            'Fitness / Gym girls': [
                {
                    'photo': 'photos/redHair/Fitness/low1.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/redHair/Fitness/low2.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/redHair/Fitness/low3.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                },
                {
                    'photo': 'photos/redHair/Fitness/low4.jpg',
                    'text': "Анна, 22 года\nБлондинка-фитнес 💎\nРост: 175 см"
                }
            ],
            'BBW / Curvy Queens': [
                {
                    'photo': 'photos/redHair/BBW/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Masturbation content': [
                {
                    'photo': 'photos/redHair/Mastur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Feet / Fetish content': [
                {
                    'photo': 'photos/redHair/Fetish/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'FemDom / Domination': [
                {
                    'photo': 'photos/redHair/FemDom/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'MILFS / Moms': [
                {
                    'photo': 'photos/redHair/MILFS/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Cosplay / E-girls / Alt girls': [
                {
                    'photo': 'photos/redHair/Cospl/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Young girls': [
                {
                    'photo': 'photos/redHair/Young/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Europeans': [
                {
                    'photo': 'photos/redHair/Eur/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Asian': [
                {
                    'photo': 'photos/redHair/Asian/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ],
            'Russian': [
                {
                    'photo': 'photos/redHair/Ru/low1.jpg',
                    'text': "Мария, 25 лет\nПышная блондинка 🌸"
                }
            ]
        }
    }
}


# ========== ОСНОВНОЙ КОД ==========
def create_models_menu(models, language, class_type):
    """Создает меню с привязкой к группе"""
    markup = InlineKeyboardMarkup()
    group_id = class_ids[language][class_type]

    for model in models:
        model_id = model_ids[language][model]
        callback_data = f"group|{language[:2]}|{group_id}|{model_id}|0"
        markup.add(InlineKeyboardButton(model, callback_data=callback_data))

    return markup


def send_gallery_page(chat_id, group_type, model_name, language, class_type, model_id, class_id, lang_code, page=0):
    """Отправляет галерею с учетом группы"""
    try:
        # Access nested gallery structure
        group_galleries = GALLERIES[language].get(group_type, {})
        photos_data = group_galleries.get(model_name, [])

        # Calculate pagination
        total_pages = len(photos_data) // 3 + (1 if len(photos_data) % 3 else 0)
        page = max(0, min(page, total_pages - 1))

        # Send photos with group-specific content
        for i in range(page * 3, min((page + 1) * 3, len(photos_data))):
            photo_data = photos_data[i]
            with open(photo_data['photo'], 'rb') as photo:
                markup = InlineKeyboardMarkup()
                markup.row(
                    InlineKeyboardButton("Boosty🔥", url="https://boosty.com"),
                    InlineKeyboardButton("Private Chat🔞", url="https://t.me/IlyaV200")
                )

                bot.send_photo(
                    chat_id,
                    photo,
                    caption=f"{photo_data['text']}\n({i + 1}/{len(photos_data)})",
                    reply_markup=markup
                )

        # Navigation buttons
        nav_markup = InlineKeyboardMarkup()
        if page > 0 and page < total_pages - 1:
            nav_markup.row(
                InlineKeyboardButton("←", callback_data=f"group|{lang_code}|{class_id}|{model_id}|{page - 1}"),
                InlineKeyboardButton(f"{page + 1}/{total_pages}", callback_data="none"),
                InlineKeyboardButton("→", callback_data=f"group|{lang_code}|{class_id}|{model_id}|{page + 1}")
            )
        elif page > 0:
            nav_markup.row(
                InlineKeyboardButton("←", callback_data=f"group|{lang_code}|{class_id}|{model_id}|{page - 1}"),
                InlineKeyboardButton(f"{page + 1}/{total_pages}", callback_data="none")
            )
        else:
            nav_markup.row(
                InlineKeyboardButton(f"{page + 1}/{total_pages}", callback_data="none"),
                InlineKeyboardButton("→", callback_data=f"group|{lang_code}|{class_id}|{model_id}|{page + 1}")
            )

        bot.send_message(
            chat_id,
            f"{'Страница' if language == 'rus' else 'Page'} {page + 1}/{total_pages}",
            reply_markup=nav_markup
        )
    except Exception as e:
        print(f"Gallery error: {e}")
        bot.send_message(chat_id, "Ошибка загрузки галереи / Gallery loading error")


# Обработчики (остаются без изменений)
@bot.callback_query_handler(func=lambda call: call.data.startswith('model|'))
@bot.callback_query_handler(func=lambda call: call.data.startswith('group|'))
@bot.callback_query_handler(func=lambda call: call.data.startswith('group|'))
def handle_group_selection(call):
    try:
        _, lang_code, class_id, model_id, page = call.data.split('|')
        language = 'rus' if lang_code == 'ru' else 'eng'

        # Get group type from class_ids
        group_type = next(
            k for k, v in class_ids[language].items()
            if v == class_id
        )

        # Get model name
        model_name = next(
            k for k, v in model_ids[language].items()
            if v == model_id
        )

        send_gallery_page(
            call.message.chat.id,
            group_type,
            model_name,
            language,
            group_type,  # This is the class_type (group name)
            model_id,
            class_id,
            lang_code,
            int(page)
        )
    except Exception as e:
        print(f"Group selection error: {e}")
    finally:
        bot.answer_callback_query(call.id)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Please select language: 🇷🇺/🇬🇧", reply_markup=language_keyboard)


@bot.message_handler(func=lambda message: message.text in ['Русский🇷🇺', 'English🇬🇧'])
def handle_language_choice(message):
    if message.text == 'Русский🇷🇺':
        bot.send_message(message.chat.id,
                         """Привет 😏
 Ты в каталоге 🔥самых горячих моделей🔥 Boosty
 🔞 Здесь ты найдёшь тех, кто знает, как привлечь внимание.
 💋 Удобный выбор по параметрам.
 Выбирай, кто тебе по вкусу — и наслаждайся.""",
                         reply_markup=rus_class_keyboard)
    else:
        bot.send_message(message.chat.id,
                         """Hi 😏
 You are in the catalog of 🔥hottest models🔥 Boosty.
 🔞 Here you will find those who know how to attract attention.
 💋 Convenient selection of parameters.
 Choose who you like - and enjoy.""",
                         reply_markup=eng_class_keyboard)


@bot.message_handler(func=lambda message: message.text in ['Блондинки💋', 'Брюнетки / шатенки🔞', 'Рыжие🍓'])
def handle_russian_class(message):
    models = MODELS['rus'][message.text]
    markup = create_models_menu(models, 'rus', message.text)
    bot.send_message(message.chat.id, "Выберите модель:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Blondes💋', 'Brunettes / shades🔞', 'Redheads🍓'])
def handle_english_class(message):
    models = MODELS['eng'][message.text]
    markup = create_models_menu(models, 'eng', message.text)
    bot.send_message(message.chat.id, "Select model:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    bot.send_message(message.chat.id,
                     "Пожалуйста, используйте кнопки для выбора / Please use buttons to choose",
                     reply_markup=language_keyboard)


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)