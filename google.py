from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep
import requests
from lxml import etree
from selenium.webdriver.common.by import By


def collect():
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
    # js = open('stealth.min.js').read()
    # driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
    # proxies = '127.0.0.1:2233'

    proxies = {
        'http': 'http:' + '127.0.0.1:2233',
        'https': 'https:' + '127.0.0.1:2233'
    }
    rows = open('./ids.txt', encoding='utf-8').readlines()
    rows = [i.strip() for i in rows if i.strip()]
    with open('./picUrl.txt', mode="a", encoding='utf-8') as f:  # 使用with open()新建对象f
        f.seek(0)
        f.truncate()
    for skuId in rows:
        try:
            url = f'https://www.google.com/search?q={skuId}&tbm=isch'
            driver.get(url)
            sleep(2)

            for block in driver.find_elements(By.XPATH, '//div[@class="islrc"]/div'):
                try:
                    block.click()
                    sleep(2)
                    page = driver.page_source
                    tree = etree.HTML(page)
                    pictUrls = tree.xpath('//a[@role="link"]/img[contains(@src, "http")]/@src')
                    # 裁切字符串
                    if pictUrls:
                        pictUrls = pictUrls[0]
                        print(pictUrls)
                        # pics.append(pictUrls)
                        # 图片下载，换
                        #     res = requests.get(url=pictUrls, headers=headers, verify=False, proxies=proxies)
                        with open('./picUrl.txt',mode="a", encoding='utf-8') as f:  # 使用with open()新建对象f
                            f.write(pictUrls + '\n')

                        # res = requests.get(url=pictUrls, headers=headers, verify=False, proxies=proxies)
                        # # res = driver.get(pictUrls)
                        # with open('pic\\google\\' + pictUrls[-15:] + '.jpg', mode='wb') as f:
                        #     f.write(res.content)

                except Exception as e:
                    print(str(e))
        except Exception as e:
            print(str(e))
    driver.quit()


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
    }
    collect()
