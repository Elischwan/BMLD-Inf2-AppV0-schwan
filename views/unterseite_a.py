import streamlit as st

st.title("Umrechnen")

st.write("Einheiten umrechnen von Meter in Centimeter")


from functions.Einheiten import umrechnen


try:
    eingabe = st.number_input("Metern eingeben: ")
    
    m = float(eingabe)
    cm = umrechnen(m)
    print(f"{m} m entsprechen {cm} cm")
except ValueError:
    print("Bitte eine gültige Zahl eingeben.")
    submit = st.button("umrechnen")
    if submit:
        st.write("Resultat")


try:
    eingabe = st.number_input("Tage eingeben: ")
    m = float(eingabe)
    cm = umrechnen(m)
    print(f"{m} m entsprechen {cm} cm")
except ValueError:
    print("Bitte eine gültige Zahl eingeben.")
    submit = st.button("umrechnen")
    if submit:
        st.write("Resultat")


