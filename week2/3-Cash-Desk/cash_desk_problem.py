class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A " + str(self.amount) + "$ bill."

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)


class BatchBill:

    def __init__(self, batch):
        self.batch = bills

    def __len__(self):
        return len(self.batch)

    def __int__(self):
        return self.total()

    def total(self):
        bills_amount = 0

        for bill in batch:
            bills_amount += int(bill)

        return bills_amount

    def __getitem__(self, index):
        return self.batch[index]


class CashDesk:

    def __init__(self):
        self.vault = []

    def take_money(self, currency):
        self.vault.append(currency)

    def total(self):
        total_amount = 0

        for money in self.vault:
            total_amount += int(money)

        return total_amount

    def inspect(self):
        result = {}

        for money in self.vault:
            if isinstance(money, BatchBill):
                for bill_object in money:
                    bill = int(bill_object)
                    if bill not in result.keys():
                        result[bill] = 1
                    else:
                        result[bill] += 1
            else:
                bill = int(money)
                if bill not in result.keys():
                    result[bill] = 1
                else:
                    result[bill] += 1
        for elem in sorted(result.keys()):
            print(str(int(elem)) + "$ bills - " + str(result[elem]))


if __name__ == '__main__':
    a = Bill(10)
    b = Bill(5)
    c = Bill(10)

    print(int(a))  # 10
    print(str(a))  # "A 10$ bill"
    print(a)  # A 10$ bill

    print(a == b)  # False
    print(a == c)  # True

    money_holder = {}

    money_holder[a] = 1  # We have one 10% bill

    if c in money_holder:
        money_holder[c] += 1

    print(money_holder)  # { "A 10$ bill": 2 }

    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total())  # 390
    desk.inspect()
