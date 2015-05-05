import requests
from bs4 import BeautifulSoup
from histogram import Histogram


class Crawler:

    def __init__(self):
        self.external_links = []
        self.internal_links = []
        self.servers = Histogram()
        self.starter = "http://register.start.bg/"

    def crawl(self):
        queue = [self.starter]

        while len(queue):
            try:
                site = queue.pop()
                r = requests.get(site)
                soup = BeautifulSoup(r.text)

                all_links = self.get_links(soup)
                self.external_links = self.get_external_links(all_links)
                self.internal_links = self.get_internal_links(all_links)

                for external in self.external_links:
                    try:
                        r = requests.head(site + "/" + external, allow_redirects=True, timeout=10)
                        server = self.get_header_server(r.headers)
                        self.servers.add(server)
                        print(server)
                    except requests.exceptions.ReadTimeout:
                        continue
                    except requests.exceptions.ConnectionError:
                        continue

                queue += self.internal_links
            except KeyboardInterrupt:
                break

        self.servers.save()

    def get_links(self, soup):
        return [link.get('href') for link in soup.find_all('a') if link.get('href')]

    def get_internal_links(self, links):
        return [link for link in links if link.endswith(".start.bg/")]

    def get_external_links(self, links):
        return [link for link in links if "link.php" in link]

    def get_header_server(self, headers):
        if 'server' in headers.keys():
            return headers['server']
        if 'Server' in headers.keys():
            return headers['Server']

if __name__ == '__main__':
    crawler = Crawler()
    crawler.crawl()
    print(crawler.servers.get_dict())
