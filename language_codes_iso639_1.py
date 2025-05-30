#!/bin/python
# Belong to (TTS) Script
# Written by: Othmane Moutaouakkil [ moutaouakkil ]



# firstly install [tabulate module] by typing: pip install module (on all Operating Systems)


from tabulate import tabulate

print('\n'*2 + " -->[ ISO 3166-1 alpha-2 ]<--\n".upper())


mydata = [("(Afan) Oromo", "om", "Abkhazian", "ab","Afar", "aa"),
("Afrikaans", "af", "Albanian", "sq", "Amharic", "am"),
("Arabic", "ar", "Armenian", "hy", "Assamese", "as"),
("Aymara", "ay", "Azerbaijani", "az", "Basque", "eu"),
("Bengali", "bn", "Bhutani", "dz", "Bihari", "bh"),
("Bislama", "bi", "Breton", "br", "Bulgarian", "bg"),
("Burmese", "my", "Byelorussian", "be", "Cambodian", "km"),
("Catalan", "ca", "Chinese", "zh", "Corsican", "co"),
("Croatian", "hr", "Czech", "cs", "Danish", "da"),
("Dutch", "nl", "English", "en", "Esperanto", "eo"),
("Estonian", "et", "Faeroese", "fo", "Fiji", "fj"),
("Finnish", "fi", "French", "fr", "Frisian", "fy"),
("Galician", "gl", "Georgian", "ka", "German", "de"),
("Greek", "el", "Greenlandic", "kl", "Guarani", "gn"),
("Gujarati", "gu", "Hausa", "ha", "Hebrew (former iw)", "he"),
("Hindi", "hi", "Hungarian", "hu", "Icelandic", "is"),
("Indonesian (former in)", "id", "Interlingua", "ia", "Interlingue", "ie"),
("Inupiak", "ik", "Inuktitut (Eskimo)", "iu", "Irish", "ga"),
("Italian", "it", "Japanese", "ja", "Javanese", "jw"),
("Kannada", "kn", "Kashmiri", "ks", "Kazakh", "kk"),
("Kinyarwanda", "rw", "Kirghiz", "ky", "Kirundi", "rn"),
("Korean", "ko", "Kurdish", "ku", "Laothian", "lo"),
("Latin", "la", "Latvian, Lettish", "lv", "Lingala", "ln"),
("Lithuanian", "lt", "Macedonian", "mk", "Malagasy", "mg"),
("Malay", "ms", "Malayalam", "ml", "Maltese", "mt"),
("Maori", "mi", "Marathi", "mr", "Moldavian", "mo"),
("Mongolian", "mn", "Nauru", "na", "Nepali", "ne"),
("Norwegian", "no", "Occitan", "oc", "Oriya", "or"),
("Pashto, Pushto", "ps", "Persian", "fa", "Polish", "pl"),
("Portuguese", "pt", "Punjabi", "pa", "Quechua", "qu"),
("Rhaeto-Romance", "rm", "Romanian", "ro", "Russian", "ru"),
("Samoan", "sm", "Sangro", "sg", "Sanskrit", "sa"),
("Scots Gaelic", "gd", "Serbian", "sr", "Serbo-Croatian", "sh"),
("Sesotho", "st", "Setswana", "tn", "Shona", "sn"),
("Sindhi", "sd", "Singhalese", "si", "Siswati", "ss"),
("Slovak", "sk", "Slovenian", "sl", "Somali", "so"),
("Spanish", "es", "Sudanese", "su", "Swahili", "sw"),
("Swedish", "sv", "Tagalog", "tl", "Tajik", "tg"),
("Tamil", "ta", "Tatar", "tt", "Tegulu", "te"),
("Thai", "th", "Tibetan", "bo", "Tigrinya", "ti"),
("Tonga", "to", "Tsonga", "ts", "Turkish", "tr"),
("Turkmen", "tk", "Twi", "tw", "Uigur", "ug"),
("Ukrainian", "uk", "Urdu", "ur", "Uzbek", "uz"),
("Vietnamese", "vi", "Volapuk", "vo", "Welch", "cy"),
("Wolof", "wo", "Xhosa", "xh", "Yiddish (former ji)", "yi"),
("Yoruba", "yo", "Zhuang", "za", "Zulu", "zu")]


myheaders = ["Language", "ISO", "Language", "ISO", "Language", "ISO"]


print(tabulate(mydata, headers = myheaders, tablefmt = "grid"))


# tells that the operation was successfully done
print("\n [ Done! ]")


# exit
input('\n'*2 + ' [!] Hit enter to exit...')
