city_num = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

total = distances[0] * prices[0]
current = 1
while current < len(distances):
    destination = current + 1
    while (destination < len(distances)) & (prices[current] <= prices[destination]):
        destination += 1
    total += (sum(distances[current:destination+1]) * prices[current])
    current = destination

print(total)