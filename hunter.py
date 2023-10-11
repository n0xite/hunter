from webHandler import Search, WebInit
from queryHandler import queryResolver



#add A mode seleciton list or input mode. List mode gets names from config same as with links. List mode automatically turns off linkview


clean_name = ""



def Start():
    name = input("Full name: ")
    return name





def Main():
    queries = queryResolver(Start())

    Search(queries, WebInit())
    

    d = "Yes" #input("Do you want to look for someone else?: ") 

    if d == "Yes" or "Y" or "y":
        queries.clear()
        Main()
    elif d == "No" or "N" or "n":
        exit

Main()
