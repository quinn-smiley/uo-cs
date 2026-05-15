"""Project 4
Quinn Smiley, 2026-04-27, CS 211"""


# One global environment variable
from typing import Dict
ENV: Dict[str, "Const "] = {}



class Expr():
 """Abstract base class of all expressions."""
 def eval(self) -> "Const":
    """Implementations of eval should return an integer constant."""
    raise NotImplementedError(
        f"'eval' not implemented in {self.__class__.__name__}\n"
        "Each concrete Expr class must define 'eval'")
 def __str__(self) -> str:
    """Implementations of __str__ should return the expression
    in algebraic notation"""
    raise NotImplementedError(
        f"'__str__' not implemented in {self.__class__.__name__}\n"
        "Each concrete Expr class must define '__str__'")
 def __repr__(self) -> str:
    """Implementations of __repr__ should return a string that
    looks like the constructor,
    e.g., Plus(Const(5), Const(4))
    """
    raise NotImplementedError(
        f"'__repr__' not implemented in {self.__class__.__name__}\n"
        "Each concrete Expr class must define '__repr__'")



class Const(Expr):
 def __init__(self, number):
      self.number = number
    
 def __str__(self):
      return f"{self.number}"

 def __repr__(self):
       return f"Const({self.number})"
    
 def eval(self):
       return self

 def __eq__(self, other: Expr):
       return isinstance(other, Const ) and self.number == other.number
 








# Variables and Assignment
class Var(Expr):
 def __init__(self, name: str):
       self.name = name
 def __str__(self):
       return self.name
 def __repr__(self):
       return f"Var({self.name})"
 def eval(self):
       global ENV
       if self.name in ENV:
          return ENV[self.name]
       else:
          raise UndefinedVariable(f"{self.name} has not been assigned a value")
 
 def assign(self, value: Const):
     global ENV
     ENV[self.name] = value


class UndefinedVariable(Exception):
 """Raised when expression tries to use a variable that
 is not in ENV
 """
 pass


class Assign(Expr):
 """Assignment: x = E represented as Assign(x, E)"""
 def __init__(self, left: Var, right: Expr):
       assert isinstance(left, Var) # Can only assign to variables!
       self.left = left
       self.right = right

 def eval(self) -> Const :
       r_val = self.right.eval()
       self.left.assign(r_val)
       return r_val
 
 def __str__(self):
       return f"{self.left} = {self.right}"
 
 def __repr__(self):
       return f"Assign({repr(self.left)}, {repr(self.right)})"
 








# Operations
class BinOp(Expr):
 def __init__(self, left: Expr, right: Expr, symbol: str="?Operation symbol undefined"):
      self.left = left
      self.right = right
      self.symbol = symbol

 def __str__(self) -> str:
      return f"({self.left} {self.symbol} {self.right})"
   
 def __repr__(self, operator: str):
      return (f"{operator}(Const({(self.left)}), Const({(self.right)}))")
   
 def _apply(self, left_val: int, right_val: int) -> int:
      """Each concrete BinOp subclass provides the appropriate method"""
      raise NotImplementedError(
         f"'_apply' not implemented in {self.__class__.__name__}\n"
         "Each concrete BinOp class must define '_apply'")
   
 def eval(self) -> "Const ":
      """Each concrete subclass must define _apply(int, int)->int"""
      left_val = self.left.eval()
      right_val = self.right.eval()
      return Const(self._apply(left_val.number, right_val.number))
 

   
class Plus(BinOp):
 def __init__(self, left, right):
      super().__init__(left, right, symbol = "+")

 def _apply(self, left_val: int, right_val: int) -> int:
      return left_val + right_val

 def __repr__(self):
       return (f"Plus(Const({(self.left)}), Const({(self.right)}))")
    


class Minus(BinOp):
 def __init__(self, left, right):
      super().__init__(left, right, symbol = "-")

 def _apply(self, left_val: int, right_val: int) -> int:
      return left_val - right_val

 def __repr__(self):
      return (f"Minus(Const({(self.left)}), Const({(self.right)}))")
 

    
class Times(BinOp):
 def __init__(self, left, right):
      super().__init__(left, right, symbol = "*")
   
 def _apply(self, left_val: int, right_val: int) -> int:
      return left_val * right_val

 def __repr__(self) -> str:
      return f"Times({repr(self.left)}, {repr(self.right)})"
   


class Div(BinOp):
 def __init__(self, left, right):
      super().__init__(left, right, symbol = "//")

 def _apply(self, left_val: int, right_val: int) -> int:
      return left_val // right_val

 def __repr__(self):
      return f"Div({repr(self.left)}, {repr(self.right)})"
 








# Unary Operations
class UnOp(Expr): # Used Cursor to understand how to best set up UnOp
 def __init__(self, left, symbol: str = "?"):
      self.left = left
      self.symbol = symbol
      
 def __str__(self):
      return f"({self.symbol}({self.left}))"
   
 def _apply(self, left_val: int): 
       raise NotImplementedError
   
 def eval(self) -> "Const":
       left_const = self.left.eval()
       return Const(self._apply(left_const.number))
 


class Abs(UnOp):
 def __init__(self, left: Expr):
       super().__init__(left, symbol = "@")

 def _apply(self, left_val: int):
       return abs(left_val)
 
 def __repr__(self):
     return f"Abs({repr(self.left)})"
 


class Neg(UnOp):
 def __init__(self, left: Expr):
       super().__init__(left, symbol = "~")
 
 def _apply(self, left_val: int):
       return -left_val
 
 def __repr__(self):
       return f"Neg({repr(self.left)})"