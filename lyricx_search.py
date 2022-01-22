from bisect import bisect_left, bisect_right

def bi_search(target,llist):
    ref1 = target.replace('?','a')
    ref2 = target.replace('?','z')
    start = bisect_left(llist,ref1)
    end = bisect_right(llist,ref2)
    return end-start
    
def solution(words, queries):
    words_by_len = [[] for _ in range(10001)]
    words_by_len_reverse = [[] for _ in range(10001)]
    answer = []
    for i in words:
        idx = len(i)
        words_by_len[idx].append(i)
        words_by_len_reverse[idx].append(i[::-1])

    for j in words_by_len:
        if j: j.sort()
    for j in words_by_len_reverse:
        if j: j.sort()
    
    for k in queries:
        if k[0] != '?':
            answer.append(bi_search(k,words_by_len[len(k)]))
        else:
            answer.append(bi_search(k[::-1],words_by_len_reverse[len(k)]))

    return answer