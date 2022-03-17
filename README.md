# wallet-ethereum
A Simple Wallet which enables users to check balance, receive and send ether to accounts on the blockchain.
## Desenvolvedor
Jeferson Cruz
## Tecnologia
Python
## Endpoints
> [GET] 
http://127.0.0.1:5000/health

> [GET] 
http://127.0.0.1:5000/balance?account=0x

> [POST] 
http://127.0.0.1:5000/transfer
## Usage
```
curl http://127.0.0.1:5000/health

curl http://127.0.0.1:5000/balance?account=0xc6029C825205AAB6Aa303b30bfdE945869930AC6

curl --location --request POST '127.0.0.1:5000/transfer' \
--header 'Content-Type: application/json' \
--data-raw '{
    "account": "0xc6029C825205AAB6Aa303b30bfdE945869930AC6",
    "private": "7a8a54ee6ea2dbcf0bf7b5d456b7269dcec0233822e40602cde9e8db7b58766b",
    "to": "0xe3030EDe42ce7eAD7daB6736d7EadbBaAfCf00be",
    "amount": "10"
}'
```

