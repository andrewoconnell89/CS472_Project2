##Higher level class to that is given a cache and mainMemory
from CacheSim.SystemMemoryManager import SystemMemoryManager

def main():
    smm = SystemMemoryManager()

    # smm.write(0x1A2,0xFF)
    # smm.displayCache()
    #
    # smm.read(0x2A2)
    # smm.displayCache()
    # print('{0:x}'.format(smm.memory.mm[0x1A1]))
    # print('{0:x}'.format(smm.memory.mm[0x1A2]))
    # print('{0:x}'.format(smm.memory.mm[0x1A3]))

    runFromFile(smm, 'SampleInput.txt')

def runFromFile(smm, fileName):
    #Test the Sample output
    with open(fileName, 'r') as f:
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

if __name__ == '__main__':
    main()
