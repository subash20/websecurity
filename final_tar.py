#!/usr/bin/env python

import os
import tarfile,datetime
import sys,MySQLdb

db=MySQLdb.connect('localhost','root','luka@12','Backup')
cursor=db.cursor()

for item in os.listdir(sys.argv[1]):
    if tarfile.is_tarfile(item):
        print item +"is tar file"
        size=os.path.getsize(item)
        print "size :",size
        sql="insert into backup (file_name, file_size) values('%s','%d');"%(item,size)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print e
            db.rollback()
        data=tarfile.open(item,'r:gz')
        print "######### tar file info #########"
        #print data.name + " : size is :"+str(data.size)
        for thing in data:
            time=thing.mtime    # time in mtime format
            time_obj=datetime.datetime.fromtimestamp(time) # time format change as (2019 ,2 ,6,15, 50,48)
            time_mode=time_obj.strftime("%Y%m%d_%H:%M:%S") # time name 
            print "name:"+thing.name +'   '+ "size:"+str(thing.size)+'    '+"time:"+time_mode
            sqla="insert into backup(file_name,file_size,mtime) values('%s','%d','%s');"%(thing.name, thing.size,time_mode)
            try:
                cursor.execute(sqla)
                db.commit()
            except Exception as e:
                print e
                db.rollback()
        print "**********************************"
        data.close()
       # for info in data:
       #     print info.list()
    else:
        print item +"is not tar file"


