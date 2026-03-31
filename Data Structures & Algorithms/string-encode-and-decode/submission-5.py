class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        for s in strs:
            sizes.append(len(s))

        res = ""
        for i in range(len(sizes)):
            if i == len(sizes) - 1:
                res += str(sizes[i])
            else:
                res += str(sizes[i])
                res += ","
        res += "#"

        for s in strs:
            res += s

        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        old_res = s.split("#", 1)
        sizes = old_res[0].split(",")
        strs = old_res[1]

        if sizes[0] == '':
            return []

        res = []
        curr = 0
        for i in range(len(sizes)):
            res.append(strs[curr: curr + int(sizes[i])])
            curr += int(sizes[i])

        return res

# ["Hello","World"]
# "5,5#HelloWorld""

# sizes: "5,5"
# strs: "HelloWorld"