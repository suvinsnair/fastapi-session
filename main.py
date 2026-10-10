from fastapi import FastAPI, Request

app = FastAPI(title="Campus API")

@app.get("/")
def home():
    return {"message": "Welcome to Tathva API!!!"}



@app.get("/greet/{student_name}")
def greet_student(student_name: str):
    return {
        "greeting": f"Welcome {student_name}",
        "department": "Computer Science"
    }

@app.get("/get-ip")
def read_root(request: Request):
    # Retrieve the direct connecting IP address
    client_host = request.client.host if request.client else "Unknown"
    return {"client_ip": client_host}

@app.get("/grade/{score}")
def calculate_grade(score: int):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >=70:
        grade = "C"
    else:
        grade = "F"
    return {
        "score": score,
        "grade": grade,
        "passed": score >= 60
    }