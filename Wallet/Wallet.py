from Mainnet import EthMainnet


class Wallet:
    def __init__(self, chain, wid, initial_money=0):
        self._id = wid
        self.chain = chain
        self.chain.set_balance_of_addr(wid, initial_money)

    def get_wallet_id(self):
        return self._id

    def send_transaction(self, contract=None, function=None, args=None):
        if not (contract is None) and contract.name == 'TC':
            if function == 'deposit':
                contract.deposit({'note': args, 'called_addr': self._id})
            if function == 'withdraw':
                contract.withdraw({'note': args, 'called_addr': self._id})
        if not (contract is None) and contract.name == 'OTHER':
            contract.transfer({'called_addr': self._id})
        if contract is None and function is None:
            self.chain.commit({
                'txn': EthMainnet.get_transaction_hash(self._id),
                'from': self._id,
                'to': args.get('to'),
                'method': 'transfer',
                'transaction': args.get('amount'),
                'block': self.chain.get_current_block_id_update(),
                'gas': self.chain.get_gas_price(),
                'args': None
            })

    def get_balance(self):
        return self.chain.get_balance_of_addr(self._id)
