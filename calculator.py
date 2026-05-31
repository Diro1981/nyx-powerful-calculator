import math
import cmath
import os
from datetime import datetime

# Memory for storing results
memory = 0
history = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate(expression):
    global memory
    try:
        # Safe math context with powerful functions
        allowed_names = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "asin": math.asin, "acos": math.acos, "atan": math.atan,
            "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
            "sqrt": math.sqrt, "cbrt": lambda x: x**(1/3),
            "log": math.log, "log10": math.log10, "log2": math.log2,
            "exp": math.exp, "pow": pow, "abs": abs,
            "pi": math.pi, "e": math.e, "tau": math.tau,
            "degrees": math.degrees, "radians": math.radians,
            "factorial": math.factorial, "gcd": math.gcd,
            "lcm": math.lcm, "ceil": math.ceil, "floor": math.floor,
            "round": round, "complex": complex,
            # Complex math
            "polar": cmath.polar, "rect": cmath.rect,
        }
        
        # Allow memory recall
        allowed_names["M"] = memory
        allowed_names["mem"] = memory
        
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        
        # Store in history and memory
        history.append(f"{expression} = {result}")
        if len(history) > 50:
            history.pop(0)
        memory = result
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def show_help():
    print("\n=== POWERFUL CALCULATOR COMMANDS ===")
    print("Basic: 2+3*4, 15/3, 2**8")
    print("Trig: sin(30* pi/180), cos(radians(45))")
    print("Advanced: sqrt(16), log(100), 2**10, factorial(5)")
    print("Memory: M (last result), mem")
    print("Special: clear, history, help, exit")
    print("===================================\n")

print("=== NYX POWERFUL CALCULATOR ====")
show_help()

while True:
    try:
        expr = input("\n> ").strip()
        
        if expr.lower() in ['exit', 'quit']:
            print("Goodbye.")
            break
        elif expr.lower() == 'clear':
            clear_screen()
            print("=== NYX POWERFUL CALCULATOR ===")
            continue
        elif expr.lower() == 'history':
            print("\n--- HISTORY ---")
            for item in history[-10:]:
                print(item)
            print("---------------")
            continue
        elif expr.lower() == 'help':
            show_help()
            continue
        elif expr == '':
            continue
            
        result = calculate(expr)
        print(f"Result: {result}")
        
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")