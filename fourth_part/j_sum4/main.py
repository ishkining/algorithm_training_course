import sys


def main():
    n = int(input())
    target = int(input())
    nums = [int(number) for number in sys.stdin.readline().rstrip().split(' ')]
    result = []
    nums.sort()

    def kSum(k, start_index, inner_target, example_array):
        if k > 2:
            for i in range(start_index, len(nums) - k + 1):
                if i == start_index or (i > start_index and nums[i] != nums[i - 1]):
                    kSum(k - 1, i + 1, inner_target - nums[i], example_array + [nums[i]])
        else:
            left, right = start_index, len(nums) - 1
            while left < right:
                magic_sum = nums[left] + nums[right]
                if magic_sum == inner_target:
                    result.append(example_array + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif magic_sum > inner_target:
                    right -= 1
                else:
                    left += 1

    kSum(4, 0, target, [])
    print(len(result))
    for sub_array in result:
        print(*sub_array)


if __name__ == '__main__':
    main()