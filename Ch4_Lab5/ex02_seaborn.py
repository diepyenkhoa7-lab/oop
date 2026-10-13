import seaborn as sns
import matplotlib.pyplot as plt
import statistics

study_hours = [2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 12, 12, 13, 14]
exam_scores = [45, 50, 52, 58, 60, 63, 68, 70, 72, 75, 78, 80, 83, 85, 88, 90, 92, 94, 95, 98]
majors = ['CNTT','CNTT','KTPM','KTPM','CNTT','HTTT','KTPM','CNTT','HTTT','CNTT','KTPM','CNTT','HTTT','CNTT','KTPM','HTTT','CNTT','KTPM','CNTT','KTPM']
sns.set_theme(style='whitegrid')


#Nhiem vu 1 
fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(x=exam_scores, kde=True, bins=6, color='teal', ax=ax)
#ax.lines[0].set_color('red')
ax.set_title('Phân Bố Điểm Thi Lập Trình Python')
ax.set_xlabel('Điểm số')
ax.set_ylabel('Tần suất')
plt.tight_layout()
plt.show()

#Nhiem vu 2 
fig, (ax) = plt.subplots(figsize=(6, 4))

sns.scatterplot(x=study_hours, y=exam_scores, hue=majors, palette='Set1', ax=ax)
ax.set_title('Thời Gian Học và Điểm Số')
ax.set_xlabel('Thời gian học (giờ/tuần)')
ax.set_ylabel('Điểm số')
plt.tight_layout()
plt.show()

#Nhiem vu 3 
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(x=majors, y=exam_scores, ax=ax)
ax.set_title('Phân Bố Điểm Theo Chuyên Ngành')
ax.set_xlabel('Chuyên Ngành')
ax.set_ylabel('Điểm số')
plt.tight_layout()
plt.savefig("Ch4_Lab5\\images\\phantich_diemso_seaborn.png", dpi=300)
plt.show()
#Tinh diem trung vi
for m in sorted(set(majors)):
    scores = [s for s, mj in zip(exam_scores, majors) if mj == m]
    print(m, statistics.median(scores))