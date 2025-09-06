n=int(input())
word_list=[]
for i in range(0,n):
    word=input("")
    word_list.append(word)
for i in range(0,n):
    word=word_list[i]
    length=len(word)
    if length>=11:
       print(word[0],end="")
       print(len(word[1:length-1]),end="")
       print(word[length-1])
    else:
       print(word_list[i])
