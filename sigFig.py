from time import sleep
numb=str(raw_input())
numb = numb+"t"
print numb
sigfig=0
zeroCounter=0
for i in numb:
    if i!="0" and i!="t" and i!=".":
        sigfig+=1

        if zeroCounter >=1:
            sigfig+=zeroCounter
            zeroCounter=0
            
        
    elif i=="0":
        zeroCounter +=1
    elif i=="t":
        sigfig+=zeroCounter
        zeroCounter=0

print sigfig
sleep(10)



