from openpyxl import load_workbook
import subprocess

nome_arquivo_cep = '/Users/gustavomendonca/Documents/cep_pycharm/ceps_py.xlsx'
planilha_dados_endereco = load_workbook(nome_arquivo_cep)

sheet_dados = planilha_dados_endereco["Cep"]
from selenium import  webdriver as WB
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as pgui
import xlsxwriter


navegador = WB.Chrome()

pgui.moveTo(x=90, y=69)
pgui.sleep(1)
pgui.click()
navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
navegador.find_element(By.NAME, 'endereco').send_keys('08142-640')
navegador.find_element(By.NAME, 'btn_pesquisar').click()
pgui.sleep(3)

for linha in range(2, len(sheet_dados['A'])+ 1):
    pgui.sleep(1)
    navegador.find_element(By.ID, 'btn_nbusca').click()
    pgui.sleep(1)

    cepPesquisa = sheet_dados['A%s' % linha].value
    pgui.sleep(1)
    navegador.find_element(By.NAME, 'endereco').send_keys(cepPesquisa)
    pgui.sleep(2)

    navegador.find_element(By.NAME, 'btn_pesquisar').click()
    pgui.sleep(1)


    endereco = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
    print(endereco)
    bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    print(bairro)
    cidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
    print(cidade)
    cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text
    print(cep)

    pgui.sleep(3)

    sheetDadosImprimir = planilha_dados_endereco["Dados"]
    linhaPlanilhaCEP = len(sheetDadosImprimir['A']) + 1


    colunaA = 'A' + str(linhaPlanilhaCEP)
    colunaB = 'B' + str(linhaPlanilhaCEP)
    colunaC = 'C' + str(linhaPlanilhaCEP)
    colunaD = 'D' + str(linhaPlanilhaCEP)

    sheetDadosImprimir[colunaA] = endereco
    sheetDadosImprimir[colunaB] = bairro
    sheetDadosImprimir[colunaC] = cidade
    sheetDadosImprimir[colunaD] = cep


planilha_dados_endereco.save(filename=nome_arquivo_cep)
subprocess.run(['open', nome_arquivo_cep])











