class Solution:
    def containsDuplicate(self, List):

        # Use a set to efficiently store unique elements
        seen = set(List)

        for num in List:
            if num in seen:
                return True  # Duplicate found, return True
            seen.add(num)  # Add the number to the set

        return False  # No duplicates found, return False
'''class Solution:
    
    def check_duplicate_distinct(self,items):
        return len(items) != len(set(items))
    '''

x=Solution()
List=[1,2,3]

print(x.containsDuplicate(List))