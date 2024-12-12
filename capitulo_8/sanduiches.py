def fazer_sanduiche(*args):
    """Resume a criacao de pizzas com varios ingredientes"""
    print("O sanduiche esta sendo feito com o seguintes ingredientes:")
    for ingrediente in args:
        print(f"\t-{ingrediente}")


fazer_sanduiche("tomate")
fazer_sanduiche("tomate", "queijo", "presunto")
fazer_sanduiche("tomate", "queijo", "presunto", "carne moida")
