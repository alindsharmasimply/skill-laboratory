class list_of_names(list[str]):
    def find_name(self, x) -> bool:
        for name in self:
            if x == name:
                return True
        return False


names = list_of_names()
names.append("Robert")
names.append("Steve")
names.append("Natasha")
print(f"Is name 'Steve' available? Ans: {names.find_name('Steve')}")
print(f"Is name 'Bruce' available? Ans: {names.find_name('Bruce')}")
