# 13주차 1차시(재정개혁론) 개념도 생성
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


# ---------------------------------------------------------------- 그림 13-1
# 예산제도 개혁의 연표: LBS -> PBS -> PPBS -> ZBB -> 신성과주의
fig, ax = plt.subplots(figsize=(13, 6.6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

cols = [
    ("품목별 예산제도\n(LBS)", "1907 뉴욕시 보건국\n1912 태프트위원회 권고\n1921 예산회계법", "통제 정향\n(투입: 무엇을 사는가)", "#f5f9fd", "#2f6fb0"),
    ("성과주의 예산제도\n(PBS)", "1949 후버위원회 건의\n1950 예산회계절차법\n연방·주·지방 확산", "관리 정향\n(산출·원가: 얼마에 하는가)", "#f4fbf6", "#2f8f4e"),
    ("계획예산제도\n(PPBS)", "1961 국방부 도입\n1965 전 연방 확대\n1971 폐지", "기획 정향\n(목표·사업: 무엇을 왜 하는가)", "#faf8fc", "#7a5fa8"),
    ("영기준 예산제도\n(ZBB)", "1970 민간(TI) 개발\n1977 연방 도입\n1981 폐지", "평가 정향\n(사업+금액: 계속할 가치)", "#fdf9f4", "#c77b2f"),
    ("신성과주의\n예산제도", "1993 GPRA 제정\n2010 GPRA 현대화법\n각국 확산", "성과 정향\n(결과: 무엇이 달라졌는가)", "#fff5f5", "#c0392b"),
]
for i, (name, hist, orient, fc, ec) in enumerate(cols):
    x = 0.35 + i * 2.72
    box(ax, x, 6.7, 2.42, 1.7, name, fc=fc, ec=ec, weight="bold")
    box(ax, x, 4.2, 2.42, 2.1, hist, fc="white", ec=ec)
    box(ax, x, 2.3, 2.42, 1.5, orient, fc=fc, ec=ec)
    if i < 4:
        arrow(ax, x + 2.5, 7.55, x + 2.72, 7.55)

box(ax, 1.5, 0.5, 11.0, 1.2,
    "새 제도는 옛 제도를 대체하지 않고 변화한 모습으로 병존한다:\n개혁의 역사는 대체가 아니라 퇴적의 역사",
    fc="#f7f7fc", ec="#5b6ee1")
ax.set_title("예산제도 개혁의 연표: 미국 연방정부를 중심으로", fontsize=14, pad=12)
fig.savefig(FIG / "fig13_timeline.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 13-2
# 네 예산제도의 재정정보 정향 비교
fig, ax = plt.subplots(figsize=(12, 6.8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis("off")

flow = [
    ("투입(input)\n품목: 인건비 · 물건비", 0.6, "#f5f9fd", "#2f6fb0"),
    ("활동 · 산출(output)\n업무단위와 원가", 5.0, "#f4fbf6", "#2f8f4e"),
    ("목표 · 계획(plan)\n사업구조와 대안", 9.4, "#faf8fc", "#7a5fa8"),
]
for t, x, fc, ec in flow:
    box(ax, x, 8.2, 4.0, 1.7, t, fc=fc, ec=ec)
for x in (4.7, 9.1):
    arrow(ax, x, 9.05, x + 0.3, 9.05)

inst = [
    ("품목별(LBS): 통제\n무엇을 사는가", 0.6, "#2f6fb0"),
    ("성과주의(PBS): 관리\n무슨 일을 얼마에 하는가", 5.0, "#2f8f4e"),
    ("계획예산(PPBS): 기획\n무엇을 왜 하는가", 9.4, "#7a5fa8"),
]
for t, x, ec in inst:
    box(ax, x, 5.0, 4.0, 1.8, t, fc="white", ec=ec)
    arrow(ax, x + 2.0, 6.9, x + 2.0, 8.1, color=ec, ls="--", lw=1.3)

box(ax, 0.6, 1.4, 12.8, 1.8,
    "영기준(ZBB): 평가 - 흐름 전체를 원점(zero base)에서 재검토\n사업대안과 금액대안(최저 · 현행 · 증액 수준)을 함께 결정",
    fc="#fdf9f4", ec="#c77b2f")
for x in (2.6, 7.0, 11.4):
    arrow(ax, x, 3.3, x, 4.9, color="#c77b2f", ls="--", lw=1.3)

ax.text(7.0, 0.6, "어느 제도도 다른 제도의 정보를 완전히 대체하지 못하며, 현실의 예산제도는 이들의 조합으로 운영된다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("네 예산제도의 재정정보 정향: 어떤 정보로 예산을 결정하는가", fontsize=14, pad=12)
fig.savefig(FIG / "fig13_orientation.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig13_*.png"))])
