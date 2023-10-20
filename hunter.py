from webHandler import Search, WebInit
from queryHandler import queryResolver




clean_name = ""



def Start():
    name = input("Full name: ")
    return name





def Main():
    queries = queryResolver(Start())

    Search(queries, WebInit())
    

input("Do you want to look for someone else?: ") 

    if d == "Yes" or "Y" or "y":
        queries.clear()
        Main()
    elif d == "No" or "N" or "n":
        exit

Main()
