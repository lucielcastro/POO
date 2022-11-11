
class Cliente:
   def __init__(self,nome, cpf, telefone):
      self.__nome = nome
      self.__cpf = cpf
      self.__telefone = telefone
      self.conta = None
      self.conta_cc = None
      self.conta_cp = None

   @property
   def nome_(self):
      return self.__nome
      
   @nome_.setter
   def nome_(self, nome):
      self.__nome = nome
   
   @property
   def cpf(self):
      return self.__cpf
   
   @cpf.setter
   def cpf(self, cpf):
      self.__cpf = cpf
   
   @property
   def telefone(self):
      return self.__telefone
   
   @telefone.setter
   def telefone(self, telefone):
      self.__telefone = telefone
   
   #composição Conta
   def criar_conta(self,numConta, agencia, saldo):
      self.conta=(Conta(numConta, agencia, saldo))

   def criar_conta_cc(self,numConta, agencia, saldo):
      self.conta_cc=(ContaCorrente(numConta, agencia, saldo))
   
   def criar_conta_cp(self,numConta, agencia, saldo):
      self.conta_cp=(ContaPoupanca(numConta, agencia, saldo))
   
   def imprimir_dados_pessoas(self):
      print(f'\nNome: {self.__nome} CPF: {self.__cpf}, Telefone: {self.__telefone}')
   
   def imprimir_dados_conta(self):
         print(f'Agencia: {self.conta.agencia} Conta: {self.conta.numConta}')
   
   def imprimir_dados_conta_c(self):
         print(f'Agencia: {self.conta_cc.agencia} Conta: {self.conta_cc.numConta}')

   def imprimir_dados_conta_p(self):
         print(f'Agencia: {self.conta_cp.agencia} Conta: {self.conta_cp.numConta} ')

   
class Conta:
   def __init__(self,numConta, agencia, saldo):
      self.__numConta = numConta
      self.__agencia = agencia
      self.__saldo = saldo
      self.chaves = []
    
   @property
   def numConta(self):
      return self.__numConta
   
   @numConta.setter
   def numconta(self, numconta):
      self.__numConta = numconta
   
   @property
   def agencia(self):
      return self.__agencia
   
   @agencia.setter
   def agencia(self, agencia):
      self.__agencia = agencia
   
   @property
   def saldo(self):
      return self.__saldo
   
   @saldo.setter
   def saldo(self, saldo):
      self.__saldo = saldo
   
   def criar_chave_pix(self, chave_pix):
      self.chaves.append(ChavePix(chave_pix))
   
   def listaChaves(self):
      for chave in self.chaves:
         print(f'Chave Pix: {chave.chave_pix}')
   
   def ver_saldo(self):
      print(f'Saldo da Conta: {self.__numConta} é de R$ {self.__saldo}')
   
   def depositar(self, valor):
      self.__saldo += valor
      #print('\n\nCreditado com sucesso!')

   def transferir(self, valor, contaDestino):
      self.__saldo -= valor
      self.__saldo -= valor * .1
      contaDestino.depositar(valor)
      print('\n\nTransferência realizado com sucesso!')

class ContaCorrente(Conta):
   
   def transferir(self, valor, contaDestino):
      taxa = .1
      self.saldo-=valor
      self.saldo -= valor * taxa * 5
      contaDestino.depositar(valor)
      print('\n\nTransferência realizado com sucesso!')
      
      
class ContaPoupanca(Conta):
   def transferir(self, valor, contaDestino):
      taxa = .1
      self.saldo -= valor
      self.saldo -= valor * taxa * 1.25
      contaDestino.depositar(valor)
      print('\n\nTransferência realizado com sucesso!')
   
   
class ChavePix:
   def __init__(self, chave_pix):
      self.__chave_pix = chave_pix
   
   @property
   def chave_pix(self):
      return self.__chave_pix

   @chave_pix.setter
   def set_chave_pix(self, chave_pix):
      self.__chave_pix = chave_pix


cliente3 = Cliente('Carlos','38784-44','9389-33')
cliente3.criar_conta_cc('1345-38','3232',1000)
cliente3.imprimir_dados_pessoas()
cliente3.imprimir_dados_conta_c()
cliente3.conta_cc.ver_saldo()


cliente4 = Cliente('Lucas','12784-44','0089-33')
cliente4.criar_conta_cc('4434-38','656',800)
cliente4.imprimir_dados_pessoas()
cliente4.imprimir_dados_conta_c()
cliente4.conta_cc.ver_saldo()

cliente3.conta_cc.transferir(100, cliente4.conta_cc)
cliente3.conta_cc.ver_saldo()
cliente4.conta_cc.ver_saldo()

cliente4.conta_cc.transferir(100, cliente3.conta_cc)
cliente4.conta_cc.ver_saldo()
cliente3.conta_cc.ver_saldo()




