import streamlit as st

st.set_page_config(page_title="Legge di Ohm", page_icon="⚡")

st.title("⚡ Calcolatore Legge di Ohm")


# Funzione per la virgola italiana
def ita(valore, dec=2):
    return f"{valore:.{dec}f}".replace('.', ',')


scelta = st.radio("Cosa vuoi calcolare?", ("Tensione (V)", "Corrente (I)", "Resistenza (R)"), horizontal=True)

st.divider()

# Inizializziamo le variabili per evitare errori
v, r, i = 0.0, 0.0, 0.0

col1, col2 = st.columns([2, 1])

with col1:
    if scelta == "Tensione (V)":
        r = st.number_input("Resistenza R [Ω]", min_value=0.1, value=100.0, step=0.1)
        i = st.number_input("Corrente I [A]", min_value=0.001, value=0.02, step=0.001)
        v = r * i
        res_finale = f"{ita(v)} V"
        formula = r"V = R \cdot I"
        c_v, c_r, c_i = "#ff4b4b", "#31333F", "#31333F"

    elif scelta == "Corrente (I)":
        v = st.number_input("Tensione V [V]", min_value=0.1, value=12.0, step=0.1)
        r = st.number_input("Resistenza R [Ω]", min_value=0.1, value=220.0, step=0.1)
        i = v / r
        res_finale = f"{ita(i, 3)} A"  # 3 decimali per gli Ampere sono meglio
        formula = r"I = \frac{V}{R}"
        c_v, c_r, c_i = "#31333F", "#31333F", "#ff4b4b"

    else:  # Resistenza (R)
        v = st.number_input("Tensione V [V]", min_value=0.1, value=5.0, step=0.1)
        i = st.number_input("Corrente I [A]", min_value=0.001, value=0.02, step=0.001)
        r = v / i
        res_finale = f"{ita(r, 1)} Ω"
        formula = r"R = \frac{V}{I}"
        c_v, c_r, c_i = "#31333F", "#ff4b4b", "#31333F"

with col2:
    st.subheader("Risultato")
    st.latex(formula)
    st.header(res_finale)

st.divider()

# Disegno del triangolo SVG (sempre visibile)
txt_v, txt_r, txt_i = ita(v, 1), ita(r, 1), ita(i, 3)

html_triangolo = f"""
<div style="display: flex; justify-content: center; background-color: white; padding: 10px; border-radius: 10px;">
    <svg width="280" height="200" viewBox="0 0 300 200">
        <path d="M 150 10 L 290 190 L 10 190 Z" fill="#f9f9f9" stroke="#31333F" stroke-width="3"/>
        <line x1="80" y1="110" x2="220" y2="110" stroke="#31333F" stroke-width="3"/>
        <line x1="150" y1="110" x2="150" y2="190" stroke="#31333F" stroke-width="3"/>
        <text x="150" y="75" text-anchor="middle" font-family="Arial" font-weight="bold" fill="{c_v}" font-size="22">V</text>
        <text x="150" y="95" text-anchor="middle" font-family="Arial" fill="{c_v}" font-size="14">{txt_v}V</text>
        <text x="80" y="150" text-anchor="middle" font-family="Arial" font-weight="bold" fill="{c_r}" font-size="22">R</text>
        <text x="80" y="170" text-anchor="middle" font-family="Arial" fill="{c_r}" font-size="14">{txt_r}Ω</text>
        <text x="220" y="150" text-anchor="middle" font-family="Arial" font-weight="bold" fill="{c_i}" font-size="22">I</text>
        <text x="220" y="170" text-anchor="middle" font-family="Arial" fill="{c_i}" font-size="14">{txt_i}A</text>
    </svg>
</div>
"""
st.markdown(html_triangolo, unsafe_allow_html=True)

# Potenza in Watt solo come info extra in fondo
potenza = v * i
st.write(f"ℹ️ **Potenza dissipata:** {ita(potenza, 3)} Watt")