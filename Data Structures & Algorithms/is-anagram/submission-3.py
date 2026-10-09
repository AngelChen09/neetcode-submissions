class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Auto reject if len diff to save sorting time
        if len(s) != len(t):
            return False

        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if s_sorted == t_sorted:
            return True
        return False
