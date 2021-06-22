from sys import argv

script, filename =argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again =open(file_again)

print(txt_again,read())
#不要在idle模式下运行，在cmd环境下运行，运行的命令(python ex-15.py ex-15_sample.txt)
