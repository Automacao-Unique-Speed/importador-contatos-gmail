import csv
import re


def formatar_telefone(numero):
    # Remove tudo que não for número
    numeros = re.sub(r'\D', '', numero)
    if len(numeros) >= 10 and not numeros.startswith('55'):
        return f'+55{numeros}'
    elif numeros.startswith('55'):
        return f'+{numeros}'
    else:
        return numero  # se não der pra formatar, mantém original


def gerar_csv_para_gmail(entrada_csv, saida_csv):
    with open(entrada_csv, newline='', encoding='utf-8') as csv_in:
        leitor = csv.reader(csv_in)
        next(leitor)  # pula cabeçalho

        with open(saida_csv, mode='w', newline='', encoding='utf-8') as csv_out:
            escritor = csv.writer(csv_out)

            # Cabeçalho exigido pelo Google
            escritor.writerow([
                'Name', 'Given Name', 'Family Name', 'Phone 1 - Type', 'Phone 1 - Value'
            ])

            for linha in leitor:
                nome = linha[0].strip()
                telefone = formatar_telefone(linha[1])

                partes_nome = nome.split()
                nome_dado = partes_nome[0]
                sobrenome = ' '.join(partes_nome[1:]) if len(partes_nome) > 1 else ''

                escritor.writerow([
                    nome, nome_dado, sobrenome, 'Mobile', telefone
                ])

    print(f'✅ Arquivo "{saida_csv}" gerado com sucesso!')


# Exemplo de uso:
entrada = 'contatos_brutos.csv'
saida = 'contatos_gmail.csv'
gerar_csv_para_gmail(entrada, saida)
