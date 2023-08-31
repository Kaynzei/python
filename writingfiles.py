"""
out_file2 = open("C:/Users/ADMIN PC/Documents/content.txt", "w")
out_file2.write('life no hard na you won make am')
""" 
#If the code above is ran, it will overwrite the existing file and replace all in it with what i have written in the bracket

#the code below will create a new file called practice in the document folder and write something inside it.
"""
out_file2 = open("C:/Users/ADMIN PC/Documents/practice.txt", "w")
out_file2.write('This is my training file for moving things in python')
"""

#to append(add a new line)
"""
out_file2 = open("C:/Users/ADMIN PC/Documents/content.txt", "a")
out_file2.write('\nThis is a new line by Baba key')
"""

python_file = open("C:/Users/ADMIN PC/Desktop/terminalfile.py",'w')
python_file.write('print(\'this is a new python file\')')