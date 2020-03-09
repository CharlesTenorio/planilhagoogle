from planilha import Planinha

def test_lista_planilha():
    plan = Planinha('19w9C3Y7o228kN97d3fzexidqowQ_-3fBdUzLEy_keLQ')
    assert plan.get_qtd_registro()==19
