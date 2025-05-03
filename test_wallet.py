from wallet_generator import generate_wallet

def test_wallet_format():
    # Just runs to see if function completes successfully
    try:
        generate_wallet()
        assert True
    except Exception:
        assert False
