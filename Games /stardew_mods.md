# Stardew Valley Mods


<br>

## Adicionando os Mods

> Para Linux, o caminho padrão da pasta de Mods (tendo em mente que está sendo usado o pacote da distro e não flatpak / snap) é
> 
> /home/{USER}/.steam/steam/steamapps/common/Stardew Valley

<br>

>[!TIP]
> Quando não tiver instução, deve sempre se baixar, descompactar e colocar na pasta padrão de mods.

<br>



### MODS PARA COMPATIBILIDADE

>[!IMPORTANT]
> Os mods abaixo tem que ser instalados antes de qualquer coisa

<br>

####  - SMAPI

- [**Download SMAPI**](https://github.com/Pathoschild/SMAPI/releases)

Baixe  o Zip, descompacte e instale de acordo com as [instruções](https://stardewvalleywiki.com/Modding:Installing_SMAPI_on_Linux).


#### - Content Patcher

- [**Download Content Patcher**](https://www.nexusmods.com/stardewvalley/mods/1915)

#### Farm Type Manager (FTM)

- [**Download Farm Type Manager**](https://www.nexusmods.com/stardewvalley/mods/3231)


<br>

### MODS VISUAIS

#### - Daisysniko's earthy recolor

> Uma recoloração quente e em tons de terra que é agradável aos olhos

- [**Download Daisysniko's earthy recolor**](https://www.nexusmods.com/stardewvalley/mods/5255)


#### - UI Info Suite 2

> Fornece informações úteis sobre coisas ao seu redor, projetadas para ajudar você a ficar ciente do que está acontecendo sem sentir que está trapaceando.

- [**Download UI Info Suite 2**](https://www.nexusmods.com/stardewvalley/mods/7098)


<!-- 
#### - Faedew - A ReShade Preset
-->

#### - Stardew Progress

> Acompanha o progresso do jogador ao longo do jogo para ajudá-lo a atingir a perfeição. Uma maneira fácil de acompanhar o que falta fazer, incluindo os ingredientes necessários para completar todas as receitas.


- [**Download Stardew Progress**](https://www.nexusmods.com/stardewvalley/mods/9786)

- [**Tradução PT-BR**](https://www.nexusmods.com/stardewvalley/mods/23923)

#### - Prettier Interior

> Reforma do interior da cidade - mais desordem e decoração atmosférica e amigável à tradição

- [**Download Prettier Interior**](https://www.nexusmods.com/stardewvalley/mods/19423)



#### - Oasis Greenhouse

> Uma linda estufa de jardim com adega, spa e muito mais

- [**Download Oasis Greenhouse**](https://www.nexusmods.com/stardewvalley/mods/3969)

#### - Visible Fishs

> Torna os peixes visíveis em lagos, rios e lagoas

- [**Download Visible Fishs**](https://www.nexusmods.com/stardewvalley/mods/8897)

#### - Dynamic Reflections

> Adiciona reflexos em rios, lagos. Adiciona poças d'água

- [**Download Dynamic Reflections**](https://www.nexusmods.com/stardewvalley/mods/12831)

### MODS PARA JOGABILIDADE


#### - Stardew Valley Extended

> Stardew Valley Expanded é uma expansão feita por fãs para Stardew Valley, da ConcernedApe. Este mod adiciona 28 novos NPCs, 58 locais, 278 eventos de personagens, 43 peixes, áreas vanilla reimaginadas, três mapas de fazenda, um mapa-múndi reimaginado refletindo todas as mudanças, novas músicas, missões, objetos, plantações, festivais e muitas adições diversas!

- [**Download Stardew Valley Extended**](https://www.nexusmods.com/stardewvalley/mods/3753)

- [**Tradução PT-BR**](https://www.nexusmods.com/stardewvalley/mods/22110)


#### - Events Expansion

> Adiciona novos eventos de coração para os aldeões. 

- [**Download Events Expansion**](https://www.nexusmods.com/stardewvalley/mods/9042)

<br>

## Criando atalhos

<br>

> Após adicionar o SMAPI, podemos criar atalhos para diferenciar quando queremos jogar com mods e sem mods. Além disso, podemos criar um backup automático

Criar um arquivo vazio com o nome "Stardew_Valley.desktop" (os ícones estão no meu Github)

```
[Desktop Entry]
Name=Stardew Mods
Name[pt_BR]=Stardew Mods
Comment=Jogar Stardew Valley com Mods e Backup
Exec=sh -c '"/home/daniel/.local/share/Steam/steamapps/common/Stardew Valley/StardewModdingAPI"; /home/daniel/backup_stardew.sh'
Icon=/home/daniel/Imagens/stardew_mods.png
Terminal=false
Type=Application
StartupNotify=true
Version=1.0
Categories=Game;

```

Para o jogo com mods

Criar um arquivo vazio com o nome "Stardew_Mods.desktop"

```
[Desktop Entry]
Name=Stardew ORIGINAL
Name[pt_BR]=Stardew ORIGINAL
Comment=Rodar Stardew sem Mods com Backup
Exec=sh -c '"/home/daniel/.local/share/Steam/steamapps/common/Stardew Valley/StardewValley-original"; /home/daniel/backup_stardew.sh'
Icon=/home/daniel/Imagens/stardew_vanilla.png
Terminal=false
Type=Application
StartupNotify=true
Version=1.0
Categories=Game;

```

<br>
<br>



Cole esses atalhos em 

>/home/daniel/.local/share/applications/

Após isso, colar no terminal para o KDE fazer o atalho na sessão "Jogos"
```
update-desktop-database ~/.local/share/applications/ 
```

## Criando Backup
<br>
Para configurar para o sistema fazer um backup automático sempre que você fecha o jogo. Copie isso e cole no terminal
<br>

```

cat << 'EOF' > ~/backup_stardew.sh
#!/bin/bash

# Configurações de pastas
SAVE_DIR="$HOME/.config/StardewValley/Saves"
BACKUP_DIR="$HOME/Stardew_Backups"
TIMESTAMP=$(date +"%d-%m-%Y_%H-%M")

# Cria a pasta de backup se ela não existir
mkdir -p "$BACKUP_DIR"

# Faz o backup compactado (.tar.gz)
tar -czf "$BACKUP_DIR/backup_$TIMESTAMP.tar.gz" -C "$SAVE_DIR" .

# LIMPEZA: Mantém apenas os 3 mais recentes e apaga o resto
ls -t "$BACKUP_DIR"/backup_*.tar.gz | tail -n +2 | xargs -r rm

echo "Backup de Stardew Valley realizado com sucesso!"
EOF

# Dá permissão para o script rodar
chmod +x ~/backup_stardew.sh

```
<br>

Para restaurar, pegue esse arquivo, descompacte e substitua pelo conteúdo na pasta

>/home/daniel/.config/StardewValley/Saves/
<br>




## Entre em contato comigo!

Se você encontrou essa página aleatóriamente na internet e gostou, ou tem alguma crítica / sugestão, sinta-se livre para me entrar em contato comigo  :smile:

[![Gmail Badge](https://img.shields.io/badge/-Gmail-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:danieldilorenzoferreira@gmail.com)](mailto:danieldilorenzoferreira@gmail.com)
