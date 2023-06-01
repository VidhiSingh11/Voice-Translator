import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pygame
import os

dic_language = {
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
    'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
    'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
    'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
    'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
    'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
    'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
    'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
    'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
    'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb',
    'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi',
    'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no',
    'odia': 'or', 'pashto': 'ps', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa',
    'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st',
    'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so',
    'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta',
    'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz',
    'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'
}

def take_command():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nKindly speak in the microphone.\nListening to the Voice")
        r1.pause_threshold = 1
        audio1 = r1.listen(source)

    try:
        print("Processing the voice")
        query_1 = r1.recognize_google(audio1, language='en-in')
        print(f"The User Spoke: {query_1}\n")
    except Exception as ep:
        print("The user is requested to please say that again")
        return "None"
    return query_1

query_1 = take_command()
while query_1 == "None":
    query_1 = take_command()

def destination_language():
    print("Please name the language in which you want to convert the above input.")
    print()

    to_language = take_command()
    while to_language == "None":
        to_language = take_command()
    to_language = to_language.lower()
    return to_language

to_language = destination_language()

while to_language not in dic_language:
    print("The language in which the user wants to convert the voice command is currently not available. Please input some other language.")
    print()
    to_language = destination_language()

to_language = dic_language[to_language]
translator1 = Translator()
text_to_translate_1 = translator1.translate(query_1, dest=to_language)
text1 = text_to_translate_1.text

speak = gTTS(text=text1, lang=to_language, slow=False)
speak.save("captured_JTP_voice.mp3")

pygame.mixer.init()
pygame.mixer.music.load("captured_JTP_voice.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

pygame.mixer.quit()
os.remove('captured_JTP_voice.mp3')

print("The translated pharse is\n", text1)
print()
