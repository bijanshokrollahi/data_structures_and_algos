import heapq


def solution(numbers: list) -> list:
    ans = [0] * (len(numbers) - 2)
    for i in range(0, len(numbers) - 2):
        if numbers[i] < numbers[i + 1] > numbers[i + 2] or numbers[i] > numbers[i + 1] < numbers[i + 2]:
            ans[i] = 1
    return ans


def tiny_solution(a, b, k) -> int:
    count = 0
    i = 0
    j = len(b) - 1
    while j >= 0 and i < len(a):
        if int(str(a[i])+(str(b[j]))) < k:
            count += 1
        i += 1
        j -= 1
    return count


def array_to_string(arr: list) -> str:
    class Letter:
        def __init__(self, letter, position):
            self.letter = letter
            self.position = position

        def __lt__(self, nxt):
            return self.position < nxt.position

    priority_queue = []
    for j in range(0, len(arr)):
        for i in range(0, len(arr[j])):
            if j < 10:
                heapq.heappush(priority_queue, Letter(arr[j][i], float(f"{i}.0{j}")))
            else:
                heapq.heappush(priority_queue, Letter(arr[j][i], float(f"{i}.{j}")))
    ans = ''
    while len(priority_queue) > 0:
        letter = heapq.heappop(priority_queue)
        ans += letter.letter
    return ans

