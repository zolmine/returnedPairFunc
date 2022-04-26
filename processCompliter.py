from websocket import create_connection
from json import loads,dumps
# from lists import polyList
# from calc import find_x_and_w,w1,w2

def decodeReserve(input):

    rererve0 = int(input[2:66], 16)
    rererve1 = int(input[66:130], 16)
    return(rererve0, rererve1)
def myFunc(e):
  return (e['w'])





def getReserve(place,baseAddr,tokenAddr,dex,amountIn,amountOut):
    tokenAdd = str(place) + str(baseAddr) + str(tokenAddr) + str(dex)
    # print(tokenAddr)
    # return True
    finalResultD = []
    firstResult = []
    secondResult = []
    thirdResult = []
    ws = create_connection(
        "wss://polygon-mainnet.g.alchemy.com/v2/p0Tqunv8aWA94L7Lqc_AKKJy0XDvlJV2")
    data = polyList[tokenAdd]

    # for one in allPairs:
    #     allData.append({"jsonrpc":"2.0","method":"eth_call","params":[{"to": one["pair"], "data":"0x0902f1ac"}, "latest"],"id":one["pair"][0:10]})

    json_data = dumps(data["request"]).encode("utf-8")
    ws.send(json_data)

    results = ws.recv()
    if results:
        results = loads(results)
    else:
        results = ws.recv()
        results = loads(results)
    for item in data["probabilities"]:
        for sOne in results:
            if item["firstPair"][0:10] == sOne["id"]:
                reserve = decodeReserve(sOne["result"])
                if item["firstBase"] == 0:
                    firstReserve0 = reserve[0]
                    firstReserve1 = reserve[1]
                elif item["firstBase"] == 1:
                    firstReserve0 = reserve[1]
                    firstReserve1 = reserve[0]
                if place == "first":
                    firstReserve0 = firstReserve0 - amountOut
                    firstReserve1 = firstReserve1 + amountIn
                firstFee = item["firstFee"]
                firstResult.append({"id": item["id"], "reserve": (
                    firstReserve0, firstReserve1), "fee": firstFee})
                # print(firstResult)
                # print(f"{item['id']},{firstReserve0,firstReserve1,firstFee},first")

            elif item["secondPair"][0:10] == sOne["id"]:
                reserve = decodeReserve(sOne["result"])
                if item["secondBase"] == 0:
                    secondReserve0 = reserve[0]
                    secondReserve1 = reserve[1]
                elif item["secondBase"] == 1:
                    secondReserve0 = reserve[1]
                    secondReserve1 = reserve[0]
                if (len(item) == 7) and (place == "last"):
                    thirdReserve0 = thirdReserve0 + amountIn
                    thirdReserve1 = thirdReserve1 - amountOut
                secondFee = item["secondFee"]
                secondResult.append({"id": item["id"], "reserve": (
                    secondReserve0, secondReserve1), "fee": secondFee})

                # print(f"{item['id']},{secondReserve0,secondReserve1,secondFee},second")
            if "thirdPair" in item:
                if item["thirdPair"][0:10] == sOne["id"]:
                    reserve = decodeReserve(sOne["result"])
                    if item["thirdBase"] == 0:
                        thirdReserve0 = reserve[0]
                        thirdReserve1 = reserve[1]
                    elif item["thirdBase"] == 1:
                        thirdReserve0 = reserve[1]
                        thirdReserve1 = reserve[0]
                    if place == "last":
                        thirdReserve0 = thirdReserve0 + amountIn
                        thirdReserve1 = thirdReserve1 - amountOut
                    thirdFee = item["thirdFee"]
                    thirdResult.append({"id": item["id"], "reserve": (
                        thirdReserve0, thirdReserve1), "fee": thirdFee})

    if not thirdResult:
        for row in firstResult:
            for elem in secondResult:
                if row["id"] == elem["id"]:
                    print(
                        f"{row['id']},{row['reserve'],row['fee']},{elem['reserve'],elem['fee']}")
    else:
        for row in firstResult:
            for elem in secondResult:
                for item in thirdResult:
                    if row["id"] == elem["id"] == item["id"]:
                        # return True
                        finalResultD.append({"id":row['id'],"first":[row['reserve'],row['fee']],"second":[elem['reserve'],elem['fee']],"third":[item['reserve'],item['fee']]})
                        # print(
                        #     f"{row['id']},{row['reserve'],row['fee']},{elem['reserve'],elem['fee']},{item['reserve'],item['fee']}")
                    if (type(row["id"]) == str and type(elem["id"]) == str) and (row["id"] == elem["id"]):
                        finalResultD.append({"id":row['id'],"first":[row['reserve'],row['fee']],"second":[elem['reserve'],elem['fee']]})
                        # print(
                                # f"{row['id']},{row['reserve'],row['fee']},{elem['reserve'],elem['fee']}")
    # print(finalResultD[6])                    
    finalShit = []
    probList = []
    for i in finalResultD:
        if i not in finalShit:
            if "third" in i:
                # print(i["first"][0][0])
                firstReserve0 = i["first"][0][0]
                firstReserve1 = i["first"][0][1]
                firstFee = int(i['first'][1])
                secondReserve0 = i['second'][0][0]
                secondReserve1 = i['second'][0][1]
                secondFee = int(i['second'][1])
                thirdReserve0 = i['third'][0][0]
                thirdReserve1 = i['third'][0][1]
                thirdFee = int(i['third'][1])

                # print(firstFee)
                # print(i)
                # if i['id'] == 4:
                #     print(firstReserve0,firstReserve1,secondReserve0,secondReserve1,thirdReserve0,thirdReserve1)
                try:
                    resulta = find_x_and_w(w2, A=firstReserve0, B=firstReserve1, fee1=firstFee, C=secondReserve0,
                        D=secondReserve1, fee2=secondFee, E=thirdReserve0, F=thirdReserve1, fee3=thirdFee)
                except:
                    resulta = None
                if resulta != None:
                    if int(resulta[0]) > 0:
                        probList.append({"id":i['id'],"x":int(resulta[0]),"w":int(resulta[1])})
                # print(resulta)
            else:

                firstReserve0 = i["first"][0][0]
                firstReserve1 = i["first"][0][1]
                firstFee = int(i['first'][1])
                secondReserve0 = i['second'][0][0]
                secondReserve1 = i['second'][0][1]
                secondFee = int(i['second'][1])
                # print(firstReserve0,firstReserve1,secondReserve0,secondReserve1)
                try:
                    resulta = find_x_and_w(w1, A=firstReserve0, B=firstReserve1, fee1=firstFee, C=secondReserve0,
                        D=secondReserve1, fee2=secondFee)
                except:
                    resulta = None
                # print(resulta)
                if resulta != None:
                    if int(resulta[0]) > 0:
                        probList.append({"id":i['id'],"x":int(resulta[0]),"w":int(resulta[1])})
            finalShit.append(i)
    # print(finalShit)
    probList.sort(reverse=True,key=myFunc)
    print(probList)
    # print(list(set.fromkeys(finalResultD)))
getReserve("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1",437739,663834)