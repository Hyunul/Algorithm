T = int(input())

print_list = []
for i in range(T):
    G1, G2, G3, G4, G5, G6 = map(int, input().split())
    S1, S2, S3, S4, S5, S6, S7 = map(int, input().split())

    G_score = G1 + G2*2 + G3*3 + G4*3 + G5*4 + G6*10
    S_score = S1 + S2*2 + S3*2 + S4*2 + S5*3 + S6*5 + S7*10
    
    if G_score > S_score:
        print_list.append("Battle %s: Good triumphs over Evil" %(i+1))
    elif G_score < S_score:
        print_list.append("Battle %d: Evil eradicates all trace of Good" %(i+1))
    else:
        print_list.append("Battle %s: No victor on this battle field" %(i+1))

for j in range(T):
    print(print_list[j])