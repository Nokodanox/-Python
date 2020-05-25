from random import sample
a = sample(range(1,300), 20)
answer = []
print(a)
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        answer.append(a[i+1])
print(answer)