
from datetime import datetime
#id,amount,category,descriptionription,data,payment-method
from enum import Enum
from typing import Any


class Expense:

    allowed_payment_methods=["upi","netbanking","cash"]

    def __init__(self,expense_id,amount,category,payment_method,description=""):

        if expense_id is None:
            raise ValueError("Provide expense_id....\n")

        if(isinstance(expense_id,bool)):
            raise TypeError("Id should not be boolean value\n")
        
        if(not isinstance(expense_id,int)):
            raise TypeError("Id has to be integer value only\n")
        if(expense_id<=0):
            raise ValueError("Id has to be positive only\n")

        if amount is None:
            raise ValueError("Provide amount value\n")
        
        if(not isinstance(amount,(float,int))):
            raise TypeError("Amount has to be float or integer value....\n")

        if(amount<=0):
            raise ValueError("Amount has to be postive only\n")

        if(not isinstance(category,str)):
            raise TypeError("Category has to be in string value..\n")

        category=category.strip()

        if len(category)==0:
            raise ValueError("Category has to be provided...\n")

        if description is None:
            description=""

        if not isinstance(description,str):
            raise TypeError("Description has to be in string format\n")

        if(description!=""):
            description=description.strip()

        cur_time=datetime.now()

        if(not isinstance(payment_method,str)):
            raise TypeError("Payment method has to be string..\n")

        if(payment_method.strip()==""):
            raise ValueError("Provide payment method information..\n")

        payment_method=payment_method.strip().lower()

        
        if payment_method not in self.allowed_payment_methods:
            raise ValueError("Payment Methods have to be in UPI,Net-Banking,Cash only....\n")


        
        self.expense_id=expense_id
        self.amount=amount
        self.category=category
        self.description=description
        self.date_paid=cur_time.strftime("%Y-%m-%dT%H:%M:%S")
        self.payment_method=payment_method

    def __str__(self):
        return f"Id : {self.expense_id}\nAmount :{self.amount}\nCategory :{self.category}\nDate-Paid : {self.date_paid}\nPayment-Method :{self.payment_method}\nDescription :{self.description}\n\n"

    def __repr__(self)-> str:
        return f"Id : {self.expense_id}\nAmount :{self.amount}\nCategory :{self.category}\nDate-Paid : {self.date_paid}\nPayment-Method :{self.payment_method}\nDescription :{self.description}\n\n"