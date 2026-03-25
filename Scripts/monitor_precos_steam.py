import requests
import time

def consultar_steam_full(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=br&l=portuguese"
    
    try:
        res = requests.get(url).json()
        if not res or not res[str(appid)]['success']:
            return f"❌ AppID {appid} não encontrado."

        data = res[str(appid)]['data']
        nome = data['name']
        
        # Se o jogo for grátis, não tem 'price_overview'
        if data.get('is_free'):
            return f"🎮 {nome}: Grátis!"

        price_info = data.get('price_overview')
        if not price_info:
            return f"🎮 {nome}: Sem informações de preço (Pode ser Pré-venda)."

        preco_atual = price_info['final_formatted']
        # O 'initial' vem em centavos (ex: 3299), precisamos dividir por 100
        preco_sem_desconto = price_info['initial'] / 100
        # O 'final' é o menor preço que a Steam está oferecendo HOJE
        preco_com_desconto = price_info['final'] / 100
        
        # Para o menor preço HISTÓRICO real em R$, o ideal é o SteamDB, 
        # mas aqui vamos mostrar o "Preço Base" vs "Preço com Desconto"
        relatorio = f"🎮 {nome}\n   💰 Preço Agora: {preco_atual}"
        
        if price_info['discount_percent'] > 0:
            relatorio += f"\n   📉 Menor preço nesta oferta: R$ {preco_com_desconto:.2f}"
            relatorio += f"\n   🏷️ Preço normal dele: R$ {preco_sem_desconto:.2f}"
        else:
            relatorio += f"\n   ✨ Está no preço cheio (R$ {preco_sem_desconto:.2f})"
            
        return relatorio + "\n"

    except Exception as e:
        return f"⚠️ Erro no jogo {appid}: {e}"

# Lista de desejos

meus_jogos = {
    3905410: "Neva: Prologe",
    1585220: "Melatonin",
    2997230: "Planet of Lana II",
    239030:"Papers Please",
    2350790:"Moonlighter 2: The Endless Vault",
    1954200:"Kena: Bridge of Spirits",
    3485810:"Kena: Scars of Kosmora",
    3161220: "Coffee Talk Tokyo",
}

print("--- Monitor de Preços do Dani ---")
for id_jogo in meus_jogos:
    print(consultar_steam_full(id_jogo))
    time.sleep(1)

# Executar no terminal com
# python3 monitor_steam.py 
