class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (В наявності: {self.stock} шт.)"

class Basket:
    def __init__(self):
        self.items = []

    def add(self, item, qty):
        if item.stock >= qty:
            self.items.append({"item": item, "qty": qty})
            item.stock -= qty
            print(f"{qty} шт. {item.name} додано до кошика.")
        else:
            print(f"Недостатньо {item.name} на складі.")

    def remove(self, item):
        for i in self.items:
            if i["item"] == item:
                item.stock += i["qty"]
                self.items.remove(i)
                print(f"{item.name} видалено з кошика.")
                return
        print(f"{item.name} не знайдено в кошику.")

    def total(self):
        return sum(i["item"].price * i["qty"] for i in self.items)

    def show(self):
        if not self.items:
            print("Кошик порожній.")
            return
        print("Ваш кошик:")
        for i in self.items:
            print(f"{i['item'].name} - {i['qty']} шт. - ${i['item'].price * i['qty']:.2f}")
        print(f"Загальна вартість: ${self.total():.2f}")

apple = Item("Яблуко", 0.5, 100)
bread = Item("Хліб", 1.2, 50)
milk = Item("Молоко", 0.8, 30)

basket = Basket()
basket.add(apple, 5)
basket.add(bread, 2)
basket.add(milk, 1)
basket.show()
basket.remove(bread)
basket.show()

print(f"Загальна вартість кошика: ${basket.total():.2f}")
