#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Removed the extra spaces and added the missing '='
    tokens = line.strip().split(',')
    
    if tokens[0] == 'A':
        for k in range(0, 2): # assuming output matrix has 2 columns
            # Fixed spacing
            print(f"{tokens[1]},{k}\tA,{tokens[2]},{tokens[3]}")
            
    elif tokens[0] == 'B':
        for i in range(0, 2): # assuming output matrix has 2 rows
            # Added missing closing bracket for tokens[1]
            print(f"{i},{tokens[2]}\tB,{tokens[1]},{tokens[3]}")