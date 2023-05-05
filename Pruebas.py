
def test_Hello():
    saludo = Hello()
    assert saludo == "HELLO FASTAPI"
    
def test_Isprime():
    numero=Isprime({10})
    assert numero == False
    
def test_Fibonnacci():
    numero=Fibonnacci(8)
    assert numero == 6