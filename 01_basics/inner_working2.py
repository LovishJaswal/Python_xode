from inner_working import print_name
print_name("Avantika")

# Output-
# Hello World!
# Tanisha
# Avantika

#WE can see that the main file is executed first and then the imported function is executed.
# Python does NOT copy-paste the function.
# It:
# -Opens inner_working.py
# -Executes the whole file top to bottom
# -Creates all functions (stores them)
# -Gives you the function you requested