import streamlit as st

st.set_page_config(page_title="Legge di Ohm", page_icon="⚡")

st.title("⚡ Calcolatore Legge di Ohm")


# Funzione per formattare i numeri con la virgola all'italiana
def format_ita(valore, decimali=2):
    return f"{valore:.{decimali}f}".replace('.', ',')


scelta = st.radio("Cosa vuoi calcolare?", ("Tensione (V)", "Corrente (I)", "Resistenza (R)"), horizontal=True)

st.divider()
col1, col2 = st.columns([2, 1])

with col1:
    if scelta == "Tensione (V)":
        r = st.number_input("Resistenza R [Ω]", min_value=0.1, value=100.0)
        i = st.number_input("Corrente I [A]", min_value=0.001, value=0.02)
        res = r * i
        unita = "V"
        v_testo, r_testo, i_testo = format_ita(res), format_ita(r, 1), format_ita(i)
        c_v, c_r, c_i = "#ff4b4b", "#31333F", "#31333F"

    elif scelta == "Corrente (I)":
        v = st.number_input("Tensione V [V]", min_value=0.1, value=12.0)
        r = st.number_input("Resistenza R [Ω]", min_value=0.1, value=220.0)
        res = v / r
        unita = "A"
        v_testo, r_testo, i_testo = format_ita(v, 1), format_ita(r, 1), format_ita(res)
        c_v, c_r, c_i = "#31333F", "#31333F", "#ff4b4b"

    else:  # Resistenza
        v = st.number_input("Tensione V [V]", min_value=0.1, value=5.0)
        i = st.number_input("Corrente I [A]", min_value=0.001, value=0.02)
        res = v / i
        unita = "Ω"
        v_testo, r_testo, i_testo = format_ita(v, 1), format_ita(res, 1), format_ita(i)
        c_v, c_r, c_i = "#31333F", "#ff4b4b", "#31333F"

with col2:
    st.subheader("Risultato")
    # Qui usiamo la virgola!
    st.header(f"{format_ita(res)} {unita}")
    st.write(f"P = {format_ita(v * i if 'v' in locals() else res * i if scelta == 'Tensione (V)' else v * i)} W")

st.divider()
st.subheader("Triangolo della Legge di Ohm")

# Disegno del triangolo con correzione per la visibilità
html_triangolo = f"""
<div style="display: flex; justify-content: center; background-color: white; padding: 20px; border-radius: 10px;">
    <svg width="300" height="200" viewBox="0 0 300 200">
        <path d="M 150 10 L 290 190 L 10 190 Z" fill="#f0f2f6" stroke="#31333F" stroke-width="3"/>
        <line x1="80" y1="110" x2="220" y2="110" stroke="#31333F" stroke-width="3"/>
        <line x1="150" y1="110" x2="150" y2="190" stroke="#31333F" stroke-width="3"/>
        <text x="150" y="70" text-anchor="middle" font-family="Arial" font-weight="bold" fill="{c_v}" font-size="20">V ({v_testo})</text>
        <text x="80" y="160" text-anchor="middle" font-family="Arial" font-weight="bold" fill="{c_r}" font-size="20">R ({r_testo})</text>
        <text x="220" y="160" text-anchor="middle" font-family="Arial" font-weight="bold" fill="{c_i}" font-size="20">I ({i_testo})</text>
    </svg>
</div>
"""
st.markdown(html_triangolo, unsafe_allow_html=True)