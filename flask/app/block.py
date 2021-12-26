import os
import hashlib
import json

current_dir = os.curdir + "/flask/app/blocks/"

def generateHash(filename):
    file = open(current_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def getFiles():
    blocks = os.listdir( current_dir )
    return sorted([int(i) for i in blocks])

def blocksCheck():
    files = getFiles()
    response = []

    for file in files[1:]:
        data       = json.load( open( current_dir + str(file) ))['hash']
        prev_block = str( file - 1 )
        prev_hash = hashlib.md5( open( current_dir + prev_block, 'rb').read() ).hexdigest()
        
        if prev_hash == data:
            res = 'OK'
        else:
            res = 'Corrupted!'
        
        response.append([ prev_block, res ])

    return response
        

def writeBlock(name, amount, to_whom):
    
    files = getFiles()
    last_block = files[-1]

    new_block_name = str(last_block + 1)
    prev_hash = generateHash(str(last_block))

    data = {
        "name": name,
        "amount": amount,
        "to_whom": to_whom,
        "hash": prev_hash,
    }
    with open(current_dir + new_block_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        

def main():
    writeBlock("Ivan", 4, "Katya")


if __name__ == "__main__":
    main()
    blocksCheck()
