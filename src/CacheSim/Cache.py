# Designed by Andy OConnell <aoconnel@bu.edu> <andrewoconnell89@gmail.com>

from CacheSim.CacheRow import CacheRow

class Cache(object):
    """
    Cache object simulates the running cache with several methods

        getAddressValue(self, address)
            returns value of data at given address

        checkCache(self,address)
            checks to see if given address is in the cache

        insertBlock((self, cacheRowObject)
            insert given cacheRow into cache at appropiate row

        updateData(self, address, value)
            updated given address with new data value
    """

    def __init__(self, size):
        self.slots = []

        #creates the 16 slows 0-F
        for row in range(size):
            self.slots.append(CacheRow(slot=row))

    def getAddressValue(self,address):
        '''Returns the value at the specified address '''
        slot = (0b000011110000 & address) >> 4
        offset = (0b000000001111 & address)
        return self.slots[slot].data[offset]

    def checkCache(self,address):
        '''Check the current Cache to see if there is a cache hit for a given
        memory address.  The method will return back a boolean True or False
        True: There was a Cache hit
        False: There was a Cache Miss '''

        #Get Slot number
        slotMASK = 0b000011110000
        slot = (slotMASK & address) >> 4
        #print('Slot: ' + str(slot))

        #Get Tag
        tagMASK = 0b111100000000
        tag = (tagMASK & address) >> 8
        #print('Tag: ' + str(tag))

        #get Offset
        offsetMASK = 0b000000001111
        offset = (offsetMASK & address)
        #print('Offset: ' + str(offset))

        #Check if the current slow with the slot of input address is valid
        # and then check if the tag matches up
        if self.slots[slot].valid == 1:
            if self.slots[slot].tag == tag:
                return True
        else:
            return False

    def isDirty(self,address):
        '''checks to see if cacheRow is dirty or not'''
        #Get Slot number
        slotMASK = 0b000011110000
        slot = (slotMASK & address) >> 4
        return self.slots[slot].dirty

    def getBlock(self,address):
        '''returns current cache row object that is associated
        with the current slot of the given address'''
        #Get Slot number
        slotMASK = 0b000011110000
        slot = (slotMASK & address) >> 4
        return self.slots[slot]

    def insertBlock(self, cacheRowObject):
        '''Inset the new cache row to it's appropiate slot tags label as well as the
        valid bit set to 1 '''
        self.slots[cacheRowObject.slot] = cacheRowObject

    def updateData(self, address, value):
        #Get Slot number
        slotMASK = 0b000011110000
        slot = (slotMASK & address) >> 4
        #print('Slot: ' + str(slot))

        #get Offset
        offsetMASK = 0b000000001111
        offset = (offsetMASK & address)
        #print('Offset: ' + str(offset))

        #Adds new datavalue as specified slot and offest
        #sets dirty bit to True
        self.slots[slot].data[offset] = value
        self.slots[slot].dirty = True

    def __str__(self):
        header = '\n{0:>6}'+\
                '{1:>6}'+\
                '{2:>6}'+\
                '{3:>6}'+\
                '{4:>10}\n'
        toReturn = header.format('Slot','Valid','Tag', 'Dirty', 'Data')
        toReturn += '---------------'+\
                    '----------------'+\
                    '----------------'+\
                    '--------------------------\n'


        for row in self.slots:
            toReturn += str(row)+'\n'
        return toReturn
