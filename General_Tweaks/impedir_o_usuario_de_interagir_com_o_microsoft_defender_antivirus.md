# 🛡️Impedir o usuário de interagir com o Microsoft Defender Antivírus

Esse procedimento é utilizado para impedir que o usuário desabilite o Microsoft Defender Antivirus, impedindo que ele desative o scan, o que o deixaria vulnerável a ameaças.

## 🛠️ Passo a Passo

1. Pressione a tecla **Windows** e digite `Editar política de grupo` (ou `gpedit.msc`).

2. Navegue pelo seguinte caminho no menu à esquerda:
   > **Configuração do Computador** > **Modelos Administrativos** > **Componentes do Windows** > **Microsoft Defender Antivirus** > **Interface cliente** 

3. Localize a opção abaixo, dê um dulplo clique nela, e muda para **Habilitado**. Após esse passo, reinicie a máquina.

- [ ] **Habilitar modo de UI sem periféricos**

---

_Documentação gerada para o repositório General-Scripts._
