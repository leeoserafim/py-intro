from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from time import sleep

def enviar(nome):
    try: 
        mensagem = driver.find_element(By.XPATH, MESSAGE_BOX)
        mensagem.click()
        mensagem.send_keys(f'Olá *{nome}*, tudo bem?')
        mensagem.send_keys(Keys.CONTROL, Keys.RETURN)
        mensagem.send_keys('Esta é uma mensagem de *Teste*.')
        sleep(3)
        botao = driver.find_element(By.XPATH, SEND)
        botao.click()
        return 'Enviado'
    
    except Exception as e:
        return 'Sem WhatsApp'

WP_LINK = 'https://web.whatsapp.com'

NEW_CHAT = '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[3]/div'

MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div'

SEND = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'

driver = webdriver.Chrome()
driver.get(WP_LINK)

lista_Telefone = ['5512991350134', '5512912345656', '5512991350134']
lista_Nome = ['Thales Santos', 'Gilson Vida Loka', 'Thales Sacilotti']

contador = True

while (contador):
    sleep(3)
    try:
        driver.find_element(By.XPATH, NEW_CHAT)
        contador = False
    
    except:
        print('Por favor scaneie o QRCode')
        contador = True

envio = []

for nome, telefone in zip(lista_Nome, lista_Telefone):
    try:
        sleep(3)
        url = f'https://web.whatsapp.com/send?phone={telefone}'
        driver.get(url)
        sleep(5)
        status = enviar(nome)
        print(f'Telefone: {telefone} - {nome} | {status}')
    
    except Exception as e:
        driver.execut_script('window.stop();')
        status = 'Erro ao enviar'
        print(f'Telefone: {telefone} - {nome} | ERRO ao Enviar')             

    envio.append(status)

print(envio)
sleep(5)
