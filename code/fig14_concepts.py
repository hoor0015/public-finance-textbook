# 14주차(1차시·2차시) 개념도 생성
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


# ---------------------------------------------------------------- 그림 14-1
# 예비타당성조사의 절차: 대상 선정 - 조사 수행 - AHP 종합평가 - 위원회 심의, 면제 트랙
fig, ax = plt.subplots(figsize=(12.5, 6))
ax.set_xlim(0, 14)
ax.set_ylim(3.1, 9.9)
ax.axis("off")

steps = [
    ("대상사업 선정\n중앙관서 신청 또는 직권,\n국회 의결 요구 시 의무", 0.3, "#f5f9fd", "#2f6fb0"),
    ("조사 수행\nKDI 공공투자관리센터·\n조세재정연구원", 3.75, "#f5f9fd", "#2f6fb0"),
    ("종합평가(AHP)\n경제성·정책성·\n지역균형발전 종합", 7.2, "#faf8fc", "#7a5fa8"),
    ("재정사업평가위원회\n심의·결과 확정", 10.65, "#f4fbf6", "#2f8f4e"),
]
for t, x, fc, ec in steps:
    box(ax, x, 7.7, 3.05, 1.8, t, fc=fc, ec=ec)
for x in (3.4, 6.85, 10.3):
    arrow(ax, x, 8.6, x + 0.32, 8.6)

ax.text(8.72, 7.3, "AHP 0.5 이상이면 시행이 바람직", ha="center", fontsize=9.5, color="#555")

# 결과 반영
box(ax, 9.9, 4.7, 3.7, 1.5, "예산편성 반영\n결과 요약 국회 제출\n(상임위·예결위)", fc="#f4fbf6", ec="#2f8f4e")
arrow(ax, 12.18, 7.6, 11.9, 6.3, color="#2f8f4e")

# 면제 트랙
box(ax, 0.3, 4.7, 3.05, 1.5, "예타 면제\n(제38조 제2항의\n10개 유형)", fc="#fdf9f4", ec="#c77b2f")
arrow(ax, 1.82, 7.6, 1.82, 6.3, color="#c77b2f")
box(ax, 4.4, 4.7, 3.5, 1.5, "사업계획 적정성 검토\n(예타에 준한\n대안·재원 분석)", fc="#fdf9f4", ec="#c77b2f")
arrow(ax, 3.45, 5.45, 4.32, 5.45, color="#c77b2f")
arrow(ax, 8.0, 5.45, 9.82, 5.45, color="#c77b2f")

ax.text(7.0, 3.6, "국가연구개발사업은 2026년 2월 법 개정으로 예타 대상에서 제외되었다(1,000억 원 이상은 맞춤형 사전검토).",
        ha="center", fontsize=10, color="#333")
ax.set_title("예비타당성조사의 절차 (2026년 기준)", fontsize=14, pad=12)
fig.savefig(FIG / "fig14_process.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 14-2
# 예타 종합평가의 계층구조 (AHP): 3대 분석 -> 시행/미시행
fig, ax = plt.subplots(figsize=(12, 6.8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 4.0, 8.2, 6.0, 1.4, "종합평가\n이 사업의 시행은 바람직한가", fc="#f7f7fc", ec="#5b6ee1", weight="bold")

mids = [
    ("경제성 분석\n비용편익분석(B/C)\n가중치 30-45%", 0.7, "#f5f9fd", "#2f6fb0"),
    ("정책성 분석\n추진 여건·정책 효과\n가중치 25-40%", 5.2, "#f4fbf6", "#2f8f4e"),
    ("지역균형발전 분석\n낙후도·경제 파급효과\n가중치 30-40%", 9.7, "#faf8fc", "#7a5fa8"),
]
for t, x, fc, ec in mids:
    box(ax, x, 5.0, 3.6, 2.0, t, fc=fc, ec=ec)
for xm in (2.5, 7.0, 11.5):
    arrow(ax, 7.0, 8.1, xm, 7.1)

box(ax, 3.2, 1.7, 3.2, 1.4, "사업 시행", fc="white", ec="#2f8f4e")
box(ax, 7.6, 1.7, 3.2, 1.4, "사업 미시행", fc="white", ec="#c0392b")
for xm, ecol in ((2.5, "#888"), (7.0, "#888"), (11.5, "#888")):
    arrow(ax, xm, 4.9, 4.8, 3.2, color=ecol, lw=1.1)
    arrow(ax, xm, 4.9, 9.2, 3.2, color=ecol, lw=1.1)

ax.text(7.0, 0.7, "가중치는 비수도권 건설사업 기준(수도권은 경제성 60-70%, 지역균형발전 제외). 평가위원별 AHP 점수의 평균이 0.5 이상이면 시행이 바람직하다고 본다.",
        ha="center", fontsize=9.5, color="#333")
ax.set_title("예비타당성조사 종합평가의 계층구조 (AHP)", fontsize=14, pad=12)
fig.savefig(FIG / "fig14_ahp.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 14-3
# 정부업무평가의 체계: 위원회 - 중앙(특정·자체), 지자체(합동·자체), 공공기관(개별법)
fig, ax = plt.subplots(figsize=(12.5, 6.6))
ax.set_xlim(0, 14)
ax.set_ylim(1.0, 9.9)
ax.axis("off")

box(ax, 3.7, 8.1, 6.6, 1.5, "정부업무평가위원회 (국무총리 소속)\n정부업무평가 기본법에 따라 평가를 총괄", fc="#f7f7fc", ec="#5b6ee1", weight="bold")

cols = [
    ("중앙행정기관", 0.5, "#2f6fb0"),
    ("지방자치단체", 5.0, "#2f8f4e"),
    ("공공기관", 9.5, "#7a5fa8"),
]
for t, x, ec in cols:
    box(ax, x, 5.9, 4.0, 1.2, t, fc="white", ec=ec, weight="bold")
arrow(ax, 5.5, 8.0, 2.5, 7.2)
arrow(ax, 7.0, 8.0, 7.0, 7.2)
arrow(ax, 8.5, 8.0, 11.5, 7.2)

box(ax, 0.5, 3.5, 4.0, 1.8, "특정평가\n국무총리가 주요 정책·\n현안을 평가", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 0.5, 1.3, 4.0, 1.8, "자체평가\n기관장이 소관 정책을\n스스로 평가", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 5.0, 3.5, 4.0, 1.8, "합동평가\n행정안전부장관이\n국가위임사무 등을 평가", fc="#f4fbf6", ec="#2f8f4e")
box(ax, 5.0, 1.3, 4.0, 1.8, "자체평가\n지방자치단체장이\n고유사무를 스스로 평가", fc="#f4fbf6", ec="#2f8f4e")
box(ax, 9.5, 1.3, 4.0, 4.0, "개별법에 따른 평가\n공기업·준정부기관\n경영평가(재정경제부),\n정부출연연구기관\n연구성과 평가 등", fc="#faf8fc", ec="#7a5fa8")

ax.set_title("정부업무평가의 체계 (정부업무평가 기본법)", fontsize=14, pad=12)
fig.savefig(FIG / "fig14_evalsys.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 14-4
# 재정성과관리제도의 3층 구조: 목표관리 - 자율평가 - 심층평가
fig, ax = plt.subplots(figsize=(12, 6.8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 3.4, 6.6, 5.2, 2.0, "③ 재정사업 심층평가 (2006년 도입)\n선별된 소수 사업\n계량분석으로 성과의 원인 규명", fc="#faf8fc", ec="#7a5fa8")
box(ax, 2.3, 3.9, 7.4, 2.0, "② 재정사업 자율평가 (2005년 도입)\n주요 재정사업\n부처 자체평가 + 기획예산처 확인·점검", fc="#f4fbf6", ec="#2f8f4e")
box(ax, 1.2, 1.2, 9.6, 2.0, "① 재정성과 목표관리 (2003년 도입)\n모든 재정사업\n성과계획서·성과보고서로 목표 달성 점검", fc="#f5f9fd", ec="#2f6fb0")

arrow(ax, 11.6, 1.6, 11.6, 8.2, color="#c77b2f", lw=1.8)
ax.text(11.9, 4.9, "위로 갈수록\n대상은 좁아지고\n분석은 깊어진다", ha="left", va="center", fontsize=10, color="#c77b2f")

ax.text(6.0, 0.45, "세 층의 평가 결과는 성과보고서와 평가등급의 형태로 다음 해 예산편성과 지출 구조조정에 환류된다.",
        ha="center", fontsize=10, color="#333")
ax.set_ylim(0, 9.1)
ax.set_title("재정성과관리제도의 3층 구조 (국가재정법 제85조의2 이하)", fontsize=14, pad=12)
fig.savefig(FIG / "fig14_tiers.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig14_*.png"))])
