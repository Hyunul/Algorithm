L, P = map(int, input().split())
news_list = list(map(int, input().split()))

for news in news_list:
    print(news - L * P, end=' ')