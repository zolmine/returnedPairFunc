from websocket import create_connection
from allPairsWithOutreserve0AndBlacklist import allPairsWithOutreserve0AndBlacklist as pairsList

# def func1(fromAdd,toAdd):
    
#     results = []
#     for item in pairsList:
#         if (fromAdd == item['token0'] or fromAdd == item['token1']) and (toAdd == item['token0'] or toAdd == item['token1']):
#             if item['token0'] == fromAdd:
#                 base = 0
#             elif item['token1'] == fromAdd:
#                 base = 1
#             results.append({'pair':item['pair'],'base':base, 'fee':item['fee']})
#     print(results)
#     return results


def func2(toAdd,fromAdd):
    usedPairs = []
    results = []
    filtredPairs = []
    allData = []
    for item in pairsList:
        if (fromAdd == item['token0'] or fromAdd == item['token1']) and (toAdd == item['token0'] or toAdd == item['token1']):
            if item['token0'] == fromAdd:
                base = 0
            elif item['token1'] == fromAdd:
                base = 1
            usedPairs.append(item['pair'])
            results.append({'pair':item['pair'],'base':base, 'fee':item['fee']})

        if (toAdd == item['token0'] or toAdd == item['token1']):
            firstPair = item['pair']
            if item['token0'] == toAdd:
                firstBase = 0
                secondBaseAdd = item['token1']
            elif item['token1'] == toAdd:
                firstBase = 1
                secondBaseAdd = item['token0']
            firstFee = item['fee']
            usedPairs.append(item['pair'])
            # print(secondBaseAdd)
            # return True
            for item2 in pairsList:
                if (secondBaseAdd == item2['token0'] or secondBaseAdd == item2['token1']) and (fromAdd == item2['token0'] or fromAdd == item2['token1']):
                    secondPair = item2['pair']
                    if item2['token0'] == secondBaseAdd:
                        secondBase = 0
                    elif item2['token1'] == secondBaseAdd:
                        secondBase = 1
                    secondFee = item2['fee']
                    usedPairs.append(item2['pair'])
                    results.append({'firstPair':firstPair,'firstBase':firstBase, 'firstFee':firstFee,'secondPair':secondPair,'secondBase':secondBase, 'secondFee':secondFee})
    # print(results)
    for elem in usedPairs:
        if elem not in filtredPairs:
            allData.append({"jsonrpc":"2.0","method":"eth_call","params":[{"to": elem, "data":"0x0902f1ac"}, "latest"],"id":elem[0:10]})
    ws = create_connection("wss://speedy-nodes-nyc.moralis.io/02799b1f72329a0eefa3b741/polygon/mainnet/ws")
    ws.send(str(allData))
    print(ws.recv())
    # print(filtredPairs)

func2("0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0xBbba073C31bF03b8ACf7c28EF0738DeCF3695683")