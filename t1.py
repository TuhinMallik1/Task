filename= "problem_sheet.csv"
import os, sys, pandas as pd
f1 = [i.split(",") for i in open(filename).readlines()]
for j, i in enumerate(f1):
	if 'Data' in i[0]:
		two=f1[j+1:]


df = pd.DataFrame(two[1:],columns =two[0])

parse = list(df["index2"])

reversestr=[]
complementstr=[]

def complement(string):
	three=[]
	complementdict={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	for i in string:
		three.append(complementdict[i])
	three="".join(three)
	return three


for i in parse:
	reversestr.append(i[::-1])
	complementstr.append(complement(i[::-1]))


print("Original\tReverse\tReverse Complement")
for i, j in enumerate(parse):
	print(j+"\t"+reversestr[i]+"\t"+complementstr[i])

