##Higher level class to that is given a cache and mainMemory
from CacheSim.SystemMemoryManager import SystemMemoryManager


smm = SystemMemoryManager()

# smm.write(0x7A2,0xFF)
# smm.displayCache()

#Test the Sample output
with open('TrialInput.txt', 'r') as f:
    cursor = str.strip(f.readline())
    while cursor != '':
        if cursor == 'R':
            cursor = str.strip(f.readline())
            tmpAddress = int(cursor, 16)
            smm.read(tmpAddress)
        elif cursor == 'W':
            cursor = str.strip(f.readline())
            tmpAddress = int(cursor, 16)
            cursor = str.strip(f.readline())
            tmpData = int(cursor, 16)
            print(tmpAddress, tmpData)
            smm.write(tmpAddress,tmpData)
        elif cursor == 'D':
            smm.displayCache()

        #Load up the next line from the file
        cursor = str.strip(f.readline())
