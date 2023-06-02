import tkinter as tk
from tkinter import ttk
from googletrans import Translator


def start_translate():
    src, dest = srcchoosen.get(), destchoosen.get()
    src, dest = lan_dict[src], lan_dict[dest]

    message = src_text.get(1.0, tk.END)

    translation = translator.translate(message, src=src, dest=dest)
    translation = translation.text

    dest_text.delete(1.0, tk.END)
    dest_text.insert(tk.END, translation)


window = tk.Tk()
window.title('Translator')
window.geometry('505x300')
window.resizable(False, False)
window.configure(bg='#F3F4F4')

translator = Translator()

lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
            'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
            'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny',
            'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co',
            'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
            'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr',
            'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el',
            'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw',
            'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is',
            'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
            'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko',
            'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
            'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg',
            'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr',
            'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no',
            'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt',
            'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd',
            'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si',
            'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su',
            'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th',
            'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz',
            'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}


style = ttk.Style()
style.theme_use('clam')
style.configure('TCombobox', fieldbackground='#FCF7F0')

srcchoosen = ttk.Combobox(window, width=30)
srcchoosen.configure(background="blue")
srcchoosen['values'] = ('afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque',
                        'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa',
                        'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech',
                        'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish',
                        'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati',
                        'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong',
                        'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese',
                        'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz',
                        'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy',
                        'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)',
                        'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi',
                        'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona',
                        'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese',
                        'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian',
                        'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu')

srcchoosen.grid(row=0, column=0, padx=10, pady=5)
srcchoosen.current(21)

destchoosen = ttk.Combobox(window, width=30)
destchoosen['values'] = ('afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque',
                        'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa',
                        'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech',
                        'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish',
                        'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati',
                        'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong',
                        'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese',
                        'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz',
                        'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy',
                        'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)',
                        'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi',
                        'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona',
                        'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese',
                        'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian',
                        'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu')

destchoosen.grid(row=0, column=1, padx=10, pady=5)
destchoosen.current(20)

src_text = tk.Text(window, height=10, width=30, bg='#EEE7EF')
src_text.grid(row=1, column=0, columnspan=1, padx=5, pady=2)

dest_text = tk.Text(window, height=10, width=30, bg='#EEE7EF')
dest_text.grid(row=1, column=1, columnspan=1, padx=1, pady=2)

translate_button = tk.Button(window, text='Translate', command=start_translate, width=10, bg='#59EF94')
translate_button.grid(row=2, column=0, padx=5, pady=5, sticky='w')


window.mainloop()
