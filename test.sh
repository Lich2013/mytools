#! /bin/bash
while true
    do
        top -n 0 >> cpu.log
        printf "\n" >> cpu.log
        sleep 2
    done
