from email.mime import base
from allPairs import allPairs

def functionOf3(place,baseAddr,tokenAddr,dex):
    filtredResult = []
    listWithoutMainPair = []
# getting the mainPair Part ------------------------------------------------------------------------------------------------------------------------------
    for one in allPairs:
        # mainPair ---------------------------------------------------------------------------------------------------------------------------------------
        if one["dex"] == dex and (one["token0"] == baseAddr or one["token0"] == tokenAddr) and (one["token1"] == baseAddr or one["token1"] == tokenAddr):
            mainPair = one["pair"]
            if one["token0"] == baseAddr:
                basePlace = 0
            else:
                basePlace = 1
            filtredResult.append({"pair":mainPair,"base":basePlace})
        # a list Without mainPair and contain the tokenAddr -----------------------------------------------------------------------------------------------
        elif (one["token0"] == tokenAddr or one["token1"] == tokenAddr) and (one["token0"] != baseAddr or one["token1"] == baseAddr):
            if one["token0"] == tokenAddr:
                tokenPlace = 0
            elif one["token1"] == tokenAddr:
                tokenPlace = 1
            filtredResult.append({"pair":one["pair"],"base":tokenPlace})
            listWithoutMainPair.append(one)
# getting the secondBaseAddr and the thirdPair
    getInThirdFor = True
    for item in listWithoutMainPair:
        secondPair = item["pair"]
        if item["token0"] == tokenAddr:
            secondBaseAddr = item["token1"]
        elif item["token1"] == tokenAddr:
            secondBaseAddr = item["token0"]
        # print(f"{baseAddr},{secondBaseAddr}")
        if getInThirdFor == True:
            for elem in allPairs:
                if (elem["token0"] == secondBaseAddr or elem["token0"] == baseAddr) and (elem["token1"] == secondBaseAddr or elem["token1"] == baseAddr):
                    print(f"{mainPair},{secondPair},{elem['pair']}")
                # print(elem)
    # print(filtredResult)
    # print("------------------------------------------------------------")
    # print(listWithoutMainPair)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------

functionOf3("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1")