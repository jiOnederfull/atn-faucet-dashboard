import requests

item_list = [
        {"type":"ethereum",     "protocol":"ethereum_goerli",    "url":"https://ethereum-goerli-rpc.allthatnode.com",               "address":"0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"},
        {"type":"ethereum",     "protocol":"ethereum_sepolia",   "url":"https://ethereum-sepolia-rpc.allthatnode.com",              "address":"0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"},
        {"type":"cosmos",       "protocol":"osmosis",            "url":"https://osmosis-testnet-rpc.allthatnode.com:1317",          "address":"osmo12xt4x49p96n9aw4umjwyp3huct27nwr2qws2hc"},
        {"type":"cosmos",       "protocol":"agoric",             "url":"https://agoric-devnet-rpc.allthatnode.com:1317",            "address":"agoric12xt4x49p96n9aw4umjwyp3huct27nwr26gp93u"},
        {"type":"cosmos",       "protocol":"archway",            "url":"https://archway-torii-rpc.allthatnode.com:1317",            "address":"archway12xt4x49p96n9aw4umjwyp3huct27nwr2a7l7ta"},
        {"type":"ethereum",     "protocol":"avalanche_fuji",     "url":"https://avalanche-fuji-rpc.allthatnode.com/ext/bc/C/rpc",   "address":"0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"},
        {"type":"cosmos",       "protocol":"axelar_lisbon",      "url":"https://axelar-lisbon-rpc.allthatnode.com:1317",            "address":"axelar12xt4x49p96n9aw4umjwyp3huct27nwr2vm4j2t"},
        {"type":"cosmos",       "protocol":"axelar_casablanca",  "url":"https://axelar-casablanca-rpc.allthatnode.com:1317",        "address":"axelar12xt4x49p96n9aw4umjwyp3huct27nwr2vm4j2t"},
        {"type":"ethereum",     "protocol":"celo_alfajores",     "url":"https://celo-alfajores-rpc.allthatnode.com",                "address":"0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"},
        {"type":"cosmos",       "protocol":"cosmos",             "url":"https://cosmos-testnet-rpc.allthatnode.com:1317",           "address":"cosmos12xt4x49p96n9aw4umjwyp3huct27nwr2g4r6p2"},
        {"type":"ethereum",     "protocol":"klaytn_baobab",      "url":"https://klaytn-baobab-rpc.allthatnode.com:8551",            "address":"0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"},
        {"type":"near",         "protocol":"near",               "url":"https://near-testnet-rpc.allthatnode.com:3030",             "address":"9bfd12934cd6fdd09199e2e267803c70bd7c6cb40832ac6f29811948dde2b723"},
        {"type":"cosmos",       "protocol":"persistence",        "url":"https://persistence-testnet-rpc.allthatnode.com:1317",      "address":"persistence12xt4x49p96n9aw4umjwyp3huct27nwr2xe9f0w"},
        {"type":"ethereum",     "protocol":"polygon_mumbai",     "url":"https://polygon-testnet-rpc.allthatnode.com:8545",          "address":"0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"},
        {"type":"cosmos",       "protocol":"sei",                "url":"https://sei-testnet-rpc.allthatnode.com:1317",              "address":"sei12xt4x49p96n9aw4umjwyp3huct27nwr29ejv8t"},
        {"type":"cosmos",       "protocol":"shentu",             "url":"https://shentu-yulei-rpc.allthatnode.com:1317",             "address":"certik12xt4x49p96n9aw4umjwyp3huct27nwr20aldqp"},
        # {"type":"cosmos",       "protocol":"tgrade",             "url":"https://tgrade-dryrunnet-rpc.allthatnode.com:1317",         "address":"tgrade15uf7krq9xs8l9ajsufwma4d6ejdvu9l6s8egd3"},
]

#####################################################################

def ethereum(protocol, url, address):
    try:
        session = requests.Session()
        headers = {'Content-type': 'application/json'}
        
        method = 'eth_getBalance'   
        params = [address, "latest"]

        payload= {"jsonrpc":"2.0", "method":method, "params":params, "id":1}
        
        response = session.post(url, json=payload, headers=headers)
        
        raw = response.json()
        balance_raw = raw['result']

        balance_float = int(balance_raw, 16) * 10e-19
        
        return balance_float
    except:
        balance_float = None
        return balance_float


def cosmos(protocol, url, address):
    try:
        session = requests.Session()

        url_final = "{}/cosmos/bank/v1beta1/balances/{}".format(url, address)
        
        response = session.get(url_final)

        raw = response.json()
        balance_raw = raw['balances']
        
        if protocol == 'sei':
            balance_float = int(balance_raw[2]['amount']) * 10e-7
        else: 
            balance_float = int(balance_raw[0]['amount']) * 10e-7
        
        return balance_float
    except:
        balance_float = None
        return balance_float
    

def near(protocol, url, address):
    try:
        session = requests.Session()
        headers = {'Content-type': 'application/json'}
        
        method = 'query'
        params = {"request_type": "view_account", "finality": "final", "account_id": address}

        payload= {"jsonrpc":"2.0", "method":method, "params":params, "id":"dontcare"}

        response = session.post(url, json=payload, headers=headers)
        
        raw = response.json()
        balance_raw = raw['result']

        balance_float = int(balance_raw['amount']) * 10e-25

        return balance_float
    except:
        balance_float = None
        return balance_float


#####################################################################

for item in item_list:
    _type = item["type"]
    protocol = item["protocol"]
    url = item["url"]
    address = item["address"]
    # print(_type, protocol, url, address)
    
    if _type == "ethereum":
        result = ethereum(protocol, url, address)
    elif _type == "cosmos":
        result = cosmos(protocol, url, address)
    elif _type == "near":
        result = near(protocol, url, address)
    else:
        print("Check the type of protocol")

    try:
        print("{}".format(protocol),f'{result:.2f}')
    except:
        pass
