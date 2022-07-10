class Usuario:
    

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount

#hacer_retiro(self, amount): haz que este método reduzca el balance del usuario en la cantidad especificada

    def hacer_retiro(self, amount):
        if amount > self.balance_cuenta:
            print("Estas pobre, trabaje mas")
        else:
            self.balance_cuenta -= amount
            
#mostrar_balance_usuario(self): haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal
    
    def mostrar_balance_usuario(self):
        #print(self.name,self.balance_cuenta)
        print(f"El usuario {self.name} tiene {self.balance_cuenta} en la cuenta.")
        
#BONUS: transfer_dinero(self, other_user, amount): haz que este método reduzca el balance del usuario por el monto y agrega esa cantidad al balance de otro_usuario 
    def transfer_dinero(self, other_user, amount):
        if amount > self.balance_cuenta:
            print(f"El usuario {self.name} no cuenta con saldo suficiente")
        else:
            other_user.hacer_deposito(amount)
            self.balance_cuenta -= amount
