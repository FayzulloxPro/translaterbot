from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


LANGUAGESTOP = {
    'uz': '🇺🇿uzbek',     'ar': '🇦🇪arabic',
    'tr': '🇹🇷turkish',   'en': '🇬🇧english',
    'de': '🇩🇪german',    'fr': '🇫🇷french',
    'ru': '🇷🇺russian',   'it': '🇮🇹italian',
    'ja': '🇯🇵japanese',  'es': '🇪🇸spanish',
    'ko': '🇰🇷korean',    'hi': '🇮🇳hindi',
    'zh-cn': '🇨🇳chinese (simplified)',
    'zh-tw': '🇨🇳chinese (traditional)',
    'id': '🇮🇩indonesian'}

list_languages_top = InlineKeyboardMarkup(row_width=2)
for key, value in LANGUAGESTOP.items():
    list_languages_top.insert(InlineKeyboardButton(text=value, callback_data=key))
list_languages_top.insert(InlineKeyboardButton(text="❌", callback_data="delete"))


dictionary_states = {"O'zbek":"uztranslation", "Ingliz":"en_translation", "Arab":"ar_translation", "Turk":"tr_translation", "Nemis":"de_translation",
                     "Fransuz":"fr_translation", "Rus":"ru_translation", "Italyan":"it_translation", "Yapon":"ja_translation",
               "Ispan":"es_translation", "Koreys":"ko_translation", "Hind":"hi_translation", "Xitoy (soddalashgan)":"zh-cn_translation", "Xitoy (an'anaviy)":"zh-tw_translation", "Indonez":"id_translation"}




LANGUAGES1 = {
    'af': 'afrikaans',      'sq': 'albanian',
    'am': 'amharic',        'hy': 'armenian',
    'az': 'azerbaijani',    'eu': 'basque',
    'be': 'belarusian',     'bn': 'bengali',
    'bs': 'bosnian',        'bg': 'bulgarian',
    'ca': 'catalan',        'ny': 'chichewa',
    'co': 'corsican',       'hr': 'croatian',
    'cs': 'czech',          'da': 'danish',
    'nl': 'dutch',          'eo': 'esperanto',
    'et': 'estonian',       'tl': 'filipino',
    'fi': 'finnish',        'fy': 'frisian',
    'gl': 'galician',       'ka': 'georgian',
    'el': 'greek',          'gu': 'gujarati',
    'ht': 'haitian creole', 'ha': 'hausa',
    'haw': 'hawaiian',      'iw': 'hebrew'}
list_languages1 = InlineKeyboardMarkup(row_width=3)
for key, value in LANGUAGES1.items():
    list_languages1.insert(InlineKeyboardButton(text=value, callback_data=key))
list_languages1.insert(InlineKeyboardButton(text="➡️", callback_data="next1"))
list_languages1.insert(InlineKeyboardButton(text="❌", callback_data="delete"))



LANGUAGES2 = {
    'he': 'hebrew',             'hmn': 'hmong',
    'hu': 'hungarian',          'is': 'icelandic',
    'ig': 'igbo',               'ga': 'irish',
    'jw': 'javanese',           'kn': 'kannada',
    'kk': 'kazakh',             'km': 'khmer',
    'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz',
    'lo': 'lao',                'la': 'latin',
    'lv': 'latvian',            'lt': 'lithuanian',
    'lb': 'luxembourgish',      'mk': 'macedonian',
    'mg': 'malagasy',           'ms': 'malay',
    'ml': 'malayalam',          'mt': 'maltese',
    'mi': 'maori',              'mr': 'marathi',
    'mn': 'mongolian',          'my': 'myanmar (burmese)',
    'ne': 'nepali',             'no': 'norwegian',
    'or': 'odia',               'ps': 'pashto'}
list_languages2 = InlineKeyboardMarkup(row_width=3)
for key, value in LANGUAGES2.items():
    list_languages2.insert(InlineKeyboardButton(text=value, callback_data=key))
list_languages2.insert(InlineKeyboardButton(text="➡️", callback_data="next2"))
list_languages2.insert(InlineKeyboardButton(text="❌", callback_data="delete"))



LANGUAGES3 = {
    'fa': 'persian',        'pl': 'polish',
    'pt': 'portuguese',     'pa': 'punjabi',
    'ro': 'romanian',       'sm': 'samoan',
    'gd': 'scots gaelic',   'sr': 'serbian',
    'st': 'sesotho',        'sn': 'shona',
    'sd': 'sindhi',         'si': 'sinhala',
    'sk': 'slovak',         'sl': 'slovenian',
    'so': 'somali',         'su': 'sundanese',
    'sw': 'swahili',        'sv': 'swedish',
    'tg': 'tajik',          'ta': 'tamil',
    'te': 'telugu',         'th': 'thai',
    'uk': 'ukrainian',      'ur': 'urdu',
    'ug': 'uyghur',         'vi': 'vietnamese',
    'cy': 'welsh',          'xh': 'xhosa',
    'yi': 'yiddish',        'yo': 'yoruba',
    'ceb': 'cebuano',       'zu': 'zulu'}
list_languages3 = InlineKeyboardMarkup(row_width=3)
for key, value in LANGUAGES3.items():
    list_languages3.insert(InlineKeyboardButton(text=value, callback_data=key))
list_languages3.insert(InlineKeyboardButton(text="⬅️", callback_data="back"))
list_languages3.insert(InlineKeyboardButton(text="❌", callback_data="delete"))
