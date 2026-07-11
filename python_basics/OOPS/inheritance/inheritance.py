class rovem:
    def speak(self):
        print('hello guys')
class student(rovem):
    def me(self):
        self.name = 'tazeen'
        print(f"My name is {self.name}")
b=student()
b.me()
b.speak()