from googletrans import Translator


def translate_german_to_english(german_text):
    translator = Translator()
    result = translator.translate(german_text, src='de', dest='en')
    return result.text

if __name__ == "__main__":
    german_text = input("Enter German text to translate to English: ")
    english_translation = translate_german_to_english(german_text)
    print("English Translation:", english_translation)
