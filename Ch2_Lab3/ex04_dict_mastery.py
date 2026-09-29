# Bài tập 4: Dictionary mastery

student = {
    "name": "Nguyen Van B",
    "age": 21,
    "major": "Khoa học máy tính",
    "scores": {
        "math": 9,
        "physics": 8,
        "english": 8.5
    }
}

# Truy cập giá trị theo khóa
print("Tên sinh viên:", student["name"])
print("Điểm Toán:", student["scores"]["math"])

# Thêm khóa mới
student["class"] = "CT01"

# Cập nhật giá trị
student["age"] = 22

# Xóa khóa
student.pop("major")

# Duyệt dictionary
for key, value in student.items():
    print(f"{key}: {value}")

print("Danh sách khóa:", list(student.keys()))
print("Danh sách giá trị:", list(student.values()))
