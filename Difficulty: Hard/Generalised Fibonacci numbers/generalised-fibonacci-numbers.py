class Solution:
    def genFibNum(self, a, b, c, n, m):
        # Base cases for n=1 and n=2
        if n <= 2:
            return 1 % m
            
        # Multiplication of two 3x3 matrices modulo m
        def multiply(A, B, m):
            C = [[0, 0, 0] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % m
            return C

        # Matrix exponentiation T^p modulo m
        def power(A, p, m):
            res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # Identity matrix
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, A, m)
                A = multiply(A, A, m)
                p //= 2
            return res

        # The transformation matrix
        T = [
            [a, b, c],
            [1, 0, 0],
            [0, 0, 1]
        ]
        
        # We need T^(n-2) to get from g(2) to g(n)
        T_n_2 = power(T, n - 2, m)
        
        # Final state: g(n) = T[0][0]*g(2) + T[0][1]*g(1) + T[0][2]*1
        # Since g(1)=1, g(2)=1:
        res = (T_n_2[0][0] * 1 + T_n_2[0][1] * 1 + T_n_2[0][2] * 1) % m
        
        return res