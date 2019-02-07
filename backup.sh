#!/bin/bash

echo "backup file "

t=$(date +"%Y%m%d_%H%M")

#config_file= $(tar -cvf config_"$t".tar /etc/)
#web_page=$( tar -cvf web_"$t".tar /var/www/)
#homed= $( tar -cvf homedir_"$t".tar /home/)
#c=config_"$t".tar

c=config_"$t".tar.gz
d=home_"$t".tar.gz
e=web_"$t".tar.gz

tar -cvzf $c /etc/apache/
tar -cvzf $d /home/
tar -cvzf $e /var/www/html/


#tar -cvf web_"$t".tar /var/www/
#tar -cvf homedir_"$t".tar /home/
rsync -azv $c  root@10.42.176.180:/Backup/ 

rsync -azv $d  root@10.42.176.180:/Backup/ 

rsync -azv $e  root@10.42.176.180:/Backup/ 

