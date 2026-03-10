import requests

def enviar_confirmacion_whatsapp(telefono, nombre_paciente, hora_turno):
    """
    Envía una notificación de WhatsApp a través de la API de UltraMsg.
    """
    # Credenciales de tu instancia activa
    instancia = "165004"
    token = "jb7bo4nf85z67fz1"
    url = f"https://api.ultramsg.com/instance{instancia}/messages/chat"
    
    # Limpieza básica del teléfono: 
    # UltraMsg prefiere formatos como +569... o 569... sin espacios ni puntos.
    telefono_limpio = str(telefono).replace(" ", "").replace(".", "").replace("-", "")
    
    # Personalizamos el mensaje profesional para Vivand
    mensaje = (
        f"Hola *{nombre_paciente}*, tu turno en *Vivand* ha sido confirmado "
        f"para las *{hora_turno}*. ¡Te esperamos! 🩺"
    )

    payload = {
        "token": token,
        "to": telefono_limpio, 
        "body": mensaje
    }
    
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    
    try:
        # Realizamos la petición POST a UltraMsg
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status() # Lanza error si el HTTP falló (4xx o 5xx)
        return response.json()
    except Exception as e:
        print(f"Error crítico enviando WhatsApp: {e}")
        return None