import numpy as np
import matplotlib.pyplot as plt
import random
import time
import threading
from abc import ABC, abstractmethod
"""
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Using credit card to pay ${amount}.")

class AliPayPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Using AliPay to pay ¥{amount}.")

class WeChatPayPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Using WeChat Pay to pay ¥{amount}.")
class Order:

    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        self.payment_strategy.pay(amount)

credit_card_payment = CreditCardPayment()
ali_pay_payment = AliPayPayment()
wechat_pay_payment = WeChatPayPayment()

order1 = Order(credit_card_payment)
order1.pay(100)

order2 = Order(ali_pay_payment)
order2.pay(200)

order3 = Order(wechat_pay_payment)
order3.pay(500)"""

"""class My(ABC):
    @abstractmethod
    def pay(self, amount):
        print(f"A{amount}")

class hehe(My):

    def pay(self, amount):
        print("asad")

de = My()
de.pay(11)"""


class Ai_net:

    def __init__(self, ratio: float):
        self.ratio = ratio

    def Rand(self) -> tuple:
        train = [random.randint(0, 10) for i in range(20)]
        label = [1 if k <= 5 else -1 for k in train]
        return (train, label)

    def Input(self):
        data, label = self.Rand()
        print(data, label)

import ttkbootstrap as ttk
root = ttk.Window(themename="darkly", size=(400, 400))
de = ttk.IntVar(value=0)
event = threading.Event()
cond = threading.Condition()
event.set()
def heh():
    for i in range(100):
        if i == 10:
            event.clear()
        if event.is_set():
            de.set(i)
            time.sleep(0.2)
        else:
            event.wait()
def co():
    while True:
        if not event.is_set():
            print("进程2获得")
            root.title("ok")
            event.set()
            break
t1 = threading.Thread(target=heh)
t2 = threading.Thread(target=co)
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
pro = ttk.Progressbar(root, orient="horizontal", mode="determinate", variable=de)
pro.pack()
root.mainloop()