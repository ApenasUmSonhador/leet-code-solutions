class Solution:
    def encode(self, strs):
        output = ""
        for x in strs:
            output += x + ":;"
        return output

    def decode(self, s):
        return s.split(":;")[:-1]
