# 4주차(1차시·2차시) 개념도 생성
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


# ---------------------------------------------------------------- 그림 4-1
# 내부거래와 이중계산: 예산총계에서 예산순계로
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 0.8, 6.9, 4.8, 2.0, "일반회계\n세출 1,000억 원", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 8.4, 6.9, 4.8, 2.0, "특별회계\n세출 500억 원\n(자체수입 300 + 전입금 200)",
    fc="#f4fbf6", ec="#2f8f4e")
arrow(ax, 5.7, 7.9, 8.3, 7.9, color="#c77b2f", lw=2.0)
ax.text(7.0, 8.25, "전출금 200억 원 (내부거래)", ha="center", fontsize=10,
        color="#c77b2f", fontweight="bold")
ax.text(7.0, 7.45, "한 번의 지출이\n두 장부에 기록된다", ha="center", va="top",
        fontsize=9, color="#555")

box(ax, 1.2, 3.3, 5.2, 1.8, "예산총계 1,500억 원\n(1,000 + 500, 중복 계상 포함)",
    fc="white", ec="#2f6fb0")
box(ax, 7.8, 3.3, 5.2, 1.8, "예산순계 1,300억 원\n(총계 1,500 - 내부거래 200)",
    fc="white", ec="#c77b2f")
arrow(ax, 3.4, 6.8, 3.6, 5.2, ls="--", lw=1.3, color="#2f6fb0")
arrow(ax, 10.6, 6.8, 5.8, 5.25, ls="--", lw=1.3, color="#2f8f4e")
arrow(ax, 6.5, 4.2, 7.7, 4.2, color="#555")
ax.text(7.1, 4.55, "내부거래 차감", ha="center", fontsize=9.5, color="#555")

ax.text(7.0, 2.2, "총계와 순계의 차이 = 내부거래의 규모.  개별 회계·기금의 활동은 총계로, 정부 전체의 규모는 순계로 읽는다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("내부거래와 이중계산: 예산총계에서 예산순계로", fontsize=14, pad=12)
fig.savefig(FIG / "fig04_gross_net.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 4-2
# 통합재정수지에서 관리재정수지로 (2025회계연도 결산)
fig, ax = plt.subplots(figsize=(12, 6.4))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 0.6, 7.0, 3.4, 1.9, "세입\n(비상환성 수입만)", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 4.9, 7.0, 3.7, 1.9, "세출및순융자\n(순융자 = 융자지출\n- 융자회수)", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 9.6, 7.0, 3.8, 1.9, "통합재정수지\n2025년 결산\n-46.7조 원", fc="#f4fbf6", ec="#2f8f4e", weight="bold")
ax.text(4.45, 7.95, "-", ha="center", va="center", fontsize=22, color="#333")
ax.text(9.1, 7.95, "=", ha="center", va="center", fontsize=22, color="#333")

arrow(ax, 11.5, 6.9, 11.5, 4.7, color="#7a5fa8", lw=2.0)
box(ax, 4.6, 4.4, 4.8, 1.7, "사회보장성기금수지 차감\n+57.5조 원 (2025년 결산)\n국민연금·사학연금·고용보험·산재보험",
    fc="#faf8fc", ec="#7a5fa8")
arrow(ax, 9.5, 5.25, 11.35, 5.7, ls="--", lw=1.3, color="#7a5fa8")

box(ax, 9.6, 2.6, 3.8, 1.9, "관리재정수지\n2025년 결산 -104.2조 원\n(GDP 대비 -3.9%)", fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 0.6, 2.6, 3.6, 1.9, "보전재원\n(국채 순발행·순차입)\n통합재정수지와\n크기 같고 부호 반대",
    fc="white", ec="#999999")

ax.text(7.0, 1.6, "두 수지의 차이가 곧 사회보장성기금의 흑자다.  국내 재정운용 목표는 관리재정수지, 국제비교는 통합재정수지를 쓴다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("통합재정수지에서 관리재정수지로 (2025회계연도 결산)", fontsize=14, pad=12)
fig.savefig(FIG / "fig04_balances.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 4-3
# 총계에서 총지출까지: 재정 규모 지표의 관계 (세로 폭포)
fig, ax = plt.subplots(figsize=(11, 7.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 11)
ax.axis("off")

box(ax, 2.6, 9.0, 6.0, 1.6, "예산·기금 총계\n(모든 회계·기금의 지출 단순 합산)",
    fc="#f5f9fd", ec="#2f6fb0")
arrow(ax, 5.6, 8.9, 5.6, 7.8, color="#555", lw=1.8)
ax.text(5.95, 8.35, "① 내부거래 차감 (전출입금·예탁예수금 등)", ha="left",
        va="center", fontsize=10, color="#333")

box(ax, 2.6, 6.2, 6.0, 1.6, "예산순계", fc="#f5f9fd", ec="#2f6fb0")
arrow(ax, 5.6, 6.1, 5.6, 5.0, color="#555", lw=1.8)
ax.text(5.95, 5.55, "② 보전거래 차감 (국채 발행·상환, 차입·상환)", ha="left",
        va="center", fontsize=10, color="#333")

box(ax, 2.6, 3.4, 6.0, 1.6, "총지출: 2026년 본예산 727.9조 원\n(융자지출은 총액 포함, 국민 체감 지출)",
    fc="#fdf9f4", ec="#c77b2f", weight="bold")
arrow(ax, 5.6, 3.3, 5.6, 2.2, color="#555", lw=1.8)
ax.text(5.95, 2.75, "③ 융자를 순액(순융자)으로, 기업특별회계 순액 처리", ha="left",
        va="center", fontsize=10, color="#333")

box(ax, 2.6, 0.5, 6.0, 1.6, "통합재정 지출 규모\n(세출 + 순융자)", fc="#f4fbf6", ec="#2f8f4e")

ax.set_title("총계에서 총지출까지: 재정 규모 지표의 관계", fontsize=14, pad=12)
fig.savefig(FIG / "fig04_expenditure.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 4-4
# 공공부문의 범위와 부채 지표: D1 · D2 · D3 (계단식)
fig, ax = plt.subplots(figsize=(12.5, 6.8))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10.5)
ax.axis("off")

rows = [
    (8.2, 2, "국가채무(D1)\n2025년 결산 1,304.5조 원\n(GDP 대비 49.0%)", "#f5f9fd", "#2f6fb0"),
    (5.6, 3, "일반정부 부채(D2)\n2024년 1,270.8조 원\n(GDP 대비 49.7%)", "#faf8fc", "#7a5fa8"),
    (3.0, 4, "공공부문 부채(D3)\n2024년 1,738.6조 원\n(GDP 대비 68.0%)", "#fdf9f4", "#c77b2f"),
]
comps = ["중앙정부\n(회계·기금)", "지방정부", "비영리\n공공기관", "비금융\n공기업"]
xs = [0.4, 3.1, 5.8, 8.5]

for y, n, label, fc, ec in rows:
    for i in range(n):
        box(ax, xs[i], y, 2.3, 1.6, comps[i], fc="white", ec="#777777", fontsize=10)
    if n >= 3:
        ax.text(5.6, y + 0.8, "+", ha="center", va="center", fontsize=15, color="#555")
    if n == 4:
        ax.text(8.3, y + 0.8, "+", ha="center", va="center", fontsize=15, color="#555")
    box(ax, 11.6, y - 0.05, 4.0, 1.7, label, fc=fc, ec=ec, weight="bold")
    arrow(ax, xs[n - 1] + 2.35, y + 0.8, 11.5, y + 0.8, color="#999999", lw=1.2, ls="--")

ax.text(2.9, 7.75, "범위: 중앙 + 지방 (현금주의·확정채무)", ha="center", fontsize=9, color="#555")
ax.text(4.25, 5.15, "범위: 일반정부 (발생주의)", ha="center", fontsize=9, color="#555")
ax.text(5.6, 2.55, "범위: 공공부문 (발생주의)", ha="center", fontsize=9, color="#555")

ax.text(8.0, 1.5, "D1은 국가재정법에 따른 법정 지표, D2·D3는 국제기준 통계로 D1보다 1년 늦게 발표된다.",
        ha="center", fontsize=10, color="#333")
ax.text(8.0, 0.9, "금융공기업(한국은행·산업은행 등)은 D3에서도 제외되며, 재무제표상 국가부채(2025회계연도 2,772조 원)는 별개의 개념이다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("공공부문의 범위와 부채 지표: D1 · D2 · D3", fontsize=14, pad=12)
fig.savefig(FIG / "fig04_sectors.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig04_*.png"))])
