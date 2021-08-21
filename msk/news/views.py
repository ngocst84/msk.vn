from django.shortcuts import render
from django.views import generic
from datetime import datetime
from requests_html import AsyncHTMLSession   
import time
import asyncio
import pyppeteer
# Create your views here.

class ViewIndex(generic.TemplateView):
    
    template_name = 'news/index.html'

    def __init__(self):
        now = datetime.now()
    
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        # session = AsyncHTMLSession()
        # r = session.get('https://baomoi.com/tin-moi.epi')

        # r.html.render(scrolldown = 2)
        # self.extra_context = {'obj':r.html.xpath('//meta[@name="author"]/@content'),'now':now}
        # obj = r.html.xpath('//*/a/text()')
        # next_time = time.time() + 10
        # obj = self.get_data_from_page()

        # wait_for = next_time - time.time()
        # if wait_for > 0:
        #     time.sleep(wait_for)
        na = nas(urls=['https://baomoi.com'])
        
        # obj = []
        obj = na.get_result

        self.extra_context = {'obj':obj,'now':now}
        return render(request, self.template_name, self.extra_context)

class nas():
    urls =[]
       
    def __init__(self,urls=None):
        self.urls = urls        
        return
    async def work (self,s,url):
        
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
        
        list_item = r.html.xpath('//*[@class="bm_AP"]')
        dsNews = []
        for item in list_item:
            t = ''.join(item.xpath('//*/h4[@class="bm_P"]//text()')).replace('\'','').replace('\"','')
            if t != '':
                dsn = {
                    'title': t,
                }
                dsNews.append(dsn)
        return dsNews

    async def main (self, urls):
        # new_loop=asyncio.new_event_loop()
        # asyncio.set_event_loop(new_loop)
      
        s = AsyncHTMLSession()
        tasks = (self.work(s,url) for url in urls)
        return await asyncio.gather(*tasks)

    def get_result(self):
        return asyncio.run(self.main(self.urls))[0]