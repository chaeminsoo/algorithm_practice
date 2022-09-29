# 1461
n,m = map(int,input().split())
books = list(map(int,input().split()))

ans = 0
m_books = []
p_books = []
most_far = 0     # 젤 멀리 있는 값은 가장 나중에 가야되기 때문에 기억
for i in books:   # 음 방향 양 방향 책 나눠 주기
    if i < 0:
        m_books.append(abs(i))
    else:
        p_books.append(i)

m_books.sort()
p_books.sort() # 젤 멀리 있는 값에 접근하기 위해 sort() : 가장 마지막 값이 젤 멀리 있는 값

def book_pop(books):
    global ans, most_far
    while books:
        book_loc = books.pop()
        most_far = max(most_far,book_loc)   # 젤 멀리 있는 값은 가장 나중에 가야되기 때문에 기억
        ans += (book_loc*2)       # 왔다 갔다니까 *2
        for _ in range(m-1):      # 가는 길에 책 갖다 놓기(가장 멀리 있는 것 부터)
            try:
                books.pop()
            except IndexError:
                break

book_pop(m_books)
book_pop(p_books)
print(ans-most_far)     # 가장 마지막에 놓은 곳(먼 거리)은 다시 돌아올 필요없기 때문