class RecentCounter:

    def __init__(self):
        self.requests = []
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        cutoff = t - 3000
        new_list = []
        for request in self.requests:
            if request >= cutoff:
                new_list.append(request)
        self.requests = new_list
        return len(self.requests)
