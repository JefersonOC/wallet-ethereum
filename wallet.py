from web3 import Web3

url = "HTTP://127.0.0.1:7545"  # Ganache RPC server
web3 = Web3(Web3.HTTPProvider(url))


def get_balance(account):
    try:
        balance = web3.fromWei(web3.eth.getBalance(account), 'ether')
        data_set = {
            "address": str(account),
            "balance": str(balance),
        }
        return data_set
    except Exception as e:
        print("Wrong account number: " + str(e))
        return {}


def send_transfer(account, private_key, account_to, amount):
    try:
        nonce = web3.eth.getTransactionCount(account)

        tx = {
            'nonce': nonce,
            'to': account_to,
            'value': web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
        }

        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        balance = web3.fromWei(web3.eth.getBalance(account), 'ether')

        data_set = {
            "transaction": str(web3.toHex(tx_hash)),
            "balance": str(balance),
        }
        return data_set
    except Exception as e:
        print("Transaction failed: " + str(e))
        return {}
