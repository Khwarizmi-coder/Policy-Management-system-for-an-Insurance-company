from datetime import datetime,timedelta
from policyholder import Policyholder
from product import Product
from payment import Payment

product1= Product(1,"Health Insurance","Covers medical insurance services.")
product2= Product(2,"Car Insurance","Covers motor vehicle repairs and liability.")


holder1=Policyholder(201,"George")
holder2=Policyholder(202,"Washington")


holder1.register_product(product1)
holder2.register_product(product2)

#process payments
payment1=Payment(150, datetime.now().date()-timedelta(days=3))
penalty1=payment1.process_payment(datetime.now().date())

payment2=Payment(200,datetime.now().date())
penalty2=payment2.process_payment(datetime.now().date())

holder1.make_payment(payment1)
holder2.make_payment(payment2)

#Print results
print("Policyholder Details:\n")
print(holder1)
for payment in holder1.payments:
    print(payment)
print("\n")
print(holder2)
for payment in holder2.payments:
    print(payment)