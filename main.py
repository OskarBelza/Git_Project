import requests


def creating_histogram(answer):
    histogram = {}
    for letter in answer:
        if letter.isalpha():
            letter.lower()
            if letter in histogram:
                histogram[letter] += 1
            else:
                histogram[letter] = 1
    return histogram


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


while True:
    print("1 - Generuj histogram \n2 - Wyjście")
    choice = input("WYbierz opcje: ")
    if choice == "1":
        text = text_source()
        if text:
            histogram = creating_histogram(text)
            for letter, counter in histogram.items():
                print(f"{letter}: {counter}")
    elif choice == "2":
        break
    else:
        print("Niepoprawny wybor")
