# Designed by Andy OConnell <aoconnel@bu.edu> <andrewoconnell89@gmail.com>

from CacheSim.CacheRow import CacheRow

class MainMemory(object):
    def __init__(self, size):
        self.size = size

        #Creates the Memeory blocks
        self.mm = []
        for row in range(self.size):
            row = row & 0b000011111111
            self.mm.append(row)

    def getBlock(self, address):
        '''Enter an address of memory that needs to be retrieved from main memory
            The method will determine what block the address is and load it and
            return back the CacheRow object to the SystemMemoryManager

            EX.  cache.getBlock(x01F)'''
        #Get Starting memory location
        startMemMASK = 0b111111110000
        startMem = startMemMASK & address

        addressSlot =  (0b000011110000 & address) >> 4
        addressTag =   (0b111100000000 & address) >> 8
        cr = CacheRow(16, slot=addressSlot, tag=addressTag, valid=1)

        cursor = startMem
        for i in range(len(cr.data)):
            cr.data[i] = self.mm[cursor]
            cursor += 0b000000000001
        return cr

    def getData(self,address):
        '''Return the value of the byte in the given address ''' 
        return self.mm[address]

    def display(self):
        """WARNING: this will print out the number of rows in the
        memory object"""
        for mem in self.mm:
            print( '{0:x}'.format(mem) )
