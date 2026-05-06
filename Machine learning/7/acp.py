def solve_circuit(a, b, c):
    
    top_and = a & b
    
  
    mid_or = b | c
    
   
    bottom_and = b & c
    
    
    combined_and = mid_or & bottom_and
    
   
    q = top_and | combined_and
    
    return q


a_val = 1
b_val = 0
c_val = 1

result = solve_circuit(a_val, b_val, c_val)
print(f"Inputs: A={a_val}, B={b_val}, C={c_val}")
print(f"Output Q: {result}")