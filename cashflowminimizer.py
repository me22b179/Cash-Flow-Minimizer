def recurrence(amount):
    maxcredit = amount.index(max(amount))
    maxdebit = amount.index(min(amount))

    if amount[maxcredit] == 0 and amount[maxdebit] == 0:
        return

    m = min(amount[maxcredit], -amount[maxdebit])
    amount[maxcredit] -= m
    amount[maxdebit] += m

    print(f"Person {maxdebit + 1} pays {m} to Person {maxcredit + 1}")

    recurrence(amount)

def mincashflow(v, n):
    amount = [0] * n

    for i in range(n):
        for j in range(n):
            amount[i] += v[j][i] - v[i][j]

    print(f"Initial net amounts: {amount}")

    recurrence(amount)

def main():
    n = int(input("Enter the Number of People: "))
    t = int(input("Enter the Number of Transactions: "))
    v = [[0] * n for _ in range(n)]
    print("Enter the Transactions in the following Format")
    print("( Person who owes money    Person who is owed money    Amount)")
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if 1 <= a <= n and 1 <= b <= n:
            v[a-1][b-1] += c  #means person a owes person b an amount c.
        else:
            print(f"Invalid transaction: {a} owes {b} {c}")

    mincashflow(v, n)

if __name__ == "__main__":
    main()