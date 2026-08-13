# 5주차(1차시·2차시) 개념도 생성
# 실행: cd $HOME/default-uv-env && PYTHONIOENCODING=utf-8 VIRTUAL_ENV= uv run python "<이 파일 경로>"
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
import koreanize_matplotlib  # noqa: E402,F401
import figfit  # noqa: E402,F401  (상자 글씨 자동 크기)

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(exist_ok=True)


def box(ax, x, y, w, h, text, fc="#f5f9fd", ec="#2f6fb0", fontsize=11, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight)


def arrow(ax, x1, y1, x2, y2, color="#555", style="-|>", lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=16, color=color, lw=lw, linestyle=ls))


# ---------------------------------------------------------------- 그림 5-1
# 세출예산 과목체계의 계층 구조 (소관-회계-분야-부문-프로그램-단위사업-세부사업-목)
fig, ax = plt.subplots(figsize=(12, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0.6, 13.7)
ax.axis("off")

rows = [
    ("소관\n(중앙관서별 구분)", 12.2, "#f7f7fc", "#5b6ee1"),
    ("회계\n(일반회계 · 특별회계)", 10.75, "#f7f7fc", "#5b6ee1"),
    ("분야 (구 '장')\n기능별 대분류 · 16개", 9.3, "#f5f9fd", "#2f6fb0"),
    ("부문 (구 '관')\n기능별 중분류", 7.85, "#f5f9fd", "#2f6fb0"),
    ("프로그램 · 정책사업 (구 '항')\n동일 목표 단위사업의 묶음", 6.4, "#f4fbf6", "#2f8f4e"),
    ("단위사업 (구 '세항')", 4.95, "#f4fbf6", "#2f8f4e"),
    ("세부사업 (구 '세세항')\n관리의 최소 단위", 3.5, "#f4fbf6", "#2f8f4e"),
    ("목 · 세목\n(인건비 · 물건비 등 품목)", 2.05, "#faf8fc", "#7a5fa8"),
]
H = 1.0
for t, y, fc, ec in rows:
    box(ax, 4.4, y, 5.2, H, t, fc=fc, ec=ec, fontsize=10.5)
for i in range(len(rows) - 1):
    y_from = rows[i][1]
    y_to = rows[i + 1][1] + H
    arrow(ax, 7.0, y_from, 7.0, y_to + 0.03)

# 왼쪽: 입법과목 · 행정과목
box(ax, 0.7, 6.4, 3.0, 3.9, "입법과목\n(장 · 관 · 항)\n변경 · 신설에\n국회 의결 필요",
    fc="#fff5f5", ec="#c0392b", fontsize=10)
box(ax, 0.7, 2.05, 3.0, 3.9, "행정과목\n(세항 · 목)\n요건을 갖춘 전용 등\n행정부 재량 운용",
    fc="#fdf9f4", ec="#c77b2f", fontsize=10)

# 오른쪽: 분류 방식
box(ax, 10.2, 7.85, 3.1, 2.45, "기능별 분류\n무슨 일에 쓰는가", fc="white", ec="#2f6fb0", fontsize=10)
box(ax, 10.2, 3.5, 3.1, 3.9, "사업별 분류\n어느 사업에 쓰는가", fc="white", ec="#2f8f4e", fontsize=10)
box(ax, 10.2, 2.05, 3.1, 1.0, "품목별 분류\n무엇을 사는가", fc="white", ec="#7a5fa8", fontsize=10)

ax.text(7.0, 1.15, "지방자치단체는 프로그램을 '정책사업', 목 · 세목을 '편성목 · 통계목'이라 부른다.\n괄호 안은 국가재정법 제21조가 쓰는 법률상 명칭이다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("세출예산 과목체계의 계층 구조 (중앙정부 기준)", fontsize=14, pad=14)
fig.savefig(FIG / "fig05_hierarchy.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 5-2
# 품목 중심에서 사업 중심으로: 예산서가 답하는 질문의 전환
fig, ax = plt.subplots(figsize=(12, 6.5))
ax.set_xlim(0, 14)
ax.set_ylim(0.3, 10)
ax.axis("off")

box(ax, 0.7, 7.6, 5.4, 1.6, "품목 중심 예산서\n(2007년 이전)", fc="#fdf9f4", ec="#c77b2f",
    fontsize=12, weight="bold")
box(ax, 7.9, 7.6, 5.4, 1.6, "프로그램 예산서\n(중앙 2007년 · 지방 2008년 도입)", fc="#f5f9fd", ec="#2f6fb0",
    fontsize=12, weight="bold")
arrow(ax, 6.35, 8.4, 7.65, 8.4, lw=2.6, color="#333")

left_rows = [
    "묻는 질문: 무엇을 사는 데 쓰는가",
    "과목의 초점: 품목(목 · 세목)",
    "지향: 투입 통제와 회계책임",
]
right_rows = [
    "묻는 질문: 무슨 사업에 쓰는가",
    "과목의 초점: 분야 - 부문 - 프로그램 - 단위사업",
    "지향: 사업 단위의 자율과 성과 책임",
]
for i, t in enumerate(left_rows):
    box(ax, 0.7, 5.9 - i * 1.5, 5.4, 1.2, t, fc="white", ec="#c77b2f", fontsize=10)
for i, t in enumerate(right_rows):
    box(ax, 7.9, 5.9 - i * 1.5, 5.4, 1.2, t, fc="white", ec="#2f6fb0", fontsize=10)

box(ax, 1.2, 0.9, 11.6, 1.4,
    "함께 추진된 재정개혁 패키지(2004-2007년): 국가재정운용계획 · 총액배분 자율편성 · 성과관리 · 디지털예산회계시스템(디브레인)",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=10.5)
ax.set_title("품목 중심에서 사업 중심으로: 예산서가 답하는 질문의 전환", fontsize=14, pad=12)
fig.savefig(FIG / "fig05_shift.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 5-3
# 프로그램 예산과 성과관리의 연계 구조 (목적의 계층 - 수단의 계층)
fig, ax = plt.subplots(figsize=(12, 7.2))
ax.set_xlim(0, 14)
ax.set_ylim(-1.5, 11.2)
ax.axis("off")

ax.text(3.0, 10.4, "목적의 계층 (왜 하는가)", ha="center", fontsize=12,
        fontweight="bold", color="#2f8f4e")
ax.text(11.0, 10.4, "수단의 계층 (무엇을 하는가)", ha="center", fontsize=12,
        fontweight="bold", color="#2f6fb0")

HH = 1.3
left_col = [
    ("임무\n(조직의 존재 이유)", 8.6),
    ("전략목표", 6.6),
    ("성과목표\n(프로그램 목표)", 4.6),
    ("성과지표\n(달성 여부의 측정)", 2.6),
]
right_col = [
    ("프로그램 (정책사업)", 4.6),
    ("단위사업", 2.6),
    ("세부사업", 0.6),
]
for t, y in left_col:
    box(ax, 0.8, y, 4.4, HH, t, fc="#f4fbf6", ec="#2f8f4e", fontsize=10.5)
for t, y in right_col:
    box(ax, 8.8, y, 4.4, HH, t, fc="#f5f9fd", ec="#2f6fb0", fontsize=10.5)

for i in range(len(left_col) - 1):
    arrow(ax, 3.0, left_col[i][1], 3.0, left_col[i + 1][1] + HH + 0.03, color="#2f8f4e")
for i in range(len(right_col) - 1):
    arrow(ax, 11.0, right_col[i][1], 11.0, right_col[i + 1][1] + HH + 0.03, color="#2f6fb0")

arrow(ax, 5.35, 5.25, 8.65, 5.25, style="<|-|>", ls="--", lw=1.4, color="#555")
ax.text(7.0, 5.55, "프로그램마다 성과목표", ha="center", fontsize=9.5, color="#333")
arrow(ax, 5.35, 3.25, 8.65, 3.25, style="<|-|>", ls="--", lw=1.4, color="#555")
ax.text(7.0, 3.55, "단위사업마다 성과지표", ha="center", fontsize=9.5, color="#333")

box(ax, 1.0, -1.2, 12.0, 1.3,
    "성과계획서 · 성과보고서로 국회 제출, 열린재정에 공개 (근거: 국가재정법 제85조의2 이하, 2021년 신설)",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=10.5)
ax.set_title("프로그램 예산과 성과관리의 연계 구조", fontsize=14, pad=12)
fig.savefig(FIG / "fig05_performance.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig05_*.png"))])
