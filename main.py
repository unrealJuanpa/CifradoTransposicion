import numpy as np

clave = input('Clave: ').upper().replace(' ', '')
msg = input('Mensaje: ').upper().replace(' ', '')

diccionario = [chr(c) for c in range(65, 77)]
diccionario.append('LL')
diccionario.extend([chr(c) for c in range(77, 91)])

while len(msg) % len(clave) != 0: msg += ' '

msg = np.array([c for c in msg])
msg = np.reshape(msg, (msg.size//len(clave), len(clave)))
indices = np.array([diccionario.index(c) for c in clave if c != ' '])
msg = msg[:, indices.argsort()].transpose()
final = ""

for i in range(len(clave)):
    final += str(list(msg[i, :])).replace('[', '').replace(']', '').replace(' ', '').replace("'", "").replace(',', '') + ' '

print(final)