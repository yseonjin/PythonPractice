from os.path import  getsize

spos=0

f1='stockcode.txt'
file_size=getsize(f1)
fsize=int(file_size / 3) + 1

print('%d  , %d '  %(file_size, fsize))

f=open('stockcode.txt' ,'r' , encoding='UTF8')
for i in range(3):
    f.seek(spos)
    data = f.read(fsize)
    h=open('stockcode(%d).txt' %(i+1) ,'w', encoding='UTF8')
    spos = spos + fsize
    print(spos)
    h.write(data)

f.close()
h.close()
