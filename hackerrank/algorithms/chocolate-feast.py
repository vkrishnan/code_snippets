# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
	
    answer = A / B
    wrappers = answer

    while wrappers >= C1:
    	count = wrappers / C1
    	answer += count
    	wrappers = count + (wrappers % C1)

    # write code to compute answer
    print answer
