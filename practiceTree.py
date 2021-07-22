#우주발사

#def countDown(n):
 #   if n == 0:
  #      print('발사')
   # else :
    #    print(n)
     #   countDown(n-1)
        
        
#countDown(5)


# 별모양 출력

#def printStar(n) :
 #   if n>0 :
  #      printStar(n-1)
   #     print('★'*n)
#printStar(5)

#구구단 출력하기

def gugu(dan, num) :
    print("%d x %d = %d" %(dan,num,dan*num))
    if num > 9 :
        gugu(dan, num+1 )
        
for dan in range(2,10):
    print("## %d단 ##" % dan)
    gugu(dan,1)
    