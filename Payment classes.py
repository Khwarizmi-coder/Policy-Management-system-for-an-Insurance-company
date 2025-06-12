from datetime import datetime,timedelta
class Payment:
    def __init__(self,amount,due_date,paid_date=None):
        self.amount=amount
        self.due_date=due_date
        self.paid_date=paid_date
        self.penalty=0

    def process_payment(self,pay_date):
        self.paid_date=pay_date
        if pay_date>self.due_date:
            delay= (pay_date-self.due_date).days
            self.penalty=delay*20 #penalty of 20 $ per day
        return self.penalty
    def reminder(self):
        today=datetime.now().date()
        if today >= self.due_date:
            return f"Payment due.Due date was {self.due_date}."
        else:
            return f"Upcoming payment due on {self.due_date}."
    def __str__(self):
        paid= f"Paid on {self.paid_date}" if self.paid_date else "Not Paid"
        return f"Amount:{self.amount},Due:{self.due_date},{paid},Penalty:${self.penalty}"