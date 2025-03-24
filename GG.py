MTG = {'Чара': [20, 'Не перманент',0], 'Волшебство': [30, 'Не перманент',0], 'Артефакт': [1, 'Не перманент',0], 'Мгновенное заклинание': [4, 'Не перманент',0], 'Существо': [0, 'Не Перманент',0]}
for i in MTG:
        a = MTG[i]
        sclad = a[0]
        c = a[1]
        class_=a[2]
        if sclad <= 20:
           sclad += 10
           MTG[i] = [sclad,class_]
        if class_== 'Перманент':
            class_="доступна в количестве" + str(sclad)
            MTG[i] = [sclad,class_]
        else:
            class_="не подходит"
            MTG[i] = [sclad,class_] 
print(MTG)
