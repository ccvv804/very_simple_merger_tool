import sys #파일명, 옵션 로드시 필요

r1=sys.argv[1] #파일 1
r2=sys.argv[2] #파일 2
outname=sys.argv[3]

f1=open(r1,"rb")
f2=open(r2,"rb")
data=f1.read()+f2.read()
w=open(outname, 'wb')
w.write(data)
w.close()