from threading import Thread, RLock
import requests
from bs4 import BeautifulSoup

urls = [
    "http://www.python.org",
    "http://www.python.org/about/",
    "http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html",
    "http://www.python.org/doc/",
    "http://www.python.org/download/",
    "http://www.python.org/getit/",
    "http://www.python.org/community/",
    "https://wiki.python.org/moin/",
]

lock = RLock()


class SyncThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        with lock:
            url = urls[self.num]
            print(f"Link {self.num}: {url}")
            r = requests.get(url)
            # print(url, r.status_code)
            soup = BeautifulSoup(r.content, "html")
            links = []
            for elem in soup.find_all("a"):
                links.append(elem.get("href"))
            for i, link in enumerate(links):
                if link[:4] != "http":
                    links.remove(link)
                else:
                    print(f"\t\t{i}. {link}")


threads = [SyncThread(1), SyncThread(2), SyncThread(3), SyncThread(4)]

for thread in threads:
    thread.start()
