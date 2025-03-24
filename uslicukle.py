MTG= {'Blood Artist': [50, 'Существо'], 'Yawgmoth': [2300, 'Существо'], 'Gravecravler': [100, 'Существо'], 'Swamp': [200, 'Земля'], 'Island': [444, 'Земля']}
#Для удобства я заменил переменные a,b,c на a-card b-price c-type
print(MTG)
def sale(y):
    for i in y:
        Card = y[i]
        price = Card[0]
        type = Card[1]
        if price >= 100:
            price -= 20
            y[i] = [price,type]
        else:
            price -= 5
            y[i] = [price,type]
        if type == 'Земля':
            price += 30
            y[i] = [price,type]
    return y
sale(MTG)
print(MTG)
