import webbrowser
from cfgHandler import cfgInit

cfgObj = cfgInit('config.ini')

defaultDecision = cfgObj[2]
linkMax = int(cfgObj[3])


def viewLink(links): #add a ALL option in config to open all of the links
    if links:
        if len(links) >= 1:
            if defaultDecision == "None":
                d = input("There are more than 1 link to be displayed, do you want to open them in a webbrowser? ")
            elif defaultDecision == "Yes" or defaultDecision == "No":
                d = defaultDecision
        
            if d == "Yes" or d == "Y" or d == "y":
                i = 0
                for l in links:
                    webbrowser.open(l)
                    i += 1
                    if i == linkMax:
                        break
                    
            elif d == "No" or d == "N" or d == "n":
                print("Displaying links to the console: " + '\n')

              