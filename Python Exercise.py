mark_list = []
n = int(input("Enter the number of tests done: "))
print("\n")
for i in range(0, n):
    print("Enter Test Score ", i + 1, )
    item = int(input())
    mark_list.append(item)
def Average(mark_list):
    return sum(mark_list) / len(mark_list)
average = Average(mark_list)
print("Average Score obtained ", round(average, 2))
