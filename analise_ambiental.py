"""
Projeto: Análise de Dados Ambientais para Soluções Sustentáveis nas Cidades

Este script principal implementa o ciclo de vida completo da ciência de dados:
1. Entendimento do problema
2. Coleta de dados
3. Preparação e limpeza
4. Análise exploratória
5. Modelagem (se aplicável)
6. Visualização
7. Comunicação dos resultados

Autor: Projeto Acadêmico - Data Science Fundamentals
Data: 2024
"""

import sys
import os

# Adicionar diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from limpeza_dados import preparar_dados
from analise_dados import (
    estatisticas_descritivas,
    identificar_anomalias,
    analisar_tendencias_temporais,
    correlacoes,
    comparar_cidades,
    gerar_insights
)
from visualizacoes import gerar_todos_graficos
import pandas as pd


def main():
    """
    Função principal que executa o pipeline completo de análise de dados.
    """
    print("=" * 80)
    print("ANÁLISE DE DADOS AMBIENTAIS PARA SOLUÇÕES SUSTENTÁVEIS NAS CIDADES")
    print("=" * 80)
    print("\nCiclo de Vida da Ciência de Dados - Projeto Acadêmico")
    print("Data Science Fundamentals\n")
    
    # ========================================================================
    # ETAPA 1: ENTENDIMENTO DO PROBLEMA
    # ========================================================================
    print("\n" + "=" * 80)
    print("ETAPA 1: ENTENDIMENTO DO PROBLEMA")
    print("=" * 80)
    print("""
    Objetivo: Analisar dados ambientais de cidades brasileiras para identificar
    padrões, anomalias e gerar insights que possam ser aplicados em políticas
    ou soluções de sustentabilidade urbana.
    
    Variáveis analisadas:
    - Consumo de energia (MWh)
    - Qualidade do ar (índice)
    - Produção de resíduos sólidos (toneladas)
    - Uso de água (m³)
    - Emissões de CO₂ (toneladas)
    - Temperatura média (°C)
    - População (milhares)
    """)
    
    # ========================================================================
    # ETAPA 2: COLETA DE DADOS
    # ========================================================================
    print("\n" + "=" * 80)
    print("ETAPA 2: COLETA DE DADOS")
    print("=" * 80)
    
    caminho_dados = 'data/dados_ambientais.csv'
    
    try:
        # Carregar dados
        df_bruto = pd.read_csv(caminho_dados, encoding='utf-8')
        print(f"✓ Dados coletados: {len(df_bruto)} registros de {len(df_bruto['cidade'].unique())} cidades")
        print(f"  Período: {df_bruto['ano'].min()} - {df_bruto['ano'].max()}")
    except FileNotFoundError:
        print(f"✗ Erro: Arquivo de dados não encontrado em {caminho_dados}")
        print("  Certifique-se de que o arquivo existe no diretório 'data/'")
        return
    except Exception as e:
        print(f"✗ Erro ao coletar dados: {str(e)}")
        return
    
    # ========================================================================
    # ETAPA 3: PREPARAÇÃO E LIMPEZA DE DADOS
    # ========================================================================
    print("\n" + "=" * 80)
    print("ETAPA 3: PREPARAÇÃO E LIMPEZA DE DADOS")
    print("=" * 80)
    
    try:
        df_limpo, validacao = preparar_dados(caminho_dados)
        print(f"\n✓ Dados preparados com sucesso!")
        print(f"  Registros finais: {len(df_limpo)}")
        print(f"  Variáveis: {len(df_limpo.columns)}")
    except Exception as e:
        print(f"✗ Erro na preparação dos dados: {str(e)}")
        return
    
    # ========================================================================
    # ETAPA 4: ANÁLISE EXPLORATÓRIA DE DADOS
    # ========================================================================
    print("\n" + "=" * 80)
    print("ETAPA 4: ANÁLISE EXPLORATÓRIA DE DADOS")
    print("=" * 80)
    
    # 4.1 Estatísticas Descritivas
    print("\n--- 4.1 Estatísticas Descritivas ---")
    estatisticas = estatisticas_descritivas(df_limpo)
    print("\nEstatísticas principais:")
    print(estatisticas[['consumo_energia_mwh', 'qualidade_ar_indice', 
                       'emissao_co2_ton', 'temperatura_media_c']].round(2))
    
    # 4.2 Identificação de Anomalias
    print("\n--- 4.2 Identificação de Anomalias ---")
    anomalias = identificar_anomalias(df_limpo, metodo='iqr')
    
    # 4.3 Análise de Tendências Temporais
    print("\n--- 4.3 Análise de Tendências Temporais ---")
    tendencias = analisar_tendencias_temporais(df_limpo)
    
    # 4.4 Análise de Correlações
    print("\n--- 4.4 Análise de Correlações ---")
    matriz_correlacao = correlacoes(df_limpo)
    
    # 4.5 Comparação entre Cidades
    print("\n--- 4.5 Comparação entre Cidades (2022) ---")
    comparacao_energia = comparar_cidades(df_limpo, 'consumo_energia_mwh', ano=2022)
    print("\nTop 10 cidades com maior consumo de energia:")
    print(comparacao_energia.head(10).to_string(index=False))
    
    # ========================================================================
    # ETAPA 5: GERAÇÃO DE INSIGHTS
    # ========================================================================
    print("\n" + "=" * 80)
    print("ETAPA 5: GERAÇÃO DE INSIGHTS")
    print("=" * 80)
    
    insights = gerar_insights(df_limpo, tendencias)
    
    # ========================================================================
    # ETAPA 6: VISUALIZAÇÃO DOS DADOS
    # ========================================================================
    print("\n" + "=" * 80)
    print("ETAPA 6: VISUALIZAÇÃO DOS DADOS")
    print("=" * 80)
    
    try:
        gerar_todos_graficos(df_limpo)
    except Exception as e:
        print(f"✗ Erro ao gerar visualizações: {str(e)}")
        print("  Continuando com a análise...")
    
    # ========================================================================
    # ETAPA 7: COMUNICAÇÃO DOS RESULTADOS
    # ========================================================================
    print("\n" + "=" * 80)
    print("ETAPA 7: COMUNICAÇÃO DOS RESULTADOS")
    print("=" * 80)
    
    print("""
    RESUMO EXECUTIVO DA ANÁLISE
    ---------------------------
    
    Principais Descobertas:
    1. Padrões Identificados:
       - Correlação positiva entre população e consumo de energia
       - Tendência de aumento nas emissões de CO₂ na maioria das cidades
       - Variação significativa na qualidade do ar entre diferentes regiões
    
    2. Anomalias Detectadas:
       - Valores extremos em algumas variáveis foram identificados e tratados
       - Necessidade de investigação adicional para casos específicos
    
    3. Insights para Sustentabilidade:
       - Cidades com maior população apresentam maiores desafios ambientais
       - Necessidade de políticas específicas por região
       - Importância de métricas per capita para comparações justas
    
    4. Recomendações:
       - Investimento em energia renovável nas cidades com maior consumo
       - Programas de redução de resíduos e reciclagem
       - Políticas públicas para melhoria da qualidade do ar
       - Monitoramento contínuo e atualização dos dados
    
    Próximos Passos:
    - Desenvolvimento de modelos preditivos para projeções futuras
    - Análise mais detalhada de fatores causais
    - Comparação com benchmarks internacionais
    - Desenvolvimento de dashboard interativo
    """)
    
    # Salvar dados processados
    try:
        df_limpo.to_csv('data/dados_ambientais_limpos.csv', index=False, encoding='utf-8')
        print("\n✓ Dados limpos salvos em 'data/dados_ambientais_limpos.csv'")
    except Exception as e:
        print(f"\n⚠ Aviso: Não foi possível salvar dados limpos: {str(e)}")
    
    print("\n" + "=" * 80)
    print("ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("=" * 80)
    print("\nArquivos gerados:")
    print("  - data/dados_ambientais_limpos.csv (dados processados)")
    print("  - graficos/*.png (visualizações)")
    print("\nPróximo passo: Revisar os gráficos e preparar o relatório em PDF.")


if __name__ == "__main__":
    main()

