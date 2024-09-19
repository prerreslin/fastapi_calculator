from .. import app


@app.get("/calculate")
def calc(task: str):
    task = task.replace(' ', '')
    chars = []
    for char in task:
        for operator in "+-":
            if operator == char:
                chars.append(operator)
    if len(chars) == 0:
        return {"Error: ":"Invalid operation"}
    numbers = task.split(chars[0])
    if len(numbers) != 2 or numbers[0] == "" or numbers[1] == "":
        return {"Error ":"Not correct format"}
    if not all(num.isdigit() for num in numbers):
        return {"Error ":"Inappropriate characters are used"}
            
    result = (int(numbers[0]) + int(numbers[1]) if chars[0] == "+" else
    int(numbers[0]) - int(numbers[1]) if chars[0] == "-" else None)
    return {"Answer": result}
    