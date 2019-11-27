
def fibonacci(n):
    f0 = 1
    f1 = 1
    fi = 2
    for i in range(2, n):
        fi = f0 + f1
        f0 = f1
        f1 = fi
    return fi

def main():
    print("hello, world")

if __name__ == "__main__":
    main()
    print(fibonacci(3))
    assert 2 == fibonacci(3)
    assert 3 == fibonacci(4)
    assert 5 == fibonacci(5)
    assert 8 == fibonacci(6)
    assert 13 == fibonacci(7)
