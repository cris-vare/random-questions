def max_pair_product(nums: list[int]) -> int:
    # Write your solution here
    #first we need to get i and j and then we multiply them and return max product int.
    max_product = nums[0] * nums[1]
    # then we continue going down the whole list until it ends and update max int each time.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = nums[i] * nums[j]
            if product > max_product:
                max_product = product
    return max_product

    pass

"""
 i is the left number, j is always ahead of i so you never repeat a
  pair:

  [3, 5, 2, 8]
  so
  i=0 (3)
        j=1  →  3 * 5 = 15   15 > 15? no
        j=2  →  3 * 2 = 6    6  > 15? no
        j=3  →  3 * 8 = 24   24 > 15? YES → max_product = 24

  i=1 (5)
        j=2  →  5 * 2 = 10   10 > 24? no
        j=3  →  5 * 8 = 40   40 > 24? YES → max_product = 40

  i=2 (2)
        j=3  →  2 * 8 = 16   16 > 40? no

  i=3 (8)
        no j left to pair with

  return 40 ✔
  """