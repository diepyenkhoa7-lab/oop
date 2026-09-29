# Bài tập 3: Set operations

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# Hợp của hai tập hợp
union_set = set_a | set_b

# Giao của hai tập hợp
intersection_set = set_a & set_b

# Hiệu của hai tập hợp
difference_set = set_a - set_b

# Phần bù đối xứng
symmetric_diff = set_a ^ set_b

print("Tập A:", set_a)
print("Tập B:", set_b)
print("Hợp:", union_set)
print("Giao:", intersection_set)
print("Hiệu A - B:", difference_set)
print("Phần bù đối xứng:", symmetric_diff)

# Thêm và xóa phần tử
set_a.add(10)
set_a.remove(1)
print("Tập A sau khi thêm/xóa:", set_a)
