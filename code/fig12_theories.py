# 12주차(1차시·2차시) 예산이론 개념도 생성
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


# ---------------------------------------------------------------- 그림 12-1
# 예산이론의 전개 지도: 키의 질문 -> 경제적/정치적 접근 -> 총체주의/점증주의 -> 통합·확장
fig, ax = plt.subplots(figsize=(12.5, 8.2))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12.8)
ax.axis("off")

box(ax, 4.2, 10.9, 5.6, 1.5,
    "키(Key, 1940)의 질문\n어떤 근거로 X달러를 B사업 대신\nA사업에 배분하는가?", fc="#f7f7fc", ec="#5b6ee1", weight="bold")
arrow(ax, 5.6, 10.8, 3.4, 10.4)
arrow(ax, 8.4, 10.8, 10.6, 10.4)

# 왼쪽: 경제적 접근 -> 총체주의
box(ax, 0.9, 9.0, 5.0, 1.2, "경제적 접근\n포괄적 · 분석적 · 체계적", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 0.9, 7.0, 5.0, 1.5,
    "루이스(1952)의 세 명제\n상대적 가치 · 증분 분석 · 상대적 효과성", fc="white", ec="#2f6fb0")
box(ax, 0.9, 4.6, 5.0, 1.7,
    "총체주의\n합리적 자원배분의 이상\n(파레토 최적 · 규범적 이론)", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
arrow(ax, 3.4, 8.9, 3.4, 8.6, color="#2f6fb0")
arrow(ax, 3.4, 6.9, 3.4, 6.4, color="#2f6fb0")

# 오른쪽: 정치적 접근 -> 점증주의
box(ax, 8.1, 9.0, 5.0, 1.2, "정치적 접근\n점증적 · 정치적 · 단편적", fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 8.1, 7.0, 5.0, 1.5,
    "버크헤드(1956)\n예산 배분은 정치적 결정\n참여자 영향력 연구", fc="white", ec="#c77b2f")
box(ax, 8.1, 4.6, 5.0, 1.7,
    "점증주의\n전년도 기초 위의 소폭 조정\n(린드블롬 · 윌다브스키, 실증적 이론)", fc="#fdf9f4", ec="#c77b2f", weight="bold")
arrow(ax, 10.6, 8.9, 10.6, 8.6, color="#c77b2f")
arrow(ax, 10.6, 6.9, 10.6, 6.4, color="#c77b2f")

# 아래: 제도화(13주차)와 통합·확장(12주차 2차시)
box(ax, 0.4, 1.4, 4.0, 1.7,
    "총체주의의 제도화\n성과주의 · PPBS · ZBB\n(13주차 재정개혁론)", fc="white", ec="#2f6fb0")
box(ax, 5.0, 1.4, 4.0, 1.7,
    "다중합리성 모형\n킹던 + 루빈의 통합\n(서마이어 · 윌러비, 2001)", fc="#faf8fc", ec="#7a5fa8")
box(ax, 9.6, 1.4, 4.0, 1.7,
    "조직과정 모형\n선언 · 형식화 · 분화 · 확산\n(그린 · 톰슨, 2001)", fc="#faf8fc", ec="#7a5fa8")
arrow(ax, 2.4, 4.5, 2.4, 3.3, color="#2f6fb0", ls="--", lw=1.3)
arrow(ax, 4.6, 4.5, 6.4, 3.3, color="#2f6fb0", ls="--", lw=1.3)
arrow(ax, 9.4, 4.5, 7.6, 3.3, color="#c77b2f", ls="--", lw=1.3)
arrow(ax, 11.6, 4.5, 11.6, 3.3, color="#c77b2f", ls="--", lw=1.3)
ax.text(9.3, 0.7, "다중합리성 모형과 조직과정 모형은 12주차 2차시에서 다룬다.",
        ha="center", fontsize=10, color="#333")
ax.set_title("예산이론의 전개: 키의 질문에서 두 갈래, 그리고 그 너머로", fontsize=14, pad=12)
fig.savefig(FIG / "fig12_map.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 12-2
# 총체주의 vs 점증주의 비교 구조도
fig, ax = plt.subplots(figsize=(12, 6.6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 3.1, 8.3, 5.0, 1.2, "총체주의", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 8.7, 8.3, 5.0, 1.2, "점증주의", fc="#fdf9f4", ec="#c77b2f", weight="bold")

rows = [
    ("미시적 과정", "총체적이고\n체계적인 분석", "연속적이고\n제한된 비교"),
    ("거시적 과정", "집권적이고 제도화된\n프로그램 예산편성", "당파적 상호 조정\n(협상과 타협)"),
    ("산출(결과)", "신규 사업과 대폭적이고\n체계적인 변화", "전년도 예산의 소폭 변화\n(기초액 + 공평한 몫)"),
    ("이론의 성격", "규범적\n(어떻게 결정해야 하는가)", "실증적\n(실제로 어떻게 결정되는가)"),
]
for i, (label, syn, inc) in enumerate(rows):
    y = 6.4 - i * 1.9
    box(ax, 0.3, y, 2.4, 1.5, label, fc="#f2f2f2", ec="#888", weight="bold")
    box(ax, 3.1, y, 5.0, 1.5, syn, fc="white", ec="#2f6fb0")
    box(ax, 8.7, y, 5.0, 1.5, inc, fc="white", ec="#c77b2f")

ax.set_title("총체주의와 점증주의: 세 축의 거울상 비교", fontsize=14, pad=12)
fig.savefig(FIG / "fig12_compare.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 12-3
# 루빈의 실시간 예산운영(RTB) 모형: 5개 의사결정 흐름
fig, ax = plt.subplots(figsize=(12.5, 7.2))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11.7)
ax.axis("off")

streams = [
    ("① 세입 흐름\n누가 얼마나 부담하는가 (설득의 정치)", "#f5f9fd", "#2f6fb0"),
    ("② 세출 흐름\n무엇에 얼마나 쓰는가 (선택의 정치)", "#f4fbf6", "#2f8f4e"),
    ("③ 균형 흐름\n정부의 범위와 역할 (제약의 정치)", "#faf8fc", "#7a5fa8"),
    ("④ 집행 흐름\n계획과 일탈의 허용범위", "#fdf9f4", "#c77b2f"),
    ("⑤ 과정 흐름\n누가 어떻게 결정하는가", "#fff5f5", "#c0392b"),
]
ys = [9.9, 7.75, 5.6, 3.45, 1.3]
for (t, fc, ec), y in zip(streams, ys):
    box(ax, 0.5, y, 6.4, 1.5, t, fc=fc, ec=ec)
for y1, y2 in zip(ys[:-1], ys[1:]):
    ax.add_patch(FancyArrowPatch((3.7, y1 - 0.06), (3.7, y2 + 1.56), arrowstyle="<|-|>",
                                 mutation_scale=10, color="#888", lw=1.0, linestyle="--"))

box(ax, 8.4, 4.8, 5.1, 2.6,
    "실시간 조정\n다른 흐름과 환경으로부터 오는\n정보 · 결정에 계속 적응", fc="#f7f7fc", ec="#5b6ee1", weight="bold")
for (_, _, ec), y in zip(streams, ys):
    arrow(ax, 6.95, y + 0.75, 8.35, 6.1, color=ec)

box(ax, 9.0, 9.2, 3.9, 1.5, "새해 예산의 성립\n(기한 내 통합)", fc="white", ec="#2f8f4e", weight="bold")
arrow(ax, 10.95, 7.5, 10.95, 9.1, color="#2f8f4e")

arrow(ax, 0.7, 0.75, 13.3, 0.75, color="#333", lw=1.8)
ax.text(7.0, 0.25, "시간의 흐름: 기한이 다가올수록 다섯 흐름은 하나의 예산으로 수렴해야 한다",
        ha="center", fontsize=10, color="#333")
ax.set_title("루빈의 실시간 예산운영(RTB) 모형: 느슨하게 연계된 다섯 개의 의사결정 흐름", fontsize=14, pad=12)
fig.savefig(FIG / "fig12_rtb.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 12-4
# 조직과정 모형의 발전 4단계 (Green & Thompson, 2001)
fig, ax = plt.subplots(figsize=(13, 6.4))
ax.set_xlim(0, 15.2)
ax.set_ylim(0, 10)
ax.axis("off")

stages = [
    ("① 선언 단계\n1950-60년대", "Simon: 제한된 합리성\nLindblom: 제한된 변화\nWildavsky(1964):\n예산과정의 정치학", "#f5f9fd", "#2f6fb0"),
    ("② 형식화 단계\n1960-70년대", "Davis · Dempster ·\nWildavsky(1966) 선형모형\nCrecine(1969) 시뮬레이션\nLarkey(1979) GRS 평가", "#f4fbf6", "#2f8f4e"),
    ("③ 분화 단계\n1980년 전후", "Padgett(1980)\n순차적 판단이론\nOMB 표준운영절차의\n여과 기능 분석", "#faf8fc", "#7a5fa8"),
    ("④ 확산 단계\n1980년대 말-90년대", "Kamlet & Mowery\nChoate & Thompson\nBaumgartner & Jones(1993)\n단절균형이론", "#fdf9f4", "#c77b2f"),
]
for i, (t1, t2, fc, ec) in enumerate(stages):
    x = 0.4 + i * 3.75
    box(ax, x, 6.7, 3.35, 1.6, t1, fc=fc, ec=ec, weight="bold")
    box(ax, x, 3.2, 3.35, 3.0, t2, fc="white", ec=ec)
    if i < 3:
        arrow(ax, x + 3.45, 7.5, x + 3.72, 7.5)

box(ax, 2.4, 1.0, 10.4, 1.5,
    "분석 단위는 '결정': 예산을 조직의 루틴 · 표준운영절차 · 선례의 산물로 설명한다",
    fc="#f7f7fc", ec="#5b6ee1")
ax.set_title("조직과정 모형의 발전 4단계 (Green & Thompson, 2001)", fontsize=14, pad=12)
fig.savefig(FIG / "fig12_stages.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig12_*.png"))])
