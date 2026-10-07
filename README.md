# Project_DataViz · Músicas e Filmes em números

Projeto Final da disciplina **Visualização de Dados** Prof. Lívia Stein Freitas

## Equipe

| Integrante | GitHub |
|---|---|
| Fernanda | @nanda-vl |
| Giovanna | @Giovanna Bento |
| Leticia | @Le-Costa |
| Maria | @Vichinheski |

## Tema

O que faz uma música ou um filme ser popular? O projeto analisa dois datasets independentes: músicas de playlists do Spotify e filmes populares do TMDB. A partir deles, investiga gênero, época de lançamento, duração, idioma e avaliação do público.

## Perguntas

**Músicas (Spotify)**
1. Quais gêneros de playlist têm as músicas mais populares?
2. A popularidade das músicas muda conforme o ano de lançamento?
3. Características do áudio (energia, acusticidade, fala, ao vivo) têm relação com a popularidade?
4. As músicas ficaram mais curtas ao longo das décadas?

**Filmes (TMDB)**

5. Quais gêneros de filme têm as maiores notas médias?
6. Como a quantidade de filmes e a nota média mudam por década de lançamento?
7. Filmes com mais votos também têm notas mais altas?
8. Quais idiomas originais aparecem mais e como são avaliados?

## Datasets

| Dataset | Arquivo | Linhas originais | Linhas após limpeza |
|---|---|---|---|
| [30000 Spotify Songs (Kaggle)](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs) | `data/musicas/spotify_songs.csv` | 32.833 | 32.221 (28.327 músicas únicas) |
| Top Movies dataset · TMDB (https://www.kaggle.com/datasets/rishabhchaudhary07/top-movies-ratings-
genres-popularity-and-metadata) | `data/filmes/top_movies_dataset.csv` | 9.837 | 9.826 |

## Estrutura

```
Project_DataViz/
├── data/
│   ├── musicas/spotify_songs.csv        # original
│   ├── filmes/top_movies_dataset.csv    # original
│   └── limpos/                          # gerado por 01_limpeza.ipynb
│       ├── musicas_limpas.csv
│       ├── filmes_limpos.csv
│       ├── filmes_generos.csv           # uma linha por filme e gênero
│       └── musicas_filmes_por_ano.csv   # junção dos dois temas por ano
├── notebooks/
│   ├── 01_limpeza.ipynb                 # limpeza + primeiras estatísticas
│   └── 02_graficos.ipynb                # um gráfico por pergunta
├── src/utils.py                         # caminhos, cores e estilo dos gráficos
├── images/                              # gráficos exportados (PNG)
├── docs/                                # documentação e slides
└── requirements.txt
```

## Como rodar

```bash
git clone https://github.com/<usuario>/Project_DataViz.git
cd Project_DataViz
pip install -r requirements.txt
jupyter notebook
```

Rode `notebooks/01_limpeza.ipynb` e depois `notebooks/02_graficos.ipynb`, do início ao fim.

## Principais decisões de limpeza

- **Músicas:** foram removidas 5 linhas sem nome nem artista, 582 repetições da mesma música dentro da mesma playlist e 25 faixas com menos de 1 minuto. O ano foi extraído da data, que vinha em três formatos diferentes. A duração foi convertida para minutos.
- **Filmes:** foram removidas 11 linhas quebradas por uma sinopse com quebras de linha. Votos e nota foram convertidos de texto para número, e a data foi convertida a partir de `dd/mm/aaaa`. A nota 0 de filmes sem votos virou ausente, e as perguntas sobre nota usam só filmes com 50 votos ou mais. Títulos repetidos foram mantidos, porque são remakes.
