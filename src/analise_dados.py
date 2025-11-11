"""
Módulo de Análise de Dados Ambientais

Este módulo contém funções para análise exploratória, identificação de padrões
e anomalias nos dados ambientais.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from scipy import stats


def estatisticas_descritivas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Gera estatísticas descritivas para todas as variáveis numéricas.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        DataFrame com estatísticas descritivas
    """
    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    estatisticas = df[colunas_numericas].describe()
    
    # Adicionar medidas adicionais
    estatisticas.loc['mediana'] = df[colunas_numericas].median()
    estatisticas.loc['moda'] = df[colunas_numericas].mode().iloc[0] if len(df[colunas_numericas].mode()) > 0 else np.nan
    estatisticas.loc['assimetria'] = df[colunas_numericas].skew()
    estatisticas.loc['curtose'] = df[colunas_numericas].kurtosis()
    
    return estatisticas


def identificar_anomalias(df: pd.DataFrame, metodo: str = 'iqr') -> Dict[str, pd.DataFrame]:
    """
    Identifica anomalias nos dados usando diferentes métodos.
    
    Args:
        df: DataFrame com os dados
        metodo: Método de detecção ('iqr' ou 'zscore')
        
    Returns:
        Dicionário com anomalias identificadas por coluna
    """
    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    anomalias = {}
    
    print(f"\n=== IDENTIFICAÇÃO DE ANOMALIAS (Método: {metodo.upper()}) ===")
    
    for col in colunas_numericas:
        if col in ['ano']:
            continue
            
        if metodo == 'iqr':
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            limite_inferior = Q1 - 1.5 * IQR
            limite_superior = Q3 + 1.5 * IQR
            
            mask_anomalias = (df[col] < limite_inferior) | (df[col] > limite_superior)
            
        elif metodo == 'zscore':
            z_scores = np.abs(stats.zscore(df[col].dropna()))
            threshold = 3
            mask_anomalias = pd.Series(False, index=df.index)
            mask_anomalias[df[col].notna()] = z_scores > threshold
        
        anomalias_col = df[mask_anomalias][['cidade', 'ano', col]].copy()
        
        if len(anomalias_col) > 0:
            anomalias[col] = anomalias_col
            print(f"\n{col}: {len(anomalias_col)} anomalias encontradas")
            print(anomalias_col.to_string(index=False))
    
    return anomalias


def analisar_tendencias_temporais(df: pd.DataFrame) -> Dict[str, Dict]:
    """
    Analisa tendências temporais por cidade.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        Dicionário com tendências por cidade e variável
    """
    cidades = df['cidade'].unique()
    tendencias = {}
    
    print("\n=== ANÁLISE DE TENDÊNCIAS TEMPORAIS ===")
    
    variaveis = ['consumo_energia_mwh', 'qualidade_ar_indice', 'residuos_solidos_ton',
                 'emissao_co2_ton', 'temperatura_media_c']
    
    for cidade in cidades:
        df_cidade = df[df['cidade'] == cidade].sort_values('ano')
        tendencias[cidade] = {}
        
        for var in variaveis:
            if var in df_cidade.columns:
                valores = df_cidade[var].values
                anos = df_cidade['ano'].values
                
                # Calcular taxa de variação média anual
                if len(valores) > 1:
                    variacao_absoluta = valores[-1] - valores[0]
                    variacao_percentual = (variacao_absoluta / valores[0]) * 100
                    variacao_media_anual = variacao_percentual / (len(valores) - 1)
                    
                    # Determinar tendência
                    if variacao_media_anual > 2:
                        tendencia = "Crescente"
                    elif variacao_media_anual < -2:
                        tendencia = "Decrescente"
                    else:
                        tendencia = "Estável"
                    
                    tendencias[cidade][var] = {
                        'valor_inicial': valores[0],
                        'valor_final': valores[-1],
                        'variacao_percentual': variacao_percentual,
                        'variacao_media_anual': variacao_media_anual,
                        'tendencia': tendencia
                    }
    
    # Exibir resumo - Top 10 cidades por população
    populacao_media = df.groupby('cidade')['populacao_mil'].mean().sort_values(ascending=False)
    top_cidades = populacao_media.head(10).index.tolist()
    
    for cidade in top_cidades:
        if cidade in tendencias:
            print(f"\n{cidade}:")
            for var, info in tendencias[cidade].items():
                print(f"  {var}: {info['tendencia']} "
                      f"({info['variacao_media_anual']:.2f}% ao ano)")
    
    return tendencias


def correlacoes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula matriz de correlação entre variáveis numéricas.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        DataFrame com matriz de correlação
    """
    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    matriz_correlacao = df[colunas_numericas].corr()
    
    print("\n=== MATRIZ DE CORRELAÇÃO ===")
    print("\nCorrelações mais fortes (> 0.7 ou < -0.7):")
    
    for i in range(len(matriz_correlacao.columns)):
        for j in range(i+1, len(matriz_correlacao.columns)):
            corr = matriz_correlacao.iloc[i, j]
            if abs(corr) > 0.7:
                print(f"  {matriz_correlacao.columns[i]} ↔ {matriz_correlacao.columns[j]}: {corr:.3f}")
    
    return matriz_correlacao


def comparar_cidades(df: pd.DataFrame, variavel: str, ano: int = None) -> pd.DataFrame:
    """
    Compara cidades em relação a uma variável específica.
    
    Args:
        df: DataFrame com os dados
        variavel: Nome da variável para comparação
        ano: Ano específico (None para média de todos os anos)
        
    Returns:
        DataFrame com comparação entre cidades
    """
    if ano:
        df_filtrado = df[df['ano'] == ano]
    else:
        df_filtrado = df.groupby('cidade')[variavel].mean().reset_index()
        df_filtrado = df.merge(df_filtrado, on='cidade', suffixes=('', '_media'))
        df_filtrado = df_filtrado.groupby('cidade').first().reset_index()
    
    comparacao = df_filtrado[['cidade', variavel]].sort_values(variavel, ascending=False)
    
    # Retornar apenas top 10
    return comparacao.head(10)


def gerar_insights(df: pd.DataFrame, tendencias: Dict) -> List[str]:
    """
    Gera insights baseados na análise dos dados.
    
    Args:
        df: DataFrame com os dados
        tendencias: Dicionário com tendências temporais
        
    Returns:
        Lista de insights em formato de texto
    """
    insights = []
    
    print("\n=== GERAÇÃO DE INSIGHTS ===")
    
    # Insight 1: Cidade com maior consumo de energia
    consumo_medio = df.groupby('cidade')['consumo_energia_mwh'].mean()
    cidade_maior_consumo = consumo_medio.idxmax()
    insights.append(f"• {cidade_maior_consumo} apresenta o maior consumo médio de energia "
                   f"({consumo_medio.max():,.0f} MWh)")
    
    # Insight 2: Cidade com melhor qualidade do ar
    qualidade_ar_media = df.groupby('cidade')['qualidade_ar_indice'].mean()
    cidade_melhor_ar = qualidade_ar_media.idxmin()  # Menor índice = melhor qualidade
    insights.append(f"• {cidade_melhor_ar} apresenta a melhor qualidade do ar "
                   f"(índice médio: {qualidade_ar_media.min():.1f})")
    
    # Insight 3: Cidade com maior crescimento de emissões
    crescimento_emissoes = {}
    for cidade, dados in tendencias.items():
        if 'emissao_co2_ton' in dados:
            crescimento_emissoes[cidade] = dados['emissao_co2_ton']['variacao_media_anual']
    
    if crescimento_emissoes:
        cidade_maior_crescimento = max(crescimento_emissoes, key=crescimento_emissoes.get)
        insights.append(f"• {cidade_maior_crescimento} apresenta o maior crescimento anual de "
                       f"emissões de CO2 ({crescimento_emissoes[cidade_maior_crescimento]:.2f}% ao ano)")
    
    # Insight 4: Relação entre população e consumo
    correlacao_pop_energia = df['populacao_mil'].corr(df['consumo_energia_mwh'])
    insights.append(f"• Existe correlação positiva forte entre população e consumo de energia "
                   f"(r = {correlacao_pop_energia:.3f})")
    
    # Insight 5: Eficiência energética
    eficiencia = df.groupby('cidade')['energia_per_capita'].mean()
    cidade_mais_eficiente = eficiencia.idxmin()
    cidade_menos_eficiente = eficiencia.idxmax()
    insights.append(f"• {cidade_mais_eficiente} é a mais eficiente em consumo per capita "
                   f"({eficiencia.min():.2f} MWh/mil hab), enquanto {cidade_menos_eficiente} "
                   f"é a menos eficiente ({eficiencia.max():.2f} MWh/mil hab)")
    
    # Insight 6: Tendência de temperatura
    temp_tendencia = df.groupby('ano')['temperatura_media_c'].mean()
    if len(temp_tendencia) > 1:
        variacao_temp = ((temp_tendencia.iloc[-1] - temp_tendencia.iloc[0]) / 
                        temp_tendencia.iloc[0]) * 100
        insights.append(f"• Temperatura média aumentou {variacao_temp:.2f}% no período analisado, "
                       f"indicando possível efeito de aquecimento urbano")
    
    for insight in insights:
        print(insight)
    
    return insights

