from googletrans import Translator, LANGUAGES


def translate_text(message, src, dest):
    translator = Translator()
    translation = translator.translate(message, src=src, dest=dest)
    translation = translation.text
    return translation


message = 'hello, how are you'
src = 'en'
dest = 'la'



translated_text = translate_text(message, src, dest)
print(translated_text)


# def get_destination_languages():
#     destination_languages = []
#     for code, name in LANGUAGES.items():
#         destination_languages.append((code, name))
#     return destination_languages
#
#
# # Example usage
# destination_languages = get_destination_languages()
# for code, name in destination_languages:
#     print(f"{code}: {name}")
