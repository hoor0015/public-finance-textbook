# 5주차 2차시 보강 그림 (그림 5-6, 5-7) 생성
# 실행: VIRTUAL_ENV= uv run --project <기본 uv 환경> python -X utf8 <이 파일 경로>
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


# ---------------------------------------------------------------- 그림 5-6
# 공통비 배부: 직접비 + 배부된 공통비 = 전체 원가 (청소행정 예시)
fig, ax = plt.subplots(figsize=(12, 6.6))
ax.set_xlim(0, 14)
ax.set_ylim(0.3, 9.6)
ax.axis("off")

ax.text(2.3, 8.7, "직접비", ha="center", va="center", fontsize=12, fontweight="bold", color="#333")
ax.text(7.0, 8.7, "배부된 공통비", ha="center", va="center", fontsize=12, fontweight="bold", color="#333")
ax.text(11.7, 8.7, "전체 원가", ha="center", va="center", fontsize=12, fontweight="bold", color="#333")

rows = [
    ("생활폐기물 수거\n직접비 12억 원", "공통비 3억 원\n(운행거리 75%)", "전체 원가\n15억 원", 6.4),
    ("재활용품 수집\n직접비 6억 원", "공통비 0.8억 원\n(운행거리 20%)", "전체 원가\n6.8억 원", 4.5),
    ("무단투기 감시\n직접비 2억 원", "공통비 0.2억 원\n(운행거리 5%)", "전체 원가\n2.2억 원", 2.6),
]
for left, mid, right, y in rows:
    box(ax, 0.7, y, 3.2, 1.3, left, fc="#f5f9fd", ec="#2f6fb0", fontsize=11)
    box(ax, 5.4, y, 3.2, 1.3, mid, fc="#fdf9f4", ec="#c77b2f", fontsize=11)
    box(ax, 10.1, y, 3.2, 1.3, right, fc="#f4fbf6", ec="#2f8f4e", fontsize=11)
    arrow(ax, 4.05, y + 0.65, 5.25, y + 0.65)
    arrow(ax, 8.75, y + 0.65, 9.95, y + 0.65)

box(ax, 4.6, 0.55, 4.8, 1.1, "공통비 원천\n청소차량 운영비 4억 원", fc="white", ec="#c77b2f", fontsize=11)
arrow(ax, 7.0, 1.75, 7.0, 2.5, color="#c77b2f", ls="--")
ax.text(1.6, 1.1, "예시", ha="center", va="center", fontsize=10, color="#555")
fig.savefig(FIG / "fig05b_costalloc.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 5-7
# 같은 사업 구조 위에서 이어지는 예산 문서들
fig, ax = plt.subplots(figsize=(12, 6.8))
ax.set_xlim(0, 14)
ax.set_ylim(0.3, 10)
ax.axis("off")

stages = [
    ("요구·편성", "예산요구서\n+ 성과계획서\n+ 전년도 성과보고서\n(국가재정법 제85조의7)"),
    ("국회 심의", "예산안\n+ 사업별 설명서\n+ 성과계획서\n(국가재정법 제34조)"),
    ("집행", "사업 구조에\n따른 집행과\n기록\n(세부사업 단위)"),
    ("결산", "세입세출결산\n+ 재무제표\n+ 성과보고서\n(국가회계법 제14조)"),
]
x0, w, gap = 0.5, 2.9, 0.4
for i, (st, doc) in enumerate(stages):
    x = x0 + i * (w + gap)
    box(ax, x, 7.6, w, 1.3, st, fc="#f7f7fc", ec="#5b6ee1", fontsize=12, weight="bold")
    box(ax, x, 4.0, w, 2.6, doc, fc="#f5f9fd", ec="#2f6fb0", fontsize=11)
    arrow(ax, x + w / 2, 7.5, x + w / 2, 6.8)
    if i < len(stages) - 1:
        arrow(ax, x + w + 0.08, 8.25, x + w + gap - 0.08, 8.25, lw=2.2, color="#333")
    arrow(ax, x + w / 2, 3.9, x + w / 2, 3.0, style="<|-|>", color="#2f8f4e")

box(ax, 0.5, 1.4, 12.8, 1.5, "공통의 단위: 프로그램(정책사업) - 단위사업 - 세부사업",
    fc="#f4fbf6", ec="#2f8f4e", fontsize=13, weight="bold")
fig.savefig(FIG / "fig05b_docflow.png", dpi=150, bbox_inches="tight")
plt.close(fig)
