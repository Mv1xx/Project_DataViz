"""Funções e constantes compartilhadas pelos notebooks do projeto."""
from pathlib import Path

import matplotlib.pyplot as plt

# Caminhos a partir da raiz do repositório
RAIZ = Path(__file__).resolve().parents[1]
DATA = RAIZ / "data"
LIMPOS = DATA / "limpos"
IMAGENS = RAIZ / "images"

# Paleta única para o projeto inteiro
COR_MUSICA = "#1DB954"   # verde (músicas)
COR_FILME = "#E50914"    # vermelho (filmes)
COR_NEUTRA = "#4A5568"

GENEROS_MUSICA = {
    "pop": "Pop", "rap": "Rap", "rock": "Rock",
    "latin": "Latina", "r&b": "R&B", "edm": "EDM",
}

IDIOMAS = {
    "en": "Inglês", "ja": "Japonês", "es": "Espanhol", "fr": "Francês",
    "ko": "Coreano", "zh": "Chinês", "it": "Italiano", "cn": "Cantonês",
    "ru": "Russo", "de": "Alemão", "pt": "Português", "hi": "Hindi",
    "da": "Dinamarquês", "no": "Norueguês", "sv": "Sueco", "pl": "Polonês",
    "nl": "Holandês", "th": "Tailandês", "tr": "Turco", "id": "Indonésio",
}


def estilo():
    """estilo padrão gráficos."""
    plt.rcParams.update({
        "figure.figsize": (10, 5.5),
        "figure.dpi": 110,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelsize": 11,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "font.size": 10,
    })


def salvar(fig, nome):
    """Salva a figura em images/ com nome padronizado."""
    IMAGENS.mkdir(exist_ok=True)
    caminho = IMAGENS / f"{nome}.png"
    fig.savefig(caminho, dpi=150, bbox_inches="tight")
    return caminho
