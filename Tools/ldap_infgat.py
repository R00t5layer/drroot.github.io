#pip3 install ldap3
import ldap3
server = ldap3.Server('10.10.11.168', get_info = ldap3.ALL, port =636, use_ssl = False) #can change to use_ssl = True
connection = ldap3.Connection(server)
connection.bind()

connection.search(search_base='DC=scrm,DC=local', search_filter='(&(objectClass=*))', search_scope='SUBTREE', attributes='*')
#connection.search('DC=scrm,DC=local', '(objectclass=*)')

print(connection.entries)

