from allPairsWithOutreserve0AndBlacklist import allPairsWithOutreserve0AndBlacklist as pairsList

def func1(fromAdd,toAdd):
    results = []
    for item in pairsList:
        if (fromAdd == item['token0'] or fromAdd == item['token1']) and (toAdd == item['token0'] or toAdd == item['token1']):
            if item['token0'] == fromAdd:
                base = 0
            elif item['token1'] == fromAdd:
                base = 1
            results.append({'pair':item['pair'],'base':base, 'fee':item['fee']})
    print(results)
    return results


def func2(fromAdd,toAdd):
    results = []
    for item in pairsList:
        if (toAdd == item['token0'] or toAdd == item['token1']):
            firstPair = item['pair']
            if item['token0'] == toAdd:
                firstBase = 0
                secondBaseAdd = item['token1']
            elif item['token1'] == toAdd:
                firstBase = 1
                secondBaseAdd = item['token0']
            firstFee = item['fee']
            print(secondBaseAdd)
            return True
            for item2 in pairsList:
                if (secondBase == item2['token0'] or toAdd == item2['token1']) and (fromAdd == item2['token0'] or fromAdd == item2['token1']):
                    secondPair = item2['pair']
                    if item2['token0'] == fromAdd:
                        secondBase = 0
                    elif item2['token1'] == fromAdd:
                        secondBase = 1
                    secondFee = item2['fee']
                    results.append({'firstPair':firstPair,'firstBase':firstBase, 'firstFee':firstFee,'secondPair':secondPair,'secondBase':secondBase, 'secondFee':secondFee})
    print(results)
    #         results.append({'pair':item['pair'],'base':base, 'fee':item['fee']})
    # print(results)
    # return results

func2("0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x172370d5Cd63279eFa6d502DAB29171933a610AF")