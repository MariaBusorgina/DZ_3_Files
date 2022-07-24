def writeData():
    allDataList = []

    with open('1.txt', encoding='utf-8') as file:
        inFile = file.readlines()
        allDataList.append({
            "name": '1.txt',
            "length": len(inFile),
            'text': inFile
        })

    with open('2.txt', encoding='utf-8') as file:
        inFile = file.readlines()
        allDataList.append({
            "name": '2.txt',
            "length": len(inFile),
            'text': inFile
        })

    with open('3.txt', encoding='utf-8') as file:
        inFile = file.readlines()
        allDataList.append({
            "name": '3.txt',
            "length": len(inFile),
            'text': inFile
        })

    trueListe = sorted(allDataList, key=lambda x: x['length'])
    print(trueListe)

    for item in trueListe:
        for data in item:
            with open('itog.txt', 'a', encoding='utf-8') as file:
                if(type(item[data]) == list):
                    for str in item[data]:
                        file.write(str)
                    file.write('\n')
                else:
                    file.write(f"{item[data]} \n")
writeData()