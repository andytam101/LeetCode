class Solution:
    def minJumps(self, arr) -> int:
        jumps = list(range(len(arr) - 1, -1, -1))
        result = {arr[-1]: [0, False]}

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] in result:
                if result[arr[i]][1]:
                    jumps[i] = min(result[arr[i]][0], jumps[i+1]+1)
                else:
                    jumps[i] = min(result[arr[i]][0] + 1, jumps[i+1]+1)
                    result[arr[i]][1] = result[arr[i]][0] + 1 == jumps[i]
                    result[arr[i]][0] = jumps[i]
            else:
                jumps[i] = min(jumps[i+1] + 1, jumps[i])
                result[arr[i]] = [jumps[i], False]
            
            if jumps[i] + 1 < jumps[i+1]:
                jumps[i+1] = jumps[i] + 1
                result[arr[i + 1]] = [jumps[i] + 1, False]
        
        return jumps[0]

if __name__ == "__main__":
    test_arr = [
        -95,100,-86,50,99,50,99,43,-86,43,-26,-7,-19,-1,50,99,100,-1,-27,2,-69,60,-1,21,-54,43,
        -94,-94,-7,67,50,57,-27,60,-19,-7,67,-19,-7,99,-69,-69,100,-95,-94,2,100,50,50,-19,-21,
        -19,60,-19,-95,-21,67,-1,57,50,50,-27,-94,50,99,-7,-21,-21,57,-95,57,-69,100,-7,-86,-31,
        -77,21,-95,-1,-54,57,-94,-27,-95,-54,2,21,50,-21,2,-7,9,100,9,-95,-73,-77,99,-54
    ]
    print(Solution().minJumps(test_arr))
