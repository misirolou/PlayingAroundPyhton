Just some information needed for BlockChain.py

need Postman or something similar to do necessary GET and POST messages to server created using flask
need to have BlockChain.py to have access to localhost that is created during that process.

http://localhost:5000 is the host being used, this can be changed to what ever you feel like

For POST Request need to add body containing necessary information also make sure you are using JSON as the info sent
http://127.0.0.1:5000/transactions/new
Example: 
{
    "sender" : "d4ee26eee15148ee92c6cd394edd974e",
    "recipient" : "someone-other-address",
    "amount" : 5
}

For GET responses you simply try to receive the information needed
http://127.0.0.1:5000/mine : Used to mine information
http://127.0.0.1:5000/chain : Used to verify blocks created

For registering purposes, to do some verifications, allowing to register nodes all over the place through different posts or IPs
POST http://127.0.0.1:5000/nodes/register
Adding info in JSON format
Example:
{
    "nodes" : ["http://127.0.0.1:5001"]
}

For the Consensus algorithm we do a GET method
http://127.0.0.1:5000/nodes/resolve: Where we can replace the chains according to which one is longer depending on each node registered

''' Example of what a single block would look like and what it should contain
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}'''