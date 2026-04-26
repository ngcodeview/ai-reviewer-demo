def process():
    try:
        gateway.charge()
    except:
        pass # Silent fail