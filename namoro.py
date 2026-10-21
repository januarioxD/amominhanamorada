import random
from datetime import date

import streamlit as st

# ============================================================
# EDITE AQUI: troque pelos dados de vocês dois
# ============================================================
SEU_NOME = "Seu nome"
NOME_DELA = "Collen"
INICIO_NAMORO = date(2026, 10, 18)  # ano, mês, dia em que vocês começaram

MOMENTOS = [
    ("O dia em que nos conhecemos", "o dia que eu te conheci foi a melhor coisa do mundo, cada sorriso e conversas que tivemos foi perfeito."),
    ("O dia em que começamos a namorar", "o dia que eu pedi para namorar foi o dia mais especial para mim pois eu soou muito apaixonado por voce."),
    
]

MOTIVOS = [
    "voce melhora meu dia.",
    "Voce realmente cuida de mim.",
    "voce e a garota mais especil do mundo.",
    "voce e a garota mais gostosa cuti cuti."
]

CARTA = """Collen,
Oi meu amor vim aqui dizer que vc e a garota mais incrivel que eu conheci, voce tornou meus dias mais felizes eu amo cada detalhe seu voce e uma garota que merece tudo e mais um pouco e quero muito ver voce minha garotinha.


Com todo o meu carinho,
{seu_nome}"""

FOTOS = []  # ex.: ["foto1.jpg", "foto2.jpg"] (arquivos na mesma pasta)
LEGENDAS = []  # ex.: ["Nossa primeira viagem", "Aquele pôr do sol"]

PEDIDO = "Quer continuar sendo a minha pessoa favorita?"

# ============================================================
# Configuração e estilo
# ============================================================
st.set_page_config(page_title=f"Para {NOME_DELA}", page_icon="💗", layout="centered")

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Nunito:wght@400;600;700&family=Caveat:wght@600&display=swap');

:root { --rosa: #FFE3EC; --framboesa: #D6336C; --lavanda: #EDE5FF; --ameixa: #3B1F3A;
        --manteiga: #FFF1B8; --branco: #FFFFFF; --suave: #7A5C78; }
html, body, [class*="css"], .stApp { font-family: 'Nunito', sans-serif; }
.stApp { background: linear-gradient(180deg, var(--rosa) 0%, #FFF7FA 45%, var(--lavanda) 100%);
         color: var(--ameixa); }
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 760px; padding-top: 2.5rem; padding-bottom: 4rem; }

.hero { text-align: center; padding: 2rem 0 1rem; }
.hero .para { font-family: 'Caveat', cursive; font-size: 1.8rem; color: var(--framboesa); margin: 0; }
.hero h1 { font-family: 'Fraunces', serif; font-weight: 700; color: var(--ameixa);
           font-size: clamp(3rem, 12vw, 5.5rem); line-height: 1; margin: .2rem 0 1rem; letter-spacing: -0.02em; }
.hero .sub { color: var(--suave); font-size: 1.1rem; }
.coracao { display: inline-block; animation: bater 1.6s ease-in-out infinite; }
@keyframes bater { 0%,100% { transform: scale(1); } 15% { transform: scale(1.18); } 30% { transform: scale(1); } 45% { transform: scale(1.12); } }
@media (prefers-reduced-motion: reduce) { .coracao { animation: none; } }

.contador { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin: 1.5rem 0 .5rem; }
.contador div { background: var(--branco); border-radius: 22px; padding: 1rem 1.4rem; text-align: center;
                min-width: 110px; box-shadow: 0 6px 18px rgba(214, 51, 108, .12); }
.contador b { display: block; font-family: 'Fraunces', serif; font-size: 2.3rem; color: var(--framboesa); }
.contador span { color: var(--suave); font-size: .9rem; }

.titulo { font-family: 'Fraunces', serif; font-weight: 700; font-size: 2rem; text-align: center;
          margin: 3.2rem 0 1.2rem; color: var(--ameixa); }

.momento { background: var(--branco); border-radius: 18px; padding: 1.1rem 1.4rem; margin-bottom: .9rem;
           border-left: 6px solid var(--framboesa); box-shadow: 0 4px 14px rgba(59, 31, 58, .06); }
.momento:nth-child(even) { border-left-color: #9B7BE8; }
.momento h3 { font-family: 'Fraunces', serif; font-size: 1.2rem; margin: 0 0 .25rem; color: var(--ameixa); }
.momento p { margin: 0; color: var(--suave); line-height: 1.6; }

.motivo { background: var(--manteiga); border-radius: 20px; padding: 1.6rem 1.8rem; text-align: center;
          font-family: 'Caveat', cursive; font-size: 2rem; line-height: 1.25; color: var(--ameixa);
          transform: rotate(-1deg); box-shadow: 0 8px 20px rgba(59, 31, 58, .1); margin: 1rem 0; }

.carta { background: var(--branco); border-radius: 18px; padding: 2rem 2.2rem; line-height: 1.8;
         font-family: 'Caveat', cursive; font-size: 1.55rem; color: var(--ameixa); white-space: pre-line;
         box-shadow: 0 8px 24px rgba(59, 31, 58, .08); }

.pedido { font-family: 'Fraunces', serif; font-size: 1.7rem; text-align: center; margin: 3rem 0 1rem; }
.fim { text-align: center; font-family: 'Caveat', cursive; font-size: 1.8rem; color: var(--framboesa); margin-top: 1.5rem; }

.stButton > button { background: var(--framboesa); color: #fff; border: none; border-radius: 999px;
                     padding: .6rem 1.6rem; font-weight: 700; font-family: 'Nunito', sans-serif; }
.stButton > button:hover { background: #B82A5C; color: #fff; }
.stButton > button:focus-visible { outline: 3px solid var(--ameixa); outline-offset: 2px; }
details, [data-testid="stExpander"] { background: var(--branco); border-radius: 16px !important; border: none !important; }
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# Início
# ============================================================
dias = (date.today() - INICIO_NAMORO).days
meses, dias_resto = divmod(max(dias, 0), 30)

st.markdown(
    f"""
<div class="hero">
  <p class="para">um cantinho só para você</p>
  <h1>{NOME_DELA} <span class="coracao">💗</span></h1>
  <p class="sub">Feito com carinho por {SEU_NOME}</p>
</div>
<div class="contador">
  <div><b>{dias}</b><span>dias juntos</span></div>
  <div><b>{meses}</b><span>meses de amor</span></div>
  <div><b>∞</b><span>motivos para ficar</span></div>
</div>
""",
    unsafe_allow_html=True,
)

# Momentos
st.markdown('<div class="titulo">Nossa história</div>', unsafe_allow_html=True)
st.markdown(
    "".join(f'<div class="momento"><h3>{t}</h3><p>{d}</p></div>' for t, d in MOMENTOS),
    unsafe_allow_html=True,
)

# Motivos
st.markdown('<div class="titulo">Motivos para te amar</div>', unsafe_allow_html=True)
if "motivo" not in st.session_state:
    st.session_state.motivo = None

st.markdown(
    f'<div class="motivo">{st.session_state.motivo or "Toque no botão para ler um motivo"}</div>',
    unsafe_allow_html=True,
)
_, centro, _ = st.columns([1, 1.4, 1])
if centro.button("Sortear um motivo", use_container_width=True):
    opcoes = [m for m in MOTIVOS if m != st.session_state.motivo]
    st.session_state.motivo = random.choice(opcoes)
    st.rerun()

# Fotos
if FOTOS:
    st.markdown('<div class="titulo">Nossos momentos</div>', unsafe_allow_html=True)
    colunas = st.columns(min(len(FOTOS), 3))
    for i, foto in enumerate(FOTOS):
        with colunas[i % len(colunas)]:
            legenda = LEGENDAS[i] if i < len(LEGENDAS) else None
            st.image(foto, caption=legenda, use_container_width=True)

# Carta
st.markdown('<div class="titulo">Uma carta para você</div>', unsafe_allow_html=True)
with st.expander("Abrir carta 💌"):
    st.markdown(f'<div class="carta">{CARTA.format(seu_nome=SEU_NOME)}</div>', unsafe_allow_html=True)

# Pedido final
st.markdown(f'<div class="pedido">{PEDIDO}</div>', unsafe_allow_html=True)
if "respondeu" not in st.session_state:
    st.session_state.respondeu = False

if not st.session_state.respondeu:
    _, a, b, _ = st.columns([1, 1.2, 1.2, 1])
    if a.button("Sim, claro!", use_container_width=True):
        st.session_state.respondeu = True
        st.rerun()
    if b.button("Com certeza!", use_container_width=True):
        st.session_state.respondeu = True
        st.rerun()
else:
    st.balloons()
    st.markdown(
        f'<div class="fim">Eu sabia! Te amo, {NOME_DELA} 💗</div>',
        unsafe_allow_html=True,
    )
