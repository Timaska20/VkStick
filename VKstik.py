import requests
import json
import os
while True:
  case=str(input("for PC 1\nfor android 2 \n"))
  if case== "1":
	  p="\\"
	  break
  elif case =="2":
	  p="/"
	  break
  else:
  	continue 
	  
	
token = "f202659091a9d880d72b060d697e0d6842902c63aaac00d27344860db67454*****************0db3e6"
peerID="1"
version="5.103"
filename = str(input('Ведите название файла без .png:\n'))
filename_grafity=str(filename+"_grafity")
os.rename(filename+".png",filename_grafity+".png")
def getMessagesUploadServer():
    response = requests.get('https://api.vk.com/method/docs.getMessagesUploadServer',params={'access_token':token,
                                                                                             'v':version,
                                                                                             'type':"graffiti",
                                                                                             "peer_id":peerID}).json()
    return response['response']['upload_url']
def save(file):
    response2 = requests.get('https://api.vk.com/method/docs.save', params={'access_token': token,
                                                                                              'v': version,
                                                                                              'file':file
                                                                                              }).json()
    print(response2)

def main():
  uploadurl = getMessagesUploadServer()
  result=requests.post(uploadurl, files={'file': open(os.getcwd()+p + filename_grafity + '.png', 'rb')}).json()
  IDfile= result['file']
  save(IDfile)
if __name__ == '__main__':
    main()
