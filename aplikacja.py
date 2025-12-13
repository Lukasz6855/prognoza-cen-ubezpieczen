"""
Główna aplikacja Streamlit do przewidywania kosztów ubezpieczenia na życie
Aplikacja pozwala na wprowadzenie danych przez formularz lub audio
oraz porównanie różnych scenariuszy
"""

# Import bibliotek
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pycaret.regression import load_model, predict_model
import os

# Import funkcji pomocniczych
from pomocnicze import (
    generuj_podpowiedzi,
    oblicz_bmi,
    interpretuj_bmi,
    konwertuj_plec_na_angielski,
    konwertuj_palacz_na_angielski,
    utworz_ramke_danych_dla_predykcji,
    sformatuj_kwote,
    oblicz_roznice_procentowe,
    wyswietl_metryki_porownawcze
)

# Konfiguracja strony Streamlit
st.set_page_config(
    page_title="Prognoza Cen Ubezpieczeń",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tytuł aplikacji
st.title("🏥 Prognoza Kosztów Ubezpieczenia na Życie")
st.markdown("---")

def wczytaj_model():
    """
    Funkcja wczytująca wytrenowany model
    Zwraca model lub None jeśli model nie istnieje
    """
    # Nazwa pliku modelu
    nazwa_modelu = 'najlepszy_model_ubezpieczenia'
    
    # Sprawdzenie czy plik modelu istnieje
    if os.path.exists(f'{nazwa_modelu}.pkl'):
        # Wczytanie modelu
        model = load_model(nazwa_modelu)
        return model
    else:
        # Zwrócenie None jeśli model nie istnieje
        return None

def przewidz_koszt(model, dane_df):
    """
    Funkcja przewidująca koszt ubezpieczenia
    
    Parametry:
    - model: wytrenowany model
    - dane_df: DataFrame z danymi wejściowymi
    
    Zwraca: przewidywany koszt
    """
    # Wykonanie predykcji
    predykcja = predict_model(model, data=dane_df)
    # Pobranie wartości predykcji z kolumny 'prediction_label'
    koszt = predykcja['prediction_label'].iloc[0]
    # Zwrócenie kosztu
    return koszt

def sekcja_formularz():
    """
    Funkcja renderująca sekcję formularza do wprowadzania danych
    Zwraca: słownik z danymi użytkownika
    """
    st.header("📋 Dane klienta")
    
    # Utworzenie dwóch kolumn dla formularza
    col1, col2 = st.columns(2)
    
    with col1:
        # Pole do wprowadzenia wieku
        wiek = st.number_input(
            "Wiek (lata)",
            min_value=18,
            max_value=100,
            value=30,
            step=1,
            help="Podaj swój wiek w latach"
        )
        
        # Pole do wyboru płci
        plec = st.selectbox(
            "Płeć",
            options=['Mężczyzna', 'Kobieta'],
            help="Wybierz swoją płeć"
        )
        
        # Pole do wprowadzenia wzrostu
        wzrost = st.number_input(
            "Wzrost (cm)",
            min_value=100,
            max_value=250,
            value=170,
            step=1,
            help="Podaj swój wzrost w centymetrach"
        )
        
        # Pole do wprowadzenia wagi
        waga = st.number_input(
            "Waga (kg)",
            min_value=30,
            max_value=300,
            value=70,
            step=1,
            help="Podaj swoją wagę w kilogramach"
        )
    
    with col2:
        # Pole do wyboru liczby dzieci
        dzieci = st.selectbox(
            "Liczba dzieci",
            options=[0, 1, 2, 3, 4, 5],
            help="Wybierz liczbę dzieci"
        )
        
        # Pole do wyboru statusu palacza
        palacz = st.selectbox(
            "Czy palisz papierosy?",
            options=['Nie', 'Tak'],
            help="Wybierz czy jesteś palaczem"
        )
        
        # Pole do wyboru regionu
        region = st.selectbox(
            "Region zamieszkania",
            options=['northeast', 'northwest', 'southeast', 'southwest'],
            format_func=lambda x: {
                'northeast': 'Północny Wschód',
                'northwest': 'Północny Zachód',
                'southeast': 'Południowy Wschód',
                'southwest': 'Południowy Zachód'
            }[x],
            help="Wybierz swój region zamieszkania"
        )
    
    # Obliczenie BMI
    bmi = oblicz_bmi(waga, wzrost)
    
    # Wyświetlenie BMI
    st.info(f"📊 Twoje BMI: **{bmi:.2f}** ({interpretuj_bmi(bmi)})")
    
    # Zwrócenie słownika z danymi
    return {
        'wiek': wiek,
        'plec': plec,
        'wzrost': wzrost,
        'waga': waga,
        'bmi': bmi,
        'dzieci': dzieci,
        'palacz': palacz,
        'region': region
    }

def sekcja_predykcja(model, dane_uzytkownika):
    """
    Funkcja renderująca sekcję z predykcją kosztów
    
    Parametry:
    - model: wytrenowany model
    - dane_uzytkownika: słownik z danymi użytkownika
    
    Zwraca: przewidywany koszt
    """
    st.header("💰 Przewidywana opłata")
    
    # Konwersja danych na format wymagany przez model
    plec_en = konwertuj_plec_na_angielski(dane_uzytkownika['plec'])
    palacz_en = konwertuj_palacz_na_angielski(dane_uzytkownika['palacz'])
    
    # Utworzenie DataFrame dla predykcji
    dane_df = utworz_ramke_danych_dla_predykcji(
        wiek=dane_uzytkownika['wiek'],
        plec=plec_en,
        bmi=dane_uzytkownika['bmi'],
        dzieci=dane_uzytkownika['dzieci'],
        palacz=palacz_en,
        region=dane_uzytkownika['region']
    )
    
    # Wykonanie predykcji
    przewidywany_koszt = przewidz_koszt(model, dane_df)
    
    # Wyświetlenie przewidywanego kosztu
    st.success(f"### Szacowany roczny koszt ubezpieczenia: **{sformatuj_kwote(przewidywany_koszt)}**")
    
    # Zwrócenie kosztu
    return przewidywany_koszt

def sekcja_podpowiedzi(dane_uzytkownika, przewidywany_koszt):
    """
    Funkcja renderująca sekcję z podpowiedziami
    
    Parametry:
    - dane_uzytkownika: słownik z danymi użytkownika
    - przewidywany_koszt: przewidywany koszt ubezpieczenia
    """
    st.header("💡 Jak obniżyć koszty ubezpieczenia?")
    
    # Konwersja danych
    palacz_en = konwertuj_palacz_na_angielski(dane_uzytkownika['palacz'])
    
    # Wygenerowanie podpowiedzi
    podpowiedzi = generuj_podpowiedzi(
        wiek=dane_uzytkownika['wiek'],
        plec=dane_uzytkownika['plec'],
        bmi=dane_uzytkownika['bmi'],
        dzieci=dane_uzytkownika['dzieci'],
        palacz=palacz_en,
        region=dane_uzytkownika['region'],
        przewidywana_oplata=przewidywany_koszt
    )
    
    # Wyświetlenie każdej podpowiedzi
    for podpowiedz in podpowiedzi:
        with st.expander(f"{podpowiedz['ikona']} {podpowiedz['tytul']}"):
            st.write(podpowiedz['opis'])
            st.caption(f"**Potencjalne oszczędności:** {podpowiedz['potencjalne_oszczednosci']}")

def sekcja_porownanie(model, dane_uzytkownika, bazowy_koszt):
    """
    Funkcja renderująca sekcję porównania scenariuszy
    
    Parametry:
    - model: wytrenowany model
    - dane_uzytkownika: słownik z danymi użytkownika
    - bazowy_koszt: bazowy koszt ubezpieczenia
    """
    st.header("📊 Porównanie scenariuszy")
    st.markdown("Użyj suwaków poniżej, aby zobaczyć jak zmiana różnych parametrów wpływa na koszt ubezpieczenia")
    
    # Utworzenie czterech kolumn dla suwaków
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        # Suwak dla wagi
        nowa_waga = st.slider(
            "Waga (kg)",
            min_value=40,
            max_value=200,
            value=dane_uzytkownika['waga'],
            step=1
        )
    
    with col2:
        # Suwak dla liczby dzieci
        nowe_dzieci = st.slider(
            "Dzieci",
            min_value=0,
            max_value=5,
            value=dane_uzytkownika['dzieci'],
            step=1
        )
    
    with col3:
        # Przełącznik dla statusu palacza
        nowy_palacz = st.select_slider(
            "Status palacza",
            options=['Nie', 'Tak'],
            value=dane_uzytkownika['palacz']
        )
    
    with col4:
        # Wybór regionu
        nowy_region = st.selectbox(
            "Region",
            options=['northeast', 'northwest', 'southeast', 'southwest'],
            index=['northeast', 'northwest', 'southeast', 'southwest'].index(dane_uzytkownika['region']),
            format_func=lambda x: {
                'northeast': 'Pn. Wschód',
                'northwest': 'Pn. Zachód',
                'southeast': 'Pd. Wschód',
                'southwest': 'Pd. Zachód'
            }[x],
            key='region_porownanie'
        )
    
    # Obliczenie nowego BMI
    nowe_bmi = oblicz_bmi(nowa_waga, dane_uzytkownika['wzrost'])
    
    # Konwersja danych
    plec_en = konwertuj_plec_na_angielski(dane_uzytkownika['plec'])
    nowy_palacz_en = konwertuj_palacz_na_angielski(nowy_palacz)
    
    # Utworzenie DataFrame dla nowej predykcji
    nowe_dane_df = utworz_ramke_danych_dla_predykcji(
        wiek=dane_uzytkownika['wiek'],
        plec=plec_en,
        bmi=nowe_bmi,
        dzieci=nowe_dzieci,
        palacz=nowy_palacz_en,
        region=nowy_region
    )
    
    # Wykonanie nowej predykcji
    nowy_koszt = przewidz_koszt(model, nowe_dane_df)
    
    # Wyświetlenie metryk porównawczych
    st.markdown("### Porównanie kosztów")
    wyswietl_metryki_porownawcze(bazowy_koszt, nowy_koszt)
    
    # Utworzenie tabeli porównawczej
    st.markdown("### Szczegółowe porównanie")
    
    # Utworzenie DataFrame z porównaniem
    porownanie_df = pd.DataFrame({
        'Parametr': ['Waga (kg)', 'BMI', 'Dzieci', 'Palacz', 'Region', 'Koszt roczny (USD)'],
        'Wartości bazowe': [
            dane_uzytkownika['waga'],
            f"{dane_uzytkownika['bmi']:.2f}",
            dane_uzytkownika['dzieci'],
            dane_uzytkownika['palacz'],
            dane_uzytkownika['region'],
            f"{bazowy_koszt:,.2f}"
        ],
        'Nowe wartości': [
            nowa_waga,
            f"{nowe_bmi:.2f}",
            nowe_dzieci,
            nowy_palacz,
            nowy_region,
            f"{nowy_koszt:,.2f}"
        ]
    })
    
    # Wyświetlenie tabeli
    st.dataframe(porownanie_df, use_container_width=True)
    
    # Utworzenie wykresu słupkowego porównania
    fig = go.Figure(data=[
        go.Bar(
            name='Bazowy koszt',
            x=['Koszt ubezpieczenia'],
            y=[bazowy_koszt],
            marker_color='lightblue'
        ),
        go.Bar(
            name='Nowy koszt',
            x=['Koszt ubezpieczenia'],
            y=[nowy_koszt],
            marker_color='lightcoral' if nowy_koszt > bazowy_koszt else 'lightgreen'
        )
    ])
    
    # Konfiguracja wykresu
    fig.update_layout(
        title='Porównanie kosztów ubezpieczenia',
        yaxis_title='Koszt (USD)',
        barmode='group',
        height=400
    )
    
    # Wyświetlenie wykresu
    st.plotly_chart(fig, use_container_width=True)
    
    # Obliczenie i wyświetlenie różnicy
    roznica = nowy_koszt - bazowy_koszt
    roznica_procent = oblicz_roznice_procentowe(bazowy_koszt, nowy_koszt)
    
    # Wyświetlenie komunikatu o różnicy
    if roznica > 0:
        st.warning(f"⚠️ Nowy scenariusz zwiększa koszt o **{sformatuj_kwote(abs(roznica))}** ({abs(roznica_procent):.1f}%)")
    elif roznica < 0:
        st.success(f"✅ Nowy scenariusz zmniejsza koszt o **{sformatuj_kwote(abs(roznica))}** ({abs(roznica_procent):.1f}%)")
    else:
        st.info(f"ℹ️ Nowy scenariusz nie zmienia kosztu")

def main():
    """
    Główna funkcja aplikacji
    """
    # Informacja w pasku bocznym
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/000000/health-insurance.png", width=100)
        st.title("O aplikacji")
        st.markdown("""
        Ta aplikacja wykorzystuje uczenie maszynowe do przewidywania kosztów ubezpieczenia na życie.
        
        **Jak używać:**
        1. Wypełnij formularz swoimi danymi
        2. Zobacz przewidywany koszt
        3. Sprawdź podpowiedzi jak obniżyć koszt
        4. Użyj suwaków do porównania scenariuszy
        
        **Technologie:**
        - 🐍 Python
        - 🎈 Streamlit
        - 🤖 PyCaret
        - 📊 Plotly
        """)
        
        st.markdown("---")
        st.caption("© 2025 Prognoza Cen Ubezpieczeń")
    
    # Wczytanie modelu
    model = wczytaj_model()
    
    # Sprawdzenie czy model został wczytany
    if model is None:
        st.error("❌ Nie znaleziono wytrenowanego modelu!")
        st.warning("⚠️ Najpierw uruchom skrypt trenowania modelu: `python trenowanie_modelu.py`")
        st.stop()
    else:
        st.success("✅ Model został pomyślnie wczytany!")
    
    # Renderowanie sekcji formularza
    dane_uzytkownika = sekcja_formularz()
    
    st.markdown("---")
    
    # Przycisk do wykonania predykcji
    if st.button("🔮 Przewiduj koszt ubezpieczenia", type="primary", use_container_width=True):
        # Zapisanie danych w session_state
        st.session_state['dane_uzytkownika'] = dane_uzytkownika
        st.session_state['wykonano_predykcje'] = True
    
    # Sprawdzenie czy wykonano predykcję
    if st.session_state.get('wykonano_predykcje', False):
        # Pobranie danych z session_state
        dane = st.session_state['dane_uzytkownika']
        
        st.markdown("---")
        
        # Renderowanie sekcji predykcji
        przewidywany_koszt = sekcja_predykcja(model, dane)
        
        # Zapisanie kosztu w session_state
        st.session_state['bazowy_koszt'] = przewidywany_koszt
        
        st.markdown("---")
        
        # Renderowanie sekcji podpowiedzi
        sekcja_podpowiedzi(dane, przewidywany_koszt)
        
        st.markdown("---")
        
        # Renderowanie sekcji porównania
        sekcja_porownanie(model, dane, przewidywany_koszt)

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
