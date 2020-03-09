from planilha import Planilha

def test_lista_planilha():
    # 1Fc2m6ywTA7WK36IQBxrJrQm3lgbHP8tCAV_s4eyylFI
    plan = Planilha('1pBh84rVKBrl1AzHb4GkjmUR9VT3yld3I10W0F1cCbI4')
    assert plan.get_qtd_registro()==3
