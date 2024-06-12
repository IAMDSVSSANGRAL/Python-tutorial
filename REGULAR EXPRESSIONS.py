#!/usr/bin/env python
# coding: utf-8

# # Introduction to Regex
# A regular expression (regex) is a sequence of characters that define a search pattern.
# Use cases include validation, searching, and extracting text.

# In[100]:


#importing necessary liabrary
import re


# ### Concept of escape sequence

# Escape sequences are combinations of characters used to represent characters that cannot be typed or displayed directly. They are preceded by a backslash (\) and are interpreted specially by the language or system. Escape sequences are commonly used in programming languages, text editors, and command-line interfaces to represent special characters, control characters, and non-printable characters.
# 
# 
# In Python and many other programming languages, escape sequences are used in string literals to represent characters such as newline (\n), tab (\t), backspace (\b), and others.
# 
# 
# Here are some common escape sequences used in Python:
# 
# \n: Newline - Moves the cursor to the beginning of the next line.
# 
# \t: Tab - Inserts a tab character.
# 
# \r: Carriage Return - Moves the cursor to the beginning of the current line.
# 
# \b: Backspace - Removes the previous character.
# 
# \\: Backslash - Inserts a literal backslash.
# 
# \': Single Quote - Inserts a literal single quote (useful in single-quoted strings).
# 
# \": Double Quote - Inserts a literal double quote (useful in double-quoted strings).
# 
# \xhh: Hexadecimal Escape - Inserts the character with the hexadecimal ASCII value hh.
# 
# \uhhhh or \Uhhhhhhhh: Unicode Escape - Inserts the Unicode character with the hexadecimal code point hhhh or hhhhhhhh.
# 

# In[182]:


print("\\")


# In[186]:


print("I'D")


# In[194]:


print('\t\t\tTab')


# In[105]:


print('Name\tAge\tLocation')
print('Alice\t30\tNew York')
print('Bob\t25\tLos Angeles')


# In[112]:


print("This is a backslash: \\")


# In[114]:


print('It\'s a beautiful day')


# In[117]:


print("She said, \"Hello!\"")


# In[118]:


print("Hello\nWorld")


# In[195]:


print("Hello\rWorld\rvishal")


# In[123]:


print("Hello\bWorld")


# In[132]:


print("\x44\x42\x43")


# FOR UNICODE HEXADECIMAL CODE USE THESE:
# https://www.rapidtables.com/code/text/unicode-characters.html

# In[165]:


print("\U+2192")


# In[166]:


print("\U00002764")


# ### Types of strings:

# In[169]:


unicode_string = "Café"  # Unicode string
print(unicode_string)


# In[170]:


byte_string = b'binary data'
print(byte_string)


# In[172]:


name = "Alice"
age = 30
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)


# In[174]:


byte_array = bytearray(b'hello')
print(byte_array)


# In[175]:


mutable_string = list("hello")
mutable_string[0] = 'H'  # Modify the first character
mutable_string = ''.join(mutable_string)  # Convert back to string
print(mutable_string)


# In[167]:


single_quoted = 'Hello'
double_quoted = "World"
triple_quoted = '''This is a 
                  multi-line string'''


# In[178]:


empty_string = ''
print(empty_string)


# In[179]:


print(r'C:\Users\Name') # raw stirng


# In[7]:


#example of raw string -  r is used to denote raw string 
print(r'\tTab')


# In Python, re.compile() is a function provided by the re module, which is used for working with regular expressions (regex). The re.compile() function compiles a regular expression pattern into a regex object, which can then be used for various operations such as searching, matching, and replacing text within strings.
# 
# 
# Here's how re.compile() works:
# 
# 
# Compilation: The re.compile() function takes a regex pattern as its first argument and compiles it into a regex object.
# 
# 
# Regex Object: The compiled regex object represents the regex pattern, and it can be reused for multiple string operations without having to recompile the pattern each time.
# 
# 
# Efficiency: Compiling the regex pattern with re.compile() can improve the performance of regex operations, especially if the same pattern is used multiple times in a program.
# 
# 
# Flags: Optional flags can be provided as a second argument to re.compile() to modify the behavior of the regex pattern, such as case-insensitive matching, multiline matching, and others.
# 
# 
# Usage: Once the regex object is created with re.compile(), it can be used with methods like search(), match(), findall(), finditer(), and sub() to perform various string operations based on the regex pattern.
# 

# In[10]:


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

havinsoh.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Vishal
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
bat
pat
flat
fat
'''


# .       - Any Character Except New Line
# 
# \d      - Digit (0-9)
# 
# \D      - Not a Digit (0-9)
# 
# \w      - Word Character (a-z, A-Z, 0-9, _)
# 
# \W      - Not a Word Character
# 
# \s      - Whitespace (space, tab, newline)
# 
# \S      - Not Whitespace (space, tab, newline)
# 
# 
# \b      - Word Boundary
# 
# \B      - Not a Word Boundary
# 
# ^       - Beginning of a String
# 
# $       - End of a String
# 
# 
# []      - Matches Characters in brackets
# 
# [^ ]    - Matches Characters NOT in brackets
# 
# |       - Either Or
# 
# ( )     - Group
# 
# 
# Quantifiers:
# 
# *       - 0 or More
# 
# +       - 1 or More
# 
# ?       - 0 or One
# 
# {3}     - Exact Number
# 
# {3,4}   - Range of Numbers (Minimum, Maximum)

# In[211]:


pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
print(matches)
for match in matches:
    print(match)


# In[212]:


print(text_to_search[1:4])


# In[214]:


pattern = re.compile(r'.')
matches = pattern.finditer(text_to_search)
for i in matches:
    print(i)


# In[221]:


text = 'vishal\nsingh\n   \t\tsangral'


# In[222]:


pattern = re.compile(r'\s')
matches = pattern.finditer(text)
for match in matches:
    print(match)


# In[223]:


pattern = re.compile(r'\n')
matches = pattern.finditer(text)
for match in matches:
    print(match)


# In[224]:


pattern = re.compile(r' ')
matches = pattern.finditer(text)
for match in matches:
    print(match)


# In[225]:


pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[17]:


#CONCEPT OF WORD BOUNDARY 
pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[234]:


#CONCEPT OF NO WORD BOUNDARIES
pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[235]:


##ONE MORE EXAMPLE
text = 'vishal singh Sa SaSa Sa'


# In[236]:


#CONCEPT OF WORD BOUNDARY 
pattern = re.compile(r'\bSa')
matches = pattern.finditer(text)
for match in matches:
    print(match)


# In[237]:


#CONCEPT OF NO WORD BOUNDARIES
pattern = re.compile(r'\BSa')
matches = pattern.finditer(text)
for match in matches:
    print(match)


# In[3]:


sentence = 'Start a sentence and then bring it to an end'


# In[5]:


#concept of carrot operator
pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)


# In[6]:


pattern = re.compile(r'^a')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)


# In[4]:


import re
pattern = re.compile(r'a')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)


# In[7]:


pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)


# In[11]:


pattern = re.compile(r'\d\d\d[*]\d\d\d[*]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[12]:


pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[15]:


pattern = re.compile(r'[4-7]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[17]:


pattern = re.compile(r'[k-zK-Z]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[42]:


pattern = re.compile(r'[^a-zA-Z]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[18]:


#here we are finding words not starting with b
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[19]:


pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[23]:


pattern = re.compile(r'Mr\.')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[24]:


pattern = re.compile(r'Mr\.?')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[28]:


pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[29]:


pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[42]:


import re

# Pattern that uses a greedy quantifier '*'
greedy_pattern = re.compile(r'<.*>')
# Pattern that uses a lazy quantifier '*?'
lazy_pattern = re.compile(r'<.*?>')

# Test string
text = "<div>Hello</div><span>World</span>"

# Find all matches using greedy and lazy quantifiers
greedy_matches = greedy_pattern.findall(text)
lazy_matches = lazy_pattern.findall(text)

print(f"Greedy matches: {greedy_matches}")
print(f"Lazy matches: {lazy_matches}")


# In[30]:


emails = '''
VishalSsangral@gmail.com
sangral.singh@university.edu
vishal-321-sangral@my-work.net
'''


# In[31]:


pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)


# In[32]:


pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(emails)
for match in matches:
    print(match)


# In[33]:


urls = '''
https://www.google.com
http://havinosh.com
https://youtube.com
https://www.isro.gov
'''


# In[34]:


print(urls)


# In[35]:


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)


# In[36]:


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0))


# In[37]:


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(1))


# In[38]:


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(2))


# In[39]:


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3))


# In[40]:


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3',urls)
print(subbed_urls)


# In[41]:


pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.findall(text_to_search)
for match in matches:
    print(match)


# ### Match Method
# The match method checks for a match only at the beginning of the string. If the pattern matches at the start, it returns a match object; otherwise, it returns None.

# In[43]:


import re

pattern = re.compile(r'\d+')

text1 = "123abc"
text2 = "abc123"

# Using match method
match1 = pattern.match(text1)
match2 = pattern.match(text2)

print(f"Match result for text1: {match1.group() if match1 else 'No match'}")  # Output: 123
print(f"Match result for text2: {match2.group() if match2 else 'No match'}")  # Output: No match


# In[98]:


#flags - re.IGNORECASE or use for re.I


# In[46]:


import re

pattern = re.compile(r'\d+')

text1 = "123abc"
text2 = "abc123"

# Using match method
match1 = pattern.finditer(text1)
match2 = pattern.finditer(text2)

for i in match1:
    print(i)
    
for i in match2:
    print(i)


# ### search Method
# The search method scans through the entire string and returns the first match it finds. It returns a match object if there is a match anywhere in the string, otherwise None.

# In[47]:


import re

pattern = re.compile(r'\d+')

text1 = "123abc"
text2 = "abc123"

# Using search method
search1 = pattern.search(text1)
search2 = pattern.search(text2)

print(f"Search result for text1: {search1.group() if search1 else 'No match'}")  # Output: 123
print(f"Search result for text2: {search2.group() if search2 else 'No match'}")  # Output: 123


# ### Finditer Method
# The finditer method returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string.
# 
# 

# In[48]:


import re

pattern = re.compile(r'\d+')

text = "123abc456def789"

# Using finditer method
matches = pattern.finditer(text)

for match in matches:
    print(f"Finditer match: {match.group()} at position {match.start()}-{match.end()}")


# ### Explanation of the Examples:
# match Method:
# 
# Behavior: Checks if the pattern matches from the beginning of the string.
# Example:
# text1: Matches because the string starts with digits (123).
# text2: Does not match because the string starts with letters (abc).
# search Method:
# 
# Behavior: Searches the entire string and returns the first occurrence of the pattern.
# Example:
# text1: Finds 123 at the beginning.
# text2: Finds 123 after the letters (abc).
# finditer Method:
# 
# Behavior: Finds all non-overlapping matches and returns them as an iterator of match objects.
# Example:
# text: Finds three matches: 123, 456, and 789.
# 

# ## Flags in regular expressions (regex) are special parameters that modify the behavior of the regex engine. They can be used to control how the pattern matching process is executed. Python's re module supports several flags that can be passed as optional parameters to regex functions. Here are some commonly used flags:
# 
# re.IGNORECASE (re.I): Makes the pattern case-insensitive, so it matches both uppercase and lowercase letters.
# 
# re.MULTILINE (re.M): Allows the ^ and $ anchors to match at the beginning and end of each line within a multiline string, rather than just at the beginning and end of the entire string.
# 
# re.DOTALL (re.S): Makes the dot (.) metacharacter match all characters, including newline characters (\n).
# 
# re.ASCII: Makes \w, \W, \b, \B, \d, \D, \s, and \S perform ASCII-only matching, disregarding any Unicode characters.
# 
# re.UNICODE (re.U): Makes \w, \W, \b, \B, \d, \D, \s, and \S perform Unicode matching.
# 
# re.VERBOSE (re.X): Allows you to write regex patterns more legibly by ignoring whitespace and comments within the pattern. Whitespace within the pattern is ignored, except when in a character class or preceded by an unescaped backslash. Additionally, # marks the start of a comment, which lasts until the end of the line.

# In[50]:


import re

# Using flags with compile method
pattern = re.compile(r'hello', re.IGNORECASE | re.MULTILINE)

# Using flags with search method
text = "Hello, World!\nHello, Universe!"
matches = pattern.findall(text)

print(matches)  # Output: ['Hello', 'Hello']


# In[51]:


import re

pattern = re.compile(r'hello.*world', re.DOTALL)

text = "hello\nworld"

match = pattern.search(text)
print(f"DOTALL match: {match.group() if match else 'No match'}")


# In[52]:


import re

pattern = re.compile(r'\w+', re.ASCII)

text = "café"

match = pattern.findall(text)
print(f"ASCII match: {match}")


# In[53]:


import re

pattern = re.compile(r'\w+', re.UNICODE)

text = "café"

match = pattern.findall(text)
print(f"UNICODE match: {match}")


# In[54]:


import re

pattern = re.compile(r'''
    \b      # Word boundary
    \d{3}   # Three digits
    -       # Hyphen
    \d{2}   # Two digits
    \b      # Word boundary
    ''', re.VERBOSE)

text = "Phone number: 123-45"

match = pattern.search(text)
print(f"VERBOSE match: {match.group() if match else 'No match'}")


# In[55]:


import re

pattern = re.compile(r'''
    ^hello      # Line starts with 'hello'
    .*          # Any character (dot) zero or more times (greedy)
    world$      # Line ends with 'world'
    ''', re.IGNORECASE | re.MULTILINE | re.DOTALL | re.VERBOSE)

text = "Hello\nworld"

match = pattern.search(text)
print(f"Combined flags match: {match.group() if match else 'No match'}")


# In[ ]:




