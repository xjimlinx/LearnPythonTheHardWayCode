from sys import argv
# import the modules argv from sys.
script, input_file = argv
# need two argv.
def print_all(f):
    print f.read()
# define a function that read the argc file.
def rewind(f):
    f.seek(0)
# ??? What is this ???
def print_a_line(line_count, f):
    print line_count, f.readline()
# define a function that print two args.
current_file = open(input_file)
# open the file input_file.
print "First let's print the whole file:\n"

print_all(current_file)
# print all the content of current_file. 
print "Now let's rewind, kind of like a tape."

rewind(current_file)
# I don't know what it is.
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
