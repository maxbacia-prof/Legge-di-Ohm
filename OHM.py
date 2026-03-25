import streamlit as st

st.set_page_config(page_title="Legge di Ohm", page_icon="⚡", layout="centered")

st.title("⚡ Calcolatore Legge di Ohm")
st.write("Inserisci due valori per calcolare il terzo e visualizzare la formula nel triangolo.")

# 1. Selezione di cosa calcolare
scelta = st.radio(
    "Cosa vuoi calcolare?",
    ("Tensione (V)", "Corrente (I)", "Resistenza (R)"),
    horizontal=True
)

st.divider()

col1, col2 = st.columns([2, 1])  # Colonna 1 più larga per gli input

with col1:
    st.subheader("Input Dati")
    if scelta == "Tensione (V)":
        r = st.number_input("Resistenza R [Ω]", min_value=0.1, value=10.0, step=0.1)
        i = st.number_input("Corrente I [A]", min_value=0.001, value=0.5, step=0.001)
        risultato = r * i
        formula_latex = r"V = R \cdot I"
        unita = "V"
        # Variabili per il triangolo (testo da mostrare)
        txt_v = f"{risultato:.2f}V"
        txt_r = f"{r:.1f}Ω"
        txt_i = f"{i:.2f}A"
        # Colori per evidenziare il risultato
        col_v = "#ff4b4b"  # Rosso Streamlit per il risultato
        col_r = "#31333F"  # Colore testo standard
        col_i = "#31333F"

    elif scelta == "Corrente (I)":
        v = st.number_input("Tensione V [V]", min_value=0.1, value=12.0, step=0.1)
        r = st.number_input("Resistenza R [Ω]", min_value=0.1, value=10.0, step=0.1)
        risultato = v / r
        formula_latex = r"I = \frac{V}{R}"
        unita = "A"
        txt_v = f"{v:.1f}V"
        txt_r = f"{r:.1f}Ω"
        txt_i = f"{risultato:.2f}A"
        col_v = "#31333F"
        col_r = "#31333F"
        col_i = "#ff4b4b"  # Rosso per il risultato

    else:  # Resistenza (R)
        v = st.number_input("Tensione V [V]", min_value=0.1, value=12.0, step=0.1)
        i = st.number_input("Corrente I [A]", min_value=0.001, value=0.1, step=0.001)
        risultato = v / i
        formula_latex = r"R = \frac{V}{I}"
        unita = "Ω"
        txt_v = f"{v:.1f}V"
        txt_r = f"{risultato:.1f}Ω"
        txt_i = f"{i:.2f}A"
        col_v = "#31333F"
        col_r = "#ff4b4b"  # Rosso per il risultato
        col_i = "#31333F"

with col2:
    st.subheader("Risultato")
    st.metric(label=scelta, value=f"{risultato:.3f} {unita}")
    st.latex(formula_latex)

st.divider()

# --- PARTE VISIVA: Il Triangolo della Legge di Ohm ---
st.subheader("Rappresentazione Visiva (Triangolo)")

# HTML/CSS per il triangolo dinamico
html_triangolo = f"""
<div style="display: flex; justify-content: center; align-items: center; margin: 20px 0; font-family: sans-serif;">
    <div style="position: relative; width: 0; height: 0; border-left: 150px solid transparent; border-right: 150px solid transparent; border-bottom: 260px solid #f0f2f6; border-radius: 10px;">

        <div style="position: absolute; top: 80px; left: -50px; width: 100px; text-align: center;">
            <div style="font-size: 1.2rem; color: {col_v}; font-weight: bold;">V</div>
            <div style="font-size: 1rem; color: {col_v};">{txt_v}</div>
        </div>

        <div style="position: absolute; top: 150px; left: -110px; width: 220px; height: 4px; background-color: #31333F;"></div>

        <div style="position: absolute; top: 154px; left: -2px; width: 4px; height: 106px; background-color: #31333F;"></div>

        <div style="position: absolute; top: 180px; left: -90px; width: 80px; text-align: center;">
            <div style="font-size: 1.2rem; color: {col_r}; font-weight: bold;">R</div>
            <div style="font-size: 1rem; color: {col_r};">{txt_r}</div>
        </div>

        <div style="position: absolute; top: 180px; left: 10px; width: 80px; text-align: center;">
            <div style="font-size: 1.2rem; color: {col_i}; font-weight: bold;">I</div>
            <div style="font-size: 1rem; color: {col_i};">{txt_i}</div>
        </div>

    </div>
</div>
"""

# Rendering dell'HTML
st.markdown(html_triangolo, unsafe_allow_html=True)

# Consiglio didattico
st.info(
    "💡 **Come usare il triangolo:** Copri con la mano la grandezza che vuoi calcolare. Quello che vedi è la formula! (es. Copri V, vedi R e I affiancate -> R * I).")