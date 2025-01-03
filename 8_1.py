# potpowiedź do zadania 8_1
# już to poprawiłem.. xD

zdanie1 = "To jest zdanie"
zdanie2 = "To jest kadjasf"

lista_zdan = [zdanie1, zdanie2]

vocab = set(sum([z.split() for z in lista_zdan], []))

print(vocab)

word_2_idx = {word: idx for idx, word in enumerate(vocab)}

print(word_2_idx)

"""
word_2_df = ...
word_2_idf = ...

wektory = []

for zdanie in lista_zdan:
    wektor_zdania = [0] * len(vocab)

    for word in zdanie:
        tf = zdanie.count(word)/len(zdanie)
        wektor_zdania[word_2_idx[word]] = tf*word_2_idf[word]

    wektory.append(wektor_zdania)
"""
