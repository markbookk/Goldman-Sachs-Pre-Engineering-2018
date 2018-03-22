# Complete the function below.

def electionWinner(votes):
	votesD = {}
	for i in votes:
		# i = i.lower()
		votesD[i] = votesD.get(i, 0) + 1

	print votesD
	highestVotes = 0
	winnerList = []
	for key in votesD:
		if (votesD.get(key) > highestVotes):
			del winnerList[:]
			winnerList.append(key)
			highestVotes = votesD.get(key)
		elif (votesD.get(key) == highestVotes):
			winnerList.append(key)
			highestVotes = votesD.get(key)
	print winnerList
	winnerListSorted = sorted(winnerList)
	print winnerListSorted
	# return winnerListSorted[-1].capitalize()
	return winnerListSorted[-1]
