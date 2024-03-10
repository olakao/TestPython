import pytest
from Sortowanie_bąbelkowe import sortowanie_bąbelkowe

def test_sortowanie_bąbelkowe():
    # prepare
    tablica = [-1, 0, 10, 100, 0, 4, 5, 6, -200, 1000]

    # execute
    wynik = sortowanie_bąbelkowe(tablica)

    # check/assert
    assert wynik == [-200, -1, 0, 0, 4, 5, 6, 10, 100, 1000]

