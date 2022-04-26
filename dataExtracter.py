var = {
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "pending": {
            "0x0015ed09a4E97FCaAa762ccb9C8c7D84FE10C886": {
                "13440": {
                    "blockHash": "null",
                    "blockNumber": "null",
                    "from": "0x0015ed09a4e97fcaaa762ccb9c8c7d84fe10c886",
                    "gas": "0xe5650",
                    "gasPrice": "0x12c",
                    "hash": "0x0d775c04268f4aca594ce9440de347447cf3695169ceaabe81aed37592a06797",
                    "input": "0x1de9c8810000000000000000000000000000000000000000000000003e3f8a30c0939a000000000000000000000000000000000000000000000000003e3f8a30c69ed7c200000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000040015000f6003c000000000000000000000000000000000000000000000000000000000000000300000000000000000000000075f44b732e12d556f4398c57de621845fbd33c97000000000000000000000000a4819aa1493e1c7257af2a7a5667d415f3c9f7200000000000000000000000005e58e0ced3a272caeb8ba00f4a4c2805df6be495",
                    "nonce": "0x3480",
                    "to": "0x820ef56b0817edf37353bd5e8bed25f35b310cb3",
                    "transactionIndex": "null",
                    "value": "0x0",
                    "type": "0x0",
                    "v": "0x136",
                    "r": "0x62c3ba6981092568d7bd6ab22aef7b051d099c06a0331be139a307b030e91033",
                    "s": "0x5fc64bd89ab55cb0693e0abe9bcdb7fdfed6c1aba784122da3c3f7251ce375e2"
                }
            },
            "0x03E7AbA583E228767E3d554f713CD4E57603ecc7": {
                "12": {
                    "blockHash": "null",
                    "blockNumber": "null",
                    "from": "0x03e7aba583e228767e3d554f713cd4e57603ecc7",
                    "gas": "0xe6bb",
                    "gasPrice": "0x6f0dcf3f6",
                    "maxFeePerGas": "0x6f0dcf3f6",
                    "maxPriorityFeePerGas": "0x6f0dcf3e8",
                    "hash": "0xcb59a467d28ea21610f96b552baac2f766d6289d3c717d6165a6f9b340756130",
                    "input": "0x095ea7b300000000000000000000000025a751bfb51560c2aadf4250de0730eb4eea50c400000000000000000000000000000000000000000000000000000000040d9900",
                    "nonce": "0xc",
                    "to": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
                    "transactionIndex": "null",
                    "value": "0x0",
                    "type": "0x2",
                    "accessList": [],
                    "chainId": "0x89",
                    "v": "0x0",
                    "r": "0x6dcae968342a5c6cf2e2e0d6d69edf12dddf6cd0401d98393a707616dff683d1",
                    "s": "0x1cf9a9352cb6f4b2148d2c58b7d6a6af05ebbbbe6463659e0bd458f9240e08d0"
                }
            }
        }
    }
}


# print(var["result"]["pending"][0])
for one in var["result"]["pending"]:
    print(one)