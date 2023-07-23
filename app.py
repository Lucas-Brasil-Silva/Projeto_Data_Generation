import PySimpleGUI as sg
import os
from gerando_dados import gerador_de_dados

sg.theme('Topanga')

layout = [
    [sg.Text('Escolha quais dados devem ser gerados')],
    [sg.Checkbox('Nomes',size=(7,1),key='nomes'),sg.Text('Quantidade:'),
        sg.Spin(values=(1,2,3,4,5,6,7,8,9,10),initial_value=1,key='Quantidade_nome',size=(2,1))],
    [sg.Checkbox('Emails',size=(7,1),key='emails'),sg.Text('Quantidade:'),
    sg.Spin(values=(1,2,3,4,5,6,7,8,9,10),initial_value=1,key='Quantidade_email',size=(2,1))],
    [sg.Checkbox('Telefones',size=(7,1),key='telefones'),sg.Text('Quantidade:'),
    sg.Spin(values=(1,2,3,4,5,6,7,8,9,10),initial_value=1,key='Quantidade_telefona',size=(2,1))],
    [sg.Checkbox('Cidades',size=(7,1),key='cidades'),sg.Text('Quantidade:'),
    sg.Spin(values=(1,2,3,4,5,6,7,8,9,10),initial_value=1,key='Quantidade_cidade',size=(2,1))],
    [sg.Checkbox('Estados',size=(7,1),key='estados'),sg.Text('Quantidade:'),
    sg.Spin(values=(1,2,3,4,5,6,7,8,9,10),initial_value=1,key='Quantidade_estado',size=(2,1))],
    [sg.Button('Gerar Dados'),sg.Button('Gerar Arquivo com Dados'),sg.Button('Parar')],
    [sg.Output(size=(55,10))]
]

window = sg.Window('Gerador de Dados',layout)

while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED,'Parar']:
        break
    elif event == 'Gerar Dados':
        dados = gerador_de_dados(values)
        if dados == []:
            sg.popup('Escolha os dados que devem ser gerados!',title='Aviso')
        else:
            print(f'{os.linesep}Segue os dados gerados:')
            for dado in dados:
                print(dado)
    elif event == 'Gerar Arquivo com Dados':
        dados = gerador_de_dados(values,salvar_dados=True)
        if dados == []:
            sg.popup('Escolha os dados que devem ser gerados!',title='Aviso')
        else:
            print(f'{os.linesep}Segue os dados gerados:')
            for dado in dados:
                print(dado)