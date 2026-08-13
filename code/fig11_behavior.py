# 11주차(1차시·2차시) 예산행태론 개념도 생성
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


# ---------------------------------------------------------------- 그림 11-1
# 소비자·절약자·수문장: 예산행태의 세 역할
fig, ax = plt.subplots(figsize=(12, 6.8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10.4)
ax.axis("off")

cols = [
    ("소비자(spender)\n증액 지향", "관심: 수입보다 지출\n성향: 사업 지향\n전형: 행정 부처 · 사업 담당자\n(필요액 이상의 요구)", "#f5f9fd", "#2f6fb0"),
    ("수문장(gatekeeper)\n균형 지향", "관심: 수입과 지출 모두\n성향: 사업 + 재정 동시 지향\n전형: 행정수반(대통령)", "#faf8fc", "#7a5fa8"),
    ("절약자(saver)\n삭감 지향", "관심: 지출보다 수입의 조건\n성향: 재정 지향\n전형: 중앙예산기관 · 예결위 ·\n부처 예산총괄(대내)", "#fdf9f4", "#c77b2f"),
]
for i, (t1, t2, fc, ec) in enumerate(cols):
    x = 0.5 + i * 4.6
    box(ax, x, 7.0, 4.0, 1.6, t1, fc=fc, ec=ec, weight="bold")
    box(ax, x, 3.6, 4.0, 2.9, t2, fc="white", ec=ec)

# 소비자·절약자의 반대 지향이 수문장에서 균형을 이룬다
arrow(ax, 4.6, 7.8, 5.0, 7.8, color="#2f6fb0")
arrow(ax, 9.4, 7.8, 9.0, 7.8, color="#c77b2f")
ax.text(7.0, 9.3, "증액 압력과 삭감 압력이 수문장의 균형에서 만난다",
        ha="center", fontsize=10.5, color="#333")

box(ax, 1.2, 0.9, 11.6, 1.7,
    "원형: 옹호자(advocate) 대 국고의 수호자(guardian of the treasury)\n"
    "서로의 역할을 기대하기에 각자 안심하고 제 역할을 한다 = 계산 장치 (Wildavsky, 1964; 1975)",
    fc="#f7f7fc", ec="#5b6ee1")
for x in (2.5, 7.0, 11.5):
    arrow(ax, x, 3.5, x, 2.75, color="#888", ls="--", lw=1.2)

ax.set_title("소비자 · 절약자 · 수문장: 예산행태의 세 역할", fontsize=14, pad=12)
fig.savefig(FIG / "fig11_roles.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 11-2
# 예산결정 4대 기관과 역할의 지도
fig, ax = plt.subplots(figsize=(13, 6.6))
ax.set_xlim(0, 15.4)
ax.set_ylim(0, 10)
ax.axis("off")

orgs = [
    ("행정 부처\n(각 중앙관서)", "소비자 · 주창자\n사업 지향 · 증액 요구", "#f5f9fd", "#2f6fb0"),
    ("기획예산처\n(중앙예산기관 ·\n국무총리 소속)", "절약자 · 수문장\n예산사정 · 총량 관리", "#fdf9f4", "#c77b2f"),
    ("대통령 · 국무회의\n(행정수반)", "수문장 · 통합자\n심의 · 승인 · 우선순위", "#faf8fc", "#7a5fa8"),
    ("국회\n(심의 · 확정)", "옹호자와 삭감자의 공존\n(2차시에서 다룬다)", "#f4fbf6", "#2f8f4e"),
]
for i, (t1, t2, fc, ec) in enumerate(orgs):
    x = 0.4 + i * 3.85
    box(ax, x, 5.6, 3.3, 2.2, t1, fc=fc, ec=ec, weight="bold")
    box(ax, x, 3.0, 3.3, 1.8, t2, fc="white", ec=ec)
    arrow(ax, x + 1.65, 5.5, x + 1.65, 4.9, color=ec, ls="--", lw=1.2)

# 부처 -> 기획예산처 (요구), 기획예산처 -> 부처 (지침)
arrow(ax, 3.75, 7.3, 4.2, 7.3, color="#2f6fb0")
ax.text(3.98, 8.15, "예산요구서 (5. 31.까지)", ha="center", fontsize=9, color="#2f6fb0")
arrow(ax, 4.2, 6.1, 3.75, 6.1, color="#c77b2f")
ax.text(3.98, 5.15, "편성지침 · 지출한도 (3. 31.까지)", ha="center", fontsize=9, color="#c77b2f")
# 기획예산처 -> 대통령 -> 국회
arrow(ax, 7.6, 6.7, 8.05, 6.7, color="#555")
ax.text(7.83, 8.15, "예산안 편성 (제32조)", ha="center", fontsize=9, color="#555")
arrow(ax, 11.45, 6.7, 11.9, 6.7, color="#555")
ax.text(11.68, 8.15, "예산안 제출 (120일 전)", ha="center", fontsize=9, color="#555")

box(ax, 2.2, 0.7, 11.0, 1.5,
    "역할 표시는 지배적 행태이며 상황에 따라 이동한다\n(예: 국정과제 사업 앞에서 중앙예산기관은 사업 지향을 갖기도 한다)",
    fc="#f7f7fc", ec="#5b6ee1")
ax.set_title("예산결정 4대 기관과 역할의 지도", fontsize=14, pad=12)
fig.savefig(FIG / "fig11_actors.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 11-3
# 국회 예산심의의 절차와 행태
fig, ax = plt.subplots(figsize=(13, 7.2))
ax.set_xlim(0, 15.4)
ax.set_ylim(0, 11.4)
ax.axis("off")

stages = [
    ("정부 예산안 제출\n(회계연도 개시 120일 전)", "#f2f2f2", "#888"),
    ("시정연설 ·\n상임위원회 예비심사", "#f5f9fd", "#2f6fb0"),
    ("예결위 종합심사\n(정책질의 · 부별 심사)", "#fdf9f4", "#c77b2f"),
    ("본회의 의결\n(개시 30일 전, 12. 2.)", "#f4fbf6", "#2f8f4e"),
]
for i, (t, fc, ec) in enumerate(stages):
    x = 0.4 + i * 3.85
    box(ax, x, 8.6, 3.3, 1.9, t, fc=fc, ec=ec, weight="bold")
    if i < 3:
        arrow(ax, x + 3.4, 9.55, x + 3.8, 9.55)

# 단계별 행태
box(ax, 4.25, 6.0, 3.3, 1.7, "증액 지향\n소관 부처의 옹호자", fc="white", ec="#2f6fb0")
arrow(ax, 5.9, 8.5, 5.9, 7.8, color="#2f6fb0", ls="--", lw=1.2)
box(ax, 8.1, 6.0, 3.3, 1.7, "삭감 지향\n재정 지향의 절약자", fc="white", ec="#c77b2f")
arrow(ax, 9.75, 8.5, 9.75, 7.8, color="#c77b2f", ls="--", lw=1.2)
ax.text(7.83, 5.55, "국회법 제84조⑤: 예비심사 존중 · 삭감분 증액 시 상임위 동의",
        ha="center", fontsize=9.5, color="#555")

# 예산안조정소위
box(ax, 7.6, 3.1, 4.3, 1.9, "예산안조정소위원회\n계수조정 = 실질적 결정\n(쪽지예산 논란)", fc="#fff5f5", ec="#c0392b", weight="bold")
arrow(ax, 9.75, 5.9, 9.75, 5.1, color="#c0392b")

# 여야의 압력
box(ax, 0.6, 0.7, 6.6, 1.6, "여당: 정부안 사수 · 기한 내 처리 (옹호자)", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 8.2, 0.7, 6.6, 1.6, "야당: 삭감 지향 · 쟁점 연계 투쟁 (삭감자)", fc="#fdf9f4", ec="#c77b2f")
arrow(ax, 5.4, 2.4, 8.6, 3.0, color="#2f6fb0", ls="--", lw=1.2)
arrow(ax, 10.6, 2.4, 10.2, 3.0, color="#c77b2f", ls="--", lw=1.2)

ax.set_title("국회 예산심의의 절차와 행태: 옹호와 삭감의 교대", fontsize=14, pad=12)
fig.savefig(FIG / "fig11_assembly.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 11-4
# 예산결정요인론의 인과 구조
fig, ax = plt.subplots(figsize=(12.5, 6.8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10.5)
ax.axis("off")

# 위 경로: 환경 -> 수요 -> 산출
box(ax, 0.5, 7.7, 4.4, 2.0, "사회경제적 환경 변수\n(소득수준 · 도시화 ·\n산업화 · 인구 특성)", fc="#f4fbf6", ec="#2f8f4e", weight="bold")
box(ax, 5.6, 7.7, 3.9, 2.0, "예산 수요의 형성\n(행정 서비스에\n대한 요구)", fc="white", ec="#2f8f4e")
box(ax, 10.2, 4.5, 3.4, 2.2, "예산 산출\n(지출의 수준과 배분)", fc="#f7f7fc", ec="#5b6ee1", weight="bold")
arrow(ax, 4.95, 8.7, 5.55, 8.7, color="#2f8f4e")
arrow(ax, 9.55, 8.3, 10.7, 6.8, color="#2f8f4e")

# 가운데: 정치적 변수 (효과 약함)
box(ax, 0.5, 4.5, 4.4, 1.8, "정치적 변수\n(정당 간 경쟁 · 투표율 ·\n정치체제의 특성)", fc="white", ec="#c0392b")
arrow(ax, 4.95, 5.4, 10.15, 5.5, color="#c0392b", ls="--", lw=1.3)
ax.text(7.5, 5.85, "독자적 효과 약함 (초기 요인론의 발견)", ha="center", fontsize=9.5, color="#c0392b")

# 아래 경로: 과정 -> 행태 -> 산출
box(ax, 0.5, 1.2, 4.4, 2.0, "정치행정적 요인\n(예산과정의 구조 ·\n결정규칙)", fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 5.6, 1.2, 3.9, 2.0, "참여자들의 예산 행태\n(소비자 · 절약자 ·\n수문장)", fc="white", ec="#c77b2f")
arrow(ax, 4.95, 2.2, 5.55, 2.2, color="#c77b2f")
arrow(ax, 9.55, 2.6, 10.7, 4.4, color="#c77b2f")

ax.text(7.0, 0.45, "Fabricant(1952) · Brazer(1959) · Dawson & Robinson(1963): 정치 변수보다 사회경제 변수가 중요하다",
        ha="center", fontsize=10, color="#333")
ax.set_title("예산결정요인론의 인과 구조: 환경이 수요를, 수요가 산출을 움직인다", fontsize=14, pad=12)
fig.savefig(FIG / "fig11_determinants.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig11_*.png"))])
