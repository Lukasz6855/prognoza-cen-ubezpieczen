"""
Skrypt demonstracyjny pokazujący działanie funkcji pomocniczych
Możesz uruchomić ten plik aby przetestować funkcje przed uruchomieniem aplikacji
"""

# Import funkcji pomocniczych
from pomocnicze import (
    oblicz_bmi,
    interpretuj_bmi,
    konwertuj_plec_na_angielski,
    konwertuj_palacz_na_angielski,
    generuj_podpowiedzi,
    utworz_ramke_danych_dla_predykcji,
    sformatuj_kwote,
    oblicz_roznice_procentowe
)

def test_obliczania_bmi():
    """Test funkcji obliczania BMI"""
    print("=" * 60)
    print("TEST 1: Obliczanie BMI")
    print("=" * 60)
    
    # Przykładowe dane
    waga = 75  # kg
    wzrost = 180  # cm
    
    # Obliczenie BMI
    bmi = oblicz_bmi(waga, wzrost)
    interpretacja = interpretuj_bmi(bmi)
    
    # Wyświetlenie wyników
    print(f"Waga: {waga} kg")
    print(f"Wzrost: {wzrost} cm")
    print(f"BMI: {bmi:.2f}")
    print(f"Interpretacja: {interpretacja}")
    print()

def test_konwersji():
    """Test funkcji konwersji danych"""
    print("=" * 60)
    print("TEST 2: Konwersja danych PL -> EN")
    print("=" * 60)
    
    # Test płci
    plec_pl = "Mężczyzna"
    plec_en = konwertuj_plec_na_angielski(plec_pl)
    print(f"Płeć (PL): {plec_pl} -> (EN): {plec_en}")
    
    # Test statusu palacza
    palacz_pl = "Tak"
    palacz_en = konwertuj_palacz_na_angielski(palacz_pl)
    print(f"Palacz (PL): {palacz_pl} -> (EN): {palacz_en}")
    print()

def test_generowania_podpowiedzi():
    """Test funkcji generowania podpowiedzi"""
    print("=" * 60)
    print("TEST 3: Generowanie podpowiedzi")
    print("=" * 60)
    
    # Przykładowe dane
    wiek = 35
    plec = "Mężczyzna"
    bmi = 28.5
    dzieci = 2
    palacz = "yes"
    region = "southeast"
    przewidywana_oplata = 25000
    
    # Wygenerowanie podpowiedzi
    podpowiedzi = generuj_podpowiedzi(
        wiek, plec, bmi, dzieci, palacz, region, przewidywana_oplata
    )
    
    # Wyświetlenie podpowiedzi
    print(f"Liczba wygenerowanych podpowiedzi: {len(podpowiedzi)}")
    print("\nPodpowiedzi:")
    for i, podpowiedz in enumerate(podpowiedzi, 1):
        print(f"\n{i}. {podpowiedz['ikona']} {podpowiedz['tytul']}")
        print(f"   {podpowiedz['opis'][:100]}...")
        print(f"   Oszczędności: {podpowiedz['potencjalne_oszczednosci']}")
    print()

def test_tworzenia_dataframe():
    """Test funkcji tworzenia DataFrame dla predykcji"""
    print("=" * 60)
    print("TEST 4: Tworzenie DataFrame dla predykcji")
    print("=" * 60)
    
    # Przykładowe dane
    wiek = 30
    plec = "male"
    bmi = 25.0
    dzieci = 1
    palacz = "no"
    region = "northwest"
    
    # Utworzenie DataFrame
    df = utworz_ramke_danych_dla_predykcji(
        wiek, plec, bmi, dzieci, palacz, region
    )
    
    # Wyświetlenie DataFrame
    print("Utworzony DataFrame:")
    print(df)
    print(f"\nKształt: {df.shape}")
    print(f"Kolumny: {list(df.columns)}")
    print()

def test_formatowania():
    """Test funkcji formatowania"""
    print("=" * 60)
    print("TEST 5: Formatowanie kwot i procentów")
    print("=" * 60)
    
    # Test formatowania kwoty
    kwota = 12345.67
    sformatowana = sformatuj_kwote(kwota)
    print(f"Kwota: {kwota} -> {sformatowana}")
    
    # Test obliczania różnicy procentowej
    stara = 10000
    nowa = 12000
    roznica = oblicz_roznice_procentowe(stara, nowa)
    print(f"\nStara wartość: {stara}")
    print(f"Nowa wartość: {nowa}")
    print(f"Różnica procentowa: {roznica:.2f}%")
    print()

def test_pelnego_scenariusza():
    """Test pełnego scenariusza użytkownika"""
    print("=" * 60)
    print("TEST 6: Pełny scenariusz użytkownika")
    print("=" * 60)
    
    # Dane użytkownika (po polsku)
    print("DANE UŻYTKOWNIKA:")
    wiek = 40
    plec_pl = "Kobieta"
    wzrost = 165
    waga = 70
    dzieci = 2
    palacz_pl = "Nie"
    region = "northeast"
    
    print(f"Wiek: {wiek}")
    print(f"Płeć: {plec_pl}")
    print(f"Wzrost: {wzrost} cm")
    print(f"Waga: {waga} kg")
    print(f"Dzieci: {dzieci}")
    print(f"Palacz: {palacz_pl}")
    print(f"Region: {region}")
    
    # Obliczenie BMI
    bmi = oblicz_bmi(waga, wzrost)
    interpretacja_bmi = interpretuj_bmi(bmi)
    print(f"\nBMI: {bmi:.2f} ({interpretacja_bmi})")
    
    # Konwersja danych
    plec_en = konwertuj_plec_na_angielski(plec_pl)
    palacz_en = konwertuj_palacz_na_angielski(palacz_pl)
    
    print(f"\nDANE PO KONWERSJI (dla modelu):")
    print(f"Płeć: {plec_en}")
    print(f"Palacz: {palacz_en}")
    
    # Utworzenie DataFrame
    df = utworz_ramke_danych_dla_predykcji(
        wiek, plec_en, bmi, dzieci, palacz_en, region
    )
    print(f"\nDataFrame gotowy do predykcji:")
    print(df)
    
    # Symulacja wyniku predykcji
    symulowana_oplata = 8500.50
    print(f"\n💰 Symulowana opłata: {sformatuj_kwote(symulowana_oplata)}")
    
    # Wygenerowanie podpowiedzi
    podpowiedzi = generuj_podpowiedzi(
        wiek, plec_pl, bmi, dzieci, palacz_en, region, symulowana_oplata
    )
    print(f"\n💡 Liczba podpowiedzi: {len(podpowiedzi)}")
    
    print("\n✅ Pełny scenariusz wykonany pomyślnie!")
    print()

def main():
    """Główna funkcja uruchamiająca wszystkie testy"""
    print("\n")
    print("🧪 DEMONSTRACJA FUNKCJI POMOCNICZYCH")
    print("=" * 60)
    print()
    
    # Uruchomienie wszystkich testów
    test_obliczania_bmi()
    input("Naciśnij Enter aby kontynuować...")
    
    test_konwersji()
    input("Naciśnij Enter aby kontynuować...")
    
    test_generowania_podpowiedzi()
    input("Naciśnij Enter aby kontynuować...")
    
    test_tworzenia_dataframe()
    input("Naciśnij Enter aby kontynuować...")
    
    test_formatowania()
    input("Naciśnij Enter aby kontynuować...")
    
    test_pelnego_scenariusza()
    
    print("=" * 60)
    print("✅ WSZYSTKIE TESTY ZAKOŃCZONE!")
    print("=" * 60)
    print("\n📝 Następne kroki:")
    print("1. Wytrenuj model: python trenowanie_modelu.py")
    print("2. Uruchom aplikację: streamlit run aplikacja.py")
    print()

# Uruchomienie testów
if __name__ == "__main__":
    main()
