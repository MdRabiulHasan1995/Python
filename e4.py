count=0;
c=dict()
a=input("Enter file name: ")
try:
    fhand = open(a)
except:
    print("File can not be opened")
    exit()

for line in fhand:
    words = line.split()
    if len(words) ==0 or words[0]!='From':
        continue
#    else:
    word=words[1]
    #print(word)
    if word in c:
        c[word] = c[word]+1
    else:
        c[word]=1
bigcount=None
bigword=None
for word, count in c.items():
    if bigcount is None or count >bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
