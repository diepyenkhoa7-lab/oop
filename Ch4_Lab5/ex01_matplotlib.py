import matplotlib.pyplot as plt
months = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11',
'T12']
sales = [120, 135, 160, 190, 210, 250, 230, 220, 195, 170, 200, 280]
ad_budget = [10, 12, 15, 20, 22, 30, 25, 24, 18, 15, 22, 35]
rainfall = [20, 15, 30, 80, 150, 220, 250, 210, 180, 120, 50, 25]
#Nhiệm vụ 1
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(months, sales, color='darkblue', linestyle='--', marker='o', label='Doanh số bán hàng')
ax.set_xlabel('Tháng')
ax.set_ylabel('Doanh số bán hàng')
ax.set_title('Xu hướng doanh số năm 2025')
ax.grid(True)
ax.legend()
plt.show()

#Nhiệm vụ 2
max_budget = max(ad_budget)
max_index = ad_budget.index(max_budget)

color = ['skyblue'] * len(ad_budget)
color[max_index] = 'crimson'

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(months, ad_budget, color=color)
ax.set_xlabel('Tháng')
ax.set_ylabel('Chi tiêu quảng cáo')
ax.set_title('Chi tiêu quảng cáo năm 2025')
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
#Nhiệm vụ 3
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].scatter(ad_budget, sales, color='green', marker='o')
axes[0].set_xlabel('Chi phí quảng cáo')
axes[0].set_ylabel('Doanh số bán hàng')
axes[0].set_title('Mối quan hệ giữa chi tiêu quảng cáo và doanh số')
axes[0].grid(True)

axes[1].plot(
    months,
    sales,
    color='blue',
    marker='o',
    label='Doanh số'
)

axes[1].plot(
    months,
    rainfall,
    color='deepskyblue',
    linestyle='--',
    marker='s',
    label='Luong mua'
)

axes[1].set_xlabel('Tháng')
axes[1].set_ylabel('Giá trị')
axes[1].set_title('Doanh Số và Lượng Mưa Năm 2025')
axes[1].legend()
axes[1].grid(True)


plt.tight_layout()
plt.savefig("images/baocao_doanhso_2025.png", dpi=300, bbox_inches='tight')
plt.show()
