import json
import os
def pcapToJSON():
    out =[]
    outdic ={}
    reqheader =["accept-language","accept-encoding","accept-encoding","accept-encoding","host","user-agent","connection"]
    with open('temp.json','r') as temp:
        data = json.load(temp)
        i = 0 
        for packet in data:
            req={}
            res={}
            headers ={}
            http = packet['_source']['layers']['http']
            http_title = list(http.keys())[0]
            if "GET" in http_title:
                i = i+1
                outdic['request'] = req
                for title in http:
                    if title == http_title:
                        req['size'] = int(packet['_source']['layers']['ip']['ip.len'])-20
                        req["method"] = http[title]['http.request.method']
                    elif title == 'http.request.full_uri':
                        req["request_uri"] = http[title]
                    val = title.replace("http.","")
                    if '_' in val:
                        val = val.replace("_","-")    
                    if val in reqheader:
                        headers[val] =http[title]
                        req['headers'] = headers
                outdic['request'] = req
            else :
                i = i+1
                resheaders =['server','content-type','cache-control']
                for title in http:  
                    if title == http_title:
                        res["size"]= int(packet['_source']['layers']['ip']['ip.len'])-20
                        res["status"] = http[title]['http.response.code']
                    val = title.replace("http.","")
                    if '_' in val:
                        val = val.replace("_","-")
                    if val in resheaders:
                        headers[val] =http[title]
                    elif val == 'date':
                        res['expires'] = http[title] 
                    elif val == 'content_length_header':
                        res['content_length_header'] = http[title]
                    elif val == 'response.line':
                        headers['content-length'] = ''.join(filter(str.isdigit, http[title]))
                res['headers'] = headers
                outdic['response'] = res
            if i%2== 0:
                outdic['label'] = "benign"
                out.append(outdic)
    return out

output = pcapToJSON()
middle = json.dumps(output,indent=4)
with open("data.json","w") as output:
    output.write(middle)

os.system("sudo tshark -r save.pcap -T json > temp.json http")
os.system("touch data.json")
pcapToJSON()
os.system("sudo rm temp.json")

