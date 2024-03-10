# funkcja sortuje dane przy pomocy algorytmu sortowania bąbelkowego, rosnąco
# input: tablica liczb
# output: tablica liczb posortowanych rosąco

def sortowanie_bąbelkowe(tablica: list[int]):
    for i in range(len(tablica)-1):
        p = True
        for j in range(len(tablica)-1, i, -1):
            if tablica[j] < tablica[j-1]:
                tablica[j], tablica[j-1] = tablica[j-1], tablica[j]
                p = False
        if p:
            break
    return tablica
