balance = 0
input1 = 0

print("1. Einzahlen")
print("2. Auszahlen")
print("3. Kontostand")
print("4. Ende")


while  True:
    input1 = input()
    match input1:

        case 1:
            print("Geben Sie den Betrag ein, den Sie einzahlen möchten:")
            input2 = float(input())
            print("Sie haben " + str(input2) + " Euro eingezahlt.")
            balance += input2

        case 2:
            print("Geben Sie den Betrag ein, den Sie abheben möchten:")
            input3 = float(input())
            print("Sie haben " + str(input3) + " Euro abgehoben.")
            balance -= input3

        case 3:
            print("Kontostand:", balance)

        case 4:
            print("Vorgang beendet")
            break

