import random

def gra_rps():
    figury = ["kamień", "nożyce", "papier"]
    punkty_gracza = 0
    punkty_komputera = 0
    proby = 0 # Licznik rund

    print("--- WITAJ W GRZE KAMIEŃ, PAPIER, NOŻYCE ---")
    print("Gramy do 3 zwycięstw!")

    while punkty_gracza < 3 and punkty_komputera < 3:
        print(f"\n--- RUNDA {punkty_gracza + punkty_komputera + 1} ---")
        
        # Pobieranie ruchu od gracza i zamiana na małe litery
        x = input("Co wybierasz? (kamień, nożyce, papier): ").lower()
        
        if x not in figury:
            print("Błędny wybór! Spróbuj jeszcze raz.")
            continue

        losowa_figura = random.choice(figury)
        print(f"Komputer wybrał: {losowa_figura}")

        # Logika gry
        if x == losowa_figura:
            print("Remis w tej rundzie!")
        
        elif (losowa_figura == "kamień" and x == "nożyce") or \
             (losowa_figura == "nożyce" and x == "papier") or \
             (losowa_figura == "papier" and x == "kamień"):
            print("Przegrana w tej rundzie!")
            punkty_komputera += 1
            
        else:
            print("Wygrana w tej rundzie!")
            punkty_gracza += 1

        # Wyświetlanie wyniku po każdej rundzie
        print(f"WYNIK -> Ty: {punkty_gracza} | Komputer: {punkty_komputera}")

    # Ogłoszenie zwycięzcy
    print("\n==========================")
    if punkty_gracza == 3:
        print("GRATULACJE! Wygrałeś całą grę!")
    else:
        print("KONIEC GRY! Komputer wygrał całą grę.")
    print("==========================")

# Uruchomienie gry
if __name__ == "__main__":
    gra_rps()
