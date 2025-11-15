#!/bin/bash
#Verifica remote

echo "Verifica Docker si Docker Compose"
docker --version
docker compose version

echo "------------------------------------------------------------"

echo "Verifica grupul docker pentru userul ansible"
groups ansible
docker ps

echo "------------------------------------------------------------"

echo "Containere active"
docker ps

echo "------------------------------------------------------------"

MONITOR_DIR="/home/ansible/platforma-monitorizare/sysmonitor"

echo "Verifica logul monitor.log"
if [ -f "$MONITOR_DIR/monitor.log" ]; then
    echo "monitor.log exista"
else
    echo "monitor.log nu exista"
    exit 1
fi

echo "------------------------------------------------------------"

echo "Verifica backup-uri"
if [ -d "$MONITOR_DIR/backup" ]; then
    ls -1 "$MONITOR_DIR/backup"
else
    echo "Dir backup nu exista"
    exit 2
fi

echo "------------------------------------------------------------"

echo "Verifica acces Nginx (localhost:80)"
if command -v curl &> /dev/null; then
    curl -s http://localhost:80 | head -n 10
else
    echo "Ceva nu e ok"
    exit 3
fi

echo "-------------------SFARSIT :)-----------------------------"
