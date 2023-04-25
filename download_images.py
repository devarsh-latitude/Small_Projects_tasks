import pandas as pd
import concurrent.futures

import requests

import time

start = time.time()
data = pd.read_excel('/home/devarsh/Downloads/example_urls.xlsx')
# print(list(data['Links']))


# imgs = list(data['Links'])
# names = list(data['Name'])

def downloadFile(url,name):
    print(f"Started Downloading {name}")
    response= requests.get(url)
    open(f"files/example{name}.png","wb").write(response.content)
    print(f"Finished Downloading {name}")

# icount=1
# for imgurl,name in zip(imgs,names):
#     downloadFile(imgurl,name)

with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = list(data['Links'])
  l2 = list(data['Name'])
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)

end = time.time()

print(end-start)