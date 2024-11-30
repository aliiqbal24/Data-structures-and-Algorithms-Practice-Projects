def fractal_eval(expr):
   
    while "[" in expr:
       
        start = expr.rfind("[")
        end = expr.find("]", start)
        
        inner_result = fractal_eval(expr[start + 1:end])
       
        squared_result = str(inner_result ** 2)
       
        expr = expr[:start] + squared_result + expr[end + 1:]
    
   
    return eval(expr)

def main():
    exp = input()
    print(round(fractal_eval(exp)))

if __name__ == "__main__":
    main()


