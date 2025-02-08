"""
TEST
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

            # Inicializace počítadel
            word_count = 0
            capital_case = 0
            upper_case = 0
            lower_case = 0
            numbers_count = 0
            numbers_sum = 0

            # Rozdělení textu na slova a zpracování
            for word in selected_text.split():
                # Odstranění interpunkce
                clean_word = ''.join(char for char in word if char.isalnum())
                if not clean_word:
                    continue
                word_count += 1  # Počet slov

                # Kontrola na Titlecase
                if clean_word.istitle():
                    capital_case += 1

                # Kontrola na Uppercase
                if clean_word.isupper():
                    upper_case += 1

                # Kontrola na Lowercase
                if clean_word.islower():
                    lower_case += 1

                # Kontrola na čísla
                if clean_word.isdigit():
                    numbers_count += 1
                    numbers_sum += int(clean_word)

            # Výstupy
            print(f"There are {word_count} words in the selected text.")
            print(f"There are {capital_case} titlecase words.")
            print(f"There are {upper_case} uppercase words.")
            print(f"There are {lower_case} lowercase words.")
            print(f"There are {numbers_count} numeric strings.")
            print(f"The sum of all numbers is {numbers_sum}.")
        else:
            print("Invalid input. Please select a number between 1 and 3.")
    else:
        print("Incorrect username or password.")

prihlaseni()