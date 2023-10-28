import requests


def text_source():
    print("1 - Wpisz z klawiatury\n2 - Podaj adres URL")
    source = input("Wybierz opcje: ")
    if source == "1":
        text = input("Podaj zdanie")
        return text
    elif source == "2":
        url = input("Podaj adres URL: ")
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Bład pobierania strony")
            return None
    else:
        print("Niepoprawny wybor")
        return None


def histogram(text):
    histogram = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in histogram:
                histogram[letter] += 1
            else:
                histogram[letter] = 1
    return histogram


def advance_histogram(sentence, letters_to_count):
    letter_histogram = {}
    sentence = sentence.replace(" ", "").lower()
    for char in sentence:
        if char.isalpha() and char in letters_to_count:
            if char not in letter_histogram:
                letter_histogram[char] = 1
            else:
                letter_histogram[char] += 1
    return letter_histogram


while True:
    print("1 - Generuj histogram \n2 - Generuj zaawansowany histogram\n3 - Wyjście")
    choice = input("WYbierz opcje: ")
    if choice == "1":
        text = text_source()
        if text:
            histogram = histogram(text)
            for letter, counter in histogram.items():
                print(f"{letter}: {counter}")
    elif choice == "2":
        text = text_source()
        if text:
            letters_to_count = input("Podaj litery do zliczania (oddzielone przecinkami): ").split(',')
            histogram = advance_histogram(text, letters_to_count)
            for letter, counter in histogram.items():
                print(f"{dupa}: {counter}")
    elif choice == "3":
        break
    else:
        print("Niepoprawny wybor")
        





