# 7주차(1차시·2차시) 재정정책론 개념도 생성
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


# ---------------------------------------------------------------- 그림 7-1
# 자동안정화장치 vs 재량적 재정정책
fig, ax = plt.subplots(figsize=(12.5, 7.6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12.2)
ax.axis("off")

box(ax, 4.2, 10.4, 5.6, 1.4, "경기 침체\n총수요 부족 · 소득 감소 · 실업 증가",
    fc="#fff5f5", ec="#c0392b", weight="bold")
arrow(ax, 5.6, 10.3, 3.4, 9.5, color="#2f6fb0")
arrow(ax, 8.4, 10.3, 10.6, 9.5, color="#c77b2f")

# 왼쪽: 자동안정화장치
box(ax, 0.6, 8.1, 5.6, 1.3, "자동안정화장치\n(automatic stabilizers)",
    fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 0.6, 6.8, 5.6, 1.0, "새로운 입법 · 의결 불필요 (제도에 내장)",
    fc="white", ec="#2f6fb0")
box(ax, 0.6, 4.8, 2.65, 1.6, "누진소득세\n세부담이 소득보다\n더 큰 비율로 감소",
    fc="white", ec="#2f6fb0")
box(ax, 3.55, 4.8, 2.65, 1.6, "실업급여\n지급이 자동으로\n증가",
    fc="white", ec="#2f6fb0")
box(ax, 0.6, 2.9, 5.6, 1.5, "가처분소득 방어 → 소비 위축 완충\n(시차 없음 · 규모는 제도가 결정)",
    fc="#f4fbf6", ec="#2f8f4e")
arrow(ax, 3.4, 8.0, 3.4, 7.9, color="#2f6fb0")
arrow(ax, 3.4, 6.7, 3.4, 6.5, color="#2f6fb0")
arrow(ax, 1.9, 4.7, 2.6, 4.5, color="#2f6fb0")
arrow(ax, 4.9, 4.7, 4.2, 4.5, color="#2f6fb0")

# 오른쪽: 재량적 재정정책
box(ax, 7.8, 8.1, 5.6, 1.3, "재량적 재정정책\n(discretionary fiscal policy)",
    fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 7.8, 6.8, 5.6, 1.0, "정부 편성 + 국회 의결 필요 (새 결정)",
    fc="white", ec="#c77b2f")
box(ax, 7.8, 4.8, 2.65, 1.6, "추가경정예산\n지출 확대\n(국가재정법 제89조)",
    fc="white", ec="#c77b2f")
box(ax, 10.75, 4.8, 2.65, 1.6, "감세\n세율 · 공제 조정",
    fc="white", ec="#c77b2f")
box(ax, 7.8, 2.9, 5.6, 1.5, "총수요 진작\n(규모 선택 가능 · 인식-결정-집행 시차)",
    fc="#f4fbf6", ec="#2f8f4e")
arrow(ax, 10.6, 8.0, 10.6, 7.9, color="#c77b2f")
arrow(ax, 10.6, 6.7, 10.6, 6.5, color="#c77b2f")
arrow(ax, 9.1, 4.7, 9.8, 4.5, color="#c77b2f")
arrow(ax, 12.1, 4.7, 11.4, 4.5, color="#c77b2f")

box(ax, 2.4, 0.7, 9.2, 1.4,
    "경기 과열 국면에서는 반대 방향으로 작동: 세수 자동 증가(자동) · 긴축 결정(재량)",
    fc="#f7f7fc", ec="#5b6ee1")
ax.set_title("경기 침체에 대응하는 재정의 두 경로", fontsize=14, pad=12)
fig.savefig(FIG / "fig07_stabilizer.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 7-2
# 승수효과의 산수: 정부지출 10조 원의 연쇄
fig, ax = plt.subplots(figsize=(12.5, 7.0))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis("off")

box(ax, 0.8, 9.0, 6.4, 1.4, "정부지출 +10조 원 (도로 건설)",
    fc="#f7f7fc", ec="#5b6ee1", weight="bold")
box(ax, 0.8, 7.1, 6.4, 1.3, "1라운드: 건설 노동자 · 기업의 소득 +10조 원",
    fc="white", ec="#2f6fb0")
box(ax, 0.8, 5.2, 4.8, 1.3, "2라운드: 소득의 절반을 소비 +5조 원",
    fc="white", ec="#2f6fb0")
box(ax, 0.8, 3.3, 3.6, 1.3, "3라운드: +2.5조 원",
    fc="white", ec="#2f6fb0")
box(ax, 0.8, 1.4, 2.8, 1.3, "4라운드 이후\n+1.25조 원 ...",
    fc="white", ec="#2f6fb0")
arrow(ax, 4.0, 8.9, 4.0, 8.6, color="#2f6fb0")
arrow(ax, 4.0, 7.0, 4.0, 6.7, color="#2f6fb0")
arrow(ax, 3.2, 5.1, 3.2, 4.8, color="#2f6fb0")
arrow(ax, 2.2, 3.2, 2.2, 2.9, color="#2f6fb0")

box(ax, 8.6, 3.3, 4.9, 4.2,
    "총수요 증가 합계\n10 + 5 + 2.5 + 1.25 + ...\n= 20조 원\n(승수 = 2)",
    fc="#f4fbf6", ec="#2f8f4e", weight="bold")
arrow(ax, 7.3, 7.75, 8.9, 7.0, color="#2f8f4e")
arrow(ax, 5.7, 5.85, 8.5, 5.7, color="#2f8f4e")
arrow(ax, 4.5, 3.95, 8.5, 4.6, color="#2f8f4e")
arrow(ax, 3.7, 2.05, 8.9, 3.6, color="#2f8f4e")

ax.text(7.0, 0.5,
        "가정: 늘어난 소득의 절반이 소비로 이어진다(한계소비성향 0.5). 승수 = 1 / (1 - 0.5) = 2.\n"
        "저축 · 수입품으로의 누출이나 구축효과가 크면 연쇄가 일찍 끊겨 승수는 작아진다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("승수효과의 산수: 정부지출 10조 원의 연쇄", fontsize=14, pad=12)
fig.savefig(FIG / "fig07_multiplier.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 7-3
# 기본소득 · 기본서비스 · 기본자산 비교 구조도
fig, ax = plt.subplots(figsize=(13, 7.8))
ax.set_xlim(0, 15.2)
ax.set_ylim(0, 12)
ax.axis("off")

cols = [
    ("기본소득 (UBI)", 2.6, "#f5f9fd", "#2f6fb0"),
    ("기본서비스 (UBS)", 6.8, "#f2fafa", "#2b7a78"),
    ("기본자산 (UBA)", 11.0, "#faf8fc", "#7a5fa8"),
]
for t, x, fc, ec in cols:
    box(ax, x, 10.0, 3.9, 1.3, t, fc=fc, ec=ec, weight="bold")

rows = [
    ("무엇을\n주는가", 8.0, 1.6,
     ["정기적 현금\n(소득의 흐름)", "무료 공공서비스\n(현물)", "생애 초기 일시금\n(자산의 밑천)"]),
    ("핵심 원칙", 6.0, 1.6,
     ["개별성 · 보편성 · 무조건성\n정기성 · 현금성", "공익성 · 기본성 · 보편성\n(공동의 바닥)", "출발선의 기회 균등\n(부의 대물림 차단)"]),
    ("대표\n실험 · 사례", 3.5, 2.1,
     ["알래스카 배당(1982-현재)\n핀란드 실험(2017-2018)\n농어촌 기본소득(2026-2027)",
      "북유럽 보편 복지 모델\nUCL 제안(2017)",
      "영국 아동신탁기금\n(2002-2011)\n사회적 지분급여 제안(1999)"]),
]
for label, y, h, cells in rows:
    box(ax, 0.3, y, 1.9, h, label, fc="#f2f2f2", ec="#888", weight="bold")
    for (t, x, fc, ec), cell in zip(cols, cells):
        box(ax, x, y, 3.9, h, cell, fc="white", ec=ec)

box(ax, 2.6, 0.8, 12.3, 1.5,
    "공통 쟁점: 재원을 어떻게 마련하는가 · 노동 유인에 어떤 영향을 미치는가 · 기존 복지와 대체인가 보완인가",
    fc="#fdf9f4", ec="#c77b2f")
for t, x, fc, ec in cols:
    arrow(ax, x + 1.95, 3.4, x + 1.95, 2.5, color=ec, ls="--", lw=1.3)

ax.set_title("기본소득 · 기본서비스 · 기본자산: 세 실험의 구조", fontsize=14, pad=12)
fig.savefig(FIG / "fig07_basics.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig07_*.png"))])
