import tkinter as tk
from tkinter import messagebox

def abrir_ficha_acompanhamento():
    janela_ficha = tk.Toplevel()
    janela_ficha.title("Ficha de Acompanhamento Funeral")
    configurar_janela(janela_ficha)

    # Dados do falecido
    label_nome_falecido = tk.Label(janela_ficha, text="Nome completo do falecido")
    label_nome_falecido.grid(row=0, column=0, pady=5, padx=10, sticky="w")
    entry_nome_falecido = tk.Entry(janela_ficha)
    entry_nome_falecido.grid(row=0, column=1, pady=5, padx=10)

    label_data_nascimento = tk.Label(janela_ficha, text="Data de nascimento")
    label_data_nascimento.grid(row=1, column=0, pady=5, padx=10, sticky="w")
    entry_data_nascimento = tk.Entry(janela_ficha)
    entry_data_nascimento.grid(row=1, column=1, pady=5, padx=10)

    label_data_obito = tk.Label(janela_ficha, text="Data do óbito")
    label_data_obito.grid(row=2, column=0, pady=5, padx=10, sticky="w")
    entry_data_obito = tk.Entry(janela_ficha)
    entry_data_obito.grid(row=2, column=1, pady=5, padx=10)

    label_hora_obito = tk.Label(janela_ficha, text="Hora do óbito")
    label_hora_obito.grid(row=3, column=0, pady=5, padx=10, sticky="w")
    entry_hora_obito = tk.Entry(janela_ficha)
    entry_hora_obito.grid(row=3, column=1, pady=5, padx=10)

    label_idade = tk.Label(janela_ficha, text="Idade")
    label_idade.grid(row=4, column=0, pady=5, padx=10, sticky="w")
    entry_idade = tk.Entry(janela_ficha)
    entry_idade.grid(row=4, column=1, pady=5, padx=10)

    label_local_corpo = tk.Label(janela_ficha, text="Local onde o corpo se encontra")
    label_local_corpo.grid(row=5, column=0, pady=5, padx=10, sticky="w")
    entry_local_corpo = tk.Entry(janela_ficha)
    entry_local_corpo.grid(row=5, column=1, pady=5, padx=10)

    label_n_do = tk.Label(janela_ficha, text="Número da D.O (Declaração de óbito)")
    label_n_do.grid(row=6, column=0, pady=5, padx=10, sticky="w")
    entry_n_do = tk.Entry(janela_ficha)
    entry_n_do.grid(row=6, column=1, pady=5, padx=10)

    # Dados do responsável/familiar
    label_nome_responsavel = tk.Label(janela_ficha, text="Nome completo do responsável")
    label_nome_responsavel.grid(row=7, column=0, pady=5, padx=10, sticky="w")
    entry_nome_responsavel = tk.Entry(janela_ficha)
    entry_nome_responsavel.grid(row=7, column=1, pady=5, padx=10)

    label_vinculo_responsavel = tk.Label(janela_ficha, text="Tipo de vínculo")
    label_vinculo_responsavel.grid(row=8, column=0, pady=5, padx=10, sticky="w")
    combo_vinculo_responsavel = tk.OptionMenu(janela_ficha, tk.StringVar(), "Pai", "Mãe", "Filho(a)", "Irmão(ã)")
    combo_vinculo_responsavel.grid(row=8, column=1, pady=5, padx=10)

    label_cpf_responsavel = tk.Label(janela_ficha, text="CPF do responsável")
    label_cpf_responsavel.grid(row=9, column=0, pady=5, padx=10, sticky="w")
    entry_cpf_responsavel = tk.Entry(janela_ficha)
    entry_cpf_responsavel.grid(row=9, column=1, pady=5, padx=10)

    label_rg_responsavel = tk.Label(janela_ficha, text="RG do responsável")
    label_rg_responsavel.grid(row=10, column=0, pady=5, padx=10, sticky="w")
    entry_rg_responsavel = tk.Entry(janela_ficha)
    entry_rg_responsavel.grid(row=10, column=1, pady=5, padx=10)

    label_endereco_responsavel = tk.Label(janela_ficha, text="Endereço do responsável")
    label_endereco_responsavel.grid(row=11, column=0, pady=5, padx=10, sticky="w")
    entry_endereco_responsavel = tk.Entry(janela_ficha)
    entry_endereco_responsavel.grid(row=11, column=1, pady=5, padx=10)

    label_telefone_responsavel = tk.Label(janela_ficha, text="Telefone do responsável")
    label_telefone_responsavel.grid(row=12, column=0, pady=5, padx=10, sticky="w")
    entry_telefone_responsavel = tk.Entry(janela_ficha)
    entry_telefone_responsavel.grid(row=12, column=1, pady=5, padx=10)

    # Dados do médico
    label_nome_medico = tk.Label(janela_ficha, text="Nome do médico que atestou o óbito")
    label_nome_medico.grid(row=13, column=0, pady=5, padx=10, sticky="w")
    entry_nome_medico = tk.Entry(janela_ficha)
    entry_nome_medico.grid(row=13, column=1, pady=5, padx=10)

    label_crm_medico = tk.Label(janela_ficha, text="CRM do médico")
    label_crm_medico.grid(row=14, column=0, pady=5, padx=10, sticky="w")
    entry_crm_medico = tk.Entry(janela_ficha)
    entry_crm_medico.grid(row=14, column=1, pady=5, padx=10)

    # Dados da funerária
    label_nome_funeraria = tk.Label(janela_ficha, text="Nome da funerária")
    label_nome_funeraria.grid(row=15, column=0, pady=5, padx=10, sticky="w")
    entry_nome_funeraria = tk.Entry(janela_ficha)
    entry_nome_funeraria.grid(row=15, column=1, pady=5, padx=10)

    label_nome_agente_funerario = tk.Label(janela_ficha, text="Nome do agente funerário")
    label_nome_agente_funerario.grid(row=16, column=0, pady=5, padx=10, sticky="w")
    entry_nome_agente_funerario = tk.Entry(janela_ficha)
    entry_nome_agente_funerario.grid(row=16, column=1, pady=5, padx=10)

    label_nome_agente_funerario2 = tk.Label(janela_ficha, text="Nome do agente funerário 2")
    label_nome_agente_funerario2.grid(row=17, column=0, pady=5, padx=10, sticky="w")
    entry_nome_agente_funerario2 = tk.Entry(janela_ficha)
    entry_nome_agente_funerario2.grid(row=17, column=1, pady=5, padx=10)

    label_local_velorio = tk.Label(janela_ficha, text="Local do velório")
    label_local_velorio.grid(row=18, column=0, pady=5, padx=10, sticky="w")
    entry_local_velorio = tk.Entry(janela_ficha)
    entry_local_velorio.grid(row=18, column=1, pady=5, padx=10)

    label_local_cremacao_sepultamento = tk.Label(janela_ficha, text="Local de cremação/sepultamento")
    label_local_cremacao_sepultamento.grid(row=19, column=0, pady=5, padx=10, sticky="w")
    entry_local_cremacao_sepultamento = tk.Entry(janela_ficha)
    entry_local_cremacao_sepultamento.grid(row=19, column=1, pady=5, padx=10)

    label_cidade_cremacao_sepultamento = tk.Label(janela_ficha, text="Cidade da cremação/sepultamento")
    label_cidade_cremacao_sepultamento.grid(row=20, column=0, pady=5, padx=10, sticky="w")
    entry_cidade_cremacao_sepultamento = tk.Entry(janela_ficha)
    entry_cidade_cremacao_sepultamento.grid(row=20, column=1, pady=5, padx=10)

    label_data_cremacao_sepultamento = tk.Label(janela_ficha, text="Data de cremação/sepultamento")
    label_data_cremacao_sepultamento.grid(row=21, column=0, pady=5, padx=10, sticky="w")
    entry_data_cremacao_sepultamento = tk.Entry(janela_ficha)
    entry_data_cremacao_sepultamento.grid(row=21, column=1, pady=5, padx=10)

    label_placa_carro_funerario = tk.Label(janela_ficha, text="Placa do carro funerário")
    label_placa_carro_funerario.grid(row=22, column=0, pady=5, padx=10, sticky="w")
    entry_placa_carro_funerario = tk.Entry(janela_ficha)
    entry_placa_carro_funerario.grid(row=22, column=1, pady=5, padx=10)

    # Botão para emitir ficha
    botao_emitir_ficha = tk.Button(janela_ficha, text="Emitir Ficha", command=emitir_ficha)
    botao_emitir_ficha.grid(row=23, column=1, pady=10)

def configurar_janela(janela):
    window_width = 640
    window_height = 480
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    janela.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    janela.minsize(window_width, window_height)

def emitir_ficha():
    messagebox.showinfo("Ficha Emitida", "A ficha de acompanhamento foi emitida com sucesso!")

# Para testar a interface, chame abrir_ficha_acompanhamento() após o login bem-sucedido
