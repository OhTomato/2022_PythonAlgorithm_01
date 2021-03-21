#PROGRAMMERS HASH PART NUMBER 1
#Q-완주하지 못한 선수
#선수 이름 배열 participant[], completion[]이 주어 졌을 때 누락된 항목을 검색 하시오.

input1 = ["marina", "josipa", "nikola", "vinko", "filipa"]
input2 = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
	participant.sort()
	completion.sort()

	for i in range(len(completion)):
		if (participant[i] != completion[i]):
			return participant[i]

	return participant[-1]



if __name__ == "__main__":
    print(solution(input1,input2))