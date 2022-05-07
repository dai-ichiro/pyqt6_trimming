import os
from urllib.request import urlretrieve
url = 'https://raw.githubusercontent.com/dai-ichiro/pyqt6_yaml/main/qtyaml.py'
fname = os.path.basename(url)
if not os.path.isfile(fname):
    urlretrieve(url, fname)