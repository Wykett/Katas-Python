from collections import Counter

class Counting:
    urls = []

    def __init__(self, urls):
        self.urls = urls

    def count(self):
        count_dict = {}
        for url in self.urls:
            filename = url[url.rfind("/")+1:]
            if filename in count_dict:
                count_dict[filename] += 1
            else:
                count_dict[filename] = 1
        c = Counter(count_dict)
        mc = c.most_common(3)
        return mc