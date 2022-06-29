import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
}
i = 1
rows = open('./picUrl.txt', encoding='utf-8').readlines()
rows = [i.strip() for i in rows if i.strip()]
for url in rows:
    try:
        res = requests.get(url=url, headers=headers)
        print(i)
        print(' ' + url)
        i += 1
        with open('pic\\all\\' + url[-12:], mode='wb') as f:
            f.write(res.content)
    except Exception as e:
        print(str(e))
