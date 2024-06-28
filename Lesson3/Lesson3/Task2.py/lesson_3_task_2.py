from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "Galaxy S21", "+79123456789")
phone2 = Smartphone("Apple", "IPhone 12", "+79749378023")
phone3 = Smartphone("Xiaomi", "Mi 11", "+79836748234")
phone4 = Smartphone("Google", "Pixel 5", "+79325637845")
phone5 = Smartphone("OnePlus", "9 Pro", "+79352675643")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")