# Dockerfile pentru imaginea scriptului de backup python
FROM python:3.11-slim

# Instalam utilitare necesare
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Setam dir de lucru
WORKDIR /appmonitor

# Copiem script backup.py in folderul aplicatiei
COPY scripts/backup.py ./backup.py

# Modificam permisiuni script - executabil
RUN chmod +x backup.py

# Setare variabile de mediu pentru interval backup si directorul de backup
ENV INTERVAL_BACKUP=5
ENV DIR_BACKUP=/sysmonitor/backup

# Montam volumul /system-log
VOLUME ["/sysmonitor"]

# Executam script la pornirea containerului
CMD ["python3", "backup.py"]

