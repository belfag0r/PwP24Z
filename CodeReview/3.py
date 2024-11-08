# 3_3
# pojawiło się wiele długich rozwiązań..
# jeżeli równe długości wystarczy
sum(a != b for a, b in zip(seq1, seq2))


# 3_4
def generator(sekwencja):
    podzial,i = [sekwencja[i:i+3] for i in range(0, len(sekwencja), 3)], 0 # <---
    while i < len(podzial):
        yield(slownik[podzial[i]])
        i+=1
# istotą generatora jest leniwe wartościowanie - oszczędzanie pamięci, tworzenie zawczasu listy kodonów niweluje ewentualne korzyści
