# Script Python pentru efectuarea backup-ului logurilor de sistem.
import os
import time
import shutil
from datetime import datetime
import hashlib

# Fisier loguri de sistem
FISIER_LOG = "/sysmonitor/monitor.log"

# Setari variabile de mediu cu valori implicite
INTERVAL = int(os.environ.get("INTERVAL_BACKUP", 5))
DIRECTOR_BACKUP = os.environ.get("DIR_BACKUP", "./backup")


# Cream directorul backup daca nu exista
os.makedirs(DIRECTOR_BACKUP, exist_ok=True)

# Functie pentru hash. Folosta pentru hash-ul fisierulului de loguri
def compute_hash(filename):
    sha = hashlib.sha256()
    try:
        f = open(filename, "rb")
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            sha.update(chunk)
        f.close()
        return sha.hexdigest()
    except Exception as e:
        print("[ERROR] Nu s-a putut calcula hash-ul:", e)
        return None

# Dictionar: { timestamp: (hash, nume_fisier) }
backupuri = {}

try:
    fisiere = os.listdir(DIRECTOR_BACKUP)
    for f in fisiere:
        if f.startswith("monitor_") and f.endswith(".log"):
            # Eliminare extensie
            nume_fara_ext = f.replace(".log", "")  # scoatem ".log"

            # DSplit dupa _
            parts = nume_fara_ext.split("_")

            # Formatul este: monitor <hash>, <timestamp>
            if len(parts) >= 3:
                hash_valoare = parts[1]
                timestamp = parts[2]
                backupuri[timestamp] = (hash_valoare, f)
except Exception as e:
    print("[ERROR] Nu am putut lista fisierele din backup:", e)

# Daca avem fisiere de backup
ultimul_hash = None
if backupuri:
    # S0rtare după timestamp (cheia in dictionar)
    ultimul_timestamp = sorted(backupuri.keys(), reverse=True)[0]

    ultimul_hash, ultimul_fisier = backupuri[ultimul_timestamp]

    print("[INFO] Ultimul fisier de backup:", ultimul_fisier)
    print("[INFO] Hash-ul ultimului fisier de backup:", ultimul_hash)
else:
    print("[INFO] Nu exista fișiere de backup.")

print("[INFO] Start backup la  ", INTERVAL, "secunde.")

while True:
    try:
        if not os.path.exists(FISIER_LOG):
            print("[WARNING] Fisierul", FISIER_LOG, "nu exista.")
        else:
            hash_fisier_log = compute_hash(FISIER_LOG)
            if hash_fisier_log is None:
                time.sleep(INTERVAL)
                continue

            # Comparare hash cu ultimul backup
            if hash_fisier_log != ultimul_hash:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                fisier_backup = DIRECTOR_BACKUP + "/monitor_" + hash_fisier_log + "_" + timestamp + ".log"
                try:
                    shutil.copy2(FISIER_LOG, fisier_backup)
                    print("[INFO] S-a facut backup:", fisier_backup)
                    ultimul_hash = hash_fisier_log
                except Exception as e:
                    print("[ERROR] Nu s-a facut backup:", e)
            else:
                print("[INFO] Fisier neschimbat.")

    except Exception as e:
        print("[ERROR] Eroare :", e)

    time.sleep(INTERVAL)
