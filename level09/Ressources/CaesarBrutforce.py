with open('./token', 'r') as file:
    encrypted_pass = file.read()[:-1]
    decrypted_pass = str()
    for i in range(0, len(encrypted_pass)):
        c = ord(encrypted_pass[i]) - i
        decrypted_pass = decrypted_pass + chr(c)
    print(decrypted_pass)
