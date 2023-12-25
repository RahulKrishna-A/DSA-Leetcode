class Solution:

    # Function to find minimum number of pages.
    def findPages(self, A, N, M):
        # code here

        def canKeep(max_pages):
            students = 1
            pages = 0
            for i in range(N):
                if pages + A[i] <= max_pages:
                    pages += A[i]
                else:
                    pages = A[i]
                    students += 1
            return students

        s = max(A)
        e = sum(A)
        if M > N:
            return -1

        while s <= e:

            mid = s + (e - s) // 2
            # print(s,e,mid,canKeep(mid))
            # if canKeep(mid)==M:
            #     e=mid-1

            if canKeep(mid) > M:
                s = mid + 1
            else:
                e = mid - 1
        return s

