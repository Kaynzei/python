#if the file is in thesame folder with our python file,all you just need to do is to declare a variable ,in that variable, open the file and state what will be done to the file
#variable = open('name of file.format', what u are to do)
#coun_file = open('countries.txt', 'r'). if not in thesame in location, paste file path


python_file = open('input.py', 'r')
print(python_file.readable())
print(python_file.readlines())
python_file.close


#for a file not in thesame folder.Remember ot change the backward slah to forward slash. 
#Then after copying that path,add the name of the file.file type

out_file = open("C:/Users/ADMIN PC/Documents/content.txt", "r")
print(out_file.readable())
print(out_file.readline())
print(out_file.readline())

out_file.close

#readline prints only a single line and then another when repeated.readlines prints everything in the file in a list form
  