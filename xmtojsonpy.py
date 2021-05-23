import pandas as pd
import numpy as np
import requests

data = pd.read_excel("./PreOrders_210423.xlsx",sheet_name="Sheet1")
header = data.columns
values = data.values
xml = ""
valuesArray = []
for i in range(0,len(values)):
    d = values[i]
    xml = "<ns0:MT_ATLAS_CUSTOMERORDER xmlns:ns0='http://smyths.com/atlas/orders/customerorder'>"
    for h in range(0,len(header)):
        if (str(header[h]) == "LineItem"):
            xml+="<LineItem><"+str(header[h])+">"+"0000"+str(d[h])+"</"+str(header[h])+">"
        else:
            xml+="<"+str(header[h])+">"+str(d[h])+"</"+str(header[h])+">"
    xml = xml.replace(str(np.nan),"")
    xml+="</LineItem></ns0:MT_ATLAS_CUSTOMERORDER>"
    valuesArray.append(xml)
    xml = ""
print(valuesArray)

for v in valuesArray:
    xml = v
    headers = {'Content-Type': 'application/xml'} # set what your server accepts
    print (requests.post('https://atlas-dev.smythstoys.com/api/sap/order-new',verify=False, data=xml, headers=headers).text)