# Estrutura do Projeto

```
analise-dados-ambientais/
│
├── data/
│   └── dados_ambientais.csv          # Dados brutos (30 registros)
│
├── src/
│   ├── __init__.py
│   ├── limpeza_dados.py              # Limpeza e preparação
│   ├── analise_dados.py              # Análise exploratória
│   └── visualizacoes.py              # Geração de gráficos
│
├── analise_ambiental.py               # Script principal
├── requirements.txt                  # Dependências
├── README.md                         # Documentação principal
├── EXEMPLO_USO.md                    # Guia de uso
├── .gitignore                        # Arquivos ignorados pelo Git
└── ESTRUTURA.md                      # Este arquivo
```

## Arquivos Principais

- **analise_ambiental.py**: Executa o pipeline completo de análise
- **src/limpeza_dados.py**: Funções para limpar e preparar dados
- **src/analise_dados.py**: Funções de análise exploratória
- **src/visualizacoes.py**: Funções para gerar gráficos

## Saídas Geradas (após execução)

- `data/dados_ambientais_limpos.csv`: Dados processados
- `graficos/*.png`: Visualizações geradas
