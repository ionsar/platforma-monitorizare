#!/bin/bash
# Script bash pentru monitorizarea resurselor sistemului.

FISIER_LOG="/sysmonitor/monitor.log"
#daca nu exista INTERVAL_LOG, setam 5 ca valoare implicita 
INTERVAL=${INTERVAL_LOG:-5}

#daca nu exista directorul il cream
mkdir -p "$(dirname "$FISIER_LOG")"

while true; do
    DATA=$(date '+%Y-%m-%d %H:%M:%S')
    echo "----------------------- Statistici din $DATA -----------------------" > "$FISIER_LOG"

    echo "****Cpu****" >> "$FISIER_LOG"
    top -bn1 | grep "Cpu(s)" >> "$FISIER_LOG"
    echo >> "$FISIER_LOG"

    echo "****Memorie****" >> "$FISIER_LOG"
    free -h >> "$FISIER_LOG"
    echo >> "$FISIER_LOG"

    echo "****Spatiul folosit****" >> "$FISIER_LOG"
    df -h >> "$FISIER_LOG"
    echo >> "$FISIER_LOG"

    echo "****Numarul de procese active****" >> "$FISIER_LOG"
    ps -e --no-headers | wc -l >> "$FISIER_LOG"
    echo >> "$FISIER_LOG"

    echo "****Top 6 procese****" >> "$FISIER_LOG"
    ps -eo pid,cmd,%mem,%cpu --sort=-%cpu --no-headers | head -n 6 >> "$FISIER_LOG"
    echo >> "$FISIER_LOG"

    echo "****Useri logati****" >> "$FISIER_LOG"
    who >> "$FISIER_LOG"
    echo >> "$FISIER_LOG"

    echo "****Hostname****" >> "$FISIER_LOG"
    hostname >> "$FISIER_LOG"
    echo >> "$FISIER_LOG"

    sleep "$INTERVAL" 
done