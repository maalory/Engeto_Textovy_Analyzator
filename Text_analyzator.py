"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Balák
email: tomasbalak@gmail.com
discord: Tomas Balak#tomasbalak
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

rozdelovac = "-" * 40

users_and_pwd = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}


# Přihlášení uživatele
def prihlaseni():
    jmeno = input("user: ")
    heslo = input("password: ")

    # Ověření uživatele a hesla
    if jmeno in users_and_pwd and users_and_pwd[jmeno] == heslo:
        print(rozdelovac)
        print("Welcome to the app, " +
              jmeno +
              "\nWe have 3 texts to be analyzed.")
        print(rozdelovac)

        # Zadání čísla uživatelem
        volba = input("Enter a number btw. 1 and 3 to select: ")

        # Kontrola vstupu
        if volba.isdigit() and 1 <= int(volba) <= 3:
            # Převod zvoleného čísla na výběrový index
            selected_text_index = int(volba) - 1
            # Zvolený text z listu = selected_text
            selected_text = TEXTS[selected_text_index]

            # COUNT CASE (poč. slov) - rozdělení textu na slova
            words_count = selected_text.split()
            count_case = len(words_count)
            print(f"There are {count_case} words in the selected text.")

            # CAPITAL CASE (počet slov začínajících velkým písmenem)
            capital_case = 0
            for char in selected_text:
                if char[0].isupper():
                    capital_case += 1
            print(f"There are {capital_case} titlecase words.")

            # UPPER CASE (počet slov psaných velkými písmeny)
            upper_case = 0
            for char in selected_text:
                if char.isupper():
                    upper_case += 1
            print(f"There are {upper_case} uppercase words.")

            # LOWER CASE (počet slov psaných malými písmeny)
            lower_case = 0
            for char in selected_text:
                if char.islower():
                    lower_case += 1
            print(f"There are {lower_case} lowercase words.")

            # NUMBERS COUNT CASE (počet čísel (ne cifer))
            numbers_count_case = 0
            for char in selected_text:
                if char.isdigit():
                    numbers_count_case += 1
            print(f"There are {numbers_count_case} numeric strings.")

            # NUMBERS SUM CASE (sumu všech čísel (ne cifer))
            numbers_sum_case = 0

            for word in words_count:
                digits_in_word = ''.join(char for char in word if char.isdigit())
                if digits_in_word:
                    numbers_sum_case += int(digits_in_word)

            print(f"The sum of all numbers {numbers_sum_case}.")

            # GRAF
            chart_word_input = selected_text.split()
            chart_word_length = {}

            for word in chart_word_input:  # Pocitani delky slov
                if word.isalpha():
                    word_lenght = len(word)
                    if word_lenght not in chart_word_length:
                        chart_word_length[word_lenght] = 1
                    else:
                        chart_word_length[word_lenght] += 1
            max_length = max(chart_word_length.keys())

            print(rozdelovac)
            print(f"{'LEN':<5}|{'OCCURRENCES':^20}|{'NR.':>5}")  # Graf-hlavicka
            print(rozdelovac)

            for length in range(1, max_length + 1):  # Graf-data
                freq = chart_word_length.get(length, 0)
                bar = '*' * freq
                print(f"{length:<5}|{bar:^20}|{freq:>5}")

            print(rozdelovac)


        # Neplatný vstup
        else:
            print("The number is out of the allowed range (1-3).")
    else:
        # Neplatný login
        print("username:", jmeno, "\npassword:", heslo, "\nunregistered user, terminating the program..")
        exit()  # Ukončení programu


# Funkce pro přihlášení
prihlaseni()