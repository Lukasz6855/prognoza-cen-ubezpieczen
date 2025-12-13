"""
Moduł pomocniczy z funkcjami wspierającymi aplikację
Zawiera funkcje do generowania podpowiedzi i analizy danych
"""

import pandas as pd
import streamlit as st

def generuj_podpowiedzi(wiek, plec, bmi, dzieci, palacz, region, przewidywana_oplata):
    """
    Funkcja generująca personalizowane podpowiedzi dla użytkownika
    jak obniżyć koszt ubezpieczenia na życie
    
    Parametry:
    - wiek: wiek użytkownika
    - plec: płeć użytkownika
    - bmi: wskaźnik masy ciała
    - dzieci: liczba dzieci
    - palacz: czy użytkownik pali (yes/no)
    - region: region zamieszkania
    - przewidywana_oplata: przewidywany koszt ubezpieczenia
    
    Zwraca: lista podpowiedzi
    """
    # Lista podpowiedzi do zwrócenia
    podpowiedzi = []
    
    # Podpowiedź dotycząca palenia
    if palacz == 'yes':
        podpowiedzi.append({
            'ikona': '🚭',
            'tytul': 'Rzuć palenie!',
            'opis': 'Palenie jest NAJWIĘKSZYM czynnikiem wpływającym na koszt ubezpieczenia. Rzucając palenie możesz zaoszczędzić nawet 50-70% kosztów!',
            'potencjalne_oszczednosci': 'Bardzo wysokie (50-70%)'
        })
    
    # Podpowiedź dotycząca BMI
    if bmi > 30:
        podpowiedzi.append({
            'ikona': '🏃',
            'tytul': 'Obniż wagę',
            'opis': f'Twoje BMI wynosi {bmi:.1f}, co wskazuje na nadwagę. Zredukowanie wagi do zdrowego zakresu (BMI 18.5-25) może znacznie obniżyć Twoją składkę.',
            'potencjalne_oszczednosci': 'Średnie (20-30%)'
        })
    elif bmi > 25:
        podpowiedzi.append({
            'ikona': '⚖️',
            'tytul': 'Dbaj o wagę',
            'opis': f'Twoje BMI wynosi {bmi:.1f}, co jest lekko powyżej normy. Utrzymanie zdrowej wagi może pomóc w obniżeniu składki.',
            'potencjalne_oszczednosci': 'Niskie (10-15%)'
        })
    
    # Podpowiedź dotycząca wieku
    if wiek < 30:
        podpowiedzi.append({
            'ikona': '⏰',
            'tytul': 'Zawrzyj umowę teraz',
            'opis': 'Jesteś w młodym wieku - to najlepszy czas na zawarcie długoterminowej polisy. Im wcześniej, tym niższe stawki!',
            'potencjalne_oszczednosci': 'Długoterminowe oszczędności'
        })
    
    # Podpowiedź dotycząca regionu
    if region in ['southeast', 'southwest']:
        podpowiedzi.append({
            'ikona': '📍',
            'tytul': 'Rozważ zmianę regionu',
            'opis': 'Twój region charakteryzuje się wyższymi kosztami ubezpieczenia. Jeśli planujesz przeprowadzkę, może to wpłynąć na koszty.',
            'potencjalne_oszczednosci': 'Niskie-Średnie (5-15%)'
        })
    
    # Ogólne podpowiedzi
    podpowiedzi.append({
        'ikona': '💰',
        'tytul': 'Porównaj oferty',
        'opis': 'Zawsze porównuj oferty różnych ubezpieczycieli. Ceny mogą się znacznie różnić przy tych samych parametrach.',
        'potencjalne_oszczednosci': 'Zróżnicowane (10-30%)'
    })
    
    podpowiedzi.append({
        'ikona': '🏥',
        'tytul': 'Regularne badania',
        'opis': 'Regularne badania lekarskie i dbanie o zdrowie mogą pomóc w uzyskaniu lepszych stawek przy odnowieniu polisy.',
        'potencjalne_oszczednosci': 'Długoterminowe oszczędności'
    })
    
    # Zwrócenie listy podpowiedzi
    return podpowiedzi

def oblicz_bmi(waga_kg, wzrost_cm):
    """
    Funkcja obliczająca BMI (Body Mass Index)
    
    Parametry:
    - waga_kg: waga w kilogramach
    - wzrost_cm: wzrost w centymetrach
    
    Zwraca: wartość BMI
    """
    # Przeliczenie wzrostu z cm na metry
    wzrost_m = wzrost_cm / 100
    # Obliczenie BMI
    bmi = waga_kg / (wzrost_m ** 2)
    # Zwrócenie wartości BMI
    return bmi

def interpretuj_bmi(bmi):
    """
    Funkcja interpretująca wartość BMI
    
    Parametry:
    - bmi: wartość BMI
    
    Zwraca: interpretacja tekstowa
    """
    # Sprawdzenie przedziału BMI i zwrócenie odpowiedniej interpretacji
    if bmi < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi < 25:
        return "Waga prawidłowa"
    elif 25 <= bmi < 30:
        return "Nadwaga"
    else:
        return "Otyłość"

def konwertuj_plec_na_angielski(plec_po_polsku):
    """
    Funkcja konwertująca płeć z polskiego na angielski format
    (wymagane przez model)
    
    Parametry:
    - plec_po_polsku: płeć po polsku (Mężczyzna/Kobieta)
    
    Zwraca: płeć po angielsku (male/female)
    """
    # Słownik mapujący
    mapping = {
        'Mężczyzna': 'male',
        'Kobieta': 'female'
    }
    # Zwrócenie zmapowanej wartości
    return mapping.get(plec_po_polsku, 'male')

def konwertuj_palacz_na_angielski(palacz_po_polsku):
    """
    Funkcja konwertująca status palacza z polskiego na angielski format
    (wymagane przez model)
    
    Parametry:
    - palacz_po_polsku: status po polsku (Tak/Nie)
    
    Zwraca: status po angielsku (yes/no)
    """
    # Słownik mapujący
    mapping = {
        'Tak': 'yes',
        'Nie': 'no'
    }
    # Zwrócenie zmapowanej wartości
    return mapping.get(palacz_po_polsku, 'no')

def utworz_ramke_danych_dla_predykcji(wiek, plec, bmi, dzieci, palacz, region):
    """
    Funkcja tworząca DataFrame w formacie wymaganym przez model
    
    Parametry:
    - wiek: wiek osoby
    - plec: płeć (male/female)
    - bmi: wskaźnik masy ciała
    - dzieci: liczba dzieci
    - palacz: czy pali (yes/no)
    - region: region zamieszkania
    
    Zwraca: DataFrame gotowy do predykcji
    """
    # Utworzenie słownika z danymi
    dane = {
        'age': [wiek],
        'sex': [plec],
        'bmi': [bmi],
        'children': [dzieci],
        'smoker': [palacz],
        'region': [region]
    }
    # Utworzenie DataFrame
    df = pd.DataFrame(dane)
    # Zwrócenie DataFrame
    return df

def sformatuj_kwote(kwota):
    """
    Funkcja formatująca kwotę w czytelny sposób
    
    Parametry:
    - kwota: kwota do sformatowania
    
    Zwraca: sformatowany string
    """
    # Formatowanie kwoty z separatorami tysięcy i 2 miejscami po przecinku
    return f"{kwota:,.2f} USD"

def oblicz_roznice_procentowe(stara_wartosc, nowa_wartosc):
    """
    Funkcja obliczająca różnicę procentową między dwiema wartościami
    
    Parametry:
    - stara_wartosc: wartość bazowa
    - nowa_wartosc: nowa wartość
    
    Zwraca: różnica procentowa
    """
    # Obliczenie różnicy procentowej
    if stara_wartosc == 0:
        return 0
    roznica = ((nowa_wartosc - stara_wartosc) / stara_wartosc) * 100
    # Zwrócenie różnicy
    return roznica

def wyswietl_metryki_porownawcze(bazowa_oplata, aktualna_oplata):
    """
    Funkcja wyświetlająca metryki porównawcze w Streamlit
    
    Parametry:
    - bazowa_oplata: bazowy koszt ubezpieczenia
    - aktualna_oplata: aktualny koszt ubezpieczenia po zmianach
    """
    # Obliczenie różnicy
    roznica = aktualna_oplata - bazowa_oplata
    roznica_procent = oblicz_roznice_procentowe(bazowa_oplata, aktualna_oplata)
    
    # Utworzenie trzech kolumn dla metryk
    col1, col2, col3 = st.columns(3)
    
    # Wyświetlenie metryk
    with col1:
        st.metric(
            label="Bazowa opłata",
            value=sformatuj_kwote(bazowa_oplata)
        )
    
    with col2:
        st.metric(
            label="Nowa opłata",
            value=sformatuj_kwote(aktualna_oplata),
            delta=f"{sformatuj_kwote(roznica)} ({roznica_procent:+.1f}%)",
            delta_color="inverse"  # Czerwony dla wzrostu, zielony dla spadku
        )
    
    with col3:
        # Określenie kierunku zmiany
        if roznica > 0:
            kierunek = "wzrost"
            kolor = "🔴"
        elif roznica < 0:
            kierunek = "spadek"
            kolor = "🟢"
        else:
            kierunek = "bez zmiany"
            kolor = "⚪"
        
        st.metric(
            label="Zmiana",
            value=f"{kolor} {abs(roznica_procent):.1f}% {kierunek}"
        )
