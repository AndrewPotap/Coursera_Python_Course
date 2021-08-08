def compute_pay(h, r):
    return h * r if h <= 40 else (h - 40) * r * 1.5 + 40 * r


h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
p = compute_pay(h, r)
print("Pay", p)
