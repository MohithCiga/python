#import string
n=input()
n=n.lower()
n=n+" "
for i in range(len(n)):
    if n[i] in 'aeiou':
        while True and i!=(len(n)-2):
            if n[i+1] in 'aeiou':
                n=n[:i+1]+"$"+n[i+2:]
                i+=1
            else:
                break
    else:
        continue
                
n=n.strip()
print(n.replace("$",""),end="")
