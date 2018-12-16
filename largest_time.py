'''

Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.
Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""

'''


class Solution(object):
    def largestTimeFromDigits(self, A):
        A = self._preprocess(A)
        ts = self._2_4_6_x(A)
        if ts:
            return ts
        ts = self._10_x_6_x(A)
        if ts:
            return ts
        return ''

    def _preprocess(self, A):
        for num in range(10):
            indices = [i for i in range(len(A)) if A[i] == num]
            cnt = 1
            for idx in indices[1:]:
                A[idx] += cnt*0.1
                cnt += 1
        return A

    def _2_4_6_x(self, A):
        if 2 not in A:
            return
        h1 = 2
        A = [d for d in A if d != h1]
        Ah2 = [d for d in A if d < 4]
        if not Ah2:
            return
        if len(Ah2) == 1:
            if not [d for d in A if d not in Ah2 and d < 6]:
                return
        h2 = max(Ah2)
        A = [d for d in A if d not in [h1, h2]]
        m = max(d for d in A if d < 6)
        s = [d for d in A if d != m][0]
        return '%d%d:%d%d' % (h1, h2, m, s)

    def _10_x_6_x(self, A):
        Ah1 = [d for d in A if d in [0, 1]]
        if not Ah1:
            return
        h1 = max(Ah1)
        A = [d for d in A if d != h1]
        Am = [d for d in A if d < 6]
        if not Am:
            return
        if len(Am) == 1:
            m = max(Am)
            A = [d for d in A if d != m]
            return '%d%d:%d%d' % (h1, max(A), m, min(A))
        h2 = max(A)
        A = [d for d in A if d != h2]
        m = max(d for d in A if d < 6)
        s = [d for d in A if d != m][0]
        return '%d%d:%d%d' % (h1, h2, m, s)
