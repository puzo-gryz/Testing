def dfs(i0):
    global marked
    stack = [(i0, 2)]
    while stack:
        i, part = stack.pop()
        if marked[i] == 0:
            marked[i] = 3 - part
            if i not in graph:
                continue
            for v in graph[i]:
                stack.append((v, marked[i]))
        else:
            if marked[i] != 3 - part:
                return False
    return True

n, m = map(int, input().split())
graph = {}

for i in range(m):
    b, e = map(int, input().split())
    b -= 1
    e -= 1
    graph[b] = graph.get(b, []) + [e]
    graph[e] = graph.get(e, []) + [b]

res = True
marked = [0] * n
for i in range(n):
    if not marked[i]:
        res = dfs(i)
        if not res:
            break

print("YES" if res else "NO")
if res:
    print(*marked)