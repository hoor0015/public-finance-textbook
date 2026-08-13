# 9주차(1차시·2차시) 재정준칙·통화정책 개념도 생성
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


# ---------------------------------------------------------------- 그림 9-1
# 재정준칙의 네 유형: 채무준칙 · 재정수지준칙 · 지출준칙 · 수입준칙
fig, ax = plt.subplots(figsize=(12.5, 7.6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11.4)
ax.axis("off")

box(ax, 3.9, 9.5, 6.2, 1.5,
    "재정준칙 (fiscal rules)\n총량적 재정지표에 대한\n법적 구속력 있는 수량적 제한",
    fc="#f7f7fc", ec="#5b6ee1", weight="bold")

cols = [
    ("채무준칙\n(debt rule)",
     "GDP 대비 국가채무 비율의\n상한 또는 감축 경로 설정\n예: EU 부채 60% 이내",
     "#f5f9fd", "#2f6fb0"),
    ("재정수지준칙\n(budget balance rule)",
     "재정수지를 균형 또는\n일정 수준으로 유지\n예: EU 적자 3%,\n독일 구조적 적자 0.35%",
     "#f4fbf6", "#2f8f4e"),
    ("지출준칙\n(expenditure rule)",
     "총지출 한도, 지출\n증가율 상한 설정\n예: 스웨덴 3년 단위\n지출상한",
     "#faf8fc", "#7a5fa8"),
    ("수입준칙\n(revenue rule)",
     "세입 감소 입법 시 대응\n재원 확보 의무화\n예: 미국 페이고(PAYGO)",
     "#fdf9f4", "#c77b2f"),
]
for i, (t1, t2, fc, ec) in enumerate(cols):
    x = 0.4 + i * 3.45
    box(ax, x, 6.7, 3.05, 1.4, t1, fc=fc, ec=ec, weight="bold")
    box(ax, x, 3.7, 3.05, 2.5, t2, fc="white", ec=ec)
    arrow(ax, 7.0, 9.4, x + 1.525, 8.25, color=ec)
    arrow(ax, x + 1.525, 6.6, x + 1.525, 6.35, color=ec)

box(ax, 0.4, 1.5, 3.05, 1.5, "저량(stock) 규율\n쌓인 빚의 크기를 묶는다",
    fc="#f5f9fd", ec="#2f6fb0")
box(ax, 3.85, 1.5, 10.0, 1.5, "유량(flow) 규율\n해마다의 수지 · 지출 · 세입의 흐름을 묶는다",
    fc="white", ec="#555555")
ax.text(7.0, 0.6, "네 유형은 서로 배타적이지 않으며, 실제 국가들은 대개 두 개 이상을 결합해 운용한다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("재정준칙의 네 유형: 무엇을 묶을 것인가", fontsize=14, pad=12)
fig.savefig(FIG / "fig09_rules.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 9-2
# 재정정책 x 통화정책 정책조합 4분면
fig, ax = plt.subplots(figsize=(11.8, 8.2))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis("off")

CX, CY = 7.0, 5.4
arrow(ax, 1.0, CY, 13.0, CY, color="#333", style="-|>", lw=1.8)
arrow(ax, 13.0, CY, 1.0, CY, color="#333", style="-|>", lw=1.8)
arrow(ax, CX, 0.8, CX, 10.0, color="#333", style="-|>", lw=1.8)
arrow(ax, CX, 10.0, CX, 0.8, color="#333", style="-|>", lw=1.8)
ax.text(13.1, CY - 0.05, "재정 확장", ha="left", va="center", fontsize=11, fontweight="bold")
ax.text(0.9, CY - 0.05, "재정 긴축", ha="right", va="center", fontsize=11, fontweight="bold")
ax.text(CX, 10.25, "통화 완화", ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.text(CX, 0.5, "통화 긴축", ha="center", va="top", fontsize=11, fontweight="bold")

box(ax, 7.8, 6.3, 4.7, 2.6,
    "확장 재정 + 완화 통화\n총수요 부양 극대화\n예: 2020년 코로나19 국면\n(추경 4차례, 기준금리 0.50%)",
    fc="#f4fbf6", ec="#2f8f4e", weight="bold")
box(ax, 1.5, 6.3, 4.7, 2.6,
    "긴축 재정 + 완화 통화\n재정건전화의 경기 부담을\n통화 완화가 완충\n예: 2010년대 유로존",
    fc="#f5f9fd", ec="#2f6fb0")
box(ax, 1.5, 1.9, 4.7, 2.6,
    "긴축 재정 + 긴축 통화\n과열 · 인플레이션 억제\n예: 1997년 외환위기 직후,\n2022-2023년 물가 대응",
    fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 7.8, 1.9, 4.7, 2.6,
    "확장 재정 + 긴축 통화\n정책 갈등 국면\n금리 상승 압력, 구축효과 우려\n정부-중앙은행 조율이 쟁점",
    fc="#fff5f5", ec="#c0392b")

ax.set_title("재정정책과 통화정책의 정책조합: 네 국면", fontsize=14, pad=12)
fig.savefig(FIG / "fig09_polmix.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 9-3
# 신용창조의 순환: 본원통화 100만 원 -> 예금통화 1,000만 원
fig, ax = plt.subplots(figsize=(12.5, 7.2))
ax.set_xlim(0, 14.6)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 0.3, 7.2, 2.7, 1.8, "한국은행\n본원통화\n100만 원 공급", fc="#f7f7fc", ec="#5b6ee1", weight="bold")

banks = [
    ("A은행\n예금 100만 원", "지급준비금\n10만 원 (10%)", 3.9),
    ("B은행\n예금 90만 원", "지급준비금\n9만 원 (10%)", 7.6),
    ("C은행\n예금 81만 원", "지급준비금\n8.1만 원 (10%)", 11.3),
]
for t_bank, t_res, x in banks:
    box(ax, x, 7.2, 2.9, 1.8, t_bank, fc="#f5f9fd", ec="#2f6fb0", weight="bold")
    box(ax, x, 4.6, 2.9, 1.4, t_res, fc="white", ec="#c77b2f")
    arrow(ax, x + 1.45, 7.1, x + 1.45, 6.15, color="#c77b2f", ls="--", lw=1.3)

arrow(ax, 3.1, 8.1, 3.8, 8.1)
ax.text(3.45, 8.35, "예금", ha="center", fontsize=9.5, color="#333")
arrow(ax, 6.9, 8.1, 7.5, 8.1)
ax.text(7.2, 9.35, "대출 90만 원이 예금으로", ha="center", fontsize=9.5, color="#333")
arrow(ax, 10.6, 8.1, 11.2, 8.1)
ax.text(10.9, 9.35, "대출 81만 원이 예금으로", ha="center", fontsize=9.5, color="#333")
ax.text(14.35, 8.1, "…", ha="center", va="center", fontsize=16, color="#333")

ax.text(7.3, 3.6, "대출이 다시 예금이 되는 순환이 반복되며, 새로 생기는 예금은 90만 원, 81만 원, 72.9만 원…으로 줄어든다.",
        ha="center", fontsize=10, color="#333")

box(ax, 2.9, 1.0, 8.8, 1.6,
    "순환의 종착점: 예금통화 총액 1,000만 원\n(본원통화 100만 원을 지급준비율 10%로 나눈 값) · 통화승수 10배",
    fc="#f7f7fc", ec="#5b6ee1", weight="bold")
arrow(ax, 7.3, 3.35, 7.3, 2.8, color="#5b6ee1")

ax.set_title("신용창조의 순환: 100만 원이 1,000만 원이 되기까지 (지급준비율 10% 가정)", fontsize=14, pad=12)
fig.savefig(FIG / "fig09_credit.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig09_*.png"))])
