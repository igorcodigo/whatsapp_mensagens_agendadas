import subprocess
import time
import pyautogui
import pyperclip
import sys
import random
import os
from datetime import datetime

# Texto que será usado para pesquisar o contato (nome)
contact_search_text = "Cesar Hideki"

# Texto da mensagem a ser enviada (string). Será enviada 1x a cada minuto.
message_text = """🌞🐄🐖🐥 *Bom dia!*  

🎶 O Sol já nasceu lá na fazendinha,  
acorda o bezerro e a vaquinha 🐮  
que já cocoricou dona galinha 🐔     

📌 *Lembrete para hoje*  

1. Switch 1 🎮  
2. Switch 2 🎮  
- 🎤 Microfones  
- 🥤 Canecas  

E não menos importante:  
- 🛍️ Procurar uma sacola da C&A e guardá-la com carinho ❤️ na sala dos organizadores ✨  
"""


# Coordenadas (x, y) — editar conforme sua tela.
# ONDE:
coords = {
    "click_search_field": (262, 183),    # exemplo
    "click_contact_result": (278, 332),  # exemplo
    "click_message_box": (1093, 699),    # exemplo
    "click_send_button": (1333, 696),   # exemplo (pode deixar None e usar Enter)
}

# Intervalo entre envios (em segundos) - 60 segundos = 1 minuto
loop_interval = 60.0

# Horário mínimo para iniciar o envio de mensagens (formato: hora, minuto)
# Exemplo: (1, 33) = 1h33 da manhã
min_time_to_send = (6, 59)

# Tempo entre ações (em segundos) — ajuste se precisar
short_pause = 0.25
long_pause = 1.0
# -------------------------------------------------------------------

pyautogui.FAILSAFE = True
pyautogui.PAUSE = short_pause

def click(coord, clicks=1, interval=0.1):
    x, y = coord
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click(clicks=clicks, interval=interval)

def paste_text(text):
    # usa clipboard para evitar problemas com caracteres especiais
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

def is_time_to_send():
    """Verifica se o horário atual é válido para envio de mensagens"""
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    
    min_hour, min_minute = min_time_to_send
    
    # Converte para minutos desde meia-noite para facilitar comparação
    current_time_minutes = current_hour * 60 + current_minute
    min_time_minutes = min_hour * 60 + min_minute
    
    return current_time_minutes >= min_time_minutes

def open_browser_with_url(exe_path, url):
    try:
        # abre navegador com URL como argumento
        subprocess.Popen([exe_path, url], shell=False)
    except Exception as e:
        print(f"[ERRO] Não foi possível abrir o navegador: {e}")
        sys.exit(1)

def setup_contact():
    """Configura o contato uma única vez no início"""
    print("Configurando contato...")
    
    # 1) clicar no campo de pesquisa do contato
    if coords.get("click_search_field"):
        click(coords["click_search_field"])
        time.sleep(short_pause)

    # 2) digitar (colar) o nome do contato
    paste_text(contact_search_text)
    time.sleep(long_pause)  # espera resultados aparecerem

    # 3) clicar no resultado do contato
    if coords.get("click_contact_result"):
        click(coords["click_contact_result"])
        time.sleep(long_pause)
    
    print("Contato configurado! Agora iniciando envio de mensagens...")

def send_message():
    """Envia uma única mensagem (passos 4 e 5)"""
    # 4) clicar na caixa de mensagem
    if coords.get("click_message_box"):
        click(coords["click_message_box"])
        
    time.sleep(short_pause)
    paste_text(message_text)
    time.sleep(0.25)

    # 5) clicar no botão enviar se coordenada fornecida, senão usar Enter
    if coords.get("click_send_button"):
        click(coords["click_send_button"])
    else:
        pyautogui.press('enter')
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Mensagem enviada.")

def main_loop():
    time.sleep(5)
    try:
        # Configura o contato uma única vez no início
        setup_contact()
        
        # Verifica se já é hora de enviar mensagens
        if not is_time_to_send():
            min_hour, min_minute = min_time_to_send
            print(f"Aguardando horário para envio (após {min_hour:02d}:{min_minute:02d})...")
            print(f"Horário atual: {datetime.now().strftime('%H:%M:%S')}")
            
            # Aguarda até o horário permitido
            while not is_time_to_send():
                time.sleep(30)  # Verifica a cada 30 segundos
                print(f"Aguardando... Horário atual: {datetime.now().strftime('%H:%M:%S')}")
        
        print(f"Horário permitido atingido! Iniciando envio de mensagens às {datetime.now().strftime('%H:%M:%S')}")
        
        iteration = 1
        while True:
            send_message()
            print(f"Envio {iteration} concluído. Aguardando {loop_interval} segundos (1 minuto) até o próximo.")

            iteration += 1
            # Dorme pelo intervalo definido (60s por padrão)
            time.sleep(loop_interval)
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    print(">>> Script de automação iniciado. Pressione Ctrl+C para interromper.")
    main_loop()
