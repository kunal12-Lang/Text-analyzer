def filtered(a):
    lst_1=[]

    for i in a:
        lst_1.append([i,a[i]])

    for j in range(len(lst_1)):
        for k in range(j+1,len(lst_1)):
            if lst_1[j][1]<lst_1[k][1]:
                lst_1[j] , lst_1[k] =lst_1[k] , lst_1[j]

    FILLER_WORDS = [
    "a", "an", "the", "and", "or", "but", "nor", "so", "yet", "if", "as",
    "of", "in", "on", "at", "to", "for", "with", "by", "from", "up", "down",
    "out", "off", "over", "under", "into", "onto", "about", "than", "then",
    "through", "after", "before", "between", "against", "upon", "again",

    "i", "me", "my", "myself", "we", "us", "our", "you", "your", "yourself",
    "he", "him", "his", "himself", "she", "her", "herself", "it", "its",
    "they", "them", "their", "who", "whom", "whose", "which", "what",
    "this", "that", "these", "those", "there", "here",

    "is", "am", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having", "do", "does", "did",
    "will", "would", "shall", "should", "can", "could", "may", "might", "must",


    "not", "no", "yes", "all", "any", "some", "such", "very", "too", "just",
    "when", "where", "why", "how", "while", "now", "also", "only", "more",
    "most", "other", "each", "both", "own", "same", "much", "many", "one",

    "s", "t", "d", "m", "ll", "ve", "re",
    "don", "doesn", "didn", "isn", "wasn", "weren", "aren", "won", "wouldn",
    "couldn", "shouldn", "haven", "hasn", "hadn",
    ]

    true_lst=[]

    for n in lst_1:
        if n[0] not in FILLER_WORDS:
            true_lst.append(n)

    best_dic={}

    for m in range(20):
        best_dic[true_lst[m][0]]=true_lst[m][1]

    return best_dic
