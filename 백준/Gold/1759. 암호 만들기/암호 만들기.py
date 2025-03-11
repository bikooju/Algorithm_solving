from itertools import combinations
import sys

L,C = list(map(int,sys.stdin.readline().split()))
alphabets = sys.stdin.readline().split()

alphabets_comb = combinations(sorted(alphabets),L)

answer = []

for alpha_comb in alphabets_comb:
    vowels_count = 0 #모음
    consonant_count = 0 #자음

    for alpha in alpha_comb:
        if alpha in "aeiou":
            vowels_count += 1
        else:
            consonant_count += 1

    if vowels_count >= 1 and consonant_count >= 2:
        print("".join(alpha_comb)) #리스트를 문자열로 출력


