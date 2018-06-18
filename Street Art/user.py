from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
tokens = {}
tokens['app_id'] = '1268e9e0'
tokens['app_key'] = '391792356eb3274447255fe097527f29'
bdb = BigchainDB('https://test.bigchaindb.com', headers=tokens)

class user:

    def __init__(self, _username):
        self.keys = generate_keypair() # generates a public and private pair
        self.username = _username # sets username of the user

    def showPublic(self):
        return self.keys.public_key #returns the public key for a user which is their unique ID

    def showPrivate(self):
        return self.keys.private_key #returns the private key for the user which they should keep safe

    def getUsername(self):
        return self.username

    def createArt(self, name, location, imageHash): #creates an asset which represents a piece of art
        # creates storage of information about an art piece in a JSON format
        art = {
            'data' : {
                'name' : name,
                'location' : location,
                'image' : imageHash #hash of the image from IPFS - needs work
            }
        }

        # creates the transaction for the creation of the art asset
        creation_tx = bdb.transactions.prepare(
            operation='CREATE', #creating the asset
            signers=self.keys.public_key, #signed by the unique users ID
            asset=art #the data for the asset we are creating
        )
        return creation_tx # returns tx ID

    # finalises the creation of an asset by signing it with the creator's private key
    def signArt(self, createTx, privateKey):
        sign_creation_tx = bdb.transactions.fulfill(
            createTx, private_keys=privateKey) # takes the creation transaction id and signs it with the private key to finalise it
        sent_creation_tx = bdb.transactions.send_commit(sign_creation_tx) # sends transaction to BigChainDB node
        return sign_creation_tx, sent_creation_tx # returns tx IDs