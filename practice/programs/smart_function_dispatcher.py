def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

def power(a,b):
    return a**b


# defining namespace to map strings to functional objects
operations = {
    "add" : add,
    "mul" : multiply,
    "pow" : power,
}


def smart_dispatcher(op_code, *operands):
    operation = operations.get(op_code)

    if callable(operation):
        try:
            return operation(*operands)
        except TypeError as e:
            return f"Error: argument mismatch for {op_code} : {e}"

    else:
        f"Error: Operation {op_code} not found or not executable!"


def main():
    print(add(10, 20))
    print(multiply(10, 20))


if __name__ == "__main__":
    main() 