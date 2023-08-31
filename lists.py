countries = [ 'united kingdom' , 'ghana' , 'Nigeria' , 'Australia' , 'Newzealand' ] #the countries made up the list
print(countries) # i can target any country using an array: 01234
print(countries[1])
#to access the individual character in each country
print(countries[1][2])
print(countries[1:]) #the colon means u should get from that index to the end
print(countries[1:4]) #this is telling to end at index number 3
print(type(countries))#to know the type(list variable)
#to chnage or replace of those countries

countries[1] = 'united states'
print(countries)
print(len(countries)) #to know the amount of nations in the list