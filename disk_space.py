import psutil
import shutil
import platform

# License: GNU GPLv3 - See LICENSE file for details.

"""
Script de diagnóstico de disco para suporte técnico.
Funciona em Windows e Linux.
- Identifica SSD/HDD (quando possível)
- Mostra espaço Total, Ocupado e Livre
- Percentual de uso
"""

def get_disk_info():
    print("--- 🔍 Relatório de Unidades de Armazenamento ---")
    
    # Lista todas as partições montadas (incluindo sua case Ugreen)
    partitions = psutil.disk_partitions()
    
    for partition in partitions:
        # Ignora partições de sistema irrelevantes (como loop e squashfs no Linux)
        if 'loop' in partition.device or 'snap' in partition.device:
            continue
            
        try:
            usage = shutil.disk_usage(partition.mountpoint)
            
            print(f"\n📌 Unidade: {partition.device} [Montada em: {partition.mountpoint}]")
            print(f"   Sistema de Arquivos: {partition.fstype}")
            
            # Cálculo de Espaço
            print(f"   Total: {usage.total // (2**30):>4} GB")
            print(f"   Usado: {usage.used // (2**30):>4} GB ({(usage.used/usage.total)*100:.1f}%)")
            print(f"   Livre: {usage.free // (2**30):>4} GB")

            # Lógica para detectar SSD/HDD dependendo do SO
            tipo = "Desconhecido"
            if platform.system() == "Linux":
                try:
                    # Tenta ler o status rotacional no Linux (sda, sdb, etc)
                    drive_name = partition.device.split('/')[-1].rstrip('123456789')
                    with open(f"/sys/block/{drive_name}/queue/rotational", "r") as f:
                        tipo = "HDD 💿" if f.read().strip() == "1" else "SSD 🚀"
                except: pass
            elif platform.system() == "Windows":
                # No Windows, o psutil não dá o tipo direto, mas costumamos assumir 
                # SSD para unidades de sistema rápidas ou via flags externas.
                tipo = "Detectado via Windows"

            print(f"   Tipo Estimado: {tipo}")
            
        except PermissionError:
            continue # Pula drives protegidos ou sem permissão

if __name__ == "__main__":
    get_disk_info()
