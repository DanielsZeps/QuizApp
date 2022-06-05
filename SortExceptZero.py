def except_zero(items: list):
    zeroIndex = []
    while True:
        try:
            if len(zeroIndex) == 0:
                zeroIndex.insert(len(zeroIndex), items.index(0))
            else:
                zeroIndex.insert(len(zeroIndex), items.index(0, zeroIndex[-1]+1))
        except:
            break
    def funct1(value):
        return value
    items.sort(key=funct1)
    items = items[len(zeroIndex)::]
    for x in zeroIndex:
        items.insert(x, 0)
    return items
