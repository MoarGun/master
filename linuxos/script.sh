#!/bin/bash
$ chmod +x script.sh 
$ linuxconfig.org:~$ ./script.sh

skaicius=$(cat konfiguracinisFailas | grep eth | wc -w)
echo "$skaicius xd"

