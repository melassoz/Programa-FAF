from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def emitir_pdf(dados):
    # Defina o nome do arquivo PDF com base no nome do falecido e data/hora
    nome_arquivo = f"{dados['nome_falecido']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    # Cria o arquivo PDF
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    
    c.setFont("Helvetica", 12)
    
    # Adiciona os dados ao PDF
    c.drawString(100, 750, f"Nome do Falecido: {dados['nome_falecido']}")
    c.drawString(100, 730, f"Data de Nascimento: {dados['data_nascimento']}")
    c.drawString(100, 710, f"Data do Óbito: {dados['data_obito']}")
    c.drawString(100, 690, f"Hora do Óbito: {dados['hora_obito']}")
    c.drawString(100, 670, f"Idade: {dados['idade']}")
    c.drawString(100, 650, f"Local do Corpo: {dados['local_corpo']}")
    c.drawString(100, 630, f"Nº D.O: {dados['numero_do']}")
    
    c.drawString(100, 610, f"Nome do Responsável: {dados['nome_responsavel']}")
    c.drawString(100, 590, f"Vínculo: {dados['vinculo']}")
    c.drawString(100, 570, f"CPF: {dados['cpf']}")
    c.drawString(100, 550, f"RG: {dados['rg']}")
    c.drawString(100, 530, f"Endereço: {dados['endereco']}")
    c.drawString(100, 510, f"Telefone: {dados['telefone']}")
    
    c.drawString(100, 490, f"Nome do Médico: {dados['nome_medico']}")
    c.drawString(100, 470, f"CRM: {dados['crm']}")
    
    c.drawString(100, 450, f"Nome da Funerária: {dados['nome_funeraria']}")
    c.drawString(100, 430, f"Nome do Agente Funerário: {dados['nome_agente_funerario']}")
    c.drawString(100, 410, f"Local do Velório: {dados['local_velorio']}")
    c.drawString(100, 390, f"Local da Cremação/Sepultamento: {dados['local_cremacao_sepultamento']}")
    c.drawString(100, 370, f"Cidade: {dados['cidade_cremacao_sepultamento']}")
    c.drawString(100, 350, f"Data de Cremação/Sepultamento: {dados['data_cremacao_sepultamento']}")
    c.drawString(100, 330, f"Placa do Carro Funerário: {dados['placa_carro_funerario']}")
    
    # Salva o arquivo PDF
    c.save()
    return nome_arquivo
