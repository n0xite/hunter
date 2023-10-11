import configparser





def cfgInit(cfgPath):
    config = configparser.ConfigParser()
    config.read(cfgPath)
    queryArray = config.get('QUERIES', 'mod')
    queryArray_clean = queryArray.split(",")
    delayMax = config.get('SETTINGS', 'DefaultDelayMax')
    defaultDecision = config.get('SETTINGS', 'DefaultDecision')
    linkMax = config.get('SETTINGS', 'LinkMax')
    #peopleArray = config.get('QUERIES', 'people')
    #peopleArray_clean = peopleArray.split("")
    return queryArray_clean, delayMax, defaultDecision, linkMax, #peopleArray_clean


