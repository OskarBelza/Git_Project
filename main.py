def histogram():
    histogram = {}
    tekst = input("Wprowadź tekst: ")

    for litera in tekst:
        if litera.isalpha():
            litera = litera.lower()
            if litera in histogram:
                histogram[litera] += 1
            else:
                histogram[litera] = 1

def advance_histogram(sentence, letters_to_count):
    letter_histogram = {}

    for char in sentence:
        if char.isalpha() and char in letters_to_count:
            if char not in letter_histogram:
                letter_histogram[char] = 1
            else:
                letter_histogram[char] += 1
    return letter_histogram

user_input = input("Wprowadź ciąg znaków: ")

letters_to_count = input("Podaj litery do zliczania (oddzielone przecinkami): ").split(',')

histogram = advance_histogram(user_input, letters_to_count)
for letter, count in histogram.items():
    print(f"{letter}: {count}")



