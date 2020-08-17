"""
Skript um einen CIP Rechner mit weniger als 7% CPU Auslastung zu Finden
"""

import paramiko
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("LOGINNAME")
password = os.getenv("PASSWORD")

hosts = ["jaspis", "karneol", "katzenauge", "labradorit", "lapislazuli", "leucit", "malachit", "morganit", "morion",
         "onyx", "opal", "peridot", "petalit", "pyrit", "rhodonit", "rubellit", "rubin", "saphir", "smaragd",
         "sodalith", "tansanit", "thulit", "tigerauge", "topas", "vesuvianit", "zirkon", "almandin", "amazonit",
         "aquamarin", "benitoit", "beryll", "brasilianit", "buergerit", "citrin", "cordierit", "danburit", "datolith",
         "diamant", "dioptas", "dravit", "elbait", "euklas", "falkenauge", "feuerachat", "feueropal", "gagat",
         "goshenit", "hackmannit", "hambergit", "heliodor", "indigiolith"]

found = False

for host in hosts:
    if found:
        break
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(
        "grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}' ")
    stdin.close()
    for line in stdout.read().splitlines():
        print(host, line)
        try:
            if float(line) < 7:
                print("--------------")
                print(host)
                print("-> Hat weniger als 7% CPU Last")
                print("--------------")
                ssh.close()
                found = True
        except:
            print("Fehler")
    ssh.close()
