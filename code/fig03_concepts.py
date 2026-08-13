# 3주차(1차시·2차시) 개념도 생성
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


# ---------------------------------------------------------------- 그림 3-1
# 정부재정의 3원 구조: 일반회계 · 특별회계 · 기금 (2026년 예산 기준)
fig, ax = plt.subplots(figsize=(12, 6.6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10.5)
ax.axis("off")

box(ax, 3.7, 8.6, 6.6, 1.5, "국가재정 (중앙정부)\n2026년 예산 기준 총지출 727.9조 원",
    fc="#f7f7fc", ec="#5b6ee1", weight="bold")

# 중간층: 예산 / 기금
box(ax, 1.0, 5.9, 7.4, 1.4, "예산 = 세입세출예산\n(국가재정법 제4조)", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 9.4, 5.9, 3.9, 1.4, "기금\n(국가재정법 제5조)", fc="#faf8fc", ec="#7a5fa8", weight="bold")
arrow(ax, 6.0, 8.5, 4.7, 7.5)
arrow(ax, 8.0, 8.5, 11.3, 7.5)

# 하단층: 일반회계 / 특별회계 / 기금 상세
box(ax, 0.5, 2.9, 3.9, 2.3,
    "일반회계 (1개)\n조세수입 등으로 국가의\n일반적 세출에 충당\n총지출의 52.9% (385.3조 원)",
    fc="white", ec="#2f6fb0")
box(ax, 4.9, 2.9, 3.9, 2.3,
    "특별회계 (21개)\n특정 사업 · 특정 자금 ·\n특정 세입을 특정 세출에 충당\n총지출의 13.2% (96.1조 원)",
    fc="white", ec="#2b7a78")
box(ax, 9.4, 2.9, 3.9, 2.3,
    "기금 (67개)\n특정 목적의 자금을\n세입세출예산 밖에서 신축 운용\n총지출의 33.9% (246.5조 원)",
    fc="white", ec="#7a5fa8")
arrow(ax, 3.4, 5.8, 2.5, 5.3)
arrow(ax, 6.2, 5.8, 6.8, 5.3)
arrow(ax, 11.3, 5.8, 11.3, 5.3)

# 예외 표시
box(ax, 3.4, 0.6, 7.2, 1.3,
    "특별회계와 기금은 2주차에서 본\n예산 단일성 · 통일성 원칙의 예외다",
    fc="#fdf9f4", ec="#c77b2f")
arrow(ax, 6.8, 2.8, 6.4, 2.0, color="#c77b2f", ls="--", lw=1.3)
arrow(ax, 11.3, 2.8, 9.4, 1.7, color="#c77b2f", ls="--", lw=1.3)

ax.set_title("정부재정의 3원 구조 (2026년 예산 기준, 자료: 국회예산정책처)", fontsize=14, pad=12)
fig.savefig(FIG / "fig03_structure.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 3-2
# 특별회계 21개의 구성 (2026년)
fig, ax = plt.subplots(figsize=(12, 6.2))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 3.9, 8.3, 6.2, 1.4, "특별회계 21개\n2026년 세출 총계 117.2조 원",
    fc="#f2fafa", ec="#2b7a78", weight="bold")

box(ax, 0.7, 5.4, 5.8, 1.6,
    "기업특별회계 (5개)\n정부가 기업처럼 사업을 운영\n세출 총계 14.9조 원", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 7.5, 5.4, 5.8, 1.6,
    "기타특별회계 (16개)\n특정 세입을 특정 세출에 충당\n세출 총계 102.3조 원", fc="#f4faf5", ec="#3a7d44", weight="bold")
arrow(ax, 5.9, 8.2, 3.9, 7.2)
arrow(ax, 8.1, 8.2, 10.1, 7.2)

box(ax, 0.7, 1.6, 5.8, 3.3,
    "우편사업 · 우체국예금 ·\n양곡관리 · 조달\n(정부기업예산법)\n+ 책임운영기관특별회계\n(12개 계정, 경찰병원 등)",
    fc="white", ec="#2f6fb0")
box(ax, 7.5, 1.6, 5.8, 3.3,
    "지역균형발전(22.9조 원) ·\n농어촌구조개선 · 교통시설 ·\n고등·평생교육지원 · 영유아 ·\n환경개선 · 에너지및자원사업 ·\n교도작업 · 등기 등",
    fc="white", ec="#3a7d44")
arrow(ax, 3.6, 5.3, 3.6, 5.0)
arrow(ax, 10.4, 5.3, 10.4, 5.0)

ax.text(7.0, 0.7, "각 특별회계는 국가재정법 [별표 1]에 규정된 법률에 의해서만 설치할 수 있다 (제4조 제3항).",
        ha="center", fontsize=10, color="#333")
ax.set_title("특별회계 21개의 구성 (2026년 예산 기준, 자료: 국회예산정책처)", fontsize=14, pad=12)
fig.savefig(FIG / "fig03_special.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 3-3
# 기금의 4유형 (2026년, 67개)
fig, ax = plt.subplots(figsize=(12, 6.4))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 3.6, 8.4, 6.8, 1.3,
    "기금 67개 (25개 부처)\n2026년 기금운용계획 기준 운용 규모 총계 990.8조 원",
    fc="#faf8fc", ec="#7a5fa8", weight="bold")

types = [
    ("사업성기금 (48개)", "특정 재정사업 수행에\n필요한 자금을 운용\n관광진흥개발기금,\n국민체육진흥기금 등",
     "#f5f9fd", "#2f6fb0"),
    ("사회보험성기금 (6개)", "연금 · 보험 지출에 대비해\n보험료 등을 운용\n국민연금기금, 고용보험기금,\n공무원연금기금 등",
     "#f4faf5", "#3a7d44"),
    ("금융성기금 (8개)", "보증 · 보험 등\n금융활동에 가까운 역할\n신용보증기금, 기술보증기금,\n무역보험기금 등",
     "#fdf9f4", "#c77b2f"),
    ("계정성기금 (5개)", "자금을 모아 사업 주체에\n전달하는 통로 역할\n공공자금관리기금,\n외국환평형기금, 복권기금 등",
     "#f2fafa", "#2b7a78"),
]
for i, (t1, t2, fc, ec) in enumerate(types):
    x = 0.4 + i * 3.45
    box(ax, x, 5.6, 3.05, 1.2, t1, fc=fc, ec=ec, weight="bold")
    box(ax, x, 1.9, 3.05, 3.3, t2, fc="white", ec=ec)
    arrow(ax, x + 1.5, 5.5, x + 1.5, 5.3)
    arrow(ax, 7.0, 8.3, x + 1.5, 6.9)

ax.text(7.0, 0.9, "유형 구분은 국회예산정책처의 분류를 따랐다. 사회보험성 · 금융성 · 계정성기금 명단은 전체이고, 사업성기금은 예시다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("기금의 4유형 (2026년 기준, 자료: 국회예산정책처)", fontsize=14, pad=12)
fig.savefig(FIG / "fig03_fundtypes.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 3-4
# 예산과 기금: 확정 절차와 집행 통제의 비교
fig, ax = plt.subplots(figsize=(12, 6.8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis("off")

# 왼쪽 열: 예산
box(ax, 0.6, 9.2, 6.0, 1.2, "예산 (일반회계 · 특별회계)", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 0.6, 7.4, 6.0, 1.3, "각 중앙관서의 예산요구서 제출", fc="white", ec="#2f6fb0")
box(ax, 0.6, 5.6, 6.0, 1.3, "기획예산처가 정부 예산안 편성", fc="white", ec="#2f6fb0")
box(ax, 0.6, 3.8, 6.0, 1.3, "국회 심의 · 의결로 확정", fc="white", ec="#2f6fb0")
box(ax, 0.6, 1.7, 6.0, 1.6, "집행: 합법성 중심의 엄격한 통제\n(목적 외 사용 금지, 변경은 추경 · 이용 · 전용)",
    fc="white", ec="#2f6fb0")

# 오른쪽 열: 기금
box(ax, 7.4, 9.2, 6.0, 1.2, "기금", fc="#faf8fc", ec="#7a5fa8", weight="bold")
box(ax, 7.4, 7.4, 6.0, 1.3, "기금관리주체가 기금운용계획안 수립", fc="white", ec="#7a5fa8")
box(ax, 7.4, 5.6, 6.0, 1.3, "기획예산처장관과 협의 · 조정", fc="white", ec="#7a5fa8")
box(ax, 7.4, 3.8, 6.0, 1.3, "국회 심의 · 의결로 확정", fc="white", ec="#7a5fa8")
box(ax, 7.4, 1.7, 6.0, 1.6, "집행: 합목적성 차원의 자율 · 탄력 운용\n(주요항목의 20-30% 이내 자율 변경)",
    fc="white", ec="#7a5fa8")

for x in (3.6, 10.4):
    for y1, y2 in ((7.3, 6.95), (5.5, 5.15), (3.7, 3.35)):
        arrow(ax, x, y1, x, y2)

box(ax, 3.7, 0.15, 6.6, 1.0, "결산: 둘 다 국회의 심의 · 의결", fc="#f7f7fc", ec="#5b6ee1", weight="bold")
arrow(ax, 3.6, 1.6, 5.3, 1.25, color="#888")
arrow(ax, 10.4, 1.6, 8.7, 1.25, color="#888")

ax.set_title("예산과 기금: 확정 절차는 닮았고, 집행 통제는 다르다", fontsize=14, pad=12)
fig.savefig(FIG / "fig03_compare.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig03_*.png"))])
