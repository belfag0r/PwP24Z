import re


dna_seq = "ATGGGGTAAATGAAATGAATGGATAG"
#          ###GGG___###AAA___###GA___

kodon_start = 'ATG'
kodon_stop = ['TAA', 'TAG', 'TGA']
kodon_wzor = r'[ACGT]{3}'

#orf_wzor = re.compile(rf'{kodon_start}(?:{kodon_wzor})*(?:{"|".join(kodon_stop)})')

orf_wzor = re.compile(r"(?P<seq>(?=(ATG(?:[ACGT]{3})*)(?:TAA|TAG|TGA)))")

dopasowanie = re.findall(orf_wzor, dna_seq)

for dop in dopasowanie:
    print(dop)
