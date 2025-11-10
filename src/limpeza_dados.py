"""
Módulo de Limpeza e Organização de Dados Ambientais

Este módulo contém funções para limpar, validar e organizar dados ambientais
de cidades brasileiras, seguindo as melhores práticas de Data Science.
"""

import pandas as pd
import numpy as np
from typing import Tuple, Dict


def carregar_dados(caminho_arquivo: str) -> pd.DataFrame:
    """
    Carrega os dados ambientais de um arquivo CSV.
    
    Args:
        caminho_arquivo: Caminho para o arquivo CSV com os dados
        
    Returns:
        DataFrame com os dados carregados
    """
    try:
        df = pd.read_csv(caminho_arquivo, encoding='utf-8')
        print(f"✓ Dados carregados: {len(df)} registros encontrados")
        return df
    except FileNotFoundError:
        print(f"✗ Erro: Arquivo não encontrado em {caminho_arquivo}")
        raise
    except Exception as e:
        print(f"✗ Erro ao carregar dados: {str(e)}")
        raise


def validar_dados(df: pd.DataFrame) -> Dict[str, any]:
    """
    Valida a estrutura e qualidade dos dados.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        Dicionário com informações de validação
    """
    validacao = {
        'total_registros': len(df),
        'colunas_esperadas': ['cidade', 'ano', 'consumo_energia_mwh', 'qualidade_ar_indice',
                              'residuos_solidos_ton', 'uso_agua_m3', 'emissao_co2_ton',
                              'temperatura_media_c', 'populacao_mil'],
        'colunas_encontradas': list(df.columns),
        'valores_nulos': df.isnull().sum().to_dict(),
        'duplicatas': df.duplicated().sum(),
        'tipos_dados': df.dtypes.to_dict()
    }
    
    print("\n=== VALIDAÇÃO DOS DADOS ===")
    print(f"Total de registros: {validacao['total_registros']}")
    print(f"Colunas encontradas: {len(validacao['colunas_encontradas'])}")
    print(f"Registros duplicados: {validacao['duplicatas']}")
    print(f"\nValores nulos por coluna:")
    for col, nulos in validacao['valores_nulos'].items():
        if nulos > 0:
            print(f"  - {col}: {nulos} ({nulos/len(df)*100:.2f}%)")
    
    return validacao


def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa e organiza os dados ambientais.
    
    Processos realizados:
    - Remove registros duplicados
    - Trata valores nulos
    - Remove outliers extremos
    - Garante tipos de dados corretos
    
    Args:
        df: DataFrame com os dados brutos
        
    Returns:
        DataFrame limpo e organizado
    """
    df_limpo = df.copy()
    
    print("\n=== LIMPEZA DOS DADOS ===")
    
    # 1. Remover duplicatas
    duplicatas_antes = len(df_limpo)
    df_limpo = df_limpo.drop_duplicates()
    duplicatas_removidas = duplicatas_antes - len(df_limpo)
    if duplicatas_removidas > 0:
        print(f"✓ Removidas {duplicatas_removidas} duplicatas")
    
    # 2. Tratar valores nulos
    # Para valores numéricos, usar mediana da cidade
    colunas_numericas = df_limpo.select_dtypes(include=[np.number]).columns
    
    for col in colunas_numericas:
        nulos = df_limpo[col].isnull().sum()
        if nulos > 0:
            # Preencher com mediana agrupada por cidade
            df_limpo[col] = df_limpo.groupby('cidade')[col].transform(
                lambda x: x.fillna(x.median())
            )
            print(f"✓ Preenchidos {nulos} valores nulos em '{col}'")
    
    # 3. Remover outliers extremos (usando IQR - Interquartile Range)
    registros_antes = len(df_limpo)
    
    for col in colunas_numericas:
        if col in ['cidade', 'ano']:
            continue
            
        Q1 = df_limpo[col].quantile(0.25)
        Q3 = df_limpo[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 3 * IQR  # 3x IQR para ser menos restritivo
        limite_superior = Q3 + 3 * IQR
        
        outliers = ((df_limpo[col] < limite_inferior) | 
                   (df_limpo[col] > limite_superior)).sum()
        
        if outliers > 0:
            # Substituir outliers pela mediana da cidade
            mask = (df_limpo[col] < limite_inferior) | (df_limpo[col] > limite_superior)
            df_limpo.loc[mask, col] = df_limpo.groupby('cidade')[col].transform('median')[mask]
            print(f"✓ Tratados {outliers} outliers em '{col}'")
    
    # 4. Garantir tipos de dados corretos
    df_limpo['cidade'] = df_limpo['cidade'].astype(str)
    df_limpo['ano'] = df_limpo['ano'].astype(int)
    
    # 5. Ordenar por cidade e ano
    df_limpo = df_limpo.sort_values(['cidade', 'ano']).reset_index(drop=True)
    
    print(f"\n✓ Limpeza concluída: {len(df_limpo)} registros válidos")
    
    return df_limpo


def criar_metricas_derivadas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria métricas derivadas úteis para análise.
    
    Args:
        df: DataFrame limpo
        
    Returns:
        DataFrame com métricas adicionais
    """
    df_metricas = df.copy()
    
    print("\n=== CRIAÇÃO DE MÉTRICAS DERIVADAS ===")
    
    # Consumo de energia per capita (MWh por mil habitantes)
    df_metricas['energia_per_capita'] = (
        df_metricas['consumo_energia_mwh'] / df_metricas['populacao_mil']
    )
    
    # Resíduos per capita (toneladas por mil habitantes)
    df_metricas['residuos_per_capita'] = (
        df_metricas['residuos_solidos_ton'] / df_metricas['populacao_mil']
    )
    
    # Uso de água per capita (m³ por mil habitantes)
    df_metricas['agua_per_capita'] = (
        df_metricas['uso_agua_m3'] / df_metricas['populacao_mil']
    )
    
    # Emissão de CO2 per capita (toneladas por mil habitantes)
    df_metricas['co2_per_capita'] = (
        df_metricas['emissao_co2_ton'] / df_metricas['populacao_mil']
    )
    
    # Intensidade energética (CO2 por MWh)
    df_metricas['intensidade_carbono'] = (
        df_metricas['emissao_co2_ton'] / df_metricas['consumo_energia_mwh']
    )
    
    # Eficiência hídrica (m³ por MWh)
    df_metricas['eficiencia_hidrica'] = (
        df_metricas['uso_agua_m3'] / df_metricas['consumo_energia_mwh']
    )
    
    print("✓ Métricas derivadas criadas:")
    print("  - Energia per capita")
    print("  - Resíduos per capita")
    print("  - Água per capita")
    print("  - CO2 per capita")
    print("  - Intensidade de carbono")
    print("  - Eficiência hídrica")
    
    return df_metricas


def preparar_dados(caminho_arquivo: str) -> Tuple[pd.DataFrame, Dict]:
    """
    Pipeline completo de preparação de dados.
    
    Args:
        caminho_arquivo: Caminho para o arquivo CSV
        
    Returns:
        Tupla com (DataFrame limpo, dicionário de validação)
    """
    # 1. Carregar dados
    df = carregar_dados(caminho_arquivo)
    
    # 2. Validar dados
    validacao = validar_dados(df)
    
    # 3. Limpar dados
    df_limpo = limpar_dados(df)
    
    # 4. Criar métricas derivadas
    df_final = criar_metricas_derivadas(df_limpo)
    
    return df_final, validacao

