from typing import Optional, Any,List
from expense import Expense

class Response:
    def __init__(self, message: str="", data: Any = None):
        
        self.message = message
        self.data = data

    def __repr__(self) -> str:
        return f"Message :{self.message}\nData :{self.data}\n\n"