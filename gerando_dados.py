import random
import os

nomes = ['Lucas', 'Marina', 'Jose', 'Carlos', 'Antonio','Maria', 'Miguel','Arthur','Davi','Bernardo']
emails = ['lucassilva@gmail.com','lucassilva@outlook.com','lucassilva@protonmail.com', 
    'lucassilva@ymail.com', 'lucassilva@mail.com', 'john.doe@example.com','jane.smith@email.com',
    'michael.wilson@outlook.com','emily.johnson@protonmail.com','david.brown@ymail.com']
telefones = ['(65) 1283-4567','(48) 9879-6543','(41) 5535-1111','(42) 2224-3333','(45) 4464-5555','(27) 6646-7777',
    '(28) 8878-9999','(71) 7776-8888','(89) 3333-2222','(61) 9993-8888']
cidades = ['Maracaju','Serra Talhada','Taubaté','Quixadá','Cachoeirinha','Lins','Sinop','Barreiras','Ijuí','Guarapuava']
estados = ['Maranhão','Pernambuco','Rondônia','Alagoas','Mato Grosso do Sul','Acre','Rio Grande do Norte','Paraná',
    'Sergipe','Amazonas']

def gerador_de_dados(escolhas,salvar_dados=False):    
    dados = []

    if escolhas['nomes']:
        dados.append(random.choices(nomes,k=escolhas['Quantidade_nome']))
    
    if escolhas['emails']:
        dados.append(random.choices(emails,k=escolhas['Quantidade_email']))
    
    if escolhas['telefones']:
        dados.append(random.choices(telefones,k=escolhas['Quantidade_telefona']))
    
    if escolhas['cidades']:
        dados.append(random.choices(cidades,k=escolhas['Quantidade_cidade']))
    
    if escolhas['estados']:
        dados.append(random.choices(estados,k=escolhas['Quantidade_estado']))

    if salvar_dados and dados != []:
        with open('Dados.txt','a',encoding='utf-8',newline='') as arquivo:
            arquivo.write(f'Segui os dados gerados:{os.linesep}')
            for dado in dados:
                arquivo.write(f'{dado}{os.linesep}')
            arquivo.write(os.linesep)

    return dados