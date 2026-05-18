import requests
def testar_site(url):
    try:
        test = requests.get(url)
    except:
        print('O site "cravei.io" não está disponivel no momento.')
    else:
        print('Site está acessivel.')

url = 'https://app.cravei.io/'
testar_site(url)