# 7주차 2차시 보강 그림: 기본소득과 부의 소득세 비교, 설계 변수 도해, 연간 재원 소요
# 실행: VIRTUAL_ENV= uv run --project $HOME/default-uv-env python -X utf8 "<이 파일 경로>"
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("white")
import koreanize_matplotlib  # noqa: E402,F401
import figfit  # noqa: E402,F401  (상자 글씨 자동 크기)

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(exist_ok=True)

BLUE, ORANGE, GREEN, PURPLE, RED = "#2f6fb0", "#c77b2f", "#2f8f4e", "#5b6ee1", "#c0392b"


def box(ax, x, y, w, h, text, fc="#f5f9fd", ec=BLUE, fontsize=11, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight)


def arrow(ax, x1, y1, x2, y2, color="#555", style="-|>", lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=16, color=color, lw=lw, linestyle=ls))


# ---------------------------------------------------------------- 그림 7-4
# 기본소득과 부의 소득세의 급여 구조 (예시 수치)
x = np.linspace(0, 160, 321)
ubi = np.full_like(x, 25.0)
nit = np.clip(50 - 0.5 * x, 0, None)

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 5.6))

a1.plot(x, ubi, color=BLUE, lw=2.6, label="기본소득 (정액 25)")
a1.plot(x, nit, color=ORANGE, lw=2.6, label="부의 소득세 (기준소득 100, 보충률 50%)")
a1.axvline(100, ymax=0.72, color="#888", lw=1, ls=":")
a1.text(101.5, 40, "기준소득 100\n(이 지점에서 급여 0)", fontsize=10, color="#555", va="center")
a1.set_xlim(0, 160)
a1.set_ylim(0, 68)
a1.set_xlabel("근로소득 (예시 단위)")
a1.set_ylabel("정부 급여액 (예시 단위)")
a1.set_title("소득이 늘면 급여는 어떻게 변하는가", fontsize=13)
a1.legend(loc="upper right", fontsize=10, frameon=False)

a2.plot(x, x, color="#999", lw=1.6, ls="--", label="급여 없음")
a2.plot(x, x + ubi, color=BLUE, lw=2.6, label="기본소득")
a2.plot(x, x + nit, color=ORANGE, lw=2.6, label="부의 소득세")
a2.axvline(100, color="#888", lw=1, ls=":")
a2.set_xlim(0, 160)
a2.set_ylim(0, 190)
a2.set_xlabel("근로소득 (예시 단위)")
a2.set_ylabel("근로소득과 급여의 합 (세전, 예시 단위)")
a2.set_title("급여를 더한 총소득", fontsize=13)
a2.legend(loc="upper left", fontsize=10, frameon=False)

fig.suptitle("기본소득과 부의 소득세의 급여 구조 비교 (예시)", fontsize=15, y=1.0)
fig.tight_layout()
fig.savefig(FIG / "fig07b_nit_vs_ubi.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 7-5
# 기본소득 제안을 읽는 세 가지 설계 변수
fig, ax = plt.subplots(figsize=(12.5, 6.4))
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis("off")

box(ax, 4.3, 6.2, 5.4, 1.3, "기본소득 제안", fc="#f7f7fc", ec=PURPLE, weight="bold")
titles = [
    (0.4, "급여 수준\n월 10만 원 부분형\n월 100만 원 완전형"),
    (4.9, "재원 조달\n증세, 기존 지출 대체,\n공유부 과세"),
    (9.4, "기존 복지와의 관계\n보완형(추가)\n대체형(흡수)"),
]
for x0, t in titles:
    box(ax, x0, 2.9, 4.2, 2.3, t, fc="white", ec=BLUE)
    arrow(ax, 7.0, 6.1, x0 + 2.1, 5.35, color=BLUE)
    arrow(ax, x0 + 2.1, 2.8, 7.0, 1.95, color=ORANGE)
box(ax, 2.2, 0.5, 9.6, 1.4, "연간 재정 소요, 순재정부담, 분배 효과, 노동 유인이 각각 달라진다",
    fc="#fdf9f4", ec=ORANGE)
ax.set_title("같은 이름 아래 다른 제도: 제안을 읽는 세 가지 설계 변수", fontsize=14, pad=10)
fig.savefig(FIG / "fig07b_design_vars.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 7-6
# 전 국민 기본소득의 연간 소요 (인구 5,000만 명 가정, 2026년 본예산 총지출 727.9조 원과 비교)
pop = 5000  # 만 명
monthly = [10, 30, 50, 100]  # 만 원
cost = [pop * m * 12 / 10000 for m in monthly]  # 조 원
budget = 727.9

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar([f"월 {m}만 원" for m in monthly], cost, color=[BLUE] * 4, edgecolor="#1f4f80",
              width=0.55)
for b, c in zip(bars, cost):
    ax.text(b.get_x() + b.get_width() / 2, c + 12, f"{c:,.0f}조 원\n(총지출의 {c / budget * 100:.1f}%)",
            ha="center", va="bottom", fontsize=11)
ax.axhline(budget, color=RED, lw=1.8, ls="--")
ax.text(3.45, budget + 10, "2026년 본예산 총지출 727.9조 원", ha="right", va="bottom",
        fontsize=11, color=RED)
ax.set_ylim(0, 820)
ax.set_ylabel("연간 소요 (조 원)")
ax.set_title("전 국민 기본소득의 연간 소요 (인구 5,000만 명 가정)", fontsize=14)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.savefig(FIG / "fig07b_ubi_cost.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("done")
