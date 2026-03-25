# 🔐 Desabilitar Transferência de Dados USB (Windows 11)

Este procedimento é utilizado para bloquear o acesso a pen-drives e unidades de armazenamento removíveis, impedindo a leitura, escrita e transferência de dados por motivos de segurança.

## 🛠️ Passo a Passo

1. Pressione a tecla **Windows** e digite `Editar política de grupo` (ou `gpedit.msc`).
2. Navegue pelo seguinte caminho no menu à esquerda:
   > **Configuração do Computador** > **Modelos Administrativos** > **Sistema** > **Acesso de Armazenamento Removível**

3. Localize as políticas abaixo e altere o estado de cada uma para **Habilitado**:

- [ ] **Discos Removíveis: Negar acesso de execução**
- [ ] **Discos Removíveis: Negar acesso de leitura**
- [ ] **Discos Removíveis: Negar acesso de gravação**

---

## 💡 Notas Importantes
* **Aplicação:** Após alterar para "Habilitado", a restrição é aplicada quase instantaneamente. Caso não funcione de imediato, rode o comando `gpupdate /force` no CMD como administrador.
* **Versões do Windows:** Este recurso está disponível nativamente nas versões *Pro*, *Enterprise* e *Education*.
* **Reversão:** Para liberar o acesso novamente, basta colocar as opções como `Não Configurado`.

---
*Documentação gerada para o repositório General-Scripts.*
