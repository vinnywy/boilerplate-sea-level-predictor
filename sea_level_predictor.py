import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
      # Importar dados
    df = pd.read_csv('epa-sea-level.csv')

    # Criar gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')

    # Linha de melhor ajuste para todos os dados
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_ext = range(1880, 2051)
    plt.plot(years_ext,
             res_all.intercept + res_all.slope * pd.Series(years_ext),
             'r', label='Best fit: 1880-2050')

    # Linha de melhor ajuste para dados desde 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    plt.plot(years_recent,
             res_recent.intercept + res_recent.slope * pd.Series(years_recent),
             'g', label='Best fit: 2000-2050')

    # Rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Salvar e retornar imagem
    plt.savefig('sea_level_plot.png')
    return plt.gca()
  