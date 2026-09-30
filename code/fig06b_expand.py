# 6주차 2차시 보강 그림: 조세지출 관리 흐름(그림 6-5), 성인지 예·결산 순환(그림 6-6)
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


# ---------------------------------------------------------------- 그림 6-5
# 조세지출의 연간 관리 흐름과 국세감면율 관리
fig, ax = plt.subplots(figsize=(12.5, 7.4))
ax.set_xlim(0, 14.3)
ax.set_ylim(0, 10.4)
ax.axis("off")

top = [
    ("기본계획 수립\n3월 31일까지\n재정경제부장관\n국무회의 심의\n(제142조 제1항)", "#f7f7fc", "#5b6ee1"),
    ("건의와 의견제출\n4월 30일까지\n중앙행정기관의 장\n재정경제부 제출\n(제2-4항)", "#f7f7fc", "#5b6ee1"),
    ("평가\n신규 300억 원 이상:\n법률안에 평가 첨부\n기한 종료 특례:\n120일 전 국회 제출", "#f7f7fc", "#5b6ee1"),
    ("조세지출예산서\n직전 연도 실적,\n해당·다음 연도 추정\n예산안 첨부서류\n(제142조의2)", "#f4faf5", "#3a7d44"),
    ("조세지출결산서\n직전 연도 실적을\n분석한 보고서\n2025년 12월 신설\n(제142조의3)", "#f4faf5", "#3a7d44"),
]
xs = [0.25 + i * 2.85 for i in range(5)]
for (t, fc, ec), x in zip(top, xs):
    box(ax, x, 6.6, 2.5, 3.0, t, fc=fc, ec=ec)
for x in xs[:-1]:
    arrow(ax, x + 2.6, 8.1, x + 2.85, 8.1)
ax.text(7.15, 10.25, "조세특례의 사전·사후관리와 예산서·결산서", ha="center", va="center",
        fontsize=12, fontweight="bold", color="#333")

# 아래: 국세감면율 관리
box(ax, 3.3, 4.0, 7.7, 1.2, "국세감면율 관리 (국가재정법 제88조)", fc="#fdf9f4", ec="#c77b2f", weight="bold")
arrow(ax, 10.05, 6.5, 10.05, 5.4, color="#c77b2f", ls="--", lw=1.3)
sub = [
    ("국세감면한도\n직전 3개 연도 평균\n국세감면율 + 0.5%포인트\n이하가 되도록 노력\n(제1항, 시행령 제41조)", 0.6),
    ("새 감면 요청 시\n기존 감면의 축소·폐지\n또는 재정지출 축소\n방안을 함께\n제출 (제2항)", 5.0),
    ("한도 초과 시\n그 내역과 사유를\n예산안 첨부서류와\n함께 국회에\n제출 (제3항)", 9.4),
]
for t, x in sub:
    box(ax, x, 0.5, 4.2, 2.7, t, fc="white", ec="#c77b2f")
    arrow(ax, x + 2.1, 3.9 if x != 5.0 else 3.9, x + 2.1, 3.4, color="#c77b2f")
fig.savefig(FIG / "fig06b_taxexp_cycle.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 6-6
# 성인지 예산서와 성인지 결산서의 순환
fig, ax = plt.subplots(figsize=(12.5, 8.4))
ax.set_xlim(0, 14.3)
ax.set_ylim(0, 11.4)
ax.axis("off")

ax.text(7.15, 11.2, "성인지 예산서와 성인지 결산서의 순환", ha="center", va="center",
        fontsize=12, fontweight="bold", color="#333")
ax.text(0.25, 10.45, "예산 단계", ha="left", va="center", fontsize=11, color="#2f6fb0", fontweight="bold")
ax.text(0.25, 6.25, "결산 단계", ha="left", va="center", fontsize=11, color="#3a7d44", fontweight="bold")

# 예산 단계 (왼쪽에서 오른쪽)
b1 = [
    ("대상사업 선정\n작성기준과 방식 제시\n기획예산처장관이\n성평등가족부장관과 협의", 0.25),
    ("성인지 예산서 작성\n각 중앙관서의 장이 작성\n성평등 기대효과, 성과목표,\n성별 수혜분석 (제26조)", 4.95),
    ("국회 제출\n예산안 첨부서류\n(제34조 제9호)\n의결 대상은 아님", 9.65),
]
for t, x in b1:
    box(ax, x, 7.3, 4.3, 2.8, t, fc="#f5f9fd", ec="#2f6fb0")
arrow(ax, 4.65, 8.7, 4.95, 8.7)
arrow(ax, 9.35, 8.7, 9.65, 8.7)

# 결산 단계 (오른쪽에서 왼쪽)
b2 = [
    ("집행\n선정된 대상사업의\n예산 집행", 9.65),
    ("성인지 결산서 작성\n집행실적, 성평등 효과분석\n및 평가 (제57조)", 4.95),
    ("국회 제출\n결산 첨부서류\n(국가회계법 제15조의2)", 0.25),
]
for t, x in b2:
    box(ax, x, 3.1, 4.3, 2.8, t, fc="#f4faf5", ec="#3a7d44")
arrow(ax, 11.8, 7.2, 11.8, 6.0, color="#555")
arrow(ax, 9.55, 4.5, 9.25, 4.5)
arrow(ax, 4.85, 4.5, 4.55, 4.5)
arrow(ax, 2.4, 6.0, 2.4, 7.2, color="#3a7d44", ls="--", lw=1.3)
ax.text(2.6, 6.6, "평가 결과를 다음 연도 예산에 반영", ha="left", va="center", fontsize=10, color="#3a7d44")

# 아래: 같은 틀의 확장
ext = [
    ("온실가스감축인지\n예산서(제27조)\n결산서(제57조의2)\n협의 상대는\n기후에너지환경부장관", 0.25),
    ("기금\n성인지 기금운용계획서\n(제68조의2)\n성인지 기금결산서\n(제73조의2)", 4.95),
    ("지방자치단체\n지방재정법 제36조의2\n지방자치단체의 장이\n성인지 예산서를\n작성", 9.65),
]
for t, x in ext:
    box(ax, x, 0.1, 4.3, 2.2, t, fc="white", ec="#7a5fa8")
ax.text(7.15, 2.66, "같은 틀이 적용되는 범위", ha="center", va="center", fontsize=10.5, color="#7a5fa8", fontweight="bold")
fig.savefig(FIG / "fig06b_gender_cycle.png", dpi=150, bbox_inches="tight")
plt.close(fig)
