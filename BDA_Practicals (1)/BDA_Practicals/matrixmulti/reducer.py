import sys
from collections import defaultdict

# Fixed variable naming (removed spaces)
current_key = None
A_vals = defaultdict(float)
B_vals = defaultdict(float)

for line in sys.stdin:
    # Added missing '='
    key, value = line.strip().split('\t')
    matrix, index, val = value.split(',')
    
    if current_key and current_key != key:
        # Added missing '=' and '*' operator
        result = sum(A_vals[k] * B_vals[k] for k in A_vals if k in B_vals)
        print(f"{current_key}\t{result}")
        
        # Fixed variable names
        A_vals.clear()
        B_vals.clear()
        
    current_key = key
    
    if matrix == 'A':
        A_vals[index] = float(val)
    else:
        # Fixed fragmented lines and missing assignment
        B_vals[index] = float(val)

# Output the last key
if current_key:
    # Fixed typos ('fork', 'kin') and missing operators
    result = sum(A_vals[k] * B_vals[k] for k in A_vals if k in B_vals)
    print(f"{current_key}\t{result}")