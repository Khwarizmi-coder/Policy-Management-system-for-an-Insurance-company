class Policyholder:
    def __init__(self,id,name,status="active"):
        self.id=id
        self.name=name
        self.status=status
        self.products=[]
        self.payments=[]
    def register(self,product):
        if self.status=="active":
            self.products.append(product)
        else:
            print(f"Can't register product.Policyholder{self.name} is {self.status}.")
        self.products.append(product)
        return f"Policy registered"
    def suspend(self):
        self.status="suspended"
    def reactivate(self):
        self.status="active"
    def make_payment(self,payment):
        self.payments.append(payment)
    def __str__(self):
        products_list=" ," .join([p.name for p in self.products])
        return f"Policyholder ID:{self.id}, Name:{self_name},Products:[{products_list}]"