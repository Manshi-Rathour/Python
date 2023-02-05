def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("this is not good")


a = increment('ad6hv')
print(a)
