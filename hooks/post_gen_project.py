import os

os.system("isort .")
os.system("black .")

print("")
print("=====================")
print("Template initialized.")
print("Please create a git repository before running tox for the first time.")
print("=====================")