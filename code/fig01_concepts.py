# 1주차(1차시·2차시) 개념도 생성
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


# ---------------------------------------------------------------- 그림 1-1
# 예산의 본질: 정책 결정 + 금액 결정, 사실판단·가치판단
fig, ax = plt.subplots(figsize=(12, 6.2))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 1.0, 7.3, 4.8, 1.8, "정책에 대한 결정\n무엇을 할 것인가", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 8.2, 7.3, 4.8, 1.8, "금액에 대한 결정\n얼마를 들일 것인가", fc="#f4fbf6", ec="#2f8f4e", weight="bold")
arrow(ax, 5.95, 8.2, 8.05, 8.2, style="<|-|>", color="#555")
ax.text(7.0, 8.55, "동시에 이루어지는\n한 쌍의 결정", ha="center", va="bottom", fontsize=9.5, color="#333")

box(ax, 1.0, 4.7, 4.8, 1.5, "노인돌봄서비스 확대\n(정책 · 사업)", fc="white", ec="#2f6fb0")
box(ax, 8.2, 4.7, 4.8, 1.5, "1,500억 원\n(금액)", fc="white", ec="#2f8f4e")
arrow(ax, 3.4, 7.2, 3.4, 6.3, color="#2f6fb0", ls="--", lw=1.3)
arrow(ax, 10.6, 7.2, 10.6, 6.3, color="#2f8f4e", ls="--", lw=1.3)

box(ax, 0.5, 1.2, 5.8, 2.3,
    "사실판단\n이 지출은 어떤 효과를 낳는가\n(인과에 대한 판단)", fc="#faf8fc", ec="#7a5fa8")
box(ax, 7.7, 1.2, 5.8, 2.3,
    "가치판단\n그 효과는 바람직한가\n다른 지출보다 중요한가", fc="#fdf9f4", ec="#c77b2f")
arrow(ax, 3.4, 3.6, 3.4, 4.6, color="#7a5fa8", lw=1.3)
arrow(ax, 10.6, 3.6, 10.6, 4.6, color="#c77b2f", lw=1.3)

ax.text(7.0, 0.4, "예산서의 숫자 한 줄에는 정책의 선택과 두 종류의 판단이 함께 담겨 있다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("예산의 본질: 숫자 뒤에 있는 정책과 판단", fontsize=14, pad=12)
fig.savefig(FIG / "fig01_budget.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 1-2
# 재정당국의 연혁 연표: 분리와 통합의 반복 (1948-2026)
fig, ax = plt.subplots(figsize=(13.5, 6.8))
ax.set_xlim(0, 16.6)
ax.set_ylim(0, 10.6)
ax.axis("off")

TOP_Y, TOP_H = 5.7, 2.4      # 기획·예산 계열
BOT_Y, BOT_H = 2.0, 2.4      # 세제·국고 계열
TALL_Y, TALL_H = 2.0, 6.1    # 통합기

# 분리기 1948/1961-1994
box(ax, 0.4, TOP_Y, 2.6, TOP_H, "경제기획원\n(1961-1994)\n기획 · 예산", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 0.4, BOT_Y, 2.6, BOT_H, "재무부\n(1948-1994)\n세제 · 국고 · 금융", fc="#f2fafa", ec="#2b7a78")
# 통합기 1994-1998
box(ax, 3.6, TALL_Y, 2.2, TALL_H, "재정경제원\n(1994-1998)", fc="#faf8fc", ec="#7a5fa8")
# 분리기 1998-2008
box(ax, 6.4, TOP_Y, 2.9, TOP_H, "기획예산위원회 · 예산청\n(1998)\n기획예산처(1999-2008)", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 6.4, BOT_Y, 2.9, BOT_H, "재정경제부\n(1998-2008)\n세제 · 국고 · 경제정책", fc="#f2fafa", ec="#2b7a78")
# 통합기 2008-2026
box(ax, 9.9, TALL_Y, 2.2, TALL_H, "기획재정부\n(2008-2026)", fc="#faf8fc", ec="#7a5fa8")
# 분리기 2026-
box(ax, 12.7, TOP_Y, 3.4, TOP_H, "기획예산처 (2026- )\n국무총리 소속\n예산 · 기금 · 재정정책\n중장기 전략", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 12.7, BOT_Y, 3.4, BOT_H, "재정경제부 (2026- )\n경제부총리 겸임\n경제정책 · 세제 · 국고", fc="#f2fafa", ec="#2b7a78")

# 연결 화살표
arrow(ax, 3.0, TOP_Y + 1.2, 3.6, 6.2)
arrow(ax, 3.0, BOT_Y + 1.2, 3.6, 3.9)
arrow(ax, 5.8, 6.2, 6.4, TOP_Y + 1.2)
arrow(ax, 5.8, 3.9, 6.4, BOT_Y + 1.2)
arrow(ax, 9.3, TOP_Y + 1.2, 9.9, 6.2)
arrow(ax, 9.3, BOT_Y + 1.2, 9.9, 3.9)
arrow(ax, 12.1, 6.2, 12.7, TOP_Y + 1.2)
arrow(ax, 12.1, 3.9, 12.7, BOT_Y + 1.2)

# 시대 구분 라벨
for x, t in [(1.7, "분리"), (4.7, "통합"), (7.85, "분리"), (11.0, "통합"), (14.4, "분리")]:
    ax.text(x, 9.0, t, ha="center", fontsize=11.5, fontweight="bold", color="#444")
# 전환 연도 라벨
for x, t in [(1.7, "1948 · 1961 설치"), (4.7, "1994년 12월 통합"), (7.85, "1998-1999년 분리"),
             (11.0, "2008년 2월 통합"), (14.4, "2026년 1월 2일 재분리")]:
    ax.text(x, 1.35, t, ha="center", fontsize=9.5, color="#555")

# 계열 라벨
ax.text(0.25, TOP_Y + TOP_H + 0.25, "기획 · 예산 계열", ha="left", fontsize=10, color="#2f6fb0")
ax.text(0.25, BOT_Y + BOT_H + 0.25, "세제 · 국고 계열", ha="left", fontsize=10, color="#2b7a78")

ax.text(8.3, 0.4, "2026년 체제는 1998-2008년의 분리형으로 돌아갔지만, 기획예산처가 중장기 전략 기능까지 맡는 점이 다르다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("재정당국의 연혁: 분리와 통합의 반복 (1948-2026)", fontsize=14, pad=12)
fig.savefig(FIG / "fig01_history.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 1-3
# 두 수준의 배분: 거시적 배분과 미시적 배분
fig, ax = plt.subplots(figsize=(12, 6.8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis("off")

box(ax, 5.0, 9.2, 4.0, 1.4, "사회의 총자원", fc="#f7f7fc", ec="#5b6ee1", weight="bold")
box(ax, 1.2, 6.3, 4.8, 1.8, "민간부문\n시장의 선택 (가격기구)", fc="white", ec="#888")
box(ax, 8.0, 6.3, 4.8, 1.8, "공공부문\n정부의 선택 (예산)", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
arrow(ax, 6.2, 9.1, 3.6, 8.2)
arrow(ax, 7.8, 9.1, 10.4, 8.2)

ax.text(3.55, 5.35, "거시적 배분: 민간과 공공 사이의 배분\n→ 재정의 총규모 (2026년 본예산 총지출 727.9조 원)",
        ha="center", fontsize=10.5, color="#2f6fb0")

sectors = ["복지 · 고용", "국방 · 치안", "교육", "연구개발", "도로 · 철도"]
for i, s in enumerate(sectors):
    x = 0.7 + i * 2.6
    box(ax, x, 2.7, 2.3, 1.5, s, fc="white", ec="#2f8f4e")
    arrow(ax, 10.4, 6.2, x + 1.15, 4.3, color="#2f8f4e", lw=1.2)

ax.text(7.0, 2.0, "미시적 배분: 주어진 총액 안에서 분야 · 부문 · 프로그램 · 단위사업 · 세부사업으로",
        ha="center", fontsize=10.5, color="#2f8f4e")
ax.text(7.0, 0.7, "거시적 배분이 파이의 크기를 정하고, 미시적 배분이 그 파이를 나눈다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("두 수준의 배분: 거시적 배분과 미시적 배분", fontsize=14, pad=12)
fig.savefig(FIG / "fig01_allocation.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 1-4
# 경제원리와 정치원리: 중간영역(twilight zone)
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9.5)
ax.axis("off")

box(ax, 0.5, 4.4, 4.2, 3.4,
    "경제원리\n어떻게 이득을 극대화할 것인가\n분석 · 사회후생 극대화\n비용편익분석 → 총체주의", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 9.3, 4.4, 4.2, 3.4,
    "정치원리\n누가 얼마만큼 가져갈 것인가\n협상 · 타협 · 몫의 정당성\n모색에 의한 결정 → 점증주의", fc="#fdf9f4", ec="#c77b2f")
box(ax, 5.1, 5.1, 3.8, 2.0, "실제의 예산결정\n정치와 효율의 중간영역\n(Wildavsky, 1961)", fc="#faf8fc", ec="#7a5fa8", weight="bold")
arrow(ax, 4.8, 6.1, 5.1, 6.1, color="#2f6fb0")
arrow(ax, 9.2, 6.1, 8.9, 6.1, color="#c77b2f")

box(ax, 1.6, 1.3, 10.8, 1.9,
    "그리즐(1986)의 상황론적 조화: 재화의 성격, 신규 · 계속 여부,\n분석의 질과 분석가의 영향력, 논쟁의 단계에 따라 두 원리의 힘이 달라진다",
    fc="#f7f7fc", ec="#5b6ee1")
arrow(ax, 7.0, 5.0, 7.0, 3.3, color="#7a5fa8", lw=1.3)

ax.set_title("경제원리와 정치원리: 중간영역에서 만나다", fontsize=14, pad=12)
fig.savefig(FIG / "fig01_twilight.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig01_*.png"))])
