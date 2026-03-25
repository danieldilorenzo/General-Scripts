import psutil
import shutil
import platform
import os

# License: GNU GPLv3 - See LICENSE file for details.

"""
Script de diagnóstico de disco para suporte técnico.
Funciona em Windows e Linux.
- Identifica SSD/HDD (quando possível)
- Mostra espaço Total, Ocupado e Livre
- Percentual de uso
"""


def get_disk_info():
    print("--- 🔍 Relatório de Unidades (HDD / SSD / NVMe) ---")
    
    partitions = psutil.disk_partitions()
    
    for partition in partitions:
        # Ignora partições virtuais do Linux (ajuda a manter o log limpo)
        if 'loop' in partition.device or 'snap' in partition.device:
            continue
            
        try:
            usage = shutil.disk_usage(partition.mountpoint)
            
            print(f"\n📌 Unidade: {partition.device} [{partition.mountpoint}]")
            
            # Cálculo de Espaço (GB)
            total_gb = usage.total // (2**30)
            used_gb = usage.used // (2**30)
            free_gb = usage.free // (2**30)
            percent = (usage.used / usage.total) * 100

            print(f"   Capacidade: {total_gb:>4} GB")
            print(f"   Em uso:     {used_gb:>4} GB ({percent:.1f}%)")
            print(f"   Disponível: {free_gb:>4} GB")

            # Identificação do Tipo de Hardware
            tipo = "Desconhecido"
            dev_name = partition.device.split('/')[-1]

            if platform.system() == "Linux":
                if "nvme" in partition.device:
                    tipo = "NVMe 🚀⚡"
                else:
                    try:
                        # Limpa o nome (ex: sda1 vira sda)
                        drive_base = "".join([i for i in dev_name if not i.isdigit()])
                        path = f"/sys/block/{drive_base}/queue/rotational"
                        if os.path.exists(path):
                            with open(path, "r") as f:
                                tipo = "HDD 💿" if f.read().strip() == "1" else "SSD SATA 🚀"
                    except: pass
            elif platform.system() == "Windows":
                # No Windows, se a unidade for C: e for rápida, geralmente é NVMe/SSD
                tipo = "Disco Local (Windows)"

            print(f"   Tecnologia: {tipo}")
            
        except PermissionError:
            continue 

if __name__ == "__main__":
    get_disk_info()
