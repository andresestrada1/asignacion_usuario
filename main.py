from usuario import Usuario


andres = Usuario("Andres", "afecestra@hotmail.com")
sebas = Usuario("Sebas", "elpuntilla@gmail.com")
diego = Usuario("Diego", "elflaco@hotmail.com")

andres.hacer_deposito(100)
andres.hacer_deposito(50)
andres.hacer_deposito(10)
andres.transfer_dinero(sebas,400)

sebas.hacer_deposito(800)
sebas.hacer_deposito(900)

sebas.transfer_dinero(diego,20)
sebas.transfer_dinero(diego,400)
sebas.mostrar_balance_usuario()

diego.hacer_deposito(50)
diego.transfer_dinero(andres,20)
diego.transfer_dinero(andres,400)
diego.transfer_dinero(andres,400)
diego.mostrar_balance_usuario()


sebas.mostrar_balance_usuario()
andres.mostrar_balance_usuario()
andres.hacer_retiro(600)

sebas.mostrar_balance_usuario()
andres.mostrar_balance_usuario()



