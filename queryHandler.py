from cfgHandler import cfgInit


cfgObj = cfgInit('config.ini')
queries = []


def queryResolver(name):
    clean_name = " ".join(name.split())
    cArray = cfgObj[0]
    for c in cArray:
        mQuery = '"' + clean_name + '" ' + c.strip(" ")
        queries.append(mQuery)
    return queries