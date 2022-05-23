"""
Automação com Python
Envio de Email
Integração com o software Outlook
"""

# Imports

import win32com.client as win32

# Integration

outlook = win32.Dispatch('outlook.application')

# Settings

email = outlook.CreateItem(0)
email.To = 'thiago.rodrigues@grupomoura.com'
email.Subject = 'Teste de envio de email'
email.HTMLBody = """
<p>Prezado Thiago Rodrigues,</p>

<p>Esse é um exemplo de envio de email através da integração do Python com o Outlook.</p>

<p>Por favor, ignorar esse email.</p>



<p>Cordialmente,</p>

<p>Thiago Rodrigues</p>
<p>UGSC | Estagiário de Engenharia</p>
"""

# Send

email.Send()
