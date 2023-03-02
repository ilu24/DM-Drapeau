def flagsort(tab):
    b = 0
    r = len(tab)-1
    w = 0
    R = False
    
    while R == False:
        if tab[w] == "bleu":
            tab[w], tab[b] = tab[b], tab[w]
            w += 1
            b += 1
        if tab[w] == "blanc":
            w +=1
        if tab[w] == "rouge":
            tab[r], tab[w] = tab[w], tab[r]
            r -= 1
        if w >= r:
            R = True
T = ["rouge", "rouge","bleu", "rouge", "blanc","blanc", "rouge","bleu", "bleu", "blanc", "bleu", "bleu", "rouge", "blanc","rouge","bleu", "blanc","bleu"]
flagsort(T)
print(T)