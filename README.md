# 🤖 Automação de Mensagens WhatsApp

Este projeto automatiza o envio de mensagens no WhatsApp Web através de automação de interface gráfica. O script envia mensagens programadas para um contato específico em intervalos regulares.

## 📋 Requisitos

### Software Necessário
- **Python 3.7+** (recomendado: Python 3.9 ou superior)
- **Google Chrome** ou **Microsoft Edge** (para WhatsApp Web)
- **Windows 10/11** (testado apenas neste sistema)

### Bibliotecas Python
```bash
pip install pyautogui pyperclip
```

## 🚀 Instalação

### 1. Clone ou Baixe o Projeto
```bash
git clone <url-do-repositorio>
# ou baixe o ZIP e extraia
```

### 2. Instale as Dependências
```bash
pip install pyautogui pyperclip
```

### 3. Configure o WhatsApp Web
- Abra o WhatsApp Web no seu navegador
- Faça login com sua conta
- **IMPORTANTE**: Deixe o WhatsApp Web aberto e visível na tela

## ⚙️ Configuração e Personalização

### 🔧 Configurações Básicas

Abra o arquivo `main_codes/main.py` e edite as seguintes variáveis:

#### 1. **Contato e Mensagem**
```python
# Nome do contato para pesquisar
contact_search_text = "Nome do Contato"

# Mensagem que será enviada
message_text = """Sua mensagem aqui
com quebras de linha
e se quiser emojis 🎉"""
```

#### 2. **Coordenadas da Tela** ⚠️ **IMPORTANTE**
```python
coords = {
    "click_search_field": (262, 183),    # Campo de pesquisa
    "click_contact_result": (278, 332),  # Resultado do contato
    "click_message_box": (1093, 699),    # Caixa de mensagem
    "click_send_button": (1333, 696),    # Botão enviar (opcional)
}
```

#### 3. **Timing e Horários**
```python
# Intervalo entre mensagens (em segundos)
loop_interval = 60.0  # 60 segundos = 1 minuto

# Horário mínimo para começar a enviar (hora, minuto)
min_time_to_send = (1, 38)  # 1h38 da manhã

# Pausas entre ações
short_pause = 0.25  # Pausa curta
long_pause = 1.0    # Pausa longa
```

## 🚦 Como Usar

### 1. **Preparação**
```bash
# 1. Abra o WhatsApp Web
# 2. Faça login
# 3. Configure as coordenadas no código
# 4. Teste as coordenadas primeiro
```

### 2. **Execução**
```bash
python main_codes/main.py
```

### 3. **Controle**
- **Ctrl+C** para parar o script
- **Mova o mouse para o canto superior esquerdo** para ativar o failsafe

## ⚠️ Avisos Importantes

### **Segurança**
- ⚠️ **Use com responsabilidade** - não abuse do WhatsApp
- ⚠️ **Respeite os limites** do WhatsApp (evite spam)
- ⚠️ **Teste primeiro** com mensagens de teste

### **Limitações**
- 🔒 **Funciona apenas no WhatsApp Web**
- 🔒 **Precisa manter a janela visível**
- 🔒 **Coordenadas específicas para cada tela**

### **Problemas Comuns**
1. **"Coordenadas erradas"** → Ajuste as coordenadas no código
2. **"WhatsApp não encontrado"** → Verifique se está aberto e visível
3. **"Mensagem não enviada"** → Verifique se o contato existe

## 🔧 Solução de Problemas

### **Erro: "Coordenadas não funcionam"**
1. Verifique a resolução da tela
2. Ajuste as coordenadas manualmente
3. Teste com cliques manuais primeiro

### **Erro: "WhatsApp não responde"**
1. Recarregue a página do WhatsApp Web
2. Verifique a conexão com a internet
3. Feche e abra o navegador novamente

### **Erro: "Mensagem não enviada"**
1. Verifique se o contato existe
2. Confirme se as coordenadas estão corretas
3. Teste enviando uma mensagem manualmente

## 📝 Exemplo de Configuração Completa

```python
# Configuração para uma mensagem de bom dia
contact_search_text = "João Silva"
message_text = """🌅 Bom dia!

Espero que tenha um ótimo dia!
Lembre-se: você é incrível! 💪"""

coords = {
    "click_search_field": (300, 200),
    "click_contact_result": (300, 250),
    "click_message_box": (800, 600),
    "click_send_button": (1000, 600),
}

loop_interval = 3600.0  # 1 hora
min_time_to_send = (7, 0)  # 7h da manhã
```

## 🤝 Contribuições

Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Adicionar novas funcionalidades
- Compartilhar suas configurações

## 📄 Licença

Este projeto é para uso pessoal e educacional. Use com responsabilidade e respeitando os termos de uso do WhatsApp.

---

**⚠️ Aviso Legal**: Este script é para fins educacionais e de automação pessoal. O usuário é responsável por seu uso adequado e em conformidade com os termos de serviço do WhatsApp.