def solution(want, number, discount):
    answer = 0
    discount_len=len(discount)
    for i in range(discount_len-9) :
        discount_dictionary=dict()
        for j in range(10) :
            if discount[i+j] in discount_dictionary :
                discount_dictionary[discount[i+j]]+=1
            else :
                discount_dictionary[discount[i+j]]=1
        want_dictionary=dict()
        for j in range(len(want)) :
            want_dictionary[want[j]]=number[j]
        if sorted(discount_dictionary.items())==sorted(want_dictionary.items()) :
            answer+=1
            print(i)
            #print(sorted(discount_dictionary.items()) , sorted(want_dictionary.items()))
    return answer