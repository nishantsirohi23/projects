from urllib.request import urlopen, urlretrieve
from time import time, sleep, ctime

from bs4 import BeautifulSoup



starttime = time()
interval = 300.0


while True:
    url = "https://www.espncricinfo.com"
    source_code = BeautifulSoup(urlopen(url).read(), "html.parser")
    # t = source_code.title.string
    # t = t.replace("Match Summary", "")
    # t = t.replace("ESPNCricinfo", "")
    # t = t.replace("|", "", 2)
    # print(ctime(), t)


    items = source_code.find("div", class_="ds-pt-2")
    #item2 = items.find("div",class_="ds-flex ds-flex-row ds-w-full ds-overflow-x-auto ds-scrollbar-hide ds-px-2 ds-items-center")
    #print(items)
    for i in items:
        print(items.text)
    sleep(interval - ((time() - starttime) % interval))