from websocket import create_connection
from json import loads,dumps
from lists import polyList

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