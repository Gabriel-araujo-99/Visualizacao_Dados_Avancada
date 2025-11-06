# 📊 Dashboard Interativo: Análise Avançada de Dados de E-commerce

°° Este projeto demonstra a criação de um dashboard web simples, mas funcional, para análise exploratória de dados (EDA) de e-commerce, utilizando o framework Dash e a biblioteca de visualização Plotly Express.

## 🌟 O Projeto e as Ferramentas

°° O dashboard exibe 7 visualizações principais para analisar a relação entre preço, quantidade vendida, notas e avaliações dos produtos.

## 🛠️ Tecnologias Utilizadas 
> **Nota:** Ferramentas Utilizadas para a realização do projeto

### Pandas :
° Biblioteca fundamental para manipulação e análise de dados. Responsável pelo carregamento do arquivo CSV...

### Plotly Express :
° Biblioteca de alto nível para a criação de gráficos interativos...

### Dash :

° Framework Python para construir a aplicação web, transformando os gráficos Plotly em uma aplicação web completa. O Dash fornece os componentes (como dcc.Graph e html.Div) para construir o layout da página e executar o servidor web local.

### NumPy e Statsmodels :

° Bibliotecas de suporte utilizadas para operações matemáticas e estatísticas. O NumPy é essencial para lidar com a filtragem de valores não finitos (np.isfinite), e o Statsmodels é usado internamente pelo Plotly para calcular a linha de Regressão Linear (OLS).

## 💻 Análise do Código Passo a Passo

° O script dashboard_ecommerce_final.py (ou Atividade_visualizacao_avancada.py) é estruturado para garantir a limpeza dos dados antes de gerar o dashboard.

# 1. Importação de Bibliotecas

> **Nota:** As bibliotecas são importadas e apelidadas para uso eficiente:

### import pandas as pd :
° Manipulação e análise de dados em formato de DataFrame (tabela).

### import plotly.express as px :
° Criação de gráficos interativos com poucas linhas de código.

### import numpy as np : 
° Funções matemáticas de alto desempenho, utilizadas para filtrar valores válidos (np.isfinite).

### from dash import Dash, dcc, html :
° Componentes essenciais do Dash para montar a interface web.

# 2. Análise Inicial e Inspeção de Dados

### print(f"Número de Linhas e Colunas: {df.shape}") :
° Mostrar o DataFrame

### print("\nTipos de Dados com valores Núlos:", df.isnull().sum()):
° Verifica a contagem de valores nulos por coluna.

### print("\nEstatística Descritiva Das Variáveis Numéricas:", df.describe()):
° Calcula estatísticas básicas (média, quartis, etc.) das variáveis numéricas.

# 3. Gráficos

## *1. Gráfico Histograma

### px.histogram(...):
° Cria o histograma da variável codificada de quantidade vendida (Qtd_Vendidos_Cod).

### nbins=100 :
° Divide os dados em 100 barras para uma visualização detalhada da distribuição.

## *2. Gráfico de Dispersão(Relação entre Variáveis)

### px.scatter(x='Qtd_Vendidos', y='Preço', ...):
° Mostra a relação entre a Quantidade Vendida e o Preço.

### color='N_Avaliações', size='N_Avaliações':
° A cor e o tamanho dos pontos são mapeados pela coluna N_Avaliações, adicionando uma terceira e quarta dimensão de análise ao gráfico.

## *3. Gráfico Mapa de calor(Correlação):

### mapa_matrix = df[mapa_corr].corr():
° Calcula a matriz de correlação entre as variáveis-chave.

### px.imshow(mapa_matrix, text_auto=".2f", ...) :
° Utiliza o Plotly para visualizar a matriz. text_auto garante que os valores de correlação apareçam dentro das células.

## *4. Gráfico de Barra:

### df['Gênero'].value_counts().reset_index():
° Agrupa e conta a frequência de produtos por gênero.

### px.bar(...): 
° Cria o gráfico de barras para visualizar a distribuição de produtos.

## *5. Gráfico de Pizza:

### df['Marca'].value_counts().nlargest(10):
Filtra e conta as 10 marcas mais frequentes no conjunto de dados.

### px.pie(...):
° Cria um gráfico de pizza (ou rosca, usando hole=.3) para mostrar a participação percentual dessas marcas.

## *6. Gráfico de Densidade:

### marginal="violin":
° O Plotly utiliza este parâmetro no histograma para adicionar uma visualização lateral de densidade (similar ao KDE), mostrando a forma exata da distribuição de preços.

### histnorm='probability density':
° Normaliza o eixo Y para mostrar a densidade de probabilidade.

## *7. Gráfico de Regressão:

### df_reg[...]:
° Esta é a etapa de filtragem essencial que remove valores inválidos (NaN/Infinito) para o cálculo estatístico.
 
### trendline="ols":
° O Plotly utiliza a biblioteca Statsmodels para sobrepor uma linha de Mínimos Quadrados Ordinários (OLS) no gráfico de dispersão, estimando a tendência da relação entre Preço e Quantidade Vendida.

# 4. Layout Dash e Execução:
> **Nota:** Esta seção finaliza a construção da aplicação web.

### app.layout = html.Div(children=[...]): 
° Define a estrutura da página usando componentes Dash.

### dcc.Graph(figure=criar_histograma(df)):
° É o componente Dash que recebe o objeto Plotly (fig) e o renderiza no navegador.
 
### app.run(debug=True, port=8050):
° Inicia o servidor local para que o dashboard possa ser acessado pelo navegador.