# Simulador de filas

O simulador usa um arquivo chamado `config.yml` para carregar os parâmetros da simulação. Para gerar um arquivo de configuração com os parâmetros padrão, basta rodar o script `generate_config.py` com o comando:

```bash
python generate_config.py queue_qtd
```

Depois de gerar o arquivo de configuração, basta alterar os valores dos parâmetros no arquivo `config.yml` para os valores desejados.

Para rodar o simulador basta executar o arquivo `main.py` com o comando:

```bash
python main.py
```
