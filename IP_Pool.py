from lxml import etree
from random import randint, choice
import requests


def ip_parse_dec(func):
    def inner():
        url = func()
        print(url)
        rs = requests.get(url=url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}, verify=False)
        print(rs.text)
        html = etree.HTML(rs.text)
        try:
            trs = html.xpath("//table//tr")
            # print(len(trs))
            single = trs[randint(0, len(trs))].xpath("td/text()")
            print(single)
            if "kuaidaili" in url:
                result = single[3].lower() + '://' + single[0] + ":" + single[1]
                return result
            if "天" in single[-1]:
                return inner()
            elif float(single[-2]) > 30:
                return inner()
            elif "https" in url:
                result = 'https://' + single[1] + ":" + single[2]
                return result
            elif "http-proxy" in url:
                result = 'http://' + single[1] + ":" + single[2]
                return result
            elif "page_id" in url:
                result = single[3].lower() + '://' + single[0] + ":" + single[1]
                return result
            elif "iphai" in url:
                if "," in single[3]:
                    result = single[3].split(",")[0].lower() + '://' + single[0] + ":" + single[1]
                else:
                    result = single[3].lower() + '://' + single[0] + ":" + single[1]
                return result
            elif "xicidaili" in url:
                result = single[5].lower()+"://"+single[0]+single[1]
                return result
        except Exception as f:
            return inner()
    return inner()


@ip_parse_dec
def ip():
    url = ['http://31f.cn/https-proxy/', 'http://31f.cn/http-proxy/',
           'http://www.feiyiproxy.com/?page_id=1457', 'http://www.iphai.com/',
           'https://www.kuaidaili.com/free/inha/', 'https://www.kuaidaili.com/free/intr/','https://www.xicidaili.com/nn/1']

    return choice(url)

print(ip)
