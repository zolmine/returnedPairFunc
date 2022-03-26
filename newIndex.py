
from allPairs import allPairs

def getReserve(allPairs):
    allData = []
    # ws = create_connection("wss://speedy-nodes-nyc.moralis.io/02799b1f72329a0eefa3b741/polygon/mainnet/ws")
    for one in allPairs:
        print(one) 
        allData.append({"jsonrpc":"2.0","method":"eth_call","params":[{"to": one["pair"], "data":"0x0902f1ac"}, "latest"],"id":one["pair"][0:10]})
    return allData



def functionOf3(place,baseAddr,tokenAddr,dex):
    totalPairList = []
    listWithoutMainPair = []
    results = []
# getting the mainPair Part ------------------------------------------------------------------------------------------------------------------------------
    for one in allPairs:
        # mainPair ---------------------------------------------------------------------------------------------------------------------------------------
        if one["dex"] == dex and (one["token0"] == baseAddr or one["token0"] == tokenAddr) and (one["token1"] == baseAddr or one["token1"] == tokenAddr):
            mainPair = one["pair"]
            if one["token0"] == baseAddr:
                firstBasePlace = 0
            else:
                firstBasePlace = 1
            mainPairfee = one["fee"]
            totalPairList.append(one["pair"])
        # a list Without mainPair and contain the tokenAddr -----------------------------------------------------------------------------------------------
        elif (one["token0"] == tokenAddr or one["token1"] == tokenAddr) and (one["token0"] != baseAddr and one["token1"] != baseAddr):
            listWithoutMainPair.append(one)
# getting the secondBaseAddr and the thirdPair----------------------------------------------------------------------------------------------------------
    
    # thirdPair ----------------------------------------------------
    for item in listWithoutMainPair:
        secondPair = item["pair"]
        secondPairFee = item["fee"]
        if item["token0"] == tokenAddr:
            secondBasePlace = 0
            secondBaseAddr = item["token1"]
        elif item["token1"] == tokenAddr:
            secondBasePlace = 1
            secondBaseAddr = item["token0"]

            for elem in allPairs:
                if (elem["token0"] == secondBaseAddr or elem["token0"] == baseAddr) and (elem["token1"] == secondBaseAddr or elem["token1"] == baseAddr):
                    if elem["token0"] == secondBaseAddr:
                        thirdBasePlace = 0
                    elif elem["token1"] == secondBaseAddr:
                        thirdBasePlace = 1
                    thirdPaireFee = elem["fee"]
                    totalPairList.append(secondPair)
                    totalPairList.append(elem['pair'])
    # print(totalPairList)
                    # print(f"{mainPair},{firstBasePlace},{secondPair},{secondBasePlace},{elem['pair']},{thirdBasePlace}")
                    results.append({"firstPair":mainPair,"firstBase":firstBasePlace,"firstFee":mainPairfee,"secondPair":secondPair,"secondBase":secondBasePlace,"secondFee":secondPairFee,"thirdPair":elem['pair'],"thirdBase":thirdBasePlace,"thirdFee":thirdPaireFee})
    totalPairList = list(dict.fromkeys(totalPairList))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
    print(results,totalPairList)
    # print("------------------------------------------------------------------------------------------------------------------------------")
# functionOf3("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1")


                        



def funcFor2(place,baseAddr,tokenAddr,dex):
    result = []
    newList = []
    for one in allPairs:
        if one["dex"] == dex and (one["token0"] == baseAddr or one["token0"] == tokenAddr) and (one["token1"] == baseAddr or one["token1"] == tokenAddr):
            mainPair = one["pair"]
            mainPairFee = one["fee"]
            if one["token0"] == baseAddr:
                basePlace = 0
            else:
                basePlace = 1

        elif one["dex"] != dex and (one["token0"] == baseAddr or one["token0"] == tokenAddr) and (one["token1"] == baseAddr or one["token1"] == tokenAddr):
                if one["token0"] == tokenAddr:
                    tokenAddrPlace = 0
                elif one["token1"] == tokenAddr:
                    tokenAddrPlace = 1
                secondPairFee = one["fee"]
                newList.append({"pair":one['pair'],"base":tokenAddrPlace,"fee":secondPairFee})
    
    for item in newList:
        result.append({"firstPair":mainPair,"firstBase":basePlace,"firstFee":mainPairFee,"secondPair":item['pair'],"secondBase":item['base'],"secondFee":item["fee"]})
    newList.append({"pair":mainPair,"base":basePlace,"fee":mainPairFee})
    request = getReserve(newList)
    print(request)
    return(result,request)


funcFor2("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1")




    # ws.send(json_data)
    
    # results = ws.recv()
    # if results:
    #     results = loads(results)
    # else:
    #     results = ws.recv()
    #     results = loads(results)
    
    # for item in allPairs:
    #     for sOne in results:
    #         if item["pair"][0:10] == sOne["id"]:
    #             reserve = decodeReserve(sOne["result"])
    #             if item["base"] == 0:
    #                 reserve0 = reserve[0]
    #                 reserve1 = reserve[1]
    #             elif item["base"] == 1:
    #                 reserve0 = reserve[1]
    #                 reserve1 = reserve[0]
    #             print(item, reserve0,reserve1)


# def functionOf4(place,baseAddr,tokenAddr,dex):
#     totalPairList = []
#     listWithoutMainPair = []
    
# # getting the mainPair Part ------------------------------------------------------------------------------------------------------------------------------
#     for one in allPairs:
#         # mainPair ---------------------------------------------------------------------------------------------------------------------------------------
#         if one["dex"] == dex and (one["token0"] == baseAddr or one["token0"] == tokenAddr) and (one["token1"] == baseAddr or one["token1"] == tokenAddr):
#             mainPair = one["pair"]
#             if one["token0"] == baseAddr:
#                 firstBasePlace = 0
#             else:
#                 firstBasePlace = 1
#             totalPairList.append(one["pair"])
#         # a list Without mainPair and contain the tokenAddr -----------------------------------------------------------------------------------------------
#         elif (one["token0"] == tokenAddr or one["token1"] == tokenAddr) and (one["token0"] != baseAddr and one["token1"] != baseAddr) and (one["token0"]  not in pirsList and one["token1"] not in pirsList):
#             listWithoutMainPair.append(one)
#     # the thirdPair ----------------------------------------------------------------------------------------------------------------------------------------
#     for item in listWithoutMainPair:
#         secondPair = item["pair"]
#         if item["token0"] == tokenAddr:
#             secondBasePlace = 0
#             secondBaseAddr = item["token1"]
#         elif item["token1"] == tokenAddr:
#             secondBasePlace = 1
#             secondBaseAddr = item["token0"]
#         # print(secondBaseAddr)
#         for elem in allPairs:
#             if (elem["token0"] == secondBaseAddr or elem["token1"] == secondBaseAddr) and (elem["pair"] != secondPair) and (elem["token0"] != baseAddr and elem["token1"] != baseAddr):
#                 if elem["token0"] == secondBaseAddr:
#                     thirdBaseAddr = elem["token1"]
#                     thirdBasePlace = 0
#                 elif elem["token1"] == secondBaseAddr:
#                     thirdBaseAddr = elem["token0"]
#                     thirdBasePlace = 1
#                 thirdPair = elem["pair"]
#                 for row in allPairs:
#                     if (row["token0"] == thirdBaseAddr or row["token0"] == baseAddr) and (row["token1"] == thirdBaseAddr or row["token1"] == baseAddr):
#                         print(f"{mainPair},{secondPair},{thirdPair},{row['pair']}")

# # functionOf4("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x2ed945Dc703D85c80225d95ABDe41cdeE14e1992","1")