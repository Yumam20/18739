import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://shell.hackcenter.dbrumley.com:34970',
    'Referer': 'http://shell.hackcenter.dbrumley.com:34970/admin-thermostat-dashboard',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

data = {
     'target_temp': 69,
}

response = requests.post(
    'http://shell.hackcenter.dbrumley.com:34970/admin-thermostat-dashboard',
    headers=headers,
    data=data,
    verify=False,
)
print(response.text)
