import base64


def desencriptar(data):
    if data[-1].isdigit():
        data = data[:-1]
    if len(data) % 4 != 0:
        data += "=" * (4 - len(data) % 4)
    decoded = base64.b64decode(data)
    text = decoded.decode("utf-8")
    return text
