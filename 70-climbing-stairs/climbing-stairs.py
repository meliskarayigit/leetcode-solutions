class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        f(0) = 1, f(1) = 1.
        f(k) = f(k-1) + f(k-2)
        i=2
        f2 = f1+ f0
         i 3
        f3= f2 +f1
        n-1 =curr
        n-2=n-1
        '''
        if n==1 or n==0:
                return 1
        n_2 =1
        n_1 = 1
        for i in range(2,n+1):
            curr = n_2 + n_1
            n_2 = n_1
            n_1= curr
            

        return n_1
