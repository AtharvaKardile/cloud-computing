def greet(name=None):
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
