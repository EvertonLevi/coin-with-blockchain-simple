import datetime
from Cryptodome.Hash import SHA
from Cryptodome.Signature import PKCS1_v1_5
import binascii
import collections


# A primeira transação é um bloco Gênesis S2

class Transaction:
  def __init__(self, sender, recipient, value):
    self.sender = sender
    self.recipient = recipient
    self.value = value
    self.time = datetime.datetime.now().timestamp()

  def to_dict(self):
    if self.sender == 'Gênesis':
      identity = 'Gênesis'
    else:
      identity = self.sender.identity

    return collections.OrderedDict({
      'sender': identity,
      'recipient': self.recipient,
      'value': self.value,
      'time': self.time
    })

  def sign_transaction(self):
    private_key = self.sender._private_key
    signer = PKCS1_v1_5.new(private_key)
    h = SHA.new(str(self.to_dict()).encode('utf8'))
    return binascii.hexlify(signer.sign(h)).decode('ascii')

  def display_transaction(transaction):
    dict = transaction.to_dict()
    print("Pagador: " + dict['sender'])
    print("\n")
    print("Recebedor: " + dict['recipient'])
    print("\n")
    print("Valor: " + str(dict['value']))
    print("\n")
    print("Hora: " + str(dict['time']))
    # TODO lógica de gerenciamento de filas
    transacoes = []

