import os
import pyaes

## Projeto elaborado dia 07|01|2024 - Alexandre Paschoal

## abrir o arquivo criptografado
file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de descriptografia

key = b'testeransomware'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar um novo arquiivo desciptografado

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()
