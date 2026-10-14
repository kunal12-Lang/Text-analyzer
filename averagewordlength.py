def average_word_length(x):
    numerator=0

    for i in x:
        numerator+=len(i)

    average=numerator/len(x)
    return average 
