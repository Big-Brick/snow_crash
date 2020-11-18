with open('./encrypted_pass', 'r') as file:
  encrypted_pass = file.read()[:-1]
  for i in range(26):
    decrypted_pass = str()
    for c in encrypted_pass:
      c = ((ord(c) - 97 + i) % 26) + 97
      decrypted_pass = decrypted_pass + chr(c)
    print('+%d: %s'% (i, decrypted_pass))
