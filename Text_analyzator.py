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
import re

spliter = "-" * 40

users_and_pwd = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# user login
def login():
    name = input("user: ")
    pwd = input("password: ")

    # user and pwd verification
    if name in users_and_pwd and users_and_pwd[name] == pwd:
        print(spliter)
        print("Welcome to the app, " +
              name +
              "\nWe have 3 texts to be analyzed.")
        print(spliter)

        # user number input
        volba = input("Enter a number btw. 1 and 3 to select: ")

        # input check
        if volba.isdigit() and 1 <= int(volba) <= 3:
            # selected number index transfer
            selected_text_index = int(volba) - 1
            # Zvolený text z listu = selected_text
            selected_text = TEXTS[selected_text_index]

            word_count = 0
            capital_case = 0
            upper_case = 0
            lower_case = 0
            numbers_count = 0
            numbers_sum = 0

            # text split&processing (rozdelení textu na slova a zpracování)
            for word in selected_text.split():
                #cleaning of the text (interpunction)
                clean_word = re.sub(r'\W+', '', word)
                if not clean_word:
                    continue
                word_count += 1

                # CAPITAL CASE (pocet slov zacínajících velkým písmenem)
                if clean_word.istitle():
                    capital_case += 1

                # UPPER CASE (pocet slov psaných velkými písmeny)
                #if clean_word.isupper() and not clean_word.isdigit():
                if clean_word.isupper() and clean_word.isalpha():
                    upper_case += 1

                # LOWER CASE (pocet slov psaných malými písmeny)
                if clean_word.islower():
                    lower_case += 1

                # NUMBERS COUNT CASE (pocet císel (ne cifer))
                if clean_word.isdigit():
                    numbers_count += 1
                    numbers_sum += int(clean_word)

            print(f"There are {word_count} words in the selected text.")
            print(f"There are {capital_case} words starting with a capital letter.")
            print(f"There are {upper_case} uppercase words.")
            print(f"There are {lower_case} lowercase words.")
            print(f"There are {numbers_count} numeric strings.")
            print(f"The sum of all numbers {numbers_sum}.")

            # CHART
            chart_word_input = [re.sub(r'\W+', '', word) for word in selected_text.split()] #removing non-alpha char (vše krome písmen a císlic)
            chart_word_length = {}
            #print(chart_word_input)

            # dict for words length
            max_length = 0
            for word in chart_word_input:
                #if word.isalpha(): #only letters
                if word.isalnum(): #alphanumeric
                    word_length = len(word)
                    chart_word_length[word_length] = chart_word_length.get(word_length, 0) + 1
                    max_length = max(max_length, word_length)

            print(spliter)
            print(f"{'LEN':<5}|{'OCCURRENCES':^20}|{'NR.':>5}")  # Chart - header
            print(spliter)

            # Generating chart (1 - max_length)
            for length in range(1, max_length + 1):
                freq = chart_word_length.get(length, 0)
                bar = '*' * freq
                print(f"{length:<5}|{bar:<20}|{freq:>5}")
            print(spliter)

        # invalid output
        else:
            print("The number is out of the allowed range (1-3).")
    else:
        # invalid login
        print("username:", name, "\npassword:", pwd, "\nunregistered user, terminating the program..")
        exit()  # program termination

# login function
login()