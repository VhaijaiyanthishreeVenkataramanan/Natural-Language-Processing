# PROGRAMMING ASSIGNMENT 1 - VHAIJAIYANTHISHREE VENKATARAMANAN
# THIS PROGRAM USES PYTHON VERSION 3 (3.6.4)
# THE LIBRARIES USED ARE:
# 		1)REGULAR EXPRESSIONS
#		2)NUMPY
# TO EXECUTE THIS PROGRAM PLEASE USE THE FOLLOWING COMMAND:
#			python3 Vhaijaiyanthi_pa1.py
# ONCE THE PROGRAM IS EXECUTED USING THE ABOVE COMMAND, PLEASE ENTER THE NAMES OF THE 
# REQUIRED SOURCE AND THE TARGET FILES IN THE RESPECTIVE FIELDS THAT APPEAR ON THE SCREEN
# *THANK YOU FOR YOUR TIME*

import re
import numpy as np
import copy

# FETCHING THE INPUT SOURCE AND TARGET FILES FROM THE USER
print("\n\nUniversity of Central Florida \nCAP6640 Spring 2018 - Dr. Glinos \n\nText Similarity Analysis by <Vhaijaiyanthishree Venkataramanan>\n\n")
origin = input("Source File: ")
destination = input("Target File: ")


# OPENING AND READING THE SOURCE AND THE TARGET FILES
source = open(origin).read()
target = open(destination).read()
print("\n")


#DISPLAYING THE RAW TOKENS
print("Raw Tokens:")
print("  Source > " + source)
print("  Target > " + target)


# TOKENIZATION OF THE RAW TOKENS
#CONVERSION OF THE TOKENS TO LOWER CASE
source = source.lower()
target = target.lower()

# ADDING SPACES BETWEEN ALPHANUMERIC AND NON-ALPHANUMERIC CHARACTERS
def my_replace(match):
    if match.group(1) is not None:
        return '{} '.format(match.group(1))  #SPACE BEFORE WORD
    else:
        return ' {}'.format(match.group(2))  #SPACE BEFORE SPACE
        
# CONVERTING THE RAW TOKENS TO NORMALIZED TOKENS
print("\nNormalized Tokens:")     
   
def normalize(string):      
	q = re.compile(r'^(\W+)|(\W+)$') # checks if the there is non alpha numeric characters at the beginning or at the end of a word 
	strings_list = []
	for term in string.split():
		e = list(filter(bool,q.sub(my_replace, term).split(' ')))
		if e:
			if len(e) == 1:
				strings_list.append(''.join(e))
			else:
				if any(f.isalnum() for f in e):
					for token in e:
						if not token.isalnum():
							index = e.index(token)
							e[index] = ' '.join(token)
						strings_list.append(' '.join(e))
	return strings_list
source = " ".join(normalize(source))
target = " ".join(normalize(target))


# SEPARATING APOSTROPE FROM WORDS
def replaces(item):
    if item.endswith("'s"):
        return re.match(r"(.*)('s$)", item).groups()
    elif item.endswith("n't"):
        return re.match(r"(.*)n't$", item).groups() + ("not",)
    elif item.endswith("'m"):
        return re.match(r"(.*)'m$", item).groups() + ("am",)
    else:
        return item

# JOINING THE STRINGS TOGETHER AFTER NORMALIZATION        
sections = []
for first_half in source.split():
    a = replaces(first_half)
    if isinstance(a, tuple):
        for x in a:
            sections.append(x)
    else:
        sections.append(a)

source = " ".join(sections)
print("  Source > " + source)
sections = []
for first_half in target.split():
    a = replaces(first_half)
    if isinstance(a, tuple):
        for x in a:
            sections.append(x)
    else:
        sections.append(a)

target = " ".join(sections)
print("  Target > " + target)


# CONSTRUCTING THE EDIT DISTANCE TABLE AND THE BACKTRACE TABLE
print("\nEdit Distance Table: \n")

source_input = source.split()
target_input = target.split()
r = len(source_input)
c = len(target_input)

#USING THE ALIGNMENT PARAMETERS
gap = -1
mismatch = -1
match = 2

# INITIALIZING THE EDIT DISTANCE MATRIX AND THE BACKTRACE MATRIX

scoreM = [[0 for col in range(c + 1)] for row in range(r + 1)]
tracebackM = [['' for col in range(c + 1)] for row in range(r + 1)]
END, DIAG, UP, LT = ('', 'DI', 'UP', 'LT')

# FILLING THE BACKTRACE TABLE
def moves(up, left, diag, tot_val):
    if tot_val == 0:
        return ''
    elif tot_val == up:
        return UP
    elif tot_val == left:
        return LT
    elif tot_val == diag:
        return DIAG
    else:
        raise ValueError('invalid')
        
# FILLING THE EDIT DISTANCE TABLE      
for i in range(1,r+1):
    for j in range(1,c+1):
        top_score = scoreM[i-1][j] + gap;
        left_score= scoreM[i][j-1] + gap;
        if source_input[i-1] == target_input[j-1]:
            diagonal_score = scoreM[i-1][j-1] + match;
        else:
            diagonal_score = scoreM[i-1][j-1] + mismatch;
        X = max(0,top_score,left_score,diagonal_score); 
        scoreM[i][j] = X
        tracebackM[i][j] = moves(top_score,left_score,diagonal_score, X)
       

# MODIFIYING THE STRING IN ORDER TO PRINT ONLY THE FIRST THREE LETTERS OF THE STRING        
def stringModifier(input_seq_list):
    list_modify = []
    for str in input_seq_list:
        if len(str) >= 3:
            list_modify.append(str[:3])
        else:
            list_modify.append(str)
    return list_modify
        
# PRINTING THE SOURCE AND THE TARGET STRINGS IN EDIT DISTANCE AND BACKTRACE TABLES
def score_output(source, target, table):
    
    src = stringModifier(list(source))
    src.insert(0,'#')
    tgt = stringModifier(list(target))
    tgt.insert(0,'#')
    matrix = copy.deepcopy(table)
    for i in range(len(src)):
        row = matrix[i]
        row.insert(0, i)
        row.insert(1, src[i])
    row_one = ['','']
    row_two = ['',''] + tgt
    for i in range(len(tgt)):
        row_one.append(i)
    matrix.insert(0, row_one)
    matrix.insert(1, row_two)

    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
        	print('{0}'.format(str(matrix[row][col])).center(4), end='   ')          
        print()
    
#PRINTING THE FINAL EDIT DISTANCE TABLE       
score_output(source_input, target_input, scoreM)

#PRINTING THE FINAL BACKTRACE TABLE
print("\nBacktrace Table: \n")
score_output(source_input, target_input, tracebackM)

#TO FIND THE MAXIMUM VALUE IN THE EDIT DISTANCE TABLE
array_max = np.max(np.array(scoreM))
print("\nMaximum value in distance table:", array_max)

# FINDING THE MAXIMA AMONGST THE MAXIMAL VALUES IN THE EDIT DISTANCE TABLE
scoreM_array = np.array(scoreM)
indices = np.where(scoreM_array == scoreM_array.max())
print("\nMaxima:")
for z in zip(indices[0], indices[1]):
    print("    ",list(z),"\n")

# CONSTRUCTING THE MAXIMAL-SIMILARITY ALIGNMENTS AND PRINTING THEM 
def string_edit(source_aligned, target_aligned):
    alignment_s = []
    for base1, base2 in zip(source_aligned, target_aligned):
        if base1 == base2:
            alignment_s.append(' ')
        elif '-' in base1:
            alignment_s.append('i')
        elif '-' in base2:
            alignment_s.append('d')
        else:
            alignment_s.append('s')

    return alignment_s
    
def alignment_sequence(max_positions, tracebackM, count):
    source_input_aligned = []
    target_input_aligned = []
    l, m = max_positions
    move = tracebackM[l][m]
    while move != END:
        if move == DIAG:
            source_input_aligned.append(source_input[l - 1])
            target_input_aligned.append(target_input[m - 1])
            l -= 1
            m -= 1
        elif move == UP:
            source_input_aligned.append(source_input[l - 1])
            target_input_aligned.append('-')
            l -= 1
        else:
            source_input_aligned.append('-')
            target_input_aligned.append(target_input[m - 1])
            m -= 1
        move = tracebackM[l][m]
        
    l1 = len(max(source_input_aligned, key=len))
    l2 = len(max(target_input_aligned, key=len))
    l3 = max(l1, l2)

    print("\n   Alignment {0} (length {1}):".format(count, len(source_input_aligned)))

    print("       Source at    {0}:".format(l), end='')
    for str1 in source_input_aligned[::-1]:
        print("{0}".format(str1).center(l3 + 3), end='')
    print()

    print("       Target at    {0}:".format(m), end='')
    for str2 in target_input_aligned[::-1]:
        print("{0}".format(str2).center(l3 + 3), end='')
    print()

    string_edited = string_edit(source_input_aligned[::-1], target_input_aligned[::-1])
    print("       Edit Action   :", end='')
    for str3 in string_edited:
        print("{0}".format(str3).center(l3 + 3), end='')
    print()

    return source_input_aligned[::-1], target_input_aligned[::-1], count

        
print("\nMaximal-similarity alignments:")
count = 0
for z in zip(indices[0], indices[1]):
    alignment_sequence(z, tracebackM, count)
    count += 1

print("\n")




