from bigchaindb_driver import BigchainDB
tokens = {}
tokens['app_id'] = '1268e9e0'
tokens['app_key'] = '391792356eb3274447255fe097527f29'
bdb = BigchainDB('https://test.bigchaindb.com', headers=tokens)

class queries:

    def searchtag(tag):
        results = bdb.assets.get(search=tag)
        return results