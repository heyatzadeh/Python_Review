def inner(address):
    print('inner: ', address)

    def outer():
        print('outer: ', address)

    return outer


iran = 'Iran'
vari = inner(iran)
del inner
iran = '10'
vari()
vari()

print(vari.__closure__[0].cell_contents)
