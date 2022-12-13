import requests

session = requests.Session()
method = 'eth_getBalance'
headers = {'Content-type': 'application/json'}

info = {"ethereum_goerli":["https://ethereum-goerli-rpc.allthatnode.com", "0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"],
        "ethereum_sepolia":["https://ethereum-sepolia-rpc.allthatnode.com", "0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"],
        "avalanche_fuji":["https://avalanche-fuji-rpc.allthatnode.com/ext/bc/C/rpc", "0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"],
        "celo_alfajores":["https://celo-alfajores-rpc.allthatnode.com", "0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"],
        "klaytn_baobab":["https://klaytn-baobab-rpc.allthatnode.com:8551", "0x08505F42D5666225d5d73B842dAdB87CCA44d1AE"],}

for key, value in info.items():
    protocol = key
    url = value[0]
    address = value[1]

    params = [address, "latest"]
    payload= {"jsonrpc":"2.0", "method":method, "params":params, "id":1}

    response = session.post(url, json=payload, headers=headers)

    raw = response.json()
    balance_raw = response.json()['result']
    balance_int = int(balance_raw, 16)
    balance_float = balance_int * 10e-19

    print("{}".format(protocol),f'{balance_float:.2f}')
