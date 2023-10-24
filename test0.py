from english_words import get_english_words_set
a = list(get_english_words_set(['web2'], lower=True))
lsta = ("qweroiutpoetklfdskfmmvmusacxocxvsdklfk", "America", "dad", "banana")
x = lsta[0].lower()
okay = True
alpha = {}
for j in x:
    if j not in alpha:
        alpha[j] = 1
    else:
        alpha[j] += 1
for j in lsta[1:]:
    y = {}
    for c in j:
        if c not in alpha:
            alpha[c] = 1
        else:
            alpha[c] += 1
    if j.lower() in a:
        for c in y.keys():
            if alpha.get(c, 0) < y.get(c):
                okay = False
    else:
        okay = False
    if okay:
        print(j.lower())
    okay = True
a.sort(key=len, reverse=True)
print(a)