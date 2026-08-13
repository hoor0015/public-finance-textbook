# 6주차(1차시·2차시) 예산의 종류·재정제도 개념도 생성
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


def box(ax, x, y, w, h, text, fc="#f5f9fd", ec="#2f6fb0", weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=11, fontweight=weight)


def arrow(ax, x1, y1, x2, y2, color="#555", style="-|>", lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=16, color=color, lw=lw, linestyle=ls))


# ---------------------------------------------------------------- 그림 6-1
# 성립 시기에 따른 예산의 종류: 시간축 위의 수정예산·본예산·추경, 아래의 불성립 대응
fig, ax = plt.subplots(figsize=(12.5, 7.6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11.2)
ax.axis("off")

# 가운데 시간축 단계
steps = [
    ("정부의\n예산안 제출\n(개시 120일 전)", 0.5),
    ("국회 심의·의결\n= 예산 성립\n(개시 30일 전)", 4.0),
    ("회계연도 개시\n(1월 1일)", 7.5),
    ("집행", 11.0),
]
for t, x in steps:
    box(ax, x, 5.2, 2.7, 1.9, t, fc="#f7f7fc", ec="#5b6ee1", weight="bold")
for x in (3.3, 6.8, 10.3):
    arrow(ax, x, 6.15, x + 0.6, 6.15)

# 위: 성립 시기에 따른 세 종류
box(ax, 1.3, 9.0, 3.6, 1.6, "수정예산\n제출 후·의결 전에\n예산안을 고쳐 다시 제출", fc="white", ec="#2f6fb0")
box(ax, 5.3, 9.0, 3.4, 1.6, "본예산\n회계연도 개시 전\n정상적으로 성립", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 9.3, 9.0, 4.1, 1.6, "추가경정예산\n성립 후의 사유로\n이미 성립된 예산을 변경", fc="white", ec="#2f6fb0")
arrow(ax, 3.1, 8.9, 3.1, 7.3, color="#2f6fb0", ls="--", lw=1.3)
arrow(ax, 7.0, 8.9, 5.9, 7.3, color="#2f6fb0", ls="--", lw=1.3)
arrow(ax, 11.3, 8.9, 11.3, 7.3, color="#2f6fb0", ls="--", lw=1.3)

# 아래: 불성립 시 대응
box(ax, 3.4, 2.9, 7.2, 1.3, "예산 불성립\n회계연도 개시까지 의결되지 못한 경우", fc="#fdf9f4", ec="#c77b2f", weight="bold")
arrow(ax, 7.0, 5.1, 7.0, 4.3, color="#c77b2f", ls="--", lw=1.3)
box(ax, 0.7, 0.6, 4.0, 1.7, "준예산 (한국)\n국회 의결 없이\n전년도 예산에 준해 집행", fc="white", ec="#c77b2f")
box(ax, 5.1, 0.6, 3.8, 1.7, "잠정예산\n일정 기간의 예산을\n의회가 사전 의결", fc="white", ec="#c77b2f")
box(ax, 9.3, 0.6, 4.0, 1.7, "가예산\n1개월 이내의 예산을\n의회가 사전 의결", fc="white", ec="#c77b2f")
for x in (2.7, 7.0, 11.3):
    arrow(ax, 7.0 if x == 7.0 else x, 2.8, x, 2.4, color="#c77b2f")
arrow(ax, 5.0, 2.9, 2.7, 2.4, color="#c77b2f")
arrow(ax, 9.0, 2.9, 11.3, 2.4, color="#c77b2f")

ax.set_title("성립 시기에 따른 예산의 종류와 불성립 대응", fontsize=14, pad=12)
fig.savefig(FIG / "fig06_types.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 6-2
# 준예산·잠정예산·가예산 비교표
fig, ax = plt.subplots(figsize=(12.5, 8.0))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10.2)
ax.axis("off")

# 헤더
box(ax, 3.2, 8.6, 3.3, 1.2, "준예산", fc="#f4faf5", ec="#3a7d44", weight="bold")
box(ax, 6.9, 8.6, 3.3, 1.2, "잠정예산", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 10.6, 8.6, 3.1, 1.2, "가예산", fc="#fdf9f4", ec="#c77b2f", weight="bold")

rows = [
    ("의회 의결", 6.6,
     "불필요\n(헌법이 직접 수권,\n사전의결 원칙의 예외)",
     "필요\n(사전 의결)",
     "필요\n(사전 의결)"),
    ("기간 제한", 4.6,
     "없음\n(예산안 의결 시까지)",
     "있음\n(잠정 기간을 정함)",
     "1개월 이내"),
    ("지출 범위", 2.6,
     "기관 유지·운영,\n법률상 지출의무,\n계속사업에 한정",
     "잠정예산에 계상된\n범위 내 집행",
     "본예산에 준하되\n기간이 짧음"),
    ("채택·사용", 0.6,
     "한국(1960년 이후,\n중앙정부 발동 없음),\n독일",
     "영국·캐나다·일본,\n미국의 잠정지출결의",
     "한국 제1공화국\n(1949-1953·1955년 사용),\n프랑스에서 유래"),
]
for label, y, c1, c2, c3 in rows:
    box(ax, 0.3, y, 2.5, 1.7, label, fc="#f7f7fc", ec="#5b6ee1", weight="bold")
    box(ax, 3.2, y, 3.3, 1.7, c1, fc="white", ec="#3a7d44")
    box(ax, 6.9, y, 3.3, 1.7, c2, fc="white", ec="#2f6fb0")
    box(ax, 10.6, y, 3.1, 1.7, c3, fc="white", ec="#c77b2f")

ax.set_title("준예산·잠정예산·가예산의 비교", fontsize=14, pad=12)
fig.savefig(FIG / "fig06_provisional.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 6-3
# 조세지출의 구조: 직접지출과의 등가성 + 유형 분류
fig, ax = plt.subplots(figsize=(12.5, 8.2))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12.4)
ax.axis("off")

box(ax, 4.6, 11.0, 4.8, 1.2, "정부의 민간 지원", fc="#f7f7fc", ec="#5b6ee1", weight="bold")
arrow(ax, 6.0, 10.9, 3.5, 10.3)
arrow(ax, 8.0, 10.9, 10.5, 10.3)

# 왼쪽: 직접지출 경로
box(ax, 0.8, 8.9, 5.4, 1.2, "직접지출 (보조금)", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 0.8, 7.2, 5.4, 1.2, "세금을 걷어 예산에 편성", fc="white", ec="#2f6fb0")
box(ax, 0.8, 5.5, 5.4, 1.2, "매년 국회 심의·의결을 통과", fc="white", ec="#2f6fb0")
box(ax, 0.8, 3.8, 5.4, 1.2, "보조금으로 지급", fc="white", ec="#2f6fb0")
for y in (8.8, 7.1, 5.4):
    arrow(ax, 3.5, y, 3.5, y - 0.4, color="#2f6fb0")

# 오른쪽: 조세지출 경로
box(ax, 7.8, 8.9, 5.4, 1.2, "조세지출 (숨겨진 보조금)", fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 7.8, 7.2, 5.4, 1.2, "세법에 조세특례를 규정", fc="white", ec="#c77b2f")
box(ax, 7.8, 5.5, 5.4, 1.2, "세금을 깎아 주거나 걷지 않음", fc="white", ec="#c77b2f")
box(ax, 7.8, 3.8, 5.4, 1.2, "국회 의결 없이 지속\n(조세지출예산서로 보고만)", fc="white", ec="#c77b2f")
for y in (8.8, 7.1, 5.4):
    arrow(ax, 10.5, y, 10.5, y - 0.4, color="#c77b2f")

box(ax, 3.6, 2.3, 6.8, 1.2, "민간이 받는 경제적 효과는 동일", fc="#f4faf5", ec="#2f8f4e", weight="bold")
arrow(ax, 3.5, 3.7, 5.3, 3.6, color="#2f8f4e")
arrow(ax, 10.5, 3.7, 8.7, 3.6, color="#2f8f4e")

box(ax, 0.8, 0.2, 6.0, 1.3, "직접감면 (영구적 경감)\n비과세 · 소득공제 · 세액공제 · 세액감면 등", fc="white", ec="#7a5fa8")
box(ax, 7.2, 0.2, 6.0, 1.3, "간접감면 (과세의 연기)\n준비금 · 과세이연 · 이월과세 등", fc="white", ec="#7a5fa8")
ax.text(7.0, 1.72, "조세지출의 유형", ha="center", fontsize=10.5, color="#7a5fa8", fontweight="bold")

ax.set_title("조세지출의 구조: 같은 지원, 다른 통제", fontsize=14, pad=12)
fig.savefig(FIG / "fig06_taxexp.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 6-4
# 예산과 법률의 관계: 한국의 의결주의 vs 미국의 세출법률주의
fig, ax = plt.subplots(figsize=(12.5, 8.6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 13.0)
ax.axis("off")

box(ax, 0.8, 11.5, 5.8, 1.2, "한국: 예산 비법률주의", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 7.4, 11.5, 5.8, 1.2, "미국: 세출법률주의", fc="#fdf9f4", ec="#c77b2f", weight="bold")

kr = [
    "정부만 예산안을 편성·제출\n(의원 발의 불가)",
    "국회 심의\n(정부 동의 없이 증액·새 비목\n설치 불가, 헌법 제57조)",
    "국회 의결로 곧바로 확정\n(공포 불요 · 거부권 없음)",
    "예산 = 독자적 법형식\n(국가기관 구속, 한 회계연도)",
]
us = [
    "의회가 세출법안을 기초·수정\n(지갑의 힘, power of the purse)",
    "상원·하원 통과",
    "대통령 서명\n(거부권 행사 가능)",
    "세출법 = 법률\n(지출의 목적·조건을 조문으로 통제)",
]
ys = (9.2, 6.9, 4.6, 2.3)
for y, t in zip(ys, kr):
    box(ax, 0.8, y, 5.8, 1.8, t, fc="white", ec="#2f6fb0")
for y, t in zip(ys, us):
    box(ax, 7.4, y, 5.8, 1.8, t, fc="white", ec="#c77b2f")
for y in (11.4, 9.1, 6.8, 4.5):
    arrow(ax, 3.7, y, 3.7, y - 0.4, color="#2f6fb0")
    arrow(ax, 10.3, y, 10.3, y - 0.4, color="#c77b2f")

box(ax, 0.8, 0.3, 5.8, 1.4, "불성립 시: 준예산 자동 작동\n(헌법 제54조 제3항, 셧다운 없음)", fc="#f4faf5", ec="#3a7d44")
box(ax, 7.4, 0.3, 5.8, 1.4, "불성립 시: 셧다운\n(2025년 43일, 역대 최장)", fc="#fff5f5", ec="#c0392b")
arrow(ax, 3.7, 2.2, 3.7, 1.8, color="#3a7d44", ls="--", lw=1.3)
arrow(ax, 10.3, 2.2, 10.3, 1.8, color="#c0392b", ls="--", lw=1.3)

ax.set_title("예산과 법률의 관계: 한국의 의결주의와 미국의 세출법률주의", fontsize=14, pad=12)
fig.savefig(FIG / "fig06_lawbudget.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig06_*.png"))])
