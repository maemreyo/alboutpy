# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
