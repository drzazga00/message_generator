import re

client_id = '23232'
#link = input('link: ')

link = 'https://helion.pl/kategorie/programowanie'

first = link[:18]
second = link[18:]

excepts = ['/ksiazki/', '/kategorie/']


for i in excepts:
    match = re.search(i, link)

if match:
    print('found'), match.group()
else:
    print('did not found')

if link == 'http://helion.pl/':
    glowna = 'https://helion.pl/view/' + client_id
    print(glowna)


##    
##if '/ksiazki/' in link:
##    #glowna = first + client_id +
##    link=re.sub('ksiazki', 'view/' + client_id, link)
##    
##if '/kategorie/' in link:
##    linkk = first + 'page/' + client_id + "/" + second
##
##if

##str = 'an example word:cat!!'
##
##match = re.search(r'word:www', str)
##
##
##if match:                      
##    print('found'), match.group()
##
##else:
##    print('did not find')
