class Counter:
    count_insta = 0
    def __init__(self):
        type(self).count_insta + 1

Counter()
Counter()
Counter()

count = Counter()
print(count)