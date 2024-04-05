with open("dishin.txt", "r") as input_file:
    n = int(input_file.readline())
    nums = [int(line) for line in input_file.readlines()]

minimum = min(nums)
maximum = max(nums)
mean = int(sum(nums) / n)

with open("dishout.txt", "w") as output_file:
    output_file.write(f"{minimum} {maximum} {mean}")
