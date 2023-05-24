import sys
import importJSON
import AO3search
import time
import pdb

if len(sys.argv) < 3:
    sys.exit('Usage: %s JSONfile csvfile [-verbose]' % sys.argv[0])

verbose = False

if len(sys.argv) > 3:
    arg = sys.argv[3]
    if arg == "-verbose" or arg == "-v":
        verbose = True

jsonfile = sys.argv[1]
csvfile = sys.argv[2]

fo = open(csvfile, "w")

searchList = importJSON.importFile(jsonfile, False)

# assume that all the searches have the same headers
searchList[0].printCSVHeaders(fo)

for s in searchList:
#    pdb.set_trace()
    if verbose:
        print("Pausing so as not to DOS AO3...")
    
    time.sleep(1.8)


    s.createSearchURL()
#    pdb.set_trace()
    try: 
        tmp = s.searchURL.decode('utf-8')
        s.searchURL = tmp
        if verbose:
            print("SUCCESS: decode URL")
    except:
        if verbose:
            print("FAIL: decode URL")

    if verbose:
        print(s.searchURL)
    s.getNumWorks(True)
#    pdb.set_trace()
    s.getTopInfo()
    if verbose:
        s.printAll()
    s.printCSV(fo)

fo.close()
