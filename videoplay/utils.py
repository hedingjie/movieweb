# encoding:utf-8
from movieweb.settings import MEDIA_DIR
import hdfs

MASTER='http://192.168.159.129:9870'
OWNER='hadoop'

LOCAL_PATH=MEDIA_DIR+'\\'
REMOTE_PATH='/user/hadoop/input/'

def download(file):
    file_path=REMOTE_PATH+file+'.mp4'
    client=hdfs.InsecureClient(url=MASTER,user=OWNER)
    flag=client.download(hdfs_path=file_path,local_path=LOCAL_PATH,overwrite=True)
    return flag

if __name__=='__main__':
    download('test.mp4')