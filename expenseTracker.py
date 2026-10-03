from expense import Expense
from response import Response

class ExpenseTracker:
    def __init__(self):
        self.expenses={}
        self.allowed_list=['amount','category','description','date_paid','payment_method']

    def add_expense(self,expense_id,amount,category,payment_method,description=""):

        if expense_id in self.expenses:
            return Response("Object already exists",)

        try:
            obj=Expense(expense_id,amount,category,payment_method,description)
        except TypeError as e:
            return Response(f"Invalid data format....\n{e}")
        except ValueError as e:
            return Response(f"Provide correct data format....\n{e}")

        self.expenses[expense_id]=obj
        
        return Response(f"Object created...\n",obj)

    def get_expense(self,expense_id):

        if expense_id in self.expenses:
            return Response("Expense retreived successfully...",self.expenses[expense_id])

        return Response("Expense with that id doesnot exists....")  
 
        

    def get_all_expenses(self):

        if len(self.expenses)==0:
            return Response("Expenses are empty")
        return Response("Expenses are as follows..",self.expenses)

    
    def update_expense(self,**kwargs):

        expense_id=kwargs.get('expense_id')
        if expense_id is None:
            return Response("Provide the expense id.....\n")
        
        if expense_id not in self.expenses:
            return Response("Expense with that id doesnot exists........")
        
        if len(kwargs)<2:
            return Response("Provide the fields for updation..\n")

        for key,value in kwargs.items():
            if key not in self.allowed_list and key!='expense_id':
                return Response(f"{key} is not allowed to update...\n")

        obj=self.expenses[expense_id]
        #check if attributes are allowed to update
        for key,value in kwargs.items():
            if key in self.allowed_list and hasattr(obj,key):
                setattr(obj,key,value)
        
        return Response(f"Expense with {expense_id} is updated successfully....\n",obj)



    def delete_expense(self,expense_id):

        if expense_id not in self.expenses:
            return Response("Expense with that id doesnot exists........")

        del self.expenses[expense_id]

        return Response(f"Expense with {expense_id} is deleted successfully...\n")
