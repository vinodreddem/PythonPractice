#Strings are creed by using quotes
str_1 = "double quoted"
str_2= 'single quoted'

print (str_1,str_2)
why_1 = 'to use double quote in the string "Hello" then use single quote for string representation '
why_2 = "to use single quote inside the string say reddem's use double quotes in string declaration"
print (why_1)
print(why_2)

why_not_1 = "It is \"Hello\" greetingd "
print (why_not_1)

why_not_2 = 'It\'s greetingd '
print (why_not_2)

# \n is used for new line and \t used for tab \\ is used for black slash in the string
esc_seq1= "its example \n sequence \t for blackslash \\"
print(esc_seq1)

# We have raw Strings prevented from the escape sequences , if we use 'r' before string declaration
#then it is a raw string so escape sequences will not effect
raw_line_1 = r'it is a \nrawString\nescape sequence \nwill not effect'
raw_line_2 =r"itd\trawstring\\"
print(raw_line_1)
print(raw_line_2)

sub_text ="double"

#concatination of String
print(sub_text+sub_text)

#repeat same char multiple times by using the * symbol
print('a' * 50)

#return length ,min and Max functions in the given string.
print("the length of the String " ,len(sub_text))
print("the min of the String " ,min(sub_text))
print("the max of the String " ,max(sub_text))

main_text= "It's a double value"
#Check the given string is present in the main string or not by using
#'not in' and 'in' functions 
print("The sub string is present in the main string  ", sub_text in main_text)
print("The sub string is not  present in the main string  " , sub_text not in main_text)

#String objects have many methods like
print('the count is ' ,sub_text.count('e')) # number of e is existing in the string 
print('the count is ' ,sub_text.index('e')) # index where the e is exists
print('the count is ' ,sub_text.index('u',0,5)) # index where the e is exists,if char is not exists then "ValueError: substring not found" not exists 
print('the count is ' ,sub_text.find('e')) # if string exists returns true else returns false

# We have startWith , upper ,lower ,endsWith ,split , join , isalpha, isdigit() mehods exists

zenPython = '''

The Zen of Python, by Tim Peters



Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!

'''

words = zenPython.split(sep = " ",maxsplit=-1)
print(len(words))

print(words)
words =[ w.strip('\n.*!-.') for w in words]
print(words)

words = [w.replace('\n','') for w in words]
print(words)
#print(words)

words_list = []
mulltiline_list = zenPython.splitlines()
for line in mulltiline_list :
    if line != "":
        wordsList_inline =line.split()
        words_list.extend(wordsList_inline)
print(len(words_list))
print(words_list)


words_list = [w.lower() for w in words_list]
print(words_list)
print(len(words_list))

#How can we get a unique set of values from a list -We need to use set

unique_words = set(words_list)
print(len(unique_words))

print(unique_words)


dict = {word : words_list.count(word) for word in  words_list }

total_words =0;
for value in dict :
    total_words += dict[value]
print(total_words)
print("dict is",dict)


frequent_words  = { words :count for (words,count) in dict.items() if count >5}

print(frequent_words)

