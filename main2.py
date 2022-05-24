#Tukaj gledamo še neke problemčke
from item import Item

item1 = Item("MyItem",750)

item1.apply_increment(0.2)
print(item1.price)

#%%
from item import Item

item1 = Item("MyItem",750,6)

item1.send_email()

#%%

from phone import Phone

item1 = Phone("jscPhone",1000,3)

item1.send_email()
print(item1.price)
# %%
