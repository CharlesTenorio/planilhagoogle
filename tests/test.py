from planilha import Planilha

def test_lista_planilha():
    # 1Fc2m6ywTA7WK36IQBxrJrQm3lgbHP8tCAV_s4eyylFI
    plan = Planilha('19w9C3Y7o228kN97d3fzexidqowQ_-3fBdUzLEy_keLQ')
    assert plan.get_qtd_registro()==19
