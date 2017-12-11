#python 2.7 script: write data to csv,each list map to a column

import csv
from itertools import izip_longest
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['f', 'g', 'i', 'j']
combinelist = [list1, list2]
export_data = izip_longest(*combinelist, fillvalue = '') #make both length = max(list1,list2)

#note:python2: open('output.csv', 'wb') equal to python3:open('output.csv', 'w',newline='')
with open('output.csv', 'wb') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(['List1', 'List2'])#first row
      wr.writerows(export_data)
myfile.close()
