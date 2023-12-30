import requests

API_KEY = 'cf2371dd01d6ff259e1ccc3effb113ba'
cidade = 'London'
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&lang=pt_br&appid={API_KEY}'

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f'{temperatura:5f}°C')