from json import dump, load
from allPairsWithOutreserve0AndBlacklist import allPairsWithOutreserve0AndBlacklist as pairsList
from whitelist import whitelist


fromList = [
    "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270",
    "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
    "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
    "0xc2132D05D31c914a87C6611C10748AEb04B58e8F"
]

def intoJsonFile(data):
    loading = []
    outfile = open('data.json', 'r')
    try:
        loading = load(outfile)
    except:
        loading = []
    loading.append(data)
    outfile = open('data.json', 'w')
    dump(loading, outfile)
    outfile.close()

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
    for elem in usedPairs:
        if elem not in filtredPairs:
            allData.append({"jsonrpc":"2.0","method":"eth_call","params":[{"to": elem, "data":"0x0902f1ac"}, "latest"],"id":elem[0:10]})

    finalResult = {fromAdd:{toAdd:{
        'probability':results,
        'request':allData
    }}}
    intoJsonFile(finalResult)

def executer():
    for item in whitelist:
        if item not in fromList:
            for item2 in fromList:
                func2(item,item2)

executer()