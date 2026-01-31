print("Podaj klucz szyfru, liczbę całkowitą:")
klucz_szyfru = int(input())
print("Podaj tekst do zaszyfrowania małymi literami:")

tekst_do_zaszyfrowania = str(input())
zaszyfrowany_tekst = []

n = len(tekst_do_zaszyfrowania); # liczymy dlugosc elementow w ramach tekstu podanego przez uzytkownika np 15 liter z 3 słów do zakodowania

for x in range(n):
    if tekst_do_zaszyfrowania[x] == " ":
        zaszyfrowany_tekst.append(" ") # Zostaw spację w spokoju!
        continue
    znak_na_numer = ord(tekst_do_zaszyfrowania[x])
    znak_na_numer = znak_na_numer + klucz_szyfru
    if znak_na_numer > 122:
        znak_na_numer = znak_na_numer - 26
    numer_na_znak = chr(znak_na_numer)
    zaszyfrowany_tekst.append(numer_na_znak)

zlaczony_tekst = "".join(zaszyfrowany_tekst)

print(zlaczony_tekst)
