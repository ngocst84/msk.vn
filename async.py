from requests_html import AsyncHTMLSession
import asyncio
import time
import pyppeteer

async def work (s,url):
    browser = await pyppeteer.launch({ 
        'ignoreHTTPSErrors':True, 
        'headless':True, 
        'handleSIGINT':False, 
        'handleSIGTERM':False, 
        'handleSIGHUP':False
        })
    s._browser = browser
    r = await s.get(url)
    await r.html.arender(scrolldown = 10, sleep = 0.1)

    print (url)
    products = []
    desc = r.html.xpath('//*[@class="bm_AP"]')
    # print (desc)
    i = 0
    for item in desc:
        i +=1
        product = {
            str(i) + 'title': item.xpath('//*/h4[@class="bm_P"]//text()'),
            'price': '',
        }
        print (product)
        products.append(product)
    await s.close()
    return products

async def main (urls):
    # new_loop=asyncio.new_event_loop()
    # asyncio.set_event_loop(new_loop)

    s = AsyncHTMLSession()
    tasks = (work(s,url) for url in urls)
    return await asyncio.gather(*tasks)

start = time.perf_counter()
urls =['https://baomoi.com']
result = asyncio.run(main(urls))
# print (result)
fin = time.perf_counter() - start
print (fin)