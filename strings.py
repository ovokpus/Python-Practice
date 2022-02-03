"""COUNT"""
#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Count"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (
    sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

# ====================================

data = "cloudacademy.python.2019"
letter1 = 'a'
word1 = 'cloud'
num1 = '2019'

# CODE1: Count occurrences of letters and words
print("CODE1:")
print(f"count '{letter1}' = {data.count(letter1)}")
print(f"count '{word1}' = {data.count(word1)}")
print(f"count '{num1}' = {data.count(num1)}")
print()

# CODE2: Get length of string
print("CODE2:")
length = len(data)
print(f"len '{data}' = {length}")
print()

# CODE3: Get max of string - the highest char in the string
print("CODE3:")
maximum = max(data)
print(f"max '{data}' = {maximum}")
print()

# CODE4: Get min of string - the lowest char in the string
print("CODE4:")
minimum = min(data)
print(f"min '{data}' = {minimum}")
print()


"""FIND"""

#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Find"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (
    sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

# ====================================

data = "cloudacademy.python.2019"
letter1 = 'a'
word1 = 'cloud'
num1 = '2019'

# CODE1: Find word/letter in string
print("CODE1:")
print(f"find '{letter1}' = {data.find(letter1)}")
# Find the index of the first 'a' starting at index 6
print(f"find '{letter1}' = {data.find(letter1,6)}")
print(f"find '{word1}' = {data.find(word1)}")
print(f"index '{num1}' = {data.index(num1)}")
print()

# CODE2: Check string endswith and/or startswith another string
print("CODE2:")
print(f"endswith = {data.endswith('2019')}")
print(f"startswith = {data.startswith(letter1)}")
print()

# CODE3: Is string alphanum, alpha, and/or digit
print("CODE3:")
print(f"isalnum = {data.isalnum()}")  # Not alphanumeric because of '.'
print(f"isalpha = {data.isalpha()}")  # Not alpha because of '.' and digits
print(f"isdigit = {num1.isdigit()}")
print()


"""FORMAT"""
#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Format"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (
    sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

# ====================================

data = "cloudacademy.PYTHON.2019"
data_spaces = "     DevOps"
letter1 = 'a'
word1 = 'cloud'
num1 = '2019'

# CODE1: Strip format string
print("CODE1:")
print(f"strip = {data_spaces.strip()}")
print(f"lstrip = {data.lstrip(word1)}")
print(f"rstrip = {data.rstrip(num1)}")
print()

# CODE2: Lower and upper case string
print("CODE2")
print(f"upper = {data.upper()}")
print(f"lower = {data.lower()}")
print()

# CODE3: Swap case string
print("CODE3")
print(f"swapcase = {data.swapcase()}")
print()

# CODE4: Title case string
print("CODE4")
print(f"title = {data.title()}")
print()

# CODE5: Center string
print("CODE5")
print(word1.center(20))
print(word1.center(20, '*'))
print()

# CODE6: Left and Right adjust string
print("CODE6")
print(word1.ljust(20, '*'))
print(word1.rjust(20, '*'))
print()


"""SPLIT"""
#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Split"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (
    sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

# ====================================

data = "cloudacademy.python.2019"
letter1 = 'a'
word1 = 'cloud'
num1 = '2019'

# CODE1: Split and Partition word
print("CODE1:")
print(f"split = {data.split('.')}")
print(f"partition = {data.partition('python')}")
print()


# CODE2: Join on letter
print("CODE2:")
print(f"join = {'*'.join(word1)}")
print(f"join = {'*'.join([letter1, word1, num1])}")
print()

# CODE3: Replace word/letter in string
print("CODE3:")
print(f"replace = {data.replace('.','*')}")
print(f"replace = {data.replace(word1,num1)}")
print()
