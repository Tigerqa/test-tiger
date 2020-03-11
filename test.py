d = dict (weather = "clima", earth = "terra" , rain = "chuva")

def Translate_To_protoguese(world):
    return d[world]

world = input ("Enter world: ")
print(Translate_To_protoguese(world))