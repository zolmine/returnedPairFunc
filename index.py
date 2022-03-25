

from json import loads,dumps
from websocket import create_connection
from lists import t_172370d5Cd63279eFa6d502DAB29171933a610AF,t_2ed945Dc703D85c80225d95ABDe41cdeE14e1992,pairs,listToMade
# var = t_172370d5Cd63279eFa6d502DAB29171933a610AF
data = {
    "0x172370d5Cd63279eFa6d502DAB29171933a610AF" : t_172370d5Cd63279eFa6d502DAB29171933a610AF,
    "0x2ed945Dc703D85c80225d95ABDe41cdeE14e1992" : t_2ed945Dc703D85c80225d95ABDe41cdeE14e1992,
}
def funcFor2(place,baseAddr,tokenAddr,dex):
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
        for line in data[tokenAddr]:
            if line["pair"] != mainPair:
                newList.append(line)

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
        if place == "first":
            test = mainPair,basePlace,secondPair,tokenPlace
            # print(test)
            result.append(test)
            # print(f"{mainPair},{basePlace},{secondPair},{tokenPlace}")
        elif place == "last":
            test = mainPair,basePlace,secondPair,tokenPlace
            result.append(test)
    return result
            # print(f"{mainPair},{basePlace},{secondPair},{tokenPlace}")

# funcFor2(0,"0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1")
# funcFor2(1,"0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174","0x2ed945Dc703D85c80225d95ABDe41cdeE14e1992","1")

def funcFor3(place,baseAddr,tokenAddr,dex):
    pathOf2 = funcFor2(place,baseAddr,tokenAddr,dex)
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
            filtredResult.append({"pair":mainPair,"base":basePlace})
# ________________________________________________________________________________________________________________________________________
    if mainPair:
        for line in data[tokenAddr]:
            if line["pair"] != mainPair:
                newList.append(line)
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
        filtredResult.append({"pair":secondPair,"base":tokenPlace})
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
                    filtredResult.append({"pair":thirdPair,"base":tokenPlace3})
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
                test = mainPair,basePlace,secondPair,tokenPlace,item['pair'],thirdPairTokenPlace
                result.append(test)
                # print(f"{mainPair},{basePlace},{secondPair},{tokenPlace},{item['pair']},{thirdPairTokenPlace}")
            elif place == "last":
                test = mainPair,basePlace,secondPair,tokenPlace,item['pair'],thirdPairTokenPlace
                result.append(test)
                # print(f"{mainPair},{basePlace},{secondPair},{tokenPlace},{item['pair']},{thirdPairTokenPlace}")
# ____________________________________________________________________________________________________________________________________________
    
    print(filtredResult)
    # return(pathOf2,result)

allPairs = [{'pair': '0x634F9d9f8680349b518cb615017C105aF46CCFd2', 'base': 0}, {'pair': '0x396E655C309676cAF0acf4607a868e0CDed876dB', 'base': 0}, {'pair': '0xc4e595acDD7d12feC385E5dA5D43160e8A0bAC0E', 'base': 1}, {'pair': '0xadbF1854e5883eB8aa7BAf50705338739e558E5b', 'base': 1}, {'pair': '0x6Cf8654e85AB489cA7e70189046D507ebA233613', 'base': 1}, {'pair': '0x2FE46369b1C261Be62F9fD327ff5A9B17Ab0F451', 'base': 1}, {'pair': '0x679B8Ab80F298bF802fB294137765C6386D43dcA', 'base': 1}, {'pair': '0x982c529Fd47CBa8f627c2aBE30286c69aB593501', 'base': 0}, {'pair': '0x140EA3fae80A2732eBc4DE0511FF84EF1A575217', 'base': 1}, {'pair': '0x5F3EeCeeaD64ee34b78e80cD574496E82e537541', 'base': 0}, {'pair': '0x8982D71337003cd172198739238adA0D5d0BD2Fe', 'base': 0}, {'pair': '0xaB4F7A3199B2Cd7A8bFb425941EAd08FAcb6d617', 'base': 0}, {'pair': '0xF16ad36077422B7579814660b691Eac1eb73290b', 'base': 0}, {'pair': '0x2ec2fC0c682F351c9d322f392F60A7Ee440552E4', 'base': 0}, {'pair': '0x7433aFe84dF37d0954fF87D7F5788F124f8597F8', 'base': 1}, {'pair': '0x8bf34FF5945d519cf3EB4360e97585605C99DaA6', 'base': 0}, {'pair': '0x39A9B6474db467C2874DB622a0e048013489501c', 'base': 0}, {'pair': '0x3a8A6831a1E866C64Bc07c3dF0f7B79ac9Ef2fA2', 'base': 0}, {'pair': '0xCF8172441b953e9609C425FCE91B32BE780FDFBD', 'base': 0}, {'pair': '0xD8D7030b88144c9984bfFbB09364384eE875Dc46', 'base': 0}, {'pair': '0x32398C45A6D9772BE73596242174744F26914E7b', 'base': 0}, {'pair': '0xfEC6F467B2eE93a0Bafb580784314A1001219581', 'base': 1}]

def decodeReserve(input):

        rererve0 = int(input[2:66],16)
        rererve1 = int(input[66:130],16)
        return(rererve0,rererve1)

def reservePlacement(reserve):
    print


def getReserve(allPairs):
    allData = []
    ws = create_connection("wss://speedy-nodes-nyc.moralis.io/02799b1f72329a0eefa3b741/polygon/mainnet/ws")
    for one in allPairs:
        
        allData.append({"jsonrpc":"2.0","method":"eth_call","params":[{"to": one["pair"], "data":"0x0902f1ac"}, "latest"],"id":one["pair"][0:10]})
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
            if item["pair"][0:10] == sOne["id"]:
                reserve = decodeReserve(sOne["result"])
                if item["base"] == 0:
                    reserve0 = reserve[0]
                    reserve1 = reserve[1]
                elif item["base"] == 1:
                    reserve0 = reserve[1]
                    reserve1 = reserve[0]
                print(item, reserve0,reserve1)
        # print(item)
    # json_data = dumps(allData).encode("utf-8")

getReserve(allPairs)
# allData = {"jsonrpc":"2.0","method":"eth_call","params":[{"to": pairAddress, "data":"0x0902f1ac"}, "latest"],"id":5}
# json_data = dumps(allData).encode("utf-8")

# funcFor3("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1")
# funcFor3("first","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF","1")
