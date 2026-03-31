class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        for s in strs:
            sizes.append(len(s))
        
        res = ""
        for i in range(len(sizes)):
            size = sizes[i]
            if i == len(sizes) - 1:
                res += str(size)
            else:
                res += str(size) + ","
        res += "#"
        
        for s in strs:
            res += s

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        header, payload = s.split("#", 1)

        if header == "":
            return []

        sizes_str = header.split(",")
        sizes_int = []
        for s in sizes_str:
            sizes_int.append(int(s))

        result = [""] * len(sizes_str)

        ind = 0
        for c in payload:
            if len(result[ind]) < sizes_int[ind]:
                result[ind] += c
            else:
                ind += 1
                result[ind] += c

        return result
            
