total = 0

for x in range(1, 10, 1) :
    total += x * int(input())

checksum = int(input())
mod = total % 11
print("OK" if mod == checksum else "FOUT")