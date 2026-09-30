# 6주차 1차시 보강 그림: 추경 편성 추이(그림 6-2), 재정수요 대응 경로(그림 6-3)
# 실행: VIRTUAL_ENV= uv run --project $HOME/default-uv-env python -X utf8 "<이 파일 경로>"
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
import koreanize_matplotlib  # noqa: E402,F401
import figfit  # noqa: E402,F401  (상자 글씨 자동 크기)

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(exist_ok=True)


def box(ax, x, y, w, h, text, fc="#f5f9fd", ec="#2f6fb0", weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=11, fontweight=weight)


def arrow(ax, x1, y1, x2, y2, color="#555", style="-|>", lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=16, color=color, lw=lw, linestyle=ls))


# ---------------------------------------------------------------- 그림 6-2
# 연도별 추경 규모 (추경규모 = 세출 증가와 세입 감소 등을 합친 재원 조달 규모, 조 원)
# 출처: 기획재정부 연도별 예산서(e-나라지표 추경편성 추이), 2026년은 정책브리핑(2026-04-11)
data = {
    2008: [4.6],
    2009: [28.4],
    2013: [17.4],
    2015: [11.6],
    2016: [11.0],
    2017: [11.0],
    2018: [3.8],
    2019: [5.8],
    2020: [11.7, 12.2, 35.1, 7.8],
    2021: [14.9, 34.9],
    2022: [16.9, 62.0],
    2025: [13.8, 31.8],
    2026: [26.2],
}
years = list(range(2008, 2027))
colors = ["#9dbfe0", "#2f6fb0", "#c77b2f", "#2b7a78"]
labels = ["1회", "2회", "3회", "4회"]

fig, ax = plt.subplots(figsize=(12.5, 6.4))
used = set()
for yr in years:
    vals = data.get(yr, [])
    bottom = 0.0
    for i, v in enumerate(vals):
        ax.bar(yr, v, bottom=bottom, width=0.62, color=colors[i], ec="white", lw=0.8,
               label=labels[i] if i not in used else None)
        used.add(i)
        bottom += v
    if vals:
        ax.text(yr, bottom + 1.2, f"{bottom:.1f}", ha="center", va="bottom", fontsize=10)
    else:
        ax.text(yr, 1.0, "없음", ha="center", va="bottom", fontsize=9, color="#888")

ax.set_xticks(years)
ax.set_xticklabels([str(y) for y in years], fontsize=10)
ax.set_ylim(0, 88)
ax.set_xlim(2007.3, 2026.7)
ax.set_ylabel("추경 규모 (조 원)", fontsize=11)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", color="#e6e6e6", lw=0.8)
ax.set_axisbelow(True)
ax.legend(title="편성 회차", loc="upper left", frameon=False, fontsize=10, title_fontsize=10)
ax.set_title("연도별 추가경정예산 규모 (2008-2026년)", fontsize=14, pad=12)
fig.text(0.01, -0.02,
         "자료: 기획재정부 연도별 예산서(e-나라지표 추경편성 추이), 2026년은 기획예산처 발표(2026-04-11). "
         "추경 규모는 세출 증가와 세입 감소 등을 합친 재원 조달 규모.",
         fontsize=9, color="#555")
fig.savefig(FIG / "fig06a_supplementary_trend.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 6-3
# 성립된 예산의 집행 중 재정수요가 생겼을 때의 대응 경로
fig, ax = plt.subplots(figsize=(12.5, 8.2))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11.4)
ax.axis("off")

box(ax, 2.6, 9.4, 8.0, 1.4, "성립된 예산의 집행 중\n추가 재정수요 또는 세입 부족 발생",
    fc="#f7f7fc", ec="#5b6ee1", weight="bold")
box(ax, 11.4, 9.4, 2.4, 1.4, "의결 전이라면\n수정예산안\n(제35조)", fc="white", ec="#2f6fb0")
ax.plot([10.7, 11.3], [10.1, 10.1], color="#2f6fb0", lw=1.3, ls="--")

arrow(ax, 6.6, 9.3, 6.6, 8.3)
box(ax, 2.6, 6.6, 8.0, 1.6, "질문 1. 예비비, 이용·전용 등\n기존 신축성 수단으로 충당할 수 있는가?",
    fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 11.4, 6.6, 2.4, 1.6, "기존 수단으로\n대응\n(국회 의결 범위 안)", fc="#f4faf5", ec="#3a7d44")
arrow(ax, 10.7, 7.4, 11.3, 7.4, color="#3a7d44")
ax.text(11.0, 7.75, "예", ha="center", va="bottom", fontsize=11, color="#3a7d44")

arrow(ax, 6.6, 6.5, 6.6, 5.5, color="#c77b2f")
ax.text(6.9, 5.95, "아니오", ha="left", va="center", fontsize=11, color="#c77b2f")
box(ax, 2.6, 3.8, 8.0, 1.6, "질문 2. 국가재정법 제89조 제1항의\n세 가지 사유에 해당하는가?",
    fc="#fdf9f4", ec="#c77b2f", weight="bold")

arrow(ax, 4.2, 3.7, 3.4, 2.7, color="#3a7d44")
ax.text(3.3, 3.25, "예", ha="right", va="center", fontsize=11, color="#3a7d44")
arrow(ax, 9.0, 3.7, 10.2, 2.7, color="#c77b2f")
ax.text(10.2, 3.25, "아니오", ha="left", va="center", fontsize=11, color="#c77b2f")

box(ax, 0.6, 0.6, 5.6, 2.0, "추경안 편성·국회 제출\n국회 확정 전에는\n배정·집행 금지(제2항)",
    fc="#f4faf5", ec="#3a7d44", weight="bold")
box(ax, 7.4, 0.6, 5.6, 2.0, "추경 편성 불가\n다음 연도 본예산의\n편성 과정에서 검토",
    fc="white", ec="#c77b2f")

ax.set_title("추가 재정수요가 생겼을 때의 대응 경로", fontsize=14, pad=12)
fig.savefig(FIG / "fig06a_response_path.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("done")
