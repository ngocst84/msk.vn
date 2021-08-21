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
    await r.html.arender(scrolldown = 2)

    print (url)
    products = []
    desc = r.html.xpath('//*[@id="rso"]/div')
    # print (desc)
    for item in desc:
        product = {
            'title': item.xpath('//*/h3//text()')[0],
            'price': ''.join(item.xpath('//*/div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"]//text()[normalize-space()]'))
        }
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
urls =['https://www.google.com/search?q=scroll+infinite&sxsrf=ALeKk03noJ8yFPsCrkpmOTl6OgZzWwUXXw%3A1629519633913&source=hp&ei=EX8gYdjfNNzNz7sPrKuEoAM&iflsig=AINFCbYAAAAAYSCNIefQPKUQUELRRJoOPlhrZpAuC5ty&oq=&gs_lcp=Cgdnd3Mtd2l6EAEYCTIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1AAWABgq83dBGgBcAB4AIABAIgBAJIBAJgBALABCg&sclient=gws-wiz']
result = asyncio.run(main(urls))
print (result)
fin = time.perf_counter() - start
print (fin)