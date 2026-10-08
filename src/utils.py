"""Funções e constantes compartilhadas pelos notebooks do projeto."""
from pathlib import Path

import matplotlib.pyplot as plt

# Caminhos a partir da raiz do repositório
RAIZ = Path(__file__).resolve().parents[1]
DATA = RAIZ / "data"
LIMPOS = DATA / "limpos"
IMAGENS = RAIZ / "images"

# Paleta do projeto: uma cor por tema, sempre a mesma em todos os gráficos.
# Azul e laranja em vez de verde e vermelho, que são difíceis de separar
# para quem tem daltonismo.
COR_MUSICA = "#2A78D6"         # azul: músicas
COR_MUSICA_CLARA = "#BFD6F2"
COR_FILME = "#E8590C"          # laranja: filmes
COR_FILME_CLARA = "#F8C9AE"
COR_CINZA = "#C5CAD3"          # o que não é destaque
COR_TEXTO = "#3F4652"          # rótulos e anotações
COR_SUBTITULO = "#6B7280"

FONTE_MUSICAS = "Fonte: Spotify, via dataset 30000 Spotify Songs (Kaggle)"
FONTE_FILMES = "Fonte: TMDB, via dataset Top Movies (Kaggle)"

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
    """Aplica o estilo padrão dos gráficos."""
    plt.rcParams.update({
        "figure.figsize": (10, 5.5),
        "figure.dpi": 110,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#9CA3AF",
        "axes.labelcolor": COR_TEXTO,
        "axes.labelsize": 11,
        "axes.grid": False,
        "xtick.color": COR_TEXTO,
        "ytick.color": COR_TEXTO,
        "font.size": 10,
    })


def titulos(ax, titulo, subtitulo):
    """Título com a conclusão (negrito) e subtítulo com medida e período (cinza)."""
    ax.set_title(titulo, loc="left", fontsize=14, fontweight="bold", pad=30, color="#111827")
    ax.text(0, 1.035, subtitulo, transform=ax.transAxes, fontsize=10.5,
            color=COR_SUBTITULO, va="bottom", ha="left")


def fonte(fig, texto):
    """Nota de fonte no rodapé da figura."""
    fig.text(0.01, -0.01, texto, fontsize=8.5, color=COR_SUBTITULO, ha="left", va="top")


def salvar(fig, nome):
    """Salva a figura em images/ com nome numerado e descritivo."""
    IMAGENS.mkdir(exist_ok=True)
    caminho = IMAGENS / f"{nome}.png"
    fig.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    return caminho
