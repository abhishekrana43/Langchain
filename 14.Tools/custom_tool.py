from langchain.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    return a * b

result = multiply.invoke({'a': 3, 'b': 5})
print(result)