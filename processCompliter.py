from websocket import create_connection
from json import loads,dumps
from lists import polyList
from calc import find_x_and_w,w1,w2

def decodeReserve(input):

    rererve0 = int(input[2:66], 16)
    rererve1 = int(input[66:130], 16)
    return(rererve0, rererve1)


def getReserve(tokenAdd):
    finalResultD = []
    firstResult = []
    secondResult = []
    thirdResult = []
    ws = create_connection(
        "wss://speedy-nodes-nyc.moralis.io/02799b1f72329a0eefa3b741/polygon/mainnet/ws")
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
    finalShit = []
    for i in finalResultD:
        if i not in finalShit:
            if "third" in i:
                # print(i["first"][0][0])
                firstReserve0 = i["first"][0][0]
                firstReserve1 = i["first"][0][1]
                secondReserve0 = i['second'][0][0]
                secondReserve1 = i['second'][0][1]
                thirdReserve0 = i['third'][0]
                print(firstReserve0,firstReserve1)
                # find_x_and_w(w2, A=11000, B=10000, fee1=5, C=10000,
                # D=9000, fee2=14, E=9200, F=12500, fee3=26)
            finalShit.append(i)

    # print(list(set.fromkeys(finalResultD)))
getReserve("0x172370d5Cd63279eFa6d502DAB29171933a610AF")