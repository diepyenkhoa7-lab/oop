# Bài tập 2: Tuple unpacking

# Tạo tuple chứa thông tin sinh viên
student = ("Nguyen Van A", 20, "CNTT")

# Unpack tuple
name, age, major = student

print("Tên:", name)
print("Tuổi:", age)
print("Ngành:", major)

# Ví dụ với tuple lồng nhau
scores = (("Toan", 9), ("Ly", 8), ("Hoa", 10))
for subject, score in scores:
    print(f"Môn {subject}: {score}")
