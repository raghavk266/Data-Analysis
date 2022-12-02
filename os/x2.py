import os 
import urllib.request
url1 = 'https://hub.jovian.ml/wp-content/uploads/2020/08/loans1.txt'
url2 = 'https://hub.jovian.ml/wp-content/uploads/2020/08/loans2.txt'
url3 = 'https://hub.jovian.ml/wp-content/uploads/2020/08/loans3.txt'
urllib.request.urlretrieve(url1,'./os/loans1.txt')
urllib.request.urlretrieve(url2, './os//data/loans2.txt')
urllib.request.urlretrieve(url3, './os/loans3.txt')
