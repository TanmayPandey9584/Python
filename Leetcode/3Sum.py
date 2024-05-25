class Solution:
    def threeSum(self, List):
        List.sort()
        triplets = []
        n = len(List)

        for i in range(n - 1):

            left = i + 1
            right = n - 1

            while left < right:
                total = List[i] + List[left] + List[right]

                if total == 0:
                    triplets.append([List[i], List[left], List[right]])

                    while left < right and List[left] == List[left + 1]:
                        left += 1
                    while left < right and List[right] == List[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                else:
                    left += 1
                    right -= 1
        seen_triplets = {}
        for triplet in triplets:
            sorted_triplet = tuple(triplet)
            seen_triplets[sorted_triplet] = triplet
            print(seen_triplets)

        u= list(seen_triplets.values())
        return u

x=Solution()
nums=[0,0,0,0]
print(x.threeSum(nums))