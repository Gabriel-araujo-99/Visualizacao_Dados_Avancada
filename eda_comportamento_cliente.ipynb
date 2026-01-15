from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/Neon/PycharmProjects/ecommerce_estatistica.csv')


df['Qtd_Vendidos'] = df['Qtd_Vendidos'].astype(str).str.replace(r'[+,]', '', regex=True)
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')
df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')
df['N_Avaliações'] = pd.to_numeric(df['N_Avaliações'], errors='coerce')
df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce')
df['Desconto'] = pd.to_numeric(df['Desconto'], errors='coerce')
df['Qtd_Vendidos_Cod'] = pd.to_numeric(df['Qtd_Vendidos_Cod'], errors='coerce')

print("\n--- Análise Inicial ---")
print(f"Número de Linhas e Colunas: {df.shape}")
print("\nTipos de Dados com valores Núlos:", df.isnull().sum())
print("\nTop 5 Marcas:", df['Marca'].value_counts().head(5))
print("\nEstatística Descritiva Das Variáveis Numéricas:", df.describe())


def criar_histograma(df):
    # 1. Gráfico de Histograma
    fig1 = px.histogram(
        df,
        x="Qtd_Vendidos_Cod",
        nbins=100,
        color_discrete_sequence=['green'],
        opacity=0.8,
        title='Histograma de Quantidades de Vendidos Cod',
        labels={'Qtd_Vendidos_Cod': 'Quantidade de Vendidos (Codificada)', 'count': 'Frequência'}
    )

    fig1.update_layout(
        bargap=0.01
    )
    return fig1

def criar_dispersao(df):
    # 2. Gráfico de dispersão
    fig2 = px.scatter(df, x='Qtd_Vendidos', y='Preço', color='N_Avaliações', size='N_Avaliações', hover_data=['Marca', 'Título'])
    fig2.update_layout(
        title='Relação entre Vendas e Preço por N° de Avaliações',
        xaxis_title='Quantidade',
        yaxis_title='Preço'
    )
    return fig2

def criar_mapa_calor(df):
    # 3. Gráfico Mapa de Calor
    mapa_corr = ['Preço', 'Nota', 'N_Avaliações', 'Desconto']
    mapa_matrix = df[mapa_corr].corr()

    fig3 = px.imshow(
        mapa_matrix,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale='RdBu_r',
        title="Mapa de Calor: Matriz de Correlação Variáveis Chaves"
    )
    fig3.update_layout(xaxis=dict(tickangle=-45))
    return fig3

def criar_grafico_barras(df):
    # 4. Gráfico de Barras
    df_grouped = df['Gênero'].value_counts().reset_index()
    df_grouped.columns = ['Gênero', 'Contagem']

    fig4 = px.bar(
        df_grouped,
        x='Gênero',
        y='Contagem',
        color='Gênero',
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Gráfico de Barras: Distribuição de Produtos por Gênero'
    )
    fig4.update_layout(
        xaxis_title='Gênero',
        yaxis_title='N° de Produtos'
    )
    return fig4

def criar_grafico_pizza(df):
    # 5. Gráfico de Pizza
    top_marcas_counts = df['Marca'].value_counts().nlargest(10).reset_index()
    top_marcas_counts.columns = ['Marca', 'Contagem']

    fig5 = px.pie(
        top_marcas_counts,
        names='Marca',
        values='Contagem',
        title='Gráfico de Pizza: Top 10 Marcas',
        hole=.3
    )
    return fig5

def criar_distribuicao_preco(df):
    # 6. Gráfico de Densidade
    fig6 = px.histogram(
        df,
        x="Preço",
        marginal="violin", # 'kde' não está disponível, mas 'violin' mostra bem a densidade
        histnorm='probability density',
        color_discrete_sequence=['#1A5A99'],
        opacity=0.8,
        title="6. Distribuição de Densidade dos Preços",
        labels={'Preço': 'Preço', 'y': 'Densidade (Frequência Relativa)'}
    )
    fig6.update_layout(yaxis_title='Densidade', bargap=0.05)
    return fig6

def criar_regressao(df):
    df_reg = df.copy()
    df_reg = df_reg[np.isfinite(df_reg['Preço']) & np.isfinite(df_reg['Qtd_Vendidos'])]

    fig7 = px.scatter(df_reg, x="Preço", y="Qtd_Vendidos", trendline="ols",
                      title="7. Gráfico de Regressão: Relação entre Preço e Quantidade Vendida (OLS)")
    return fig7


def criar_app(df):
    app = Dash(__name__)


    app.layout = html.Div(style={'padding': '10px'}, children=[

        html.H1(children='Dashboard de E-commerce',
                style={'textAlign': 'center', 'color': '#333333'}),

        html.Hr(),

        # Gráfico 1: Histograma
        dcc.Graph(id='g1-histograma', figure=criar_histograma(df)),

        html.Hr(),

        # Gráfico 2: Dispersão
        dcc.Graph(id='g2-dispersao', figure=criar_dispersao(df)),

        html.Hr(),

        # Gráfico 3: Mapa de Calor
        dcc.Graph(id='g3-mapa-calor', figure=criar_mapa_calor(df)),

        html.Hr(),

        # Gráfico 4: Barras
        dcc.Graph(id='g4-barras', figure=criar_grafico_barras(df)),

        html.Hr(),

        # Gráfico 5: Pizza
        dcc.Graph(id='g5-pizza', figure=criar_grafico_pizza(df)),

        html.Hr(),

        # Gráfico 6: Distribuição de Preço (Densidade)
        dcc.Graph(id='g6-dist-preco', figure=criar_distribuicao_preco(df)),

        html.Hr(),

        # Gráfico 7: Regressão
        dcc.Graph(id='g7-regressao', figure=criar_regressao(df)),
    ])
    return app



if __name__ == '__main__':
    # 1. Cria o objeto app do Dash
    app = criar_app(df)

    print("\nIniciando o servidor Dash...")


    app.run(debug=True, port=8050)
