# 10주차(1차시·2차시) 재정과정론 개념도 생성
# 실행: cd $HOME/default-uv-env && PYTHONIOENCODING=utf-8 VIRTUAL_ENV= uv run python "<이 파일 경로>"
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
import koreanize_matplotlib  # noqa: E402,F401
import figfit  # noqa: E402,F401  (상자 글씨 자동 크기)

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

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


# ---------------------------------------------------------------- 그림 10-1
# 중첩된 예산주기: 한 해에 세 개의 예산이 돈다
fig, ax = plt.subplots(figsize=(13, 6.6))
ax.set_xlim(0, 15.4)
ax.set_ylim(0, 10.8)
ax.axis("off")

years = [2024, 2025, 2026, 2027, 2028]
col_x = {y: 1.7 + i * 2.7 for i, y in enumerate(years)}
COL_W = 2.5

# 2026년 강조 밴드 (맨 먼저 그려 배경으로)
bx = col_x[2026]
ax.add_patch(Rectangle((bx - 0.12, 1.75), COL_W + 0.24, 8.6,
                       fc="#fff8e1", ec="#c77b2f", lw=1.2, ls="--", zorder=0))
ax.text(bx + COL_W / 2, 9.85, "2026년: 세 개의 예산이\n동시에 진행", ha="center",
        va="center", fontsize=10.5, color="#b06a20", fontweight="bold")

# 연도 라벨
for y in years:
    ax.text(col_x[y] + COL_W / 2, 8.75, f"{y}년", ha="center", fontsize=12,
            fontweight="bold", color="#333")

stages = [
    ("편성·심의", "#f5f9fd", "#2f6fb0"),
    ("집행", "#f4fbf6", "#2f8f4e"),
    ("결산·회계검사", "#fdf9f4", "#c77b2f"),
]
rows = [("2025년도 예산", 2024, 6.8), ("2026년도 예산", 2025, 4.6), ("2027년도 예산", 2026, 2.4)]
for label, start_year, ry in rows:
    ax.text(0.85, ry + 0.75, label, ha="center", va="center", fontsize=11,
            fontweight="bold", color="#333")
    for k, (st, fc, ec) in enumerate(stages):
        x0 = col_x[start_year + k]
        box(ax, x0, ry, COL_W, 1.5, st, fc=fc, ec=ec)
        if k < 2:
            arrow(ax, x0 + COL_W + 0.02, ry + 0.75, col_x[start_year + k + 1] - 0.02, ry + 0.75,
                  color="#888", lw=1.2)

ax.text(7.7, 0.85, "편성·심의는 전년도(t-1), 집행은 당해 연도(t), 결산·회계검사는 다음 연도(t+1)에 이루어진다.",
        ha="center", fontsize=10.5, color="#333")
ax.set_title("중첩된 예산주기: 하나의 예산은 3년을 살고, 한 해에는 세 예산이 겹친다", fontsize=14, pad=12)
fig.savefig(FIG / "fig10_cycle.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 10-2
# 예산편성의 법정 시간표: 기획예산처의 1년
fig, ax = plt.subplots(figsize=(12.5, 8.6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 13.2)
ax.axis("off")

box(ax, 1.0, 11.7, 4.6, 1.0, "기획예산처", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 8.4, 11.7, 4.6, 1.0, "각 중앙관서의 장", fc="#f4fbf6", ec="#2f8f4e", weight="bold")

L, R = 1.0, 8.4
W, H = 4.6, 1.35
steps = [
    ("L", 9.75, "① 국가재정운용계획 수립지침 통보\n(전년도 12월 31일까지 · 시행령 제2조)"),
    ("R", 8.05, "② 중기사업계획서 제출\n(1월 31일까지 · 법 제28조)"),
    ("L", 6.35, "③ 예산안편성지침 통보 · 지출한도 포함 가능\n(3월 31일까지 · 법 제29조)"),
    ("R", 4.65, "④ 예산요구서 제출\n(5월 31일까지 · 법 제31조)"),
    ("L", 2.95, "⑤ 예산사정과 예산안 편성\n(6-8월 · 법 제32조)"),
]
for side, y, text in steps:
    x = L if side == "L" else R
    ec = "#2f6fb0" if side == "L" else "#2f8f4e"
    fc = "#f5f9fd" if side == "L" else "#f4fbf6"
    box(ax, x, y, W, H, text, fc=fc, ec=ec)

# 순서 연결 화살표 (지그재그)
arrow(ax, L + W, 10.15, R, 8.95, color="#2f6fb0")
arrow(ax, R, 8.45, L + W, 7.35, color="#2f8f4e")
arrow(ax, L + W, 6.75, R, 5.55, color="#2f6fb0")
arrow(ax, R, 5.05, L + W, 3.95, color="#2f8f4e")
ax.text(3.3, 5.8, "편성지침은 국회 예산결산특별위원회에 보고(법 제30조)",
        ha="center", fontsize=9.2, color="#555")

box(ax, 2.6, 0.6, 8.8, 1.6,
    "⑥ 국무회의 심의 · 대통령 승인(법 제32조)\n→ 정부가 회계연도 개시 120일 전까지 국회 제출(법 제33조)",
    fc="#f7f7fc", ec="#5b6ee1", weight="bold")
arrow(ax, 3.3, 2.9, 4.6, 2.3, color="#2f6fb0")

ax.set_title("예산편성의 법정 시간표: 지침이 내려가고 요구가 올라온다", fontsize=14, pad=12)
fig.savefig(FIG / "fig10_formation.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 10-3
# 예산심의의 절차: 제출에서 확정까지
fig, ax = plt.subplots(figsize=(12.5, 8.8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 13.6)
ax.axis("off")

M, MW = 0.8, 7.4
flow = [
    (11.9, 1.3, "정부 예산안 국회 제출\n(회계연도 개시 120일 전 · 9월 초)", "#f5f9fd", "#2f6fb0"),
    (10.1, 1.3, "본회의: 정부의 시정연설 (국회법 제84조)", "#f5f9fd", "#2f6fb0"),
    (8.1, 1.5, "소관 상임위원회 예비심사\n제안설명 → 검토보고 → 대체토론 → 소위 심사·계수조정", "#f5f9fd", "#2f6fb0"),
    (6.1, 1.5, "예산결산특별위원회 종합심사\n종합정책질의 → 부별 심사 → 예산안등조정소위 계수조정", "#f5f9fd", "#2f6fb0"),
    (4.1, 1.5, "본회의 심의·의결\n(회계연도 개시 30일 전 · 12월 2일까지, 헌법 제54조)", "#f7f7fc", "#5b6ee1"),
    (2.3, 1.2, "예산 확정 → 집행 단계로", "#f4fbf6", "#2f8f4e"),
]
for y, h, text, fc, ec in flow:
    box(ax, M, y, MW, h, text, fc=fc, ec=ec)
ys = [(11.9, 11.4), (10.1, 9.6), (8.1, 7.6), (6.1, 5.6), (4.1, 3.5)]
for y_top, y_next in ys:
    arrow(ax, M + MW / 2, y_top - 0.02, M + MW / 2, y_next + 0.12 - 0.5 + 0.4, color="#555")

box(ax, 9.0, 10.3, 4.6, 1.5, "헌법 제57조\n정부 동의 없이 증액이나\n새 비목 설치 불가", fc="#faf8fc", ec="#7a5fa8")
arrow(ax, 10.4, 10.25, 8.3, 8.9, color="#7a5fa8", ls="--", lw=1.3)

box(ax, 9.0, 7.0, 4.6, 1.8, "국회법 제85조의3 (자동부의)\n11월 30일까지 심사 미완료 시\n12월 1일 본회의에 자동 부의", fc="#fdf9f4", ec="#c77b2f")
arrow(ax, 10.4, 6.95, 8.3, 5.4, color="#c77b2f", ls="--", lw=1.3)

ax.text(7.0, 1.5, "예산은 법률과 달리 공포 절차 없이 본회의 의결로 성립한다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("예산심의의 절차: 두 겹의 위원회 심사를 지나는 깔때기", fontsize=14, pad=12)
fig.savefig(FIG / "fig10_deliberation.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 10-4
# 결산의 법정 일정: 2월에서 9월까지
fig, ax = plt.subplots(figsize=(13, 5.6))
ax.set_xlim(0, 15.2)
ax.set_ylim(0, 8.0)
ax.axis("off")

relay = [
    (0.4, "각 중앙관서의 장\n중앙관서결산보고서 작성\n2월 말일까지 제출 (제58조)", "#f5f9fd", "#2f6fb0"),
    (4.2, "재정경제부장관\n국가결산보고서 작성 · 대통령 승인\n4월 10일까지 기획예산처장관과\n감사원에 제출 (제59조)", "#f4fbf6", "#2f8f4e"),
    (8.0, "감사원 결산검사\n5월 20일까지\n재정경제부장관에게 송부 (제60조)", "#fdf9f4", "#c77b2f"),
    (11.8, "정부\n5월 31일까지\n국회에 제출 (제61조)", "#faf8fc", "#7a5fa8"),
]
for x, text, fc, ec in relay:
    box(ax, x, 4.6, 3.0, 2.6, text, fc=fc, ec=ec)
for x1, x2 in [(3.4, 4.2), (7.2, 8.0), (11.0, 11.8)]:
    arrow(ax, x1 + 0.02, 5.9, x2 - 0.02, 5.9, color="#555")

box(ax, 2.6, 1.3, 10.0, 1.6,
    "국회 결산심사: 상임위 예비심사 → 예결위 종합심사 → 본회의 의결\n(정기회 개회 전까지 · 국회법 제128조의2)",
    fc="#f7f7fc", ec="#5b6ee1", weight="bold")
arrow(ax, 13.3, 4.55, 10.5, 2.95, color="#7a5fa8")

ax.text(7.6, 0.55, "모든 기한은 회계연도가 끝난 다음 연도(t+1년)의 날짜다. 헌법 제99조에 따라 감사원은 검사 결과를 대통령과 차년도 국회에 보고한다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("결산의 법정 일정: 네 기관을 거치는 릴레이", fontsize=14, pad=12)
fig.savefig(FIG / "fig10_settlement.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig10_*.png"))])
