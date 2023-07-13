import base64


def desencriptar(data):
    # Verifica que la cadena tenga un número al final
    if data[-1].isdigit():
        # Elimina el último carácter
        data = data[:-1]
    # Verifica que la longitud sea múltiplo de 4
    if len(data) % 4 != 0:
        # Agrega el carácter "=" al final hasta que la longitud sea múltiplo de 4
        data += "=" * (4 - len(data) % 4)
    # Decodifica la cadena base64
    decoded = base64.b64decode(data)
    text = decoded.decode("utf-8")  # Texto en utf-8
    return text
