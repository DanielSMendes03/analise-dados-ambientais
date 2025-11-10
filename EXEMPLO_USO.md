# Exemplo de Uso - Análise de Dados Ambientais

## Execução Rápida

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

ou

```bash
pip3 install -r requirements.txt
```

### 2. Executar Análise Completa

```bash
python3 analise_ambiental.py
```

### 3. Verificar Resultados

Após a execução, você encontrará:

- **Console**: Análises e insights impressos
- **Arquivo CSV**: `data/dados_ambientais_limpos.csv` (dados processados)
- **Gráficos PNG**: Pasta `graficos/` com todas as visualizações

## Estrutura de Saída

```
graficos/
├── evolucao_consumo_energia_mwh.png
├── evolucao_qualidade_ar_indice.png
├── tendencia_emissoes_co2.png
├── comparacao_consumo_energia_mwh_2022.png
├── comparacao_qualidade_ar_indice_2022.png
├── comparacao_emissao_co2_ton_2022.png
├── distribuicao_temperatura_media_c.png
├── distribuicao_qualidade_ar_indice.png
├── matriz_correlacao.png
└── indicadores_sustentabilidade_2022.png
```

## Exemplo de Saída no Console

```
================================================================================
ANÁLISE DE DADOS AMBIENTAIS PARA SOLUÇÕES SUSTENTÁVEIS NAS CIDADES
================================================================================

Ciclo de Vida da Ciência de Dados - Projeto Acadêmico
Data Science Fundamentals

================================================================================
ETAPA 1: ENTENDIMENTO DO PROBLEMA
================================================================================
...

✓ Dados carregados: 30 registros encontrados
✓ Limpeza concluída: 30 registros válidos
✓ Métricas derivadas criadas
...
```

## Personalização

### Analisar apenas algumas cidades

Edite `analise_ambiental.py` e modifique a função `grafico_evolucao_temporal`:

```python
# Exemplo: analisar apenas São Paulo e Rio de Janeiro
grafico_evolucao_temporal(df_limpo, 'consumo_energia_mwh',
                         cidades=['São Paulo', 'Rio de Janeiro'],
                         salvar=True)
```

### Adicionar novos dados

1. Edite `data/dados_ambientais.csv`
2. Adicione novas linhas seguindo o formato existente
3. Execute novamente `analise_ambiental.py`

## Troubleshooting

### Erro: "ModuleNotFoundError"

Instale as dependências:

```bash
pip3 install pandas numpy matplotlib seaborn scipy scikit-learn
```

### Erro: "FileNotFoundError: data/dados_ambientais.csv"

Certifique-se de que o arquivo existe em `data/dados_ambientais.csv`

### Gráficos não aparecem

- Verifique se o matplotlib está configurado corretamente
- Em ambientes sem display (servidores), os gráficos serão apenas salvos
- Use `plt.show()` apenas se tiver interface gráfica

## Próximos Passos

1. Revisar os gráficos gerados em `graficos/`
2. Incluir os gráficos no relatório PDF
3. Preparar apresentação com os insights obtidos
4. Gravar vídeo pitch explicando o projeto
