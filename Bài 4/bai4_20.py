def in_tam_giac_pascal(n):
    """ham in ran dong dau tiencua tam giac pascal."""
    for i in range(n):
        hang = [1] * (i + 1)
        for j in range(1, i):
            hang[j] = prev_row[j - i] + prev_row[j]
        print(' '.join(map(str, hang)))
        prev_row = hang
n = int(input('Nhap so nguyen n: '))
in_tam_giac_pascal(n)
print("Nguyễn Mạnh Kiên")
print("MSSV:235752020710017")