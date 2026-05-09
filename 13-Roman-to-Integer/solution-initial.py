class Solution:
    def romanToInt(self, s: str) -> int:
        return ((s.count("M")*1000)+(s.count("D")*500)+(s.count("C")*100)+(s.count("L")*50)+(s.count("X")*10)+(s.count("V")*5)+(s.count("I")))-(((s.count("CM")+s.count("CD"))*200)+((s.count("XC")+s.count("XL"))*20)+((s.count("IX")+s.count("IV"))*2))