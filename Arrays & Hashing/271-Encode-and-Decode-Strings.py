class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ""
        for x in strs:
            output += x + ":;"
        return output

    def decode(self, s: str) -> List[str]:
        return s.split(":;")[:-1]
