""" 
Program, który pobiera od użytkownika dowolne pojedyncze znaki i zapisuje je w liście. 
Zakończenie pobierania następuje, gdy użytkownik wciśnie zero. 
Dalej program na podstawie stworzonej listy oblicza
liczbę permutacji n!, jakie można stworzyć z podanych znaków. 
Do oblicznie liczby permutacji zastosowano funkcję rekurencyjną. 
"""

def pobieranieZnaków():
    print("Rozpoczynamy pobieranie pojedyńczych znaków!")
    print("Aby zakończyć pobieranie znaków, wciśnij 0")
    lista = []
    while True:
        znak = input("Podaj proszę dowolny pojedyńczy znak ")
        if znak == "0":
            return lista
        elif len(znak) != 1:
            print('Błąd, miałeś wpisać pojedyńczy znak drogi użytkowniku!')
        else:
            lista.append(znak)

def zamianaNaZbiór():
    znaki = pobieranieZnaków()
    zbiór = set(znaki)
    print("Oto znaki jakie podałeś:")
    print(zbiór)
    return len(zbiór)

def liczbaPermutacji(n):
    if n == 0:
        return 1
    else:
        return n * liczbaPermutacji(n-1)

print("Liczba permutacji, jakie można stworzyć z podanych znaków:", \
      liczbaPermutacji(zamianaNaZbiór()))
