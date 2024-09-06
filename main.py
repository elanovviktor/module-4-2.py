def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function ()# 'Я в области видимости функции test_function'
inner_functioni()# ошибка, ПЧ не видит , потому что inner_function внутри другой функции