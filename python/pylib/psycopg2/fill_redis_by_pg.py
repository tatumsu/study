import psycopg2 as db
import redis

DB_NAME = 'victory_packaging'
DB_HOST = 'localhost'
DB_USER = 'postgres'

REDIS_HOST = 'localhost'

class Address:
    """Simple entitiy to represents an address"""
    def __init__(self, sid, identity, address, city, zipcode, state, country, latitude, longitude, telephone, fax):
        self.sid = sid
        self.identity = identity
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.state = state
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.telephone = telephone
        self.fax = fax

class AddressManager:
    """Provides to manage address entity"""
    @staticmethod
    def getAllAddress():
        conn = db.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER)
        cur = conn.cursor()
        statement = '''
        SELECT
            sid,
            identity,
            address_1 as address,
            city,
            zip as zipcod,
            state,
            country,
            latitude,
            longitude,
            telephone,
            fax
        FROM ods.common_entities_address
        WHERE mark_for_delete=false AND sid > 500000 AND sid < 600000
        '''
        cur.execute(statement)
        addresses = []
        for row in cur:
           address = Address(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
           addresses.append(address)

        conn.close()
        return addresses

addresses = AddressManager.getAllAddress()

r = redis.StrictRedis(host=REDIS_HOST)
for address in addresses:
    key = 'address:' + str(address.sid)
    r.hset(key, 'identity', address.identity)
    r.hset(key, 'address', address.address)
    r.hset(key, 'city', address.city)
    r.hset(key, 'zipcode', address.zipcode)
    r.hset(key, 'state', address.state)
    r.hset(key, 'country', address.country)
