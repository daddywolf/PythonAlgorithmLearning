class Solution(object):
    def countBits(self, num):
        li = []
        for i in range(num+1):
            li.append(str(bin(i).replace('0b', '')).count('1'))
        return li


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(5))
