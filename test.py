# -*- cofing:utf-8 -*


def set_var(val):
    """Fonction nous permettant de tester la portée 
    des variables ds fonctions"""

    try:
        print('avant, notre var vaut: {}'.format(var))
    except NameError:
        print('Var n\'existe pas encore')
    var = val
    print('après, notre var vaut{}'.format(var))

set_var(5)
print(var)