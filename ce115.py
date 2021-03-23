def includes(items, it, st_index=0):
    if type(items) == list or type(items) == str:
        return it in items[st_index:]
    return it in items.values()
