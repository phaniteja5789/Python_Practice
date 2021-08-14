#Remove SPSS from list and add SPARK into list

input_list=['SAS','R','PYTHON','SPSS']
input_list.pop()
input_list.append('SPARK')
print(input_list)


#Converting a String into List by Splitting with &
input_str="I Love DataScience & Python"
print(input_str.split('&'))

#Converting a List into a String with delimited by &
input_list_1=["Pythons Syntax is very easy to learn "," Python Syntax is very clear"]
print('&'.join(input_list_1))


#Extract Python from Nested List

input_list_2=[['SAS','R'],['Tableau','SQL'],['Python','JAVA']]

print(input_list_2[2][0])


#Output of t[0][2]
t=("disco",12,4.5)
print(t[0][2])

#Program to check if string is Palindrome or not if Yes print 1 if No print 0
print("Give input string as an input to check for palindrome")
input_str=input()
if input_str== input_str[-1::-1]:
    print ("String is Palindrome "+str(1))
else:
    print ("String is not Palindrome "+str(0))


#Reverse Order of Words in Sentence
print("Give Input Sentence as an input to check for Reversal of Words")
input_str1=input()
print(" ".join(input_str1.split()[-1::-1]))


#String Formatting

print("Provide a String to check the String formatting")
input_str2=input()
print('_'.join(input_str2.lower().split()))



