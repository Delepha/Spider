import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
}
url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=0%2C0&fp=detail&logid=7528424350085874088&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=-1&word=%E6%96%87%E7%89%A9&z=0&ic=0&hd=&latest=&copyright=&s=undefined&se=&tab=0&width=&height=&face=undefined&istype=2&qc=&nc=&fr=&simics=&srctype=&bdtype=0&rpstart=0&rpnum=0&cs=1646690724%2C4241597669&catename=&nojc=undefined&album_id=&album_tab=&cardserver=&tabname=&pn=0&rn=60&gsm=17&1656402823894='
response = requests.get(url, headers=headers)
total_url = response.json()['data']

for i in range(60):
    print(i)
    hoverURL_i = total_url[i]['hoverURL']
    print(hoverURL_i)

    res = requests.get(url=hoverURL_i, headers=headers)
    with open('pic\\baidu\\'+hoverURL_i[27:50]+'.jpeg', mode='wb')as f:
        f.write(res.content)

print("success!")


