import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建图表
fig, ax = plt.subplots(figsize=(10, 5))

# 设定节点位置
elements = {
    "User": (0.1, 0.5),
    "Frontend\n(React/Vue)": (0.3, 0.5),
    "Backend\n(Django/Flask)": (0.5, 0.5),
    "Database\n(PostgreSQL)": (0.7, 0.7),
    "Cloud Storage\n(AWS S3)": (0.7, 0.3),
    "External APIs\n(Google OAuth, Email)": (0.9, 0.5)
}

# 绘制元素
for name, pos in elements.items():
    if "User" in name:
        ax.text(pos[0], pos[1], "🧑‍💻", ha="center", va="center", fontsize=15)
        ax.text(pos[0], pos[1] - 0.1, name, ha="center", va="center", fontsize=10, fontweight="bold")
    else:
        rect = patches.Rectangle((pos[0] - 0.05, pos[1] - 0.05), 0.1, 0.1, linewidth=1.5, edgecolor="black", facecolor="white")
        ax.add_patch(rect)
        ax.text(pos[0], pos[1], name, ha="center", va="center", fontsize=9, fontweight="bold")

# 连接线
connections = [
    ("User", "Frontend\n(React/Vue)"),
    ("Frontend\n(React/Vue)", "Backend\n(Django/Flask)"),
    ("Backend\n(Django/Flask)", "Database\n(PostgreSQL)"),
    ("Backend\n(Django/Flask)", "Cloud Storage\n(AWS S3)"),
    ("Backend\n(Django/Flask)", "External APIs\n(Google OAuth, Email)")
]

for start, end in connections:
    start_pos = elements[start]
    end_pos = elements[end]
    ax.annotate("", xy=end_pos, xytext=start_pos, arrowprops=dict(arrowstyle="->", lw=1.5))

# 去除坐标轴
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# 保存并显示图像
plt.savefig("high_level_system_architecture.png", dpi=300)
plt.show()
