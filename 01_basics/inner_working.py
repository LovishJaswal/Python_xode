print("Hello World!")

def print_name(x):
    print(x)

print_name("Tanisha")

# When you run a Python file, Python first reads your source code and converts it into bytecode ,
# which is a low-level, platform-independent version of your program that the Python Virtual Machine (PVM)
# can execute. To save time in future runs, Python stores this bytecode inside the __pycache__ folder
# so it doesn’t have to recompile the file every time — it simply checks if the source code changed, and if not, 
# it loads the cached bytecode for faster execution (this is usually
# hidden from you in normal circumstances). The same thing happens when you import another file:
# Python doesn’t just “grab” the function you asked for — it must execute the entire imported file once
# to create all its functions and variables in memory, which is why any print statements or top-level code
# inside that file also run. After this first execution, Python keeps the module loaded and uses the
# cached bytecode from __pycache__ so the imported file isn’t re-executed repeatedly.
# In simple words: Python compiles to bytecode → stores it in __pycache__ → PVM runs the bytecode → 
# and imports also trigger this process once to prepare everything.