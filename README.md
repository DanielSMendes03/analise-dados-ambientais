# Análise de Dados Ambientais para Soluções Sustentáveis nas Cidades

**Projeto Acadêmico - Data Science Fundamentals**

---

## 📋 Índice

1. [Descrição do Projeto](#1-descrição-do-projeto)
2. [Objetivos](#2-objetivos)
3. [Ciclo de Vida da Ciência de Dados](#3-ciclo-de-vida-da-ciência-de-dados)
4. [Estrutura do Projeto](#4-estrutura-do-projeto)
5. [Instalação e Execução](#5-instalação-e-execução)
6. [Funcionalidades Implementadas](#6-funcionalidades-implementadas)
7. [Resultados e Insights](#7-resultados-e-insights)
8. [Entregáveis](#8-entregáveis)

---

## 1. Descrição do Projeto

Este projeto consiste em analisar dados ambientais de cidades brasileiras para propor soluções inovadoras que promovam a sustentabilidade urbana. A análise utiliza técnicas de Data Science para identificar padrões, anomalias e gerar insights aplicáveis em políticas públicas e soluções sustentáveis.

### Contexto da Situação-Problema

- **O que?** Análise de dados ambientais (consumo energético, qualidade do ar, resíduos sólidos, uso de recursos naturais)
- **Quem?** Estudantes de Ciência de Dados em equipes multidisciplinares
- **Quando?** Projeto semestral com marcos intermediários
- **Onde?** Ambiente virtual e presencial com Python, Jupyter Notebook e Power BI
- **Por quê?** A análise de dados é essencial para entender problemas ambientais e propor soluções práticas

### Desafios Propostos

- ✅ Limpar e organizar os dados fornecidos
- ✅ Identificar padrões e anomalias nos dados
- ✅ Gerar insights aplicáveis à sustentabilidade
- ✅ Desenvolver apresentação visual com gráficos e dados explicativos

---

## 2. Objetivos

### Objetivo Principal

Aplicar o ciclo de vida completo da ciência de dados para analisar dados ambientais urbanos e gerar insights que contribuam para soluções sustentáveis.

### Objetivos Específicos

1. **Preparação de Dados**

   - Limpeza e validação de dados
   - Tratamento de valores nulos e outliers
   - Criação de métricas derivadas

2. **Análise Exploratória**

   - Estatísticas descritivas
   - Identificação de padrões e tendências
   - Detecção de anomalias
   - Análise de correlações

3. **Visualização**

   - Gráficos de evolução temporal
   - Comparações entre cidades
   - Matriz de correlação
   - Indicadores de sustentabilidade

4. **Geração de Insights**
   - Identificação de problemas críticos
   - Recomendações para políticas públicas
   - Análise de eficiência energética
   - Tendências ambientais

---

## 3. Ciclo de Vida da Ciência de Dados

O projeto segue o ciclo de vida completo da ciência de dados:

### 1. Entendimento do Problema

- Definição do objetivo: analisar dados ambientais para sustentabilidade urbana
- Identificação de variáveis relevantes
- Estabelecimento de métricas de sucesso

### 2. Coleta de Dados

- Carregamento de dados de arquivo CSV
- Validação da estrutura dos dados
- Verificação de completude

### 3. Preparação e Limpeza

- Remoção de duplicatas
- Tratamento de valores nulos
- Identificação e tratamento de outliers
- Criação de métricas derivadas (per capita, intensidade, etc.)

### 4. Análise Exploratória

- Estatísticas descritivas
- Análise de tendências temporais
- Identificação de anomalias
- Análise de correlações entre variáveis

### 5. Modelagem (Opcional)

- Análise de padrões usando estatística descritiva
- Identificação de clusters (se aplicável)

### 6. Visualização

- Gráficos de linha para evolução temporal
- Gráficos de barras para comparações
- Heatmaps de correlação
- Análises de distribuição

### 7. Comunicação dos Resultados

- Geração de insights acionáveis
- Relatório descritivo das descobertas
- Visualizações para apresentação

---

## 4. Estrutura do Projeto

```
sabor-express-fecaf/
│
├── data/
│   ├── dados_ambientais.csv          # Dados brutos
│   └── dados_ambientais_limpos.csv   # Dados processados (gerado)
│
├── src/
│   ├── __init__.py
│   ├── limpeza_dados.py              # Módulo de limpeza e preparação
│   ├── analise_dados.py              # Módulo de análise exploratória
│   └── visualizacoes.py              # Módulo de visualizações
│
├── graficos/                         # Gráficos gerados (criado automaticamente)
│   ├── evolucao_*.png
│   ├── comparacao_*.png
│   ├── matriz_correlacao.png
│   └── ...
│
├── analise_ambiental.py              # Script principal
├── requirements.txt                  # Dependências do projeto
└── README.md                         # Este arquivo
```

---

## 5. Instalação e Execução

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou baixe o repositório**

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

### Execução

Execute o script principal:

```bash
python analise_ambiental.py
```

O script irá:

1. Carregar os dados de `data/dados_ambientais.csv`
2. Limpar e preparar os dados
3. Realizar análises exploratórias
4. Gerar visualizações (salvas em `graficos/`)
5. Exibir insights e resultados no console

### Saída Esperada

- **Console**: Análises, estatísticas e insights impressos
- **Arquivos CSV**: `data/dados_ambientais_limpos.csv` (dados processados)
- **Gráficos PNG**: Pasta `graficos/` com todas as visualizações

---

## 6. Funcionalidades Implementadas

### 6.1 Limpeza e Preparação de Dados (`limpeza_dados.py`)

- ✅ Carregamento de dados CSV
- ✅ Validação de estrutura e qualidade
- ✅ Remoção de duplicatas
- ✅ Tratamento de valores nulos (preenchimento com mediana)
- ✅ Identificação e tratamento de outliers (método IQR)
- ✅ Criação de métricas derivadas:
  - Energia per capita
  - Resíduos per capita
  - Água per capita
  - CO₂ per capita
  - Intensidade de carbono
  - Eficiência hídrica

### 6.2 Análise Exploratória (`analise_dados.py`)

- ✅ Estatísticas descritivas (média, mediana, desvio padrão, etc.)
- ✅ Identificação de anomalias (métodos IQR e Z-score)
- ✅ Análise de tendências temporais por cidade
- ✅ Cálculo de matriz de correlação
- ✅ Comparação entre cidades
- ✅ Geração automática de insights

### 6.3 Visualizações (`visualizacoes.py`)

- ✅ Gráficos de evolução temporal (linha)
- ✅ Gráficos de comparação entre cidades (barras)
- ✅ Matriz de correlação (heatmap)
- ✅ Análises de distribuição (histograma + boxplot)
- ✅ Indicadores de sustentabilidade normalizados
- ✅ Tendência de emissões de CO₂

---

## 7. Resultados e Insights

### Principais Descobertas

1. **Padrões Identificados**

   - Correlação positiva entre população e consumo de energia
   - Tendência de aumento nas emissões de CO₂ na maioria das cidades
   - Variação significativa na qualidade do ar entre diferentes regiões

2. **Anomalias Detectadas**

   - Valores extremos identificados e tratados automaticamente
   - Necessidade de investigação adicional para casos específicos

3. **Insights para Sustentabilidade**
   - Cidades com maior população apresentam maiores desafios ambientais
   - Necessidade de políticas específicas por região
   - Importância de métricas per capita para comparações justas

### Recomendações Geradas

- Investimento em energia renovável nas cidades com maior consumo
- Programas de redução de resíduos e reciclagem
- Políticas públicas para melhoria da qualidade do ar
- Monitoramento contínuo e atualização dos dados

---

## 8. Entregáveis

### 8.1 Parte Teórica – Relatório em PDF (2,0 pontos)

O relatório deve conter:

- ✅ Descrição dos passos do ciclo de vida da ciência de dados aplicados
- ✅ Anexos com os gráficos gerados em Python
- ✅ Conclusão descritiva explicando descobertas, relevância e impacto

**Gráficos disponíveis em `graficos/` para anexar ao relatório**

### 8.2 Parte Prática – Código-Fonte em Python (4,0 pontos)

**Arquivo principal:** `analise_ambiental.py`

**Características do código:**

- ✅ Importação e manipulação de dados
- ✅ Tratamento e visualização (gráficos, estatísticas)
- ✅ Comentários explicativos nos trechos principais
- ✅ Organização e boas práticas de escrita em Python

**Módulos organizados:**

- `src/limpeza_dados.py`: Limpeza e preparação
- `src/analise_dados.py`: Análise exploratória
- `src/visualizacoes.py`: Visualizações

### 8.3 Vídeo Pitch de até 4 minutos (2,0 pontos)

O vídeo deve apresentar:

- Problema abordado
- Passos executados (ciclo de vida da ciência de dados)
- Funcionalidades implementadas em Python
- Resultados obtidos
- Gráficos e análises geradas

**Dica:** Execute o script e mostre os gráficos gerados durante a apresentação.

---

## 📊 Dados Analisados

O projeto trabalha com dados ambientais de cidades brasileiras incluindo:

- **Consumo de energia** (MWh)
- **Qualidade do ar** (índice)
- **Resíduos sólidos** (toneladas)
- **Uso de água** (m³)
- **Emissões de CO₂** (toneladas)
- **Temperatura média** (°C)
- **População** (milhares)

**Período:** 2020-2022  
**Cidades:** São Paulo, Rio de Janeiro, Belo Horizonte, Curitiba, Porto Alegre, Brasília, Salvador, Recife, Fortaleza, Manaus

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem de programação
- **Pandas**: Manipulação e análise de dados
- **NumPy**: Computação numérica
- **Matplotlib**: Visualizações básicas
- **Seaborn**: Visualizações estatísticas avançadas
- **SciPy**: Análises estatísticas

---

## 📚 Fontes de Pesquisa

- Artigo Científico: "The Role of Data Science in Urban Sustainability" - IEEE Xplore
- Livro: Data Science for Environmental and Sustainability Analysis
- Relatório: World Energy Outlook 2023 - Agência Internacional de Energia (IEA)
- Website: Plataforma de Dados Ambientais da ONU - https://data.unep.org/

---

## 👥 Autores

Desenvolvido como projeto acadêmico para a disciplina de **Data Science Fundamentals**

---

## 📝 Licença

Este projeto é para fins educacionais.

---

## 🔄 Próximos Passos Sugeridos

1. Desenvolvimento de modelos preditivos para projeções futuras
2. Análise mais detalhada de fatores causais
3. Comparação com benchmarks internacionais
4. Desenvolvimento de dashboard interativo
5. Integração com APIs de dados ambientais em tempo real

---

**Última atualização:** 2024
