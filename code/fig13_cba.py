# 13주차 2차시(비용편익분석) 수치 그래프 생성
# 실행: cd $HOME/default-uv-env && PYTHONIOENCODING=utf-8 VIRTUAL_ENV= uv run python "<이 파일 경로>"
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("whitegrid")
import koreanize_matplotlib  # noqa: E402,F401
import figfit  # noqa: E402,F401  (상자 글씨 자동 크기)

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(exist_ok=True)

# ---------------------------------------------------------------- 그림 13-3
# 할인율에 따른 미래 100만 원의 현재가치 감소 곡선
years = np.arange(0, 31)
rates = [(0.03, "#2f8f4e", "할인율 3%"),
         (0.045, "#2f6fb0", "할인율 4.5% (한국 예비타당성조사)"),
         (0.08, "#c0392b", "할인율 8%")]

fig, ax = plt.subplots(figsize=(10, 6))
for r, c, label in rates:
    pv = 100 / (1 + r) ** years  # 단위: 만 원
    ax.plot(years, pv, color=c, lw=2.2, label=label)
    ax.annotate(f"{pv[-1]:.0f}만 원", xy=(30, pv[-1]), xytext=(30.4, pv[-1]),
                color=c, fontsize=10, va="center")

ax.set_xlim(0, 33.5)
ax.set_ylim(0, 105)
ax.set_xlabel("편익이 발생하는 시점 (몇 년 후인가)", fontsize=11)
ax.set_ylabel("100만 원의 현재가치 (만 원)", fontsize=11)
ax.legend(fontsize=10, loc="upper right")
ax.set_title("할인율에 따른 미래 100만 원의 현재가치 감소", fontsize=14, pad=12)
fig.savefig(FIG / "fig13_pv_discount.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 13-4
# 고속도로 사례: 할인율에 따른 NPV 변화와 내부수익률
# 비용: 1년차 부지 90, 2-4년차 건설 매년 100, 5-34년차 유지 매년 0.5 (백만 달러)
# 편익: 5-34년차 매년 30.5 (백만 달러)


def npv(rate):
    b = sum(30.5 / (1 + rate) ** t for t in range(5, 35))
    c = (90 / (1 + rate)
         + sum(100 / (1 + rate) ** t for t in (2, 3, 4))
         + sum(0.5 / (1 + rate) ** t for t in range(5, 35)))
    return b - c


rr = np.linspace(0.03, 0.09, 121)
vv = np.array([npv(r) for r in rr])

# IRR (이분법)
lo, hi = 0.04, 0.08
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if npv(mid) > 0 else (lo, mid)
irr = (lo + hi) / 2

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(rr * 100, vv, color="#2f6fb0", lw=2.4)
ax.axhline(0, color="#555", lw=1.2)
ax.axvline(irr * 100, color="#c77b2f", lw=1.4, ls="--")
ax.annotate(f"IRR = {irr * 100:.1f}%\n(NPV = 0이 되는 할인율)",
            xy=(irr * 100, 0), xytext=(irr * 100 + 0.35, 55),
            fontsize=10.5, color="#c77b2f",
            arrowprops=dict(arrowstyle="->", color="#c77b2f", lw=1.2))

for r, dy in [(0.04, 14), (0.06, -20), (0.08, -20)]:
    v = npv(r)
    ax.plot(r * 100, v, "o", color="#c0392b", ms=6)
    ax.annotate(f"{r * 100:.0f}%: {v:+.1f}", xy=(r * 100, v),
                xytext=(r * 100 - 0.15, v + dy), fontsize=10, color="#c0392b")

ax.fill_between(rr * 100, vv, 0, where=vv > 0, color="#2f8f4e", alpha=0.10)
ax.fill_between(rr * 100, vv, 0, where=vv < 0, color="#c0392b", alpha=0.08)
ax.text(3.6, 12, "타당성 있음 (NPV > 0)", fontsize=10, color="#2f8f4e")
ax.text(7.1, -48, "타당성 없음 (NPV < 0)", fontsize=10, color="#c0392b")

ax.set_xlabel("적용한 할인율 (%)", fontsize=11)
ax.set_ylabel("순현재가치 NPV (백만 달러)", fontsize=11)
ax.set_title("고속도로 사업의 NPV 곡선: 할인율이 판정을 가른다", fontsize=14, pad=12)
fig.savefig(FIG / "fig13_npv_irr.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig13_*.png"))])
