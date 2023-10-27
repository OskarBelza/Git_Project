zdanie = input("podaj ciąg znaków z którego zostanie utworzony histogram: ")

histogram ={}

for litera in zdanie:
    if litera.isalpha():
        litera.lower()
        if litera in histogram:
            histogram[litera]+=1
        else:
            histogram[litera]=1
