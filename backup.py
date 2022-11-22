from subprocess import run, PIPE,Popen
import subprocess
import os
import json
import shutil
from os import listdir
from os.path import isfile, join

path = os.getcwd()
print('path=',path)
f = open(path+'/psqlsetup.json')
data = json.load(f)
host = data['host']
database = data['database']
user = data['user']
password = data['password']
path = data['path']


def dump_table(host_name,database_name,user_name,database_password,path):
    port = '5432'
    proc = Popen(['pg_dump', '-h' ,host_name ,'-U',user_name ,'-f', path,database_name],
                 shell=True, stdin=PIPE,encoding='utf8')
    proc.wait()

src = r"{}".format(data['src'])
dst = r"{}".format(data['dst'])
sql_src = r"{}".format(data['sql_src'])
sql_dst = r"{}".format(data['sql_dst'])
def main():
    dump_table(host,database,user,password,path)
    try:
        shutil.rmtree(sql_dst)  
    except:
        pass
    shutil.copytree(sql_src, sql_dst)
    try:
        shutil.rmtree(dst)  
    except:
        pass
    shutil.copytree(src, dst)
if __name__ == "__main__":
    main()