import hashlib
from cliente import Cliente
from transaction import Transaction
from bloco import Bloco

if __name__ == '__main__':
    presidente = Cliente()
    governador = Cliente()
    secretario = Cliente()

    transacoes = []
    Coins = []

    ultimo_bloco_hash = ""
    ultima_transacao_index = 0

    t0 = Transaction(
        "Gênesis",
        presidente.identity,
        100
    )

    t1 = Transaction(
        governador,
        secretario.identity,
        54.5
    )

    t2 = Transaction(
        "Gênesis",
        presidente.identity,
        36.7
    )

    t3 = Transaction(
        secretario,
        governador.identity,
        98.1
    )

    transacoes.append(t0)
    transacoes.append(t1)
    transacoes.append(t2)
    transacoes.append(t3)


    def dump_blockchain(self):
        print("Número de blocos na corrente: " + str(len(self)))
        for i in range(len(Coins)):
            bloco_temp = Coins[i]
            print("Bloco: " + str(i) + "\n")
            for transaction in bloco_temp.verified_transacoes:
                Transaction.display_transaction(transaction)
                print('---------------------')
            print('==-=--=-=-=-=--=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=--=-')

    def sha256(mensagem):
        return hashlib.sha256(mensagem.encode('ascii')).hexdigest()

    def mine(mensagem, dificuldade=1):
        # TODO revisar função mine
        assert dificuldade >= 1
        prefixo = '0' * dificuldade
        for i in range(1000):
            digest = sha256(str(hash(mensagem)) + str(i))
            if digest.startswith(prefixo):
                print('After ' + str(i) + " iterations found nonce: \n" + digest)
                return digest


    bloco = Bloco()
    for i in range(len(transacoes)):
        temp_transaction = transacoes[ultima_transacao_index]
        bloco.verified_transacoes.append(temp_transaction)
        ultima_transacao_index += 1

    bloco.previous_bloco_hash = ultimo_bloco_hash
    bloco.Nonce = mine(bloco, 2)
    digest = hash(bloco)
    Coins.append(bloco)
    ultimo_bloco_hash = digest

    dump_blockchain(Coins)


