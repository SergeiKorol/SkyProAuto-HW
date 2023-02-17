from user import User
from card import Card


Alex = User("Alex")
Blex = User("Blex")
Clex = User("Clex")

Clex.sayName()
Blex.sayName()
Alex.sayName()

Alex.sayAge()
Alex.satAge(44)
Alex.sayAge()


card = Card("4545 7878 1212 9898", "11/28", "Alex F")
Alex.addCard(card)
Alex.getCard().pay(1000)
card.pay(1000)
