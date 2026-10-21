from netmiko import ConnectHandler
from pyfiglet import Figlet
from datetime import datetime

import time
import re
import os

os.system("clear")

# Logo
fig = Figlet(font='slant')

print("\033[1;32m")
print(fig.renderText("AutoDefender"))
print("\033[0m")

print("\033[1;36m====================================================")
print("        Intelligent Intrusion Prevention System")
print("====================================================\033[0m")

time.sleep(1)

# Router Config
router = {
    "device_type": "cisco_ios",
    "host": "192.168.50.1",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco",

    "disabled_algorithms": {
        "pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]
    },

    "conn_timeout": 20,
    "global_delay_factor": 2,
    "banner_timeout": 20
}

# Snort Alert File
alert_file = "/var/log/snort/alert"

blocked_ips = set()

print("\033[1;34m[*] Starting Snort Monitoring Engine...\033[0m")
time.sleep(1)

print("\033[1;32m[+] IDS Protection ACTIVE\033[0m")
print("\033[1;33m[*] Monitoring Interface : ens33\033[0m")
print("\033[1;36m[*] Waiting For Threat Activity...\033[0m\n")

try:

    with open(alert_file, "r") as f:

        f.seek(0, 2)

        while True:

            line = f.readline()

            if not line:
                time.sleep(1)
                continue

            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+->', line)

            if ip_match:

                attacker_ip = ip_match.group(1)

                if attacker_ip.startswith("192.168"):
                    continue

                if attacker_ip in blocked_ips:
                    continue

                current_time = datetime.now().strftime("%H:%M:%S")

                print("╔══════════════════════════════════════════════╗")
                print("║              🚨 THREAT DETECTED 🚨           ║")
                print("╠══════════════════════════════════════════════╣")
                print(f"║ TIME      : {current_time:<31}  ║")
                print(f"║ ATTACKER  : {attacker_ip:<31}  ║")
                print("║ STATUS    : BLOCKING ATTACKER                ║")
                print("╚══════════════════════════════════════════════╝")

                try:

                    # SSH Connection
                    net_connect = ConnectHandler(**router)

                    net_connect.enable()

                    commands = [
                        f"ip route {attacker_ip} 255.255.255.255 Null0"
                    ]

                    net_connect.send_config_set(commands)

                    net_connect.save_config()

                    blocked_ips.add(attacker_ip)

                    print("\033[1;32m")
                    print("┌──────────────────────────────────────────────┐")
                    print(f"│ [+] IP BLOCKED SUCCESSFULLY : {attacker_ip:<15}│")
                    print("└──────────────────────────────────────────────┘")
                    print("\033[0m")

                except Exception as e:

                    print("\033[1;31m")
                    print(f"[ERROR] {e}")
                    print("\033[0m")

except KeyboardInterrupt:

    print("\n\033[1;31m[!] AutoDefender Engine Stopped Gracefully\033[0m")
