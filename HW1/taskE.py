K1, M, K2, P2, N2 = map(int, input().split())

if M != 1:

    for i in range(1,1000000):

        if N2==((K2-1)//i)+1:

            P1 = (((K1-1)//i)//(M-1))+1

            N1=((K1-1)//i)%(M-1)

if M == 1:

    N1 = 1

    for i in range(1,1000000):

        while K1 % i != 0:

            K1 = K1 + 1

        P1 = (K1//i)

if K2 < P2 * N2 or N2 > M or K2 // P2 < M:

    P1 = -1

    N1 = -1

if P2 == 1 and N2 == 1:

    P1 = 0

print(P1, N1)

