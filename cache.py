from lru_cache.lru_cache_distributed import LRUCacheDistributed

def load_callback(key):
    """This function has the responsibility to load the content 
       to store into the cache
    """
    return key

local_cache = LRUCacheDistributed(
    load_callback=load_callback,
    maximum_capacity=3333,
    expiration_time=3600,
    connection_timeout=3600,
    remote_address=('192.168.1.1', '5352'),  # to be a client
    local_address=('', '9090')  # to be a server
)

# get data from the cache; it will call `load_callback` if the 
# value is not available
data_from_cache = local_cache.get('key')

# set data manually into the cache
data_from_cache = local_cache.set('key', 'value')