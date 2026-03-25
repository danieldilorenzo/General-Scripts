import psutil
import shutil
import platform
import os

# License: GNU GPLv3 - See LICENSE file for details.


"""
Script de diagnóstico de disco para suporte técnico.
Funciona em Windows e Linux.
- Identifica o tipo de hardware HDD / SSD / NVMe
- Mostra espaço Total, Ocupado e Livre
- Percentual de uso

Compatível com Linux e Windows 11.

"""

def get_disk_info():
    print("--- 🔍 Relatório de Unidades (HDD / SSD / NVMe) ---")
    
    # all=False remove partições virtuais/loop do Linux, limpando o log
    partitions = psutil.disk_partitions(all=False)
    
    for partition in partitions:
        # Filtro extra para Linux (evita tmpfs e outros lixos de sistema)
        if platform.system() == "Linux":
            if any(x in partition.device for x in ['loop', 'snap', 'tmpfs']):
                continue
            
        try:
            usage = shutil.disk_usage(partition.mountpoint)
            
            print(f"\n📌 Unidade: {partition.device} [{partition.mountpoint}]")
            
            # Conversão de Bytes para GB (GiB real do sistema)
            total_gb = usage.total // (2**30)
            used_gb = usage.used // (2**30)
            free_gb = usage.free // (2**30)
            percent = (usage.used / usage.total) * 100

            print(f"   Capacidade: {total_gb:>4} GB")
            print(f"   Em uso:     {used_gb:>4} GB ({percent:.1f}%)")
            print(f"   Disponível: {free_gb:>4} GB")

            # Identificação da Tecnologia de Hardware
            tipo = "Desconhecido"
            dev_name = partition.device.split('/')[-1]

            if platform.system() == "Linux":
                # Detecção inteligente de NVMe (como seu Kingston NV2)
                if "nvme" in partition.device:
                    tipo = "NVMe 🚀⚡"
                else:
                    try:
                        # Limpa o nome (ex: sda1 vira sda) para checar rotação
                        drive_base = "".join([i for i in dev_name if not i.isdigit()])
                        path = f"/sys/block/{drive_base}/queue/rotational"
                        if os.path.exists(path):
                            with open(path, "r") as f:
                                tipo = "HDD 💿" if f.read().strip() == "1" else "SSD SATA 🚀"
                    except:
                        pass
            elif platform.system() == "Windows":
                # No Windows, diferencia entre disco fixo e removível (USB)
                tipo = "Unidade Local" if "fixed" in partition.opts else "Removível (USB)"

            print(f"   Tecnologia: {tipo}")
            
        except (PermissionError, OSError):
            # Pula drives protegidos ou vazios (ex: leitor de cartão sem cartão)
            continue 

if __name__ == "__main__":
    get_disk_info()
