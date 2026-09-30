# 7주차 1차시 보강 그림 (목표-수단 구조, 재정 기조와 경기 국면, 재정정책의 시차)
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


def box(ax, x, y, w, h, text, fc="#f5f9fd", ec="#2f6fb0", fontsize=11, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight)


def arrow(ax, x1, y1, x2, y2, color="#555", style="-|>", lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=16, color=color, lw=lw, linestyle=ls))


# ---------------------------------------------------------------- 그림 7-2
# 재정정책의 목표-수단 구조
fig, ax = plt.subplots(figsize=(12.5, 8.0))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12.2)
ax.axis("off")

box(ax, 2.5, 10.3, 9.0, 1.5, "궁극 목표\n국민의 경제적 존엄성 확보 (Sperling, 2020)",
    fc="#f7f7fc", ec="#5b6ee1", weight="bold")
mids = [(0.8, "경기 안정\n(총수요 관리)"), (5.1, "성장\n(잠재력 배양)"), (9.4, "분배\n(소득 재분배)")]
for x, t in mids:
    box(ax, x, 7.9, 3.8, 1.6, t, fc="#f5f9fd", ec="#2f6fb0")
    arrow(ax, x + 1.9, 10.2, x + 1.9, 9.65, color="#5b6ee1")

box(ax, 0.8, 4.7, 5.9, 2.1, "세입 측면의 수단\n조세 · 세외수입 · 국공채 발행",
    fc="#f2fafa", ec="#2b7a78")
box(ax, 7.3, 4.7, 5.9, 2.1, "세출 측면의 수단\n지출구조조정 · 특정 분야 재정지출",
    fc="#fdf9f4", ec="#c77b2f")
arrow(ax, 2.7, 7.8, 3.6, 6.95, color="#555")
arrow(ax, 6.9, 7.8, 5.4, 6.95, color="#555")
arrow(ax, 7.1, 7.8, 8.6, 6.95, color="#555")
arrow(ax, 11.3, 7.8, 10.3, 6.95, color="#555")

box(ax, 0.8, 2.4, 12.4, 1.6, "정책혼합 (세입 + 세출)\n재정 적자 · 흑자 정책, 긴축 · 확장 정책",
    fc="#f4fbf6", ec="#2f8f4e", weight="bold")
arrow(ax, 3.7, 4.6, 3.7, 4.15, color="#555")
arrow(ax, 10.2, 4.6, 10.2, 4.15, color="#555")

box(ax, 0.8, 0.2, 12.4, 1.5,
    "트릴레마: 재정지출 확대 · 재정 건전성 확보 · 낮은 조세 부담은 동시에 달성할 수 없다",
    fc="#fdf9f4", ec="#c77b2f")
ax.set_title("재정정책의 목표-수단 계층제", fontsize=14, pad=12)
fig.savefig(FIG / "fig07a_goals.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 7-3
# 재정 기조와 경기 국면: 경기대응적 대 경기순응적
fig, ax = plt.subplots(figsize=(12.5, 7.4))
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 10.4)
ax.axis("off")

box(ax, 3.0, 8.3, 5.4, 1.3, "경기 불황", fc="#fff5f5", ec="#c0392b", weight="bold")
box(ax, 8.9, 8.3, 5.4, 1.3, "경기 호황", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 0.3, 4.6, 2.3, 3.1, "확장\n지출 증가\n감세", fc="#f2f2f2", ec="#888", weight="bold")
box(ax, 0.3, 0.9, 2.3, 3.1, "긴축\n지출 감축\n증세", fc="#f2f2f2", ec="#888", weight="bold")

box(ax, 3.0, 4.6, 5.4, 3.1,
    "경기대응적 (안정화)\n침체를 완충한다\n예) 불황기의\n추경과 감세",
    fc="#f4fbf6", ec="#2f8f4e")
box(ax, 8.9, 4.6, 5.4, 3.1,
    "경기순응적\n과열을 더 키운다\n예) 세수가 넘치는\n호황기의 지출 확대",
    fc="#fdf9f4", ec="#c77b2f")
box(ax, 3.0, 0.9, 5.4, 3.1,
    "경기순응적\n침체를 더 깊게 한다\n예) 위기 국면의\n긴축 요구",
    fc="#fdf9f4", ec="#c77b2f")
box(ax, 8.9, 0.9, 5.4, 3.1,
    "경기대응적 (안정화)\n과열을 식힌다\n예) 호황기 지출 억제와\n세수 초과분 상환",
    fc="#f4fbf6", ec="#2f8f4e")
ax.set_title("재정 기조와 경기 국면: 같은 확장도 시점에 따라 역할이 갈린다", fontsize=14, pad=12)
fig.savefig(FIG / "fig07a_stance.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 7-5
# 재정정책의 시차와 2026년 고유가 추경의 실제 일정
fig, ax = plt.subplots(figsize=(12.5, 7.6))
ax.set_xlim(0, 15.4)
ax.set_ylim(0, 10.6)
ax.axis("off")

box(ax, 3.3, 8.5, 5.3, 1.2, "내부시차: 정책이 결정되기까지", fc="#f7f7fc", ec="#5b6ee1", weight="bold")
box(ax, 9.3, 8.5, 5.3, 1.2, "외부시차: 결정 뒤 효과가 나타나기까지", fc="#f7f7fc", ec="#5b6ee1", weight="bold")

xs = [0.3, 3.3, 6.3, 9.3, 12.3]
labels = ["경기 충격 발생", "인식시차\n충격을 파악", "결정시차\n편성 + 국회 의결",
          "집행시차\n배정 · 지급", "효과시차\n소비 · 고용 반응"]
fcs = ["#fff5f5", "#f5f9fd", "#f5f9fd", "#fdf9f4", "#fdf9f4"]
ecs = ["#c0392b", "#2f6fb0", "#2f6fb0", "#c77b2f", "#c77b2f"]
for x, t, fc, ec in zip(xs, labels, fcs, ecs):
    box(ax, x, 5.9, 2.3, 2.0, t, fc=fc, ec=ec)
for i in range(4):
    arrow(ax, xs[i] + 2.4, 6.9, xs[i + 1] - 0.1, 6.9, color="#555")

box(ax, 0.3, 2.6, 4.6, 2.3, "자동안정화장치는\n이 경로를 거치지 않아\n결정시차가 없다",
    fc="#f4fbf6", ec="#2f8f4e")
box(ax, 5.4, 2.6, 3.8, 2.3, "2026년 고유가 추경\n3월 31일 제출\n4월 11일 국회 확정\n(11일)",
    fc="white", ec="#2f6fb0")
box(ax, 9.7, 2.6, 3.8, 2.3, "4월 27일 지급 개시\n(확정 후 16일)",
    fc="white", ec="#c77b2f")
arrow(ax, 7.45, 5.8, 7.3, 5.05, color="#2f6fb0", ls="--", lw=1.3)
arrow(ax, 10.45, 5.8, 11.3, 5.05, color="#c77b2f", ls="--", lw=1.3)

box(ax, 0.3, 0.2, 14.3, 1.6,
    "시차가 길어 집행 시점에 경기가 이미 회복되었다면 확장 재정은 오히려 호황을 키울 수 있다",
    fc="#fdf9f4", ec="#c77b2f")
ax.set_title("재정정책의 시차: 재량 경로는 결정과 집행에 시간이 든다", fontsize=14, pad=12)
fig.savefig(FIG / "fig07a_lags.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig07a_*.png"))])
