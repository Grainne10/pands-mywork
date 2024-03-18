import json
FILENAME ="testdict.json" 

def readDICT():
    # this will throw an error if the files does not exist

    # it should readily just return and empty dict
    # we can do this later
    with open(FILENNAME) as f:
        return json.load(f)
    
    # test the function
    somedict = readDict()
    print(somedict)