
def cal(p,q):
	if len(p)< len(q):
		shorter = p
		longer = q
	else:
		shorter = q
		longer = p
		
	return shorter+longer+shorter
	
print(cal("3","45"))
print(cal("5", "789"))






	






