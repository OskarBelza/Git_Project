import requests

def creating_histogram(answer):
    histogram = {}
    for litera in zdanie:
        if litera.isalpha():
            litera.lower()
            if litera in histogram:
                histogram[litera] +=1
            else:
                histogram[litera]=1
    return histogram

def text_source():
    print("1 - Wpisz z klawiatury\n2 - Podaj adres URL")
    source = input("Wybierz opcje: ")
    if source == "1":
        zdanie = input("Podaj zdanie")
        return zdanie
    elif source == "2":
        url = input("Podaj adres URL: ")
        response = requests.get(url)
        return response.text
    else:
        print("Niepoprawny wybor")

while True:
    print("1 - Generuj histogram \n2 - Wyjście")
    wybor = input("WYbierz opcje: ")

    if wybor == "1":
        zdanie = input("Podaj zdanie: ")
        histogram = creating_histogram(zdanie)
        for litera, licznik in histogram.items():
            print(f"{litera}: {licznik}")
    elif wybor == "2":
        break
    else:
        print("Niepoprawny wybor")
