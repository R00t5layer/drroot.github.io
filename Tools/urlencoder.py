import urllib.parse

query = str(input("Write the payload! => "))


print(urllib.parse.quote(query))
