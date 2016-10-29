# Designed by Andy OConnell <aoconnel@bu.edu> <andrewoconnell89@gmail.com>

from CacheSim.MainMemory import MainMemory
from CacheSim.Cache import Cache
from CacheSim.Cache import CacheRow

class SystemMemoryManager(object):
    def __init__(self):
        #Initalize Main memory and Cache
        self.memory = MainMemory(2048)
        self.cache = Cache(16)

    def read(self,address):
        '''Method returns the value in the given address.  It will
        check to see if the address is a hit in the cache and if not
        load it into the cache. '''

        if self.cache.checkCache(address):
            print('HIT {0:x}'.format(address))
            return self.cache.getAddressValue(address)
        else:
            print('MISS {0:x}'.format(address))

            #Write Back to main Memory if current row is dirty
            if self.cache.isDirty(address):
                print("CACHE DIRTY Writing back to MM")
                cacheBlock = self.cache.getBlock(address)
                self.memory.writeBlock(cacheBlock)

            newRow = self.memory.getBlock(address)
            self.cache.insertBlock(newRow)


    def write(self, address, value):
        '''Writes to memory at the specified address and given value.  Will do
        some level of error checking,
        address: Must be in the range of the current memeory
        value: can not be larger than 8 bits'''

        if self.cache.checkCache(address):
            print('HIT {0:x}'.format(address))
            self.cache.updateData(address, value)

        else:
            print('MISS {0:x}'.format(address))

            #Write Back to main Memory if current row is dirty
            if self.cache.isDirty(address):
                print("CACHE DIRTY Writing back to MM")
                cacheBlock = self.cache.getBlock(address)
                self.memory.writeBlock(cacheBlock)

            newRow = self.memory.getBlock(address)
            self.cache.insertBlock(newRow)
            self.cache.updateData(address, value)

    def displayCache(self):
        '''As of wirting this i plan on just calling the cache __str__ method '''
        print(self.cache)
