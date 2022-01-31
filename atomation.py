import os
import time
import dropbox

path = "D:\Desktop\python\AutoImages"
days = 90

time_seconds = time.time()

def compare_time():
    ctime = os.stat(path).st_ctime
    return ctime

compare_time()


class TransferData:
   def __init__(self,access_token):
       self.access_token = access_token
       
   def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
        
def main():
    access_token = "sl.BAZbUPWR_VG2onA-HZcPK0F4YkyM2La5P9uvD4Q7rEobSPkBCQ3IALru_9xLDzseKxxlwx4IKzJuGbirD6v1G7ER6LusuRP9C6TAPUh60HzChlwj9Ftvbm1SK6vPLUBB_Z4ni4Q"  
    transferData = TransferData(access_token)   
    file_from = "AutoImages"   
    file_to = path
    
    transferData.upload_file(file_from,file_to)
    
    
main()    
           

def uploadImages():
    if(time.ctime > days):
        TransferData()
uploadImages()
