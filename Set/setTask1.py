goa = {"amit","sumit","raj","kunal"}
mumbai = {"sumit","jay","neha","amit"}
pune = {"prit","sneha","amit","jay","kunal"}

#find person who have attended all cities ...,....
#find person who have  "" in mumbai and pune both but not goa
#find person who have  "" in pune and goa but not in mumbai

attendedAll = pune.intersection(goa.intersection(mumbai))
print("Attended ALL : ", attendedAll)

attendedMuPu = mumbai.intersection(pune)
print("Attended Mumbai and Pune : ", attendedMuPu)
attendedPuGo = goa.intersection(pune)
print("Attended Goa and Pune : ", attendedPuGo)

#---------------------------------------------------------------------

while goa : 
    x = goa.pop()
    print(x)

