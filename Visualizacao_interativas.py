from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv('C:/Users/Neon/PycharmProjects/clientes-v3-preparado.csv')
lista_nivel_educacao = df['nivel_educacao'].unique()
options = [{'label': nivel, 'value': nivel} for nivel in lista_nivel_educacao]

def criar_grafico(selecao_nivel_educacao):
    # Gráfico de Barra
    filtro_df = df[df['nivel_educacao'].isin(selecao_nivel_educacao)]

    fig1 = px.bar(filtro_df, x="estado_civil", y="salario", color="nivel_educacao", barmode="group", color_discrete_sequence=px.colors.sequential.Viridis)
    fig1.update_layout(
        title='Salário por Estado Cívil e Nível de Educação',
        xaxis_title='Estado Cívil',
        yaxis_title='Salário',
        legend_title='Nível de Educação',
        plot_bgcolor='rgb(222, 255, 253, 1)', # Funndo interno
        paper_bgcolor='rgb(186, 245, 241, 1)' # Fundo externo
    )
    fig2 = px.scatter_3d(filtro_df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')
    fig2.update_layout(
        title='Salário vs Idade e Anos de Experiência',
        scene=dict(
            xaxis_title='Idade',
            yaxis_title='Salario',
            zaxis_title='Anos de Experencia'
        )
    )
    return fig1, fig2

def criar_app():
    # criar App
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Dashboard Interativo"),
        html.Div('''
        Interatividade entre os 
        dados.'''),
        html.Br(),
        html.H2("Gráfico de Salário por Estado Cívil"),
        dcc.Checklist(
            id='id_selecao_nivel_educador',
            options=options,
            value=[lista_nivel_educacao[0]], # Definir valor padrão
        ),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_3d')
    ])
    return app




# Executar App
if __name__ == '__main__':
    app = criar_app()

    @app.callback(
    [
        Output('id_grafico_barra', 'figure'),
        Output('id_grafico_3d', 'figure'),
    ],
    [Input('id_selecao_nivel_educador', 'value')]
    )
    def atualizar_grafico(selecao_nivel_educacao):
        fig1, fig2 = criar_grafico(selecao_nivel_educacao)
        return fig1, fig2
    app.run(debug=True, port=8050) # Default 8050
