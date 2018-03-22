# Complete the function below.

def minNum(A, K, P):
	solvedA = P
	solvedK = 0
	days = 0
	if (P < 0):
		return -1
	if (K <= A):
		return -1

	while (solvedK <= solvedA):
		days = days + 1
		solvedA = solvedA + A
		solvedK = solvedK + K
	return days