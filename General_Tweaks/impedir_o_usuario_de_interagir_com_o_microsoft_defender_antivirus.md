# 🛡️Impedir o usuário de interagir com o Microsoft Defender Antivírus

Esse procedimento é utilizado para impedir que o usuário desabilite o Microsoft Defender Antivirus, impedindo que ele desative o scan, o que o deixaria vulnerável a ameaças.

## 🛠️ Passo a Passo

1. Pressione a tecla **Windows** e digite `Editar política de grupo` (ou `gpedit.msc`).

2. Navegue pelo seguinte caminho no menu à esquerda:
   > **Configuração do Computador** > **Modelos Administrativos** > **Componentes do Windows** > **Microsoft Defender Antivirus** > **Interface cliente** 

3. Localize a opção abaixo, dê um dulplo clique nela, e muda para **Habilitado**:

- [ ] **Habilitar modo de UI sem periféricos**

---

## 💡 Notas Importantes
* **Aplicação:** Após alterar para "Habilitado", a restrição é aplicada quase instantaneamente. Caso não funcione de imediato, rode o comando `gpupdate /force` no CMD como administrador.
* **Versões do Windows:** Este recurso está disponível nativamente nas versões *Pro*, *Enterprise* e *Education*.
* **Reversão:** Para liberar o acesso novamente, basta colocar as opções como `Não Configurado`.

_Documentação gerada para o repositório General-Scripts._
