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
        values = count_dict.values()
        values = [int(x) for x in values]    
        values.sort(reverse=True);
        return values[0:3]