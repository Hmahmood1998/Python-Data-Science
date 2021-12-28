class Account:


    def __init__(self,Holder_name,Account_number,Balance,Date):
        self.Holder_name=Holder_name
        self.Account_number=Account_number
        self.Balance=Balance
        self.Date=Date

    def Debit(self,amnt):
        self.Balance-=amnt
        print(f"{amnt}Debited from  {self.Holder_name}'s account")

    def Credit(self,amnt):
        self.Balance+=amnt
        print(f"{amnt}Credited to  {self.Holder_name}'s account")

Acc1=Account('Hamid Mahmood','193736989','15000','10-07-2015')

print(Acc1.Holder_name)
print(Acc1.Account_number)
print(Acc1.Balance)
print(Acc1.Date)
Acc1.Debit(500)
print(Acc1.Balance)
Acc1.Credit(2500)
print(Acc1.Balance)

Acc2=Account('Piyush Singh','158468447','25000','23-08-2016')

print(Acc2.Holder_name)
print(Acc2.Account_number)
print(Acc2.Balance)
print(Acc2.Date)
Acc2.Debit(800)
print(Acc2.Balance)
Acc2.Credit(2300)
print(Acc2.Balance)


Acc3=Account('Harshit Kumar','178773836','35000','07-11-2018')

print(Acc3.Holder_name)
print(Acc3.Account_number)
print(Acc3.Balance)
print(Acc3.Date)
Acc3.Debit(900)
print(Acc3.Balance)
Acc3.Credit(3400)
print(Acc3.Balance)

