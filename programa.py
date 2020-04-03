import requests, json, hashlib

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=e8b6bbe32b89bbad9a43e0fcd834e785835bb1f8"

r = requests.get(url)

data = r.json()

with open('answer.json', 'w') as f:
    json.dump(data, f)

with open('answer.json', 'r') as f:
    msg_dict = json.load(f)
    encoding = f.encoding

message = msg_dict['cifrado']

translated = ''

for symbol in message:
    if symbol.isalpha():
        num = ord(symbol)
        num += -msg_dict['numero_casas']
        
        if symbol.islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
        translated += chr(num)
    else:
        translated += symbol

msg_dict['decifrado'] = translated

resumo = hashlib.sha1(msg_dict['decifrado'].encode(encoding)).hexdigest()
msg_dict['resumo_criptografico'] = resumo

with open('answer.json', 'w') as f:
    json.dump(msg_dict, f)

with open('answer.json', 'r') as f:
    msg_dict_outra = json.load(f)
    encoding = f.encoding


URLoutra = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=e8b6bbe32b89bbad9a43e0fcd834e785835bb1f8'

files = {'answer': open('answer.json', 'rb') }

p = requests.post(URLoutra, files=files)

print(p.text)