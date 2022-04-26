
from lists.allPairsWithOutreserve0AndBlacklist import allPairsWithOutreserve0AndBlacklist
from time import time



fromList = [
    "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270",
    "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
    "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
    "0xc2132D05D31c914a87C6611C10748AEb04B58e8F"
]

def func2(toAdd,fromAdd):
    usedPairs = []
    results = []
    filtredPairs = []
    allData = []
    for item in allPairsWithOutreserve0AndBlacklist:
        if (fromAdd == item['token0'] and toAdd == item['token1']) or (toAdd == item['token0'] and  fromAdd == item['token1'] ):
            if item['token0'] == fromAdd:
                base = 0
            elif item['token1'] == fromAdd:
                base = 1
            usedPairs.append(item['pair'])
            results.append({'P':item['pair'],'B':base, 'F':item['fee']})

        if (toAdd == item['token0'] or toAdd == item['token1']):
            firstPair = item['pair']
            if item['token0'] == toAdd:
                firstBase = 0
                secondBaseAdd = item['token1']
            elif item['token1'] == toAdd:
                firstBase = 1
                secondBaseAdd = item['token0']
            firstFee = item['fee']

            for item2 in allPairsWithOutreserve0AndBlacklist:
                if (item2['token0'] == secondBaseAdd and  item2['token1'] == fromAdd) or (item2['token0'] == fromAdd and item2['token1'] == secondBaseAdd ):
                    secondPair = item2['pair']
                    if item2['token0'] == secondBaseAdd:
                        secondBase = 0
                    elif item2['token1'] == secondBaseAdd:
                        secondBase = 1
                    secondFee = item2['fee']
                    usedPairs.append(item2['pair'])
                    usedPairs.append(item['pair'])
                    results.append({'P1':firstPair,'B1':firstBase, 'F1':firstFee,'P2':secondPair,'B2':secondBase, 'F2':secondFee})
    for elem in usedPairs:
        if elem not in filtredPairs:
            allData.append({"jsonrpc":"2.0","method":"eth_call","params":[{"to": elem, "data":"0x0902f1ac"}, "latest"],"id":elem[0:10]})
    if len(results):
        finalResult = {
            'probability':results,
            'request':allData
        }
        print(finalResult)
        return finalResult
start = time()*1000
func2("0x0B048D6e01a6b9002C291060bF2179938fd8264c","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270")
print((time()*1000)-start)