class Phone:
    def call(self, number):
        return f"Calling {number}"


class SmartPhone(Phone):
    def take_photo(self):
        return "Photo Taken"


my_phone = SmartPhone()
print(my_phone.call("88998998"))
print(my_phone.take_photo())
