# Given a sentence reverse a words

def reverse_word(sen):
    # org_arr = sen.split(' ')
    # print(org_arr)

    # final=[]
    # for each in org_arr:
    #     final.append(each[::-1])

    # print(" ".join(final))

    word_list = sen.split(' ')
    rever_lst = word_list[::-1]
    print(rever_lst)
    print(' '.join(rever_lst))


reverse_word('Hi!.. I welcome you')