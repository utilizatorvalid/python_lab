# 4. Odata pornint server-ul de la punctul 3, sa se extraga numele fisierelor .txt si sa se afiseze in consola.
import urllib
from urllib import request
import re

url = 'http://127.0.0.1:6996/'

txt = re.compile('<a href=\"[^\"]+\">([A-Za-z0-9\s]+.txt)')

try:
    response = urllib.request.urlopen(url).read().decode('utf-8')

    # print(response)
    txt_files = txt.findall(response)
    print("text files are:", txt_files)
except Exception as e:
    print("Error->", e)
