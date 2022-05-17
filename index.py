

from json import loads, dumps
from websocket import create_connection
from lists import t_172370d5Cd63279eFa6d502DAB29171933a610AF, t_2ed945Dc703D85c80225d95ABDe41cdeE14e1992, pairs
# from allPairs import allPairs

def funcFor2(place, baseAddr, tokenAddr, dex):
    array = []
    result = []
    newList = []
    for one in data[tokenAddr]:
        if one["dex"] == dex and (one["token0"] == baseAddr or one["token0"] == tokenAddr) and (one["token1"] == baseAddr or one["token1"] == tokenAddr):
            mainPair = one["pair"]
            if one["token0"] == baseAddr:
                basePlace = 0
            else:
                basePlace = 1
    if mainPair:
        for line in allPairs:
            if (line["pair"] != mainPair) and (one["token0"] == baseAddr or one["token0"] == tokenAddr) and (one["token1"] == baseAddr or one["token1"] == tokenAddr):
                newList.append(line)
        print(newList)

    # for elem in newList:

    #     if elem["token0"] == tokenAddr:
    #         secondBase = elem["token1"]
    #     else:
    #         secondBase = elem["token0"]
    #     secondPair = elem['pair']
    #     if elem["token0"] == tokenAddr:
    #             tokenPlace = 0
    #     elif elem["token1"] == tokenAddr:
    #         tokenPlace = 1
    #     if place == "first":
    #         # test = mainPair,basePlace,secondPair,tokenPlace
    #         # print(test)
    #         # result.append(test)
    #         print(f"{mainPair},{basePlace},{secondPair},{tokenPlace}")
    #     elif place == "last":
    #         # test = mainPair,basePlace,secondPair,tokenPlace
    #         # result.append(test)
    # # return result
    #         print(f"{mainPair},{basePlace},{secondPair},{tokenPlace}")

# funcFor2("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1")
# funcFor2(1,"0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174","0x2ed945Dc703D85c80225d95ABDe41cdeE14e1992","1")


def funcFor3(place, baseAddr, tokenAddr, dex):
    pathOf2 = funcFor2(place, baseAddr, tokenAddr, dex)
    newList = []
    newBasesList = []
    intoForBases = False
    result = []
    filtredResult = []
# -------------------------------------------------------------------------------------------------------------------------------------------
    for one in data[tokenAddr]:
        if one["dex"] == dex and (one["token0"] == baseAddr or one["token0"] == tokenAddr) and (one["token1"] == baseAddr or one["token1"] == tokenAddr):
            mainPair = one["pair"]

            if one["token0"] == baseAddr:
                basePlace = 0
            else:
                basePlace = 1
            filtredResult.append({"pair": mainPair, "base": basePlace})
# ________________________________________________________________________________________________________________________________________
    if mainPair:
        for line in data[tokenAddr]:
            if (line["pair"] == mainPair) or ((line["token0"] == baseAddr or line["token0"] == tokenAddr) and (line["token1"] == baseAddr or line["token1"] == tokenAddr)):
                pass
            else:
                newList.append(line)
    # print(newList)
# __________________________________________________________________________________________________________________________________________
    for elem in newList:
        if elem["token0"] == tokenAddr:
            secondBase = elem["token1"]
        else:
            secondBase = elem["token0"]
        secondPair = elem['pair']
        if elem["token0"] == tokenAddr:
            tokenPlace = 0
        elif elem["token1"] == tokenAddr:
            tokenPlace = 1
        filtredResult.append({"pair": secondPair, "base": tokenPlace})
# ----------------------------------------------------------------------------------------------------------------------------------------
        if intoForBases == False:
            for i in pairs:
                if (i["token0"] == secondBase or i["token0"] == baseAddr) and (i["token1"] == secondBase or i["token1"] == baseAddr):
                    if i["token0"] == secondBase:
                        tokenPlace3 = 0
                    elif i["token1"] == secondBase:
                        tokenPlace3 = 1
                    thirdPair = i["pair"]
                    newBasesList.append(i)
                    filtredResult.append(
                        {"pair": thirdPair, "base": tokenPlace3})
            intoForBases = True
            if not newBasesList:
                return None
# _________________________________________________________________________________________________________________________________________
        for item in newBasesList:
            if item["token0"] == secondBase:
                thirdPairTokenPlace = 0
            elif item["token1"] == secondBase:
                thirdPairTokenPlace = 1
            # print(secondBase)
            if place == "first":
                test = mainPair, basePlace, secondPair, tokenPlace, item['pair'], thirdPairTokenPlace
                result.append(test)
                print(
                    f"{mainPair},{basePlace},{secondPair},{tokenPlace},{item['pair']},{thirdPairTokenPlace}")
            elif place == "last":
                test = mainPair, basePlace, secondPair, tokenPlace, item['pair'], thirdPairTokenPlace
                result.append(test)
                print(
                    f"{mainPair},{basePlace},{secondPair},{tokenPlace},{item['pair']},{thirdPairTokenPlace}")
# ____________________________________________________________________________________________________________________________________________

    # print(filtredResult)
    # return(pathOf2,result)



def decodeReserve(input):

    rererve0 = int(input[2:66], 16)
    rererve1 = int(input[66:130], 16)
    return(rererve0, rererve1)


def getReserve(allPairs):
    allData = []
    firstResult = []
    secondResult = []
    thirdResult = []
    ws = create_connection(
        "wss://speedy-nodes-nyc.moralis.io/02799b1f72329a0eefa3b741/polygon/mainnet/ws")
    # for one in allPairs:

    #     allData.append({"jsonrpc":"2.0","method":"eth_call","params":[{"to": one["pair"], "data":"0x0902f1ac"}, "latest"],"id":one["pair"][0:10]})
    allData = ""
    json_data = dumps(allData).encode("utf-8")
    ws.send(json_data)

    results = ws.recv()
    if results:
        results = loads(results)
    else:
        results = ws.recv()
        results = loads(results)
    for item in allPairs:
        for sOne in results:
            if item["firstPair"][0:10] == sOne["id"]:
                reserve = decodeReserve(sOne["result"])
                if item["firstBase"] == 0:
                    firstReserve0 = reserve[0]
                    firstReserve1 = reserve[1]
                elif item["firstBase"] == 1:
                    firstReserve0 = reserve[1]
                    firstReserve1 = reserve[0]
                firstFee = item["firstFee"]
                firstResult.append({"id": item["id"], "reserve": (
                    firstReserve0, firstReserve1), "fee": firstFee})
                # print(f"{item['id']},{firstReserve0,firstReserve1,firstFee},first")

            elif item["secondPair"][0:10] == sOne["id"]:
                reserve = decodeReserve(sOne["result"])
                if item["secondBase"] == 0:
                    secondReserve0 = reserve[0]
                    secondReserve1 = reserve[1]
                elif item["secondBase"] == 1:
                    secondReserve0 = reserve[1]
                    secondReserve1 = reserve[0]
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
                    thirdFee = item["thirdFee"]
                    thirdResult.append({"id": item["id"], "reserve": (
                        secondReserve0, secondReserve1), "fee": secondFee})

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
                        print(
                            f"{row['id']},{row['reserve'],row['fee']},{elem['reserve'],elem['fee']},{item['reserve'],item['fee']}")


getReserve(allPairs)
# allData = {"jsonrpc":"2.0","method":"eth_call","params":[{"to": pairAddress, "data":"0x0902f1ac"}, "latest"],"id":5}
# json_data = dumps(allData).encode("utf-8")

# funcFor3("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1")
# funcFor3("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1")
