class Solution:
  def productExceptSelf(self,nums):
    n = len(nums)
    result = [1] * n  # Initialize result array with 1s (representing empty product initially)
    print(result)
    # Calculate product of all elements before the current element (easy to understand)
    for i in range(1, n):
      print(result)
      result[i] = result[i - 1] * nums[i - 1]  # Multiply previous product with current element

    # Calculate product of all elements after the current element (easy to understand)
    product = 1  # Initialize product for elements after current element
    for i in range(n-1, -1, -1):
      print(result)
      result[i] *= product  # Multiply result with product of elements after current element
      print(product)
      product *= nums[i]  # Update product for the next iteration

    return result

# Example usage
nums = [1, 2, 3, 4]
solution=Solution()
product = solution.productExceptSelf(nums)
print(product)  # Output: [24, 12, 8, 6]
