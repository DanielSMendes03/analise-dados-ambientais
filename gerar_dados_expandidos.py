"""
Script para gerar dados ambientais expandidos
Adiciona mais cidades e mais anos aos dados existentes
"""

import pandas as pd
import numpy as np
import random

# Sementes para reprodutibilidade
np.random.seed(42)
random.seed(42)

# Cidades existentes + novas cidades brasileiras
cidades = [
    # Cidades existentes (mantidas)
    "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", 
    "Porto Alegre", "Brasília", "Salvador", "Recife", "Fortaleza", "Manaus",
    # Novas cidades
    "Goiânia", "Campinas", "Guarulhos", "Belém", "Vitória", 
    "Florianópolis", "Natal", "João Pessoa", "Maceió", "Aracaju",
    "Cuiabá", "Campo Grande", "Teresina", "São Luís", "Macapá",
    "Rio Branco", "Boa Vista", "Palmas", "Vitória da Conquista", "Juiz de Fora"
]

# Anos expandidos (2018-2024)
anos = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

# Dados base por cidade (valores de 2020 como referência)
dados_base = {
    "São Paulo": {"pop": 12300, "energia": 125000, "ar": 65, "residuos": 8500000, "agua": 450000000, "co2": 12500000, "temp": 22.5},
    "Rio de Janeiro": {"pop": 6800, "energia": 95000, "ar": 58, "residuos": 6200000, "agua": 320000000, "co2": 9500000, "temp": 24.2},
    "Belo Horizonte": {"pop": 2600, "energia": 45000, "ar": 55, "residuos": 2800000, "agua": 150000000, "co2": 4500000, "temp": 22.8},
    "Curitiba": {"pop": 1950, "energia": 38000, "ar": 48, "residuos": 2200000, "agua": 120000000, "co2": 3800000, "temp": 18.5},
    "Porto Alegre": {"pop": 1500, "energia": 42000, "ar": 52, "residuos": 2500000, "agua": 140000000, "co2": 4200000, "temp": 20.1},
    "Brasília": {"pop": 3100, "energia": 35000, "ar": 45, "residuos": 1800000, "agua": 100000000, "co2": 3500000, "temp": 22.3},
    "Salvador": {"pop": 2900, "energia": 32000, "ar": 60, "residuos": 2000000, "agua": 110000000, "co2": 3200000, "temp": 26.5},
    "Recife": {"pop": 1650, "energia": 28000, "ar": 58, "residuos": 1800000, "agua": 95000000, "co2": 2800000, "temp": 26.2},
    "Fortaleza": {"pop": 2700, "energia": 30000, "ar": 56, "residuos": 1900000, "agua": 100000000, "co2": 3000000, "temp": 27.1},
    "Manaus": {"pop": 2200, "energia": 25000, "ar": 45, "residuos": 1500000, "agua": 80000000, "co2": 2500000, "temp": 27.8},
    # Novas cidades com dados realistas
    "Goiânia": {"pop": 1550, "energia": 28000, "ar": 50, "residuos": 1700000, "agua": 90000000, "co2": 2800000, "temp": 23.5},
    "Campinas": {"pop": 1200, "energia": 32000, "ar": 52, "residuos": 1900000, "agua": 100000000, "co2": 3200000, "temp": 21.8},
    "Guarulhos": {"pop": 1400, "energia": 35000, "ar": 54, "residuos": 2100000, "agua": 110000000, "co2": 3500000, "temp": 22.0},
    "Belém": {"pop": 1500, "energia": 24000, "ar": 48, "residuos": 1400000, "agua": 75000000, "co2": 2400000, "temp": 26.8},
    "Vitória": {"pop": 360, "energia": 12000, "ar": 42, "residuos": 700000, "agua": 40000000, "co2": 1200000, "temp": 24.5},
    "Florianópolis": {"pop": 500, "energia": 15000, "ar": 40, "residuos": 900000, "agua": 50000000, "co2": 1500000, "temp": 20.2},
    "Natal": {"pop": 890, "energia": 18000, "ar": 55, "residuos": 1100000, "agua": 60000000, "co2": 1800000, "temp": 26.0},
    "João Pessoa": {"pop": 800, "energia": 16000, "ar": 53, "residuos": 950000, "agua": 52000000, "co2": 1600000, "temp": 25.8},
    "Maceió": {"pop": 1020, "energia": 19000, "ar": 57, "residuos": 1150000, "agua": 63000000, "co2": 1900000, "temp": 26.5},
    "Aracaju": {"pop": 650, "energia": 14000, "ar": 52, "residuos": 850000, "agua": 46000000, "co2": 1400000, "temp": 26.2},
    "Cuiabá": {"pop": 620, "energia": 17000, "ar": 46, "residuos": 1000000, "agua": 55000000, "co2": 1700000, "temp": 25.5},
    "Campo Grande": {"pop": 900, "energia": 20000, "ar": 44, "residuos": 1200000, "agua": 65000000, "co2": 2000000, "temp": 24.8},
    "Teresina": {"pop": 870, "energia": 18000, "ar": 49, "residuos": 1050000, "agua": 58000000, "co2": 1800000, "temp": 27.2},
    "São Luís": {"pop": 1100, "energia": 22000, "ar": 51, "residuos": 1300000, "agua": 70000000, "co2": 2200000, "temp": 26.9},
    "Macapá": {"pop": 520, "energia": 13000, "ar": 43, "residuos": 750000, "agua": 41000000, "co2": 1300000, "temp": 27.5},
    "Rio Branco": {"pop": 410, "energia": 11000, "ar": 41, "residuos": 650000, "agua": 35000000, "co2": 1100000, "temp": 26.8},
    "Boa Vista": {"pop": 420, "energia": 11500, "ar": 40, "residuos": 680000, "agua": 37000000, "co2": 1150000, "temp": 27.3},
    "Palmas": {"pop": 310, "energia": 9000, "ar": 38, "residuos": 550000, "agua": 30000000, "co2": 900000, "temp": 28.0},
    "Vitória da Conquista": {"pop": 340, "energia": 8500, "ar": 47, "residuos": 500000, "agua": 28000000, "co2": 850000, "temp": 23.5},
    "Juiz de Fora": {"pop": 570, "energia": 16000, "ar": 49, "residuos": 950000, "agua": 52000000, "co2": 1600000, "temp": 20.5}
}

def gerar_dados_expandidos():
    """Gera dados expandidos com variações realistas"""
    registros = []
    
    for cidade in cidades:
        base = dados_base.get(cidade, {
            "pop": 500, "energia": 15000, "ar": 50, "residuos": 900000,
            "agua": 50000000, "co2": 1500000, "temp": 24.0
        })
        
        # Valores iniciais para 2018 (um pouco menores que 2020)
        pop_2018 = base["pop"] * 0.95
        energia_2018 = base["energia"] * 0.92
        ar_2018 = base["ar"] * 1.05  # Pior qualidade do ar no passado
        residuos_2018 = base["residuos"] * 0.90
        agua_2018 = base["agua"] * 0.90
        co2_2018 = base["co2"] * 0.92
        temp_2018 = base["temp"] - 0.3
        
        for ano in anos:
            # Calcular anos desde 2018
            anos_desde_2018 = ano - 2018
            
            # Tendências realistas
            # População cresce ~1% ao ano
            pop = pop_2018 * (1.01 ** anos_desde_2018)
            
            # Energia cresce ~2-3% ao ano (mais rápido que população)
            crescimento_energia = 1.025 ** anos_desde_2018
            energia = energia_2018 * crescimento_energia
            
            # Qualidade do ar melhora levemente (~0.5% ao ano) ou piora em algumas cidades
            variacao_ar = np.random.choice([-0.3, 0, 0.3], p=[0.3, 0.4, 0.3])
            ar = ar_2018 + variacao_ar * anos_desde_2018
            ar = max(35, min(75, ar))  # Limitar entre 35 e 75
            
            # Resíduos crescem ~2% ao ano
            residuos = residuos_2018 * (1.02 ** anos_desde_2018)
            
            # Água cresce ~1.5% ao ano
            agua = agua_2018 * (1.015 ** anos_desde_2018)
            
            # CO2 cresce ~2.5% ao ano (ligado ao consumo de energia)
            co2 = co2_2018 * (1.025 ** anos_desde_2018)
            
            # Temperatura aumenta ~0.1-0.2°C por ano (aquecimento global)
            temp = temp_2018 + (0.15 * anos_desde_2018)
            
            # Adicionar variação aleatória pequena (±2%)
            energia *= (1 + np.random.uniform(-0.02, 0.02))
            ar += np.random.uniform(-1, 1)
            residuos *= (1 + np.random.uniform(-0.02, 0.02))
            agua *= (1 + np.random.uniform(-0.02, 0.02))
            co2 *= (1 + np.random.uniform(-0.02, 0.02))
            temp += np.random.uniform(-0.1, 0.1)
            
            # Garantir valores mínimos e arredondar
            registros.append({
                "cidade": cidade,
                "ano": int(ano),
                "consumo_energia_mwh": int(max(5000, energia)),
                "qualidade_ar_indice": round(max(35, min(75, ar)), 1),
                "residuos_solidos_ton": int(max(200000, residuos)),
                "uso_agua_m3": int(max(10000000, agua)),
                "emissao_co2_ton": int(max(500000, co2)),
                "temperatura_media_c": round(max(15.0, min(30.0, temp)), 1),
                "populacao_mil": int(max(200, pop))
            })
    
    df = pd.DataFrame(registros)
    df = df.sort_values(['cidade', 'ano']).reset_index(drop=True)
    
    return df

if __name__ == "__main__":
    print("Gerando dados expandidos...")
    df_expandido = gerar_dados_expandidos()
    
    print(f"\n✓ Dados gerados:")
    print(f"  - {len(df_expandido)} registros")
    print(f"  - {len(df_expandido['cidade'].unique())} cidades")
    print(f"  - {len(df_expandido['ano'].unique())} anos ({df_expandido['ano'].min()}-{df_expandido['ano'].max()})")
    
    # Salvar
    arquivo_saida = 'data/dados_ambientais.csv'
    df_expandido.to_csv(arquivo_saida, index=False, encoding='utf-8')
    print(f"\n✓ Dados salvos em '{arquivo_saida}'")
    
    # Estatísticas rápidas
    print(f"\nEstatísticas:")
    print(f"  - Total de registros: {len(df_expandido)}")
    print(f"  - Cidades: {sorted(df_expandido['cidade'].unique())}")
    print(f"  - Anos: {sorted(df_expandido['ano'].unique())}")

