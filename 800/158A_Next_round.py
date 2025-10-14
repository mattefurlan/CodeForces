'''
"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n≥k), and you already know their scores. Calculate how many participants will advance to the next round.

Input
The first line of the input contains two integers n and k (1≤k≤n≤50) separated by a single space.
The second line contains n space-separated integers a1,a2,...,an (0≤ai≤100), where ai is the score earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i from 1 to n-1 the following condition is fulfilled: ai≥ai+1).

Output
Output the number of participants who advance to the next round.
Input
8 5
10 9 8 7 7 7 5 5
Output
6
Input
4 2
0 0 0 0
Output
0
'''

def round(obs, sco):
    count = 0
    trash = obs[1]
    for i in range(sco.index(obs[1])):
        if sco[i] > 0:
            count += 1
    return print(count)
        
        
    # ci torniamo


n_k = list(map(int, input().split()))
scores = list(map(int, input().split()))

round(n_k, scores)