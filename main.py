histogram ={}

"""for litera in zdanie:
    if litera.isalpha():
        litera.lower()
        if litera in histogram:
            histogram[litera]+=1
        else:
            histogram[litera]=1

print("Histogram częstości występowania liter: ")
for litera, licznik in histogram.items():
    print(f"{litera}: {licznik}")"""

while True:
    print("1 - Generuj histogram \n2 - Wyjście")
    wybor = input("WYbierz opcje: ")

    if wybor == "1":
        zdanie = input("Podaj zdanie: ")
        histogram =  # Przeniesc tworzenie histogramu do funkcji
        for litera, licznik in histogram.items():
            print(f"{litera}: {licznik}")
    elif wybor == "2":
        break
    else:
        print("Niepoprawny wybor")
