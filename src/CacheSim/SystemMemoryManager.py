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
        print('\nREAD {0:x}'.format(address))
        if self.cache.checkCache(address):
            print('HIT')
            print('Value {0:x}'.format(self.cache.getAddressValue(address)))

        else:
            print('MISS')
            #Write Back to main Memory if current row is dirty
            if self.cache.isDirty(address):
                # print("CACHE DIRTY Writing back to MM")
                cacheBlock = self.cache.getBlock(address)
                self.memory.writeBlock(cacheBlock)
            newRow = self.memory.getBlock(address)
            self.cache.insertBlock(newRow)
            print('Value {0:x}'.format(self.cache.getAddressValue(address)))


    def write(self, address, value):
        '''Writes to memory at the specified address and given value.  Will do
        some level of error checking,
        address: Must be in the range of the current memeory
        value: can not be larger than 8 bits'''
        print('\nWRITE {0:x}'.format(address))
        if self.cache.checkCache(address):
            print('HIT')
            self.cache.updateData(address, value)
            print('Value {0:x}'.format(self.cache.getAddressValue(address)))

        else:
            print('MISS')
            #Write Back to main Memory if current row is dirty
            if self.cache.isDirty(address):
                cacheBlock = self.cache.getBlock(address)
                self.memory.writeBlock(cacheBlock)
            newRow = self.memory.getBlock(address)
            self.cache.insertBlock(newRow)
            self.cache.updateData(address, value)
            print('Value {0:x}'.format(self.cache.getAddressValue(address)))

    def displayCache(self):
        '''As of wirting this i plan on just calling the cache __str__ method '''
        print(self.cache)
