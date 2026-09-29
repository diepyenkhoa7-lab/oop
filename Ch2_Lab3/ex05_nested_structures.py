# Bài tập 5: Nested structures

# Tạo một cấu trúc lồng nhau: danh sách sinh viên
students = [
    {
        "name": "An",
        "scores": {"math": 8, "english": 9, "physics": 7}
    },
    {
        "name": "Binh",
        "scores": {"math": 9, "english": 8, "physics": 8}
    },
    {
        "name": "Cuong",
        "scores": {"math": 7, "english": 10, "physics": 9}
    }
]

# Duyệt qua cấu trúc lồng nhau
for student in students:
    print("Sinh viên:", student["name"])
    for subject, score in student["scores"].items():
        print(f"  - {subject}: {score}")

# Tính điểm trung bình của từng sinh viên
for student in students:
    scores = student["scores"].values()
    average = sum(scores) / len(scores)
    print(f"Điểm trung bình của {student['name']}: {average:.2f}")

# Tạo danh sách tên sinh viên
names = [student["name"] for student in students]
print("Danh sách tên:", names)
