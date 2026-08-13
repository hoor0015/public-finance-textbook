# 2주차(1차시·2차시) 개념도 생성
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


# ---------------------------------------------------------------- 그림 2-1
# 재정의 4기능 구조도: 배분 · 재분배 · 안정 · 삶의 질
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis("off")

box(ax, 4.4, 9.0, 5.2, 1.6, "재정(정부의 경제활동)\n하나의 예산, 네 개의 기능",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=12, weight="bold")

cols = [
    ("자원배분\n(allocation)", "시장실패 교정\n공공재 공급\n(국방 · 치안)", "가치: 효율성",
     "#f5f9fd", "#2f6fb0"),
    ("소득재분배\n(distribution)", "누진세 · 이전지출로\n소득분배를 조정", "가치: 형평성",
     "#f4fbf6", "#2f8f4e"),
    ("경제안정화\n(stabilization)", "총수요 조절로 경기 조절\n(추경 · 자동안정화장치)", "가치: 안정과 성장",
     "#fdf9f4", "#c77b2f"),
    ("삶의 질 제고\n(quality of life)", "GDP 너머의\n행복 · 건강 · 환경", "가치: 행복 · 삶의 질",
     "#faf8fc", "#7a5fa8"),
]
for i, (t1, t2, t3, fc, ec) in enumerate(cols):
    x = 0.4 + i * 3.4
    box(ax, x, 6.2, 3.0, 1.5, t1, fc=fc, ec=ec, fontsize=11.5, weight="bold")
    box(ax, x, 4.0, 3.0, 1.8, t2, fc="white", ec=ec, fontsize=9.5)
    box(ax, x, 2.5, 3.0, 1.1, t3, fc=fc, ec=ec, fontsize=10)
    arrow(ax, 7.0, 8.9, x + 1.5, 7.85, color=ec)

# 아래 묶음 표시: 머스그레이브 3대 기능 / 사회적 기능
ax.plot([0.5, 10.5], [1.9, 1.9], color="#555", lw=1.2)
ax.plot([0.5, 0.5], [1.9, 2.1], color="#555", lw=1.2)
ax.plot([10.5, 10.5], [1.9, 2.1], color="#555", lw=1.2)
ax.text(5.5, 1.3, "머스그레이브의 재정 3대 기능 (경제적 기능)", ha="center",
        fontsize=11, color="#333")
ax.plot([11.0, 13.8], [1.9, 1.9], color="#7a5fa8", lw=1.2)
ax.plot([11.0, 11.0], [1.9, 2.1], color="#7a5fa8", lw=1.2)
ax.plot([13.8, 13.8], [1.9, 2.1], color="#7a5fa8", lw=1.2)
ax.text(12.4, 1.3, "사회적 기능", ha="center", fontsize=11, color="#7a5fa8")

ax.text(7.0, 0.4, "하나의 재정 활동이 여러 기능에 동시에 걸칠 수 있다 (예: 실업급여 = 재분배 + 자동안정화장치).",
        ha="center", fontsize=10, color="#333")
ax.set_title("재정의 4기능: 무엇을 하며, 어떤 가치를 추구하는가", fontsize=14, pad=12)
fig.savefig(FIG / "fig02_functions.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 2-2
# 쉬크의 3대 규범과 한국의 재정제도
fig, ax = plt.subplots(figsize=(12.5, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis("off")

rows = [
    ("① 총량적 재정규율\n(aggregate fiscal\ndiscipline)", "지출 총량을 먼저 명시적으로\n결정하고 그 준수를 강제한다",
     "국가재정운용계획\n재정준칙 논의(법제화 무산)", "#f5f9fd", "#2f6fb0", 8.2),
    ("② 배분적 효율성\n(allocative\nefficiency)", "정부의 우선순위와 사업의\n효과에 따라 부문 간 배분한다",
     "총액배분 자율편성제도\n예비타당성조사", "#f4fbf6", "#2f8f4e", 5.6),
    ("③ 운영적 효율성\n(operational\nefficiency)", "최소의 비용으로 산출을 내고\n지속적으로 효율을 개선한다",
     "재정사업 성과관리제도\n프로그램 예산제도", "#faf8fc", "#7a5fa8", 3.0),
]
for t1, t2, t3, fc, ec, y in rows:
    box(ax, 0.4, y, 3.4, 2.0, t1, fc=fc, ec=ec, fontsize=10.5, weight="bold")
    box(ax, 4.6, y, 4.6, 2.0, t2, fc="white", ec=ec, fontsize=10)
    box(ax, 10.0, y, 3.6, 2.0, t3, fc="white", ec=ec, fontsize=10)
    arrow(ax, 3.9, y + 1.0, 4.5, y + 1.0, color=ec)
    arrow(ax, 9.3, y + 1.0, 9.9, y + 1.0, color=ec)

# 규범의 위계 (총량 → 배분 → 운영)
arrow(ax, 2.1, 8.1, 2.1, 7.75, color="#555")
arrow(ax, 2.1, 5.5, 2.1, 5.15, color="#555")
ax.text(0.25, 10.6, "규범 (Schick, 1998)", fontsize=11, color="#333", ha="left")
ax.text(4.6, 10.6, "요구 내용", fontsize=11, color="#333", ha="left")
ax.text(10.0, 10.6, "한국의 제도", fontsize=11, color="#333", ha="left")

box(ax, 2.4, 0.5, 9.6, 1.5,
    "국가재정법 제16조의 법제화: 재정건전성(제1호) · 재정지출과 조세지출의 성과 제고(제3호)\n투명성과 국민참여(제4호)",
    fc="#f4faf5", ec="#3a7d44", fontsize=10)
arrow(ax, 7.0, 2.9, 7.0, 2.1, color="#3a7d44")

ax.set_title("쉬크의 공공지출관리 3대 규범과 한국의 재정제도", fontsize=14, pad=12)
fig.savefig(FIG / "fig02_norms.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 2-3
# 전통적 예산원칙과 그 예외
fig, ax = plt.subplots(figsize=(12.5, 7.5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis("off")

ax.text(3.1, 11.0, "원칙 (통제의 지향)", ha="center", fontsize=12, color="#2f6fb0",
        fontweight="bold")
ax.text(10.4, 11.0, "법률이 정한 예외 (신축성)", ha="center", fontsize=12, color="#c77b2f",
        fontweight="bold")

pairs = [
    ("사전의결의 원칙\n(헌법 제54조)", "준예산\n(헌법 제54조 제3항)", 9.1),
    ("한정성의 원칙\n(목적 · 금액 · 기간, 제3조 · 제45조)", "이용 · 전용 · 이체 · 이월\n예비비 · 계속비 · 추경", 7.2),
    ("완전성의 원칙\n(예산총계주의, 제17조)", "수입대체경비 초과 수입\n현물출자 등(제53조)", 5.3),
    ("단일성의 원칙\n(하나의 예산으로 운영)", "특별회계 · 기금 · 추경", 3.4),
    ("통일성의 원칙\n(특정 세입-세출 연계 금지)", "특별회계 · 목적세\n(교육세 · 농어촌특별세)", 1.5),
]
for t1, t2, y in pairs:
    box(ax, 0.4, y, 5.4, 1.6, t1, fc="#f5f9fd", ec="#2f6fb0", fontsize=10)
    box(ax, 7.7, y, 5.4, 1.6, t2, fc="#fdf9f4", ec="#c77b2f", fontsize=10)
    arrow(ax, 5.9, y + 0.8, 7.6, y + 0.8, color="#888", ls="--", lw=1.3)

ax.text(7.0, 0.5, "이 밖에 공개성(제9조) · 명료성 · 엄밀성의 원칙이 있다. 예외는 모두 법률의 요건과 절차 안에서만 허용된다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("전통적 예산원칙과 그 예외: 통제와 신축성의 짝", fontsize=14, pad=12)
fig.savefig(FIG / "fig02_principles.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig02_*.png"))])
