v_fabrica = float(input("digite um valor:"))

def calc_valor_distr():
    global v_fabrica
    v_com_imposto = v_fabrica+(v_fabrica*0.28)

    return v_com_imposto

def calc_imposto_gov(v):
    v += v*0.45
    return v
v_atualizado = calc_valor_distr()
v_atualizado = calc_imposto_gov(v_atualizado)

print(f"O valor será  R$ {v_atualizado}, FICA COM UM VALOR toal de r$ {v_atualizado}")


  