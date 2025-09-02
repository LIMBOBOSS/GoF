class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    foo = 'spam'

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
print(s1.foo, s2.foo)
s1.foo = 'eggs'
print(s1.foo, s2.foo)
