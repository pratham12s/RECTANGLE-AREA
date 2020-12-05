class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area=(C-A)*(D-B)+(G-E)*(H-F)
        if B>H or A>G or C<E or F>D:
            return area
        else:
            return(area -((min(C,G)-max(A,E))*(min(D,H)-max(B,F))))
        