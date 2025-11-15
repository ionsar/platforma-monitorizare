# Dockerfile pentru imaginea scriptului de monitorizare bash.
FROM ubuntu:22.04

# Instalam pachete necesare (procps pentru top, df etc)
# Curatam cache apt rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y procps bash && rm -rf /var/lib/apt/lists/*

# Setam dir de lucru
WORKDIR /appmonitor

# Copiem scriptul monitoring.sh în folderul /appmonitor
COPY scripts/monitoring.sh ./monitoring.sh

# Modificam permisiuni script - executabil
RUN chmod +x monitoring.sh

# Setam variabila de mediu pentru frecventa update
ENV INTERVAL_LOG=5

# Montam volumul /sysmonitor
VOLUME ["/sysmonitor"]

# Executam script la pornirea containerului
CMD ["./monitoring.sh"]
