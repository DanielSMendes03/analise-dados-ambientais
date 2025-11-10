"""
Módulo de Visualização de Dados Ambientais

Este módulo contém funções para criar gráficos e visualizações dos dados
ambientais, facilitando a comunicação dos resultados.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import List, Optional
import os

# Configurar estilo dos gráficos
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except OSError:
    try:
        plt.style.use('seaborn-darkgrid')
    except OSError:
        plt.style.use('ggplot')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10


def criar_diretorio_graficos(diretorio: str = 'graficos') -> str:
    """
    Cria diretório para salvar gráficos se não existir.
    
    Args:
        diretorio: Nome do diretório
        
    Returns:
        Caminho do diretório
    """
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        print(f"✓ Diretório '{diretorio}' criado")
    return diretorio


def grafico_evolucao_temporal(df: pd.DataFrame, variavel: str, 
                              cidades: Optional[List[str]] = None,
                              salvar: bool = True) -> None:
    """
    Cria gráfico de linha mostrando evolução temporal de uma variável.
    
    Args:
        df: DataFrame com os dados
        variavel: Nome da variável a ser plotada
        cidades: Lista de cidades (None para todas)
        salvar: Se True, salva o gráfico
    """
    if cidades is None:
        cidades = df['cidade'].unique()
    
    plt.figure(figsize=(14, 7))
    
    for cidade in cidades:
        df_cidade = df[df['cidade'] == cidade].sort_values('ano')
        plt.plot(df_cidade['ano'], df_cidade[variavel], 
                marker='o', label=cidade, linewidth=2, markersize=6)
    
    plt.xlabel('Ano', fontsize=12, fontweight='bold')
    plt.ylabel(variavel.replace('_', ' ').title(), fontsize=12, fontweight='bold')
    plt.title(f'Evolução Temporal: {variavel.replace("_", " ").title()}', 
             fontsize=14, fontweight='bold', pad=20)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if salvar:
        nome_arquivo = f'graficos/evolucao_{variavel}.png'
        plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
        print(f"✓ Gráfico salvo: {nome_arquivo}")
    
    plt.show()


def grafico_comparacao_cidades(df: pd.DataFrame, variavel: str, 
                               ano: int = 2022, salvar: bool = True) -> None:
    """
    Cria gráfico de barras comparando cidades em uma variável.
    
    Args:
        df: DataFrame com os dados
        variavel: Nome da variável
        ano: Ano para comparação
        salvar: Se True, salva o gráfico
    """
    df_ano = df[df['ano'] == ano].sort_values(variavel, ascending=False)
    
    plt.figure(figsize=(12, 7))
    bars = plt.barh(df_ano['cidade'], df_ano[variavel], 
                    color=sns.color_palette("husl", len(df_ano)))
    
    # Adicionar valores nas barras
    for i, (idx, row) in enumerate(df_ano.iterrows()):
        valor = row[variavel]
        plt.text(valor, i, f' {valor:,.0f}', 
                va='center', fontsize=9, fontweight='bold')
    
    plt.xlabel(variavel.replace('_', ' ').title(), fontsize=12, fontweight='bold')
    plt.title(f'Comparação entre Cidades - {variavel.replace("_", " ").title()} ({ano})', 
             fontsize=14, fontweight='bold', pad=20)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    
    if salvar:
        nome_arquivo = f'graficos/comparacao_{variavel}_{ano}.png'
        plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
        print(f"✓ Gráfico salvo: {nome_arquivo}")
    
    plt.show()


def grafico_correlacao(df: pd.DataFrame, salvar: bool = True) -> None:
    """
    Cria heatmap de correlação entre variáveis numéricas.
    
    Args:
        df: DataFrame com os dados
        salvar: Se True, salva o gráfico
    """
    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    matriz_correlacao = df[colunas_numericas].corr()
    
    plt.figure(figsize=(12, 10))
    mask = np.triu(np.ones_like(matriz_correlacao, dtype=bool))
    
    sns.heatmap(matriz_correlacao, mask=mask, annot=True, fmt='.2f', 
               cmap='coolwarm', center=0, square=True, linewidths=1,
               cbar_kws={"shrink": 0.8}, vmin=-1, vmax=1)
    
    plt.title('Matriz de Correlação entre Variáveis Ambientais', 
             fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    
    if salvar:
        nome_arquivo = 'graficos/matriz_correlacao.png'
        plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
        print(f"✓ Gráfico salvo: {nome_arquivo}")
    
    plt.show()


def grafico_distribuicao(df: pd.DataFrame, variavel: str, salvar: bool = True) -> None:
    """
    Cria histograma e boxplot da distribuição de uma variável.
    
    Args:
        df: DataFrame com os dados
        variavel: Nome da variável
        salvar: Se True, salva o gráfico
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histograma
    ax1.hist(df[variavel], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    ax1.set_xlabel(variavel.replace('_', ' ').title(), fontweight='bold')
    ax1.set_ylabel('Frequência', fontweight='bold')
    ax1.set_title('Distribuição', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Boxplot
    ax2.boxplot(df[variavel], vert=True, patch_artist=True,
               boxprops=dict(facecolor='lightblue', alpha=0.7))
    ax2.set_ylabel(variavel.replace('_', ' ').title(), fontweight='bold')
    ax2.set_title('Boxplot - Identificação de Outliers', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.suptitle(f'Análise de Distribuição: {variavel.replace("_", " ").title()}', 
                fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    if salvar:
        nome_arquivo = f'graficos/distribuicao_{variavel}.png'
        plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
        print(f"✓ Gráfico salvo: {nome_arquivo}")
    
    plt.show()


def grafico_indicadores_sustentabilidade(df: pd.DataFrame, ano: int = 2022, 
                                        salvar: bool = True) -> None:
    """
    Cria gráfico radar/spider com múltiplos indicadores de sustentabilidade.
    
    Args:
        df: DataFrame com os dados
        ano: Ano para análise
        salvar: Se True, salva o gráfico
    """
    df_ano = df[df['ano'] == ano].copy()
    
    # Normalizar indicadores para escala 0-1 (inverter quando necessário)
    indicadores = ['qualidade_ar_indice', 'energia_per_capita', 
                   'residuos_per_capita', 'co2_per_capita']
    
    # Normalizar (menor é melhor para alguns, maior é melhor para outros)
    df_normalizado = df_ano[['cidade'] + indicadores].copy()
    
    for ind in indicadores:
        if ind == 'qualidade_ar_indice':
            # Para qualidade do ar, menor índice = melhor, então inverter
            df_normalizado[ind] = 1 - (df_normalizado[ind] - df_normalizado[ind].min()) / \
                                  (df_normalizado[ind].max() - df_normalizado[ind].min())
        else:
            # Para os outros, menor é melhor
            df_normalizado[ind] = 1 - (df_normalizado[ind] - df_normalizado[ind].min()) / \
                                  (df_normalizado[ind].max() - df_normalizado[ind].min())
    
    # Criar gráfico de barras agrupadas
    x = np.arange(len(df_normalizado))
    width = 0.2
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    for i, ind in enumerate(indicadores):
        offset = (i - len(indicadores)/2) * width + width/2
        ax.bar(x + offset, df_normalizado[ind], width, 
              label=ind.replace('_', ' ').title())
    
    ax.set_xlabel('Cidades', fontsize=12, fontweight='bold')
    ax.set_ylabel('Índice Normalizado (0-1)', fontsize=12, fontweight='bold')
    ax.set_title(f'Indicadores de Sustentabilidade Normalizados ({ano})', 
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(df_normalizado['cidade'], rotation=45, ha='right')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    if salvar:
        nome_arquivo = f'graficos/indicadores_sustentabilidade_{ano}.png'
        plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
        print(f"✓ Gráfico salvo: {nome_arquivo}")
    
    plt.show()


def grafico_tendencia_emissoes(df: pd.DataFrame, salvar: bool = True) -> None:
    """
    Cria gráfico mostrando tendência de emissões de CO2 por cidade.
    
    Args:
        df: DataFrame com os dados
        salvar: Se True, salva o gráfico
    """
    plt.figure(figsize=(14, 7))
    
    cidades = df['cidade'].unique()
    cores = sns.color_palette("husl", len(cidades))
    
    for cidade, cor in zip(cidades, cores):
        df_cidade = df[df['cidade'] == cidade].sort_values('ano')
        plt.plot(df_cidade['ano'], df_cidade['emissao_co2_ton'], 
                marker='o', label=cidade, linewidth=2.5, markersize=8, color=cor)
    
    plt.xlabel('Ano', fontsize=12, fontweight='bold')
    plt.ylabel('Emissão de CO₂ (toneladas)', fontsize=12, fontweight='bold')
    plt.title('Tendência de Emissões de CO₂ por Cidade', 
             fontsize=14, fontweight='bold', pad=20)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if salvar:
        nome_arquivo = 'graficos/tendencia_emissoes_co2.png'
        plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
        print(f"✓ Gráfico salvo: {nome_arquivo}")
    
    plt.show()


def gerar_todos_graficos(df: pd.DataFrame) -> None:
    """
    Gera todos os gráficos principais do projeto.
    
    Args:
        df: DataFrame com os dados limpos
    """
    criar_diretorio_graficos()
    
    print("\n=== GERANDO VISUALIZAÇÕES ===")
    
    # Gráficos de evolução temporal
    print("\n1. Gráficos de evolução temporal...")
    grafico_evolucao_temporal(df, 'consumo_energia_mwh', salvar=True)
    grafico_evolucao_temporal(df, 'qualidade_ar_indice', salvar=True)
    grafico_tendencia_emissoes(df, salvar=True)
    
    # Gráficos de comparação
    print("\n2. Gráficos de comparação entre cidades...")
    grafico_comparacao_cidades(df, 'consumo_energia_mwh', ano=2022, salvar=True)
    grafico_comparacao_cidades(df, 'qualidade_ar_indice', ano=2022, salvar=True)
    grafico_comparacao_cidades(df, 'emissao_co2_ton', ano=2022, salvar=True)
    
    # Análise de distribuição
    print("\n3. Análises de distribuição...")
    grafico_distribuicao(df, 'temperatura_media_c', salvar=True)
    grafico_distribuicao(df, 'qualidade_ar_indice', salvar=True)
    
    # Matriz de correlação
    print("\n4. Matriz de correlação...")
    grafico_correlacao(df, salvar=True)
    
    # Indicadores de sustentabilidade
    print("\n5. Indicadores de sustentabilidade...")
    grafico_indicadores_sustentabilidade(df, ano=2022, salvar=True)
    
    print("\n✓ Todas as visualizações foram geradas e salvas na pasta 'graficos/'")

