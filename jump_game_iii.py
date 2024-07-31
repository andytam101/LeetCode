from collections import deque
class Solution:
    def canReach(self, arr, start):
        bfs = deque([start])
        visited = {start}
        n = len(arr)

        if arr[start] == 0:
            return True
        
        while len(bfs) > 0:
            current = bfs.popleft()
            
            left = current - arr[current]
            right = current + arr[current]
            
            if left >= 0 and left not in visited:
                if arr[left] == 0: return True
                bfs.append(left)
                visited.add(left)

            if right < n and right not in visited:
                if arr[right] == 0: return True
                bfs.append(right)
                visited.add(right)            

        return False
    

if __name__ == "__main__":
    arr_test = [0,1]
    start_test = 1

    print(Solution().canReach(arr_test, start_test))