from eth_account import Account
import secrets

def generate_wallet():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    print("Private Key:", private_key)
    print("Address:    ", acct.address)

if __name__ == "__main__":
    generate_wallet()
