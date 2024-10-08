import math

def driehoek(num) : 
    if not isinstance(num, int) or num < 0 :
        raise AssertionError('ongeldig aantal rijen')
    if num == 0 :
        return []
    ans = [[1]]
    for i in range(1, num) :
        temp = [1]
        for j in range(1, i) :
            temp.append(ans[i - 1][j - 1] + ans[i - 1][j])
        temp.append(1)
        ans.append(temp)
    return ans

def zeshoek(rij, kolom) :
    drie = driehoek(rij + 1)
    posities = [[-2, -2], [-2, -1], [-1, 0], [0, 0], [0, -1], [-1, -2]]
    ans = []
    for pos in posities :
        row = rij + pos[0]
        col = kolom + pos[1]
        if row < 0 or row >= len(drie) or col < 0 or col >= len(drie[row]) :
            raise AssertionError('ongeldige interne positie')
        ans.append(drie[row][col])
    return ans

def kwadraat(rij, kolom) :
    ans = zeshoek(rij, kolom)
    base = ' x '.join(map(str, ans))
    prod = math.prod(ans)
    base += f' = {prod}'
    sqrt = int(math.sqrt(prod))
    base += f' = {sqrt} x {sqrt}'
    return base
