import math
import random
import latexify
import re

class Calculator:
  def __init__(self):
    pass

  def simpleMath(self,input1,input2,selected_operation):
    if selected_operation == 'add':
      return input1 + input2

    elif selected_operation == 'subtract':
      return input1 - input2

    elif selected_operation == 'multiply':
      return input1 * input2

    elif selected_operation == 'divide':
      if input2 != 0:
        return input1 / input2
      else:
        return "Error: Division by zero"

    elif selected_operation == 'pemdas':
      return eval(str(input1), {"__builtins__": None}, vars(math))
    else:
      return "Error: Invalid operation selected" 

  def advancedMath(self,topic,selected_operation, args,shape_type=None):
    if topic == "algebra":
      print(self.algebra(selected_operation,args))

    elif topic == "geometry":
      print(self.geometry(selected_operation,shape_type,args))

    elif topic == "trigonometry":
      print(self.trigonometry(selected_operation,args))

    else:
      return "Error: Invalid operation type"

  def algebra(self,selected_operation,args): 
    if selected_operation == 'exponent':
      base, exponent = args
      return base ** exponent 
      
    elif selected_operation == "single line":
      expression = args[0]
      return eval(expression)

    elif selected_operation == "linear":
      a, b, c = args
      discriminant = b**2 - 4*a*c

      if discriminant < 0:
          return "No real roots exist for this equation.", None 

      root1 = (-b + math.sqrt(discriminant)) / (2 * a)  
      root2 = (-b - math.sqrt(discriminant)) / (2 * a)  
      return root1, root2

    elif selected_operation == "quadratic":
      a, b, c = args
      if a == 0:
          if b == 0:
               return "Not a valid equation (a and b are both zero)."
          else:
               return f"Linear equation, single root: {-c/b}"

      discriminant = b**2 - 4*a*c
      root1 = (-b + math.sqrt(discriminant)) / (2 * a)
      root2 = (-b - math.sqrt(discriminant)) / (2 * a)
      return root1, root2

    elif selected_operation == "inequalities":
      val1, val2, symbol = args
      ops = {'>': val1 > val2, '<': val1 < val2, '>=': val1 >= val2, '<=': val1 <= val2}
      return ops.get(symbol, "Invalid Symbol")

    elif selected_operation == "systems of equations":
      a1, b1, c1, a2, b2, c2 = args
      det = a1*b2 - a2*b1
      if det == 0:
        return "No unique solution"
      x = (c1*b2 - c2*b1) / det
      y = (a1*c2 - a2*c1) / det
      return x, y

    elif selected_operation == "functions":
      expression, x = args
      safe_expr = expression.replace("x", str(x))
      return eval(safe_expr)

    elif selected_operation == "transformations":
      x, y, transform_type, value = args

    elif selected_operation == "polynomials":
      a, n = args
      return f"{a*n}x^{n-1}"

    elif selected_operation == "rational":
      a, b = args
      if b == 0:
        return "Undefined (division by zero)"
      gcd = math.gcd(a, b)
      return f"{a//gcd}/{b//gcd}"

    elif selected_operation == "linear functions":
      m, b, x = args
      return m * x + b

    elif selected_operation == "quadratic functions":
      a, b, c, x = args
      return a*x*x + b*x + c

    elif selected_operation == "domain":
      if args < 0:
        raise ValueError("Input x must be >= 0 (math domain error for square root)")
      return math.sqrt(args)

    elif selected_operation == "range":
      if args < 0:
        raise ValueError("Input x must be >= 0 (math domain error for square root)")
      return math.sqrt(args)

    elif selected_operation == "slope":
      x1, y1, x2, y2 = args
      if x2 == x1:
          return "Undefined (vertical line)"
      return (y2 - y1) / (x2 - x1)

    elif selected_operation == "simplify":
      numerator, denominator = map(int, args.split('/'))
      common = math.gcd(numerator, denominator)
      simplified_n = numerator // common
      simplified_d = denominator // common
      return f"{simplified_n}/{simplified_d}"

    elif selected_operation == "factor":
      n = int(args)
      if n < 2:
        return [n]

      factors = []
      divisor = 2
      while divisor * divisor <= n:
        while n % divisor == 0:
          factors.append(divisor)
          n //= divisor
        divisor += 1
      if n > 1:
        factors.append(n)
      return factors

    else:
      return "Error: Invalid operation type"

  def geometry(self,selected_operation,shape_type,args):
    if shape_type == '3D' and selected_operation == 'volume sphere':
      radius = args[0]
      volume = (4/3) * math.pi * radius**3
      return volume

    elif shape_type == '3D' and selected_operation == 'volume prisim':
      length,width,height = args
      volume = length*width*height
      return volume

    elif shape_type == '3D' and selected_operation == 'volume cone':
      radius,height = args
      volume = (1/3)*radius**2*height
      return volume

    elif shape_type == '3D' and selected_operation == 'volume cylinder':
      radius,height = args
      volume = math.pi*radius**2*height
      return volume

    elif shape_type == '2D' and selected_operation == 'area rectangle':
      length, width = args
      return length * width

    elif shape_type == '2D' and selected_operation == 'area triangle':
      base,height = args
      area = (1/2)*base*height
      return area

  def trigonometry(self,selected_operation,args): 
    if selected_operation == 'sine':
      degrees = args[0]
      radians = math.radians(degrees)
      return math.sin(radians)
      
    elif selected_operation == 'cosine':
      degrees = args[0]
      radians = math.radians(degrees)
      return math.cos(radians)

    elif selected_operation == 'tangent':
      degrees = args[0]
      radians = math.radians(degrees)
      return math.tan(radians)
      
  def combine_like_terms(expression):
    tokens = re.findall(r"([+-]?\s*\d*[a-zA-Z]*)", expression)
    combined = {}

    for token in tokens:
        token = token.replace(" ", "")
        if not token: 
          continue

        match = re.search(r"([a-zA-Z]+)", token)
        if match:
            var = match.group(1)
            coeff_str = token.replace(var, "")
        else:
            var = ""
            coeff_str = token

        if coeff_str in ["", "+"]: coeff = 1
        elif coeff_str == "-": coeff = -1
        else: coeff = int(coeff_str)

        combined[var] = combined.get(var, 0) + coeff

    parts = []
    for var in sorted(combined.keys(), key=lambda x: (x == "", x)):
        val = combined[var]
        if val == 0: continue

        prefix = " + " if val > 0 and parts else ""
        if val < 0:
            prefix = " - " if parts else "-"
            val = abs(val)

        if var == "":
            parts.append(f"{prefix}{val}")
        elif val == 1:
            parts.append(f"{prefix}{var}")
        else:
            parts.append(f"{prefix}{val}{var}")

    return "".join(parts) or "0"
