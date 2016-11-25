from statistics import median

n, d = input().strip().split()
n = int(n)
d = int(d)
line = input().strip().split()

nums = [int(i) for i in line]
notifs = 0

for i in range(d, n):
    m = median(nums[i-d:i])
    if 2 * m <= nums[i]:
        notifs += 1

print(notifs)
        
