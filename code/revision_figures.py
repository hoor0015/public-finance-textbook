"""Reconstruct selected teaching figures from the original lecture decks.

The source-slide mapping is written to _site/figure_metadata/new_figure_manifest.json.
Diagram coordinates are conceptual, not measurements. All numerical examples
are explicitly educational. Web-textbook styling and 150 dpi follow 집필지침.md.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import seaborn as sns
sns.set_style('white')
import koreanize_matplotlib  # noqa: E402,F401
import figfit  # noqa: E402

ROOT=Path(__file__).resolve().parents[1]
FIG=ROOT/'figures'
VERIFY=ROOT/'_site'/'figure_metadata'
VERIFY.mkdir(parents=True,exist_ok=True)
figfit.MIN_PT=13
figfit.MAX_PT=20
figfit.FILL=.85
figfit.OUT_CAP=1.25
BLUE='#315f86'; GREEN='#3a7567'; PURPLE='#756181'; DARK='#263646'
manifest=[]
checks=[]

def canvas(h=7.2):
    fig,ax=plt.subplots(figsize=(12,h))
    fig.subplots_adjust(left=.03,right=.97,bottom=.04,top=.96)
    ax.set(xlim=(0,12),ylim=(0,h))
    ax.axis('off')
    return fig,ax

def box(ax,x,y,w,h,text,color=BLUE,fill='#f2f6fa'):
    p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.035,rounding_size=0.1',
                     lw=1.5,ec=color,fc=fill,zorder=2)
    ax.add_patch(p)
    t=ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=17,
              color=DARK,zorder=3,linespacing=1.5)
    t._revision_host=p
    return p

def arrow(ax,x1,y1,x2,y2,label=None,style='-|>',ls='-'):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,
                                mutation_scale=17,lw=1.5,color='#61717d',
                                linestyle=ls,zorder=1))
    if label:
        ax.text((x1+x2)/2+.15,(y1+y2)/2+.1,label,fontsize=14,
                ha='left',va='center',color=DARK,
                bbox=dict(fc='white',ec='none',pad=1),zorder=4)

def label(ax,x,y,text,size=15,ha='center'):
    ax.text(x,y,text,fontsize=size,ha=ha,va='center',color=DARK,linespacing=1.5)

def save(fig,name,chapter,deck,slides,kind):
    fig.savefig(FIG/name,dpi=150,bbox_inches='tight',facecolor='white')
    fig.canvas.draw();renderer=fig.canvas.get_renderer()
    for ax in fig.axes:
        for t in ax.texts:
            if hasattr(t,'_revision_host'):
                tb=t.get_window_extent(renderer)
                pb=t._revision_host.get_window_extent(renderer)
                ok=pb.contains(tb.x0,tb.y0) and pb.contains(tb.x1,tb.y1)
                checks.append(dict(file=name,text=t.get_text(),inside=bool(ok),font=t.get_fontsize()))
    plt.close(fig)
    manifest.append(dict(file=name,chapter=chapter,ppt=deck,slides=slides,kind=kind))

# PPT 04, slide 3. Distinguish government levels before accounting categories.
fig,ax=canvas(7.4)
box(ax,3.8,6.0,4.4,1.0,'정부재정의 기본 구조')
for x,title,content,decider in [
    (.25,'중앙정부','예산: 일반회계·특별회계\n기금: 기금운용계획','국회의 심의·의결'),
    (4.3,'지방자치단체','예산: 일반회계·특별회계\n기금: 기금운용계획','해당 지방의회의 심의·의결'),
    (8.35,'지방교육재정','교육비특별회계 등\n교육청의 예산·기금','시·도의회의 심의·의결')]:
    box(ax,x,4.3,3.4,1,title)
    box(ax,x,2.1,3.4,1.5,content,GREEN,'#f2f8f5')
    box(ax,x,.35,3.4,1,decider,PURPLE,'#f7f4fa')
    arrow(ax,6,5.96,x+1.7,5.34)
    arrow(ax,x+1.7,4.25,x+1.7,3.65)
    arrow(ax,x+1.7,2.05,x+1.7,1.4)
save(fig,'fig03_levels.png','03-1','04',[3],'source_diagram')

# PPT 04, slide 10, supplemented by a transparent assumed cash-flow example.
fig,ax=canvas(7.2)
label(ax,2.3,6.7,'자금 조달 110억 원',19)
label(ax,9.65,6.7,'자금 사용 110억 원',19)
for y,s in [(4.7,'부담금\n60억 원'),(2.7,'일반회계 전입금\n20억 원'),(.7,'기존 예치금 회수\n30억 원')]:
    box(ax,.4,y,3.8,1.35,s)
    arrow(ax,4.25,y+.675,5.2,3.55)
box(ax,5.25,2.65,1.5,1.8,'기금\n운용')
for y,s in [(5.1,'사업비 70억 원'),(3.6,'관리비 10억 원'),(2.1,'원금 상환 10억 원'),(.6,'여유자금 예치 20억 원')]:
    box(ax,7.9,y,3.6,1.0,s,GREEN,'#f2f8f5')
    arrow(ax,6.8,3.55,7.85,y+.5)
save(fig,'fig03_fundflow.png','03-2','04',[10],'assumed_example')

# PPT 05, slide 14. A unit that is not independent is first combined with its parent.
fig,ax=canvas(7.8)
box(ax,.3,5.65,3.15,1.55,'① 독립된\n제도단위인가?')
box(ax,4.4,5.65,3.15,1.55,'② 정부가\n지배하는가?')
box(ax,8.5,5.65,3.15,1.55,'③ 시장생산자인가?')
arrow(ax,3.5,6.425,4.35,6.425,'예')
arrow(ax,7.6,6.425,8.45,6.425,'예')
box(ax,.3,2.65,3.15,1.65,'소속 제도단위에\n포함하여 분류',PURPLE,'#f7f4fa')
box(ax,4.4,2.65,3.15,1.65,'민간부문\n(공공부문에서 제외)',PURPLE,'#f7f4fa')
arrow(ax,1.875,5.6,1.875,4.35,'아니요')
arrow(ax,5.975,5.6,5.975,4.35,'아니요')
box(ax,8.5,2.65,3.15,1.65,'공기업',GREEN,'#f2f8f5')
arrow(ax,10.075,5.6,10.075,4.35,'예')
box(ax,8.5,.35,3.15,1.15,'일반정부',GREEN,'#f2f8f5')
ax.plot([11.73,11.9,11.9,11.72],[6.2,6.2,.925,.925],color='#61717d',lw=1.5)
arrow(ax,11.89,.925,11.7,.925)
label(ax,10.1,1.95,'아니요: 비시장생산',13)
label(ax,3.95,1.0,'공공부문 = 일반정부 + 공기업',16)
save(fig,'fig04_sector_test.png','04-2','05',[14],'source_diagram')

# PPT 06, slides 2-4,11. One record, several classification dimensions.
fig,ax=canvas(5.8)
box(ax,3.0,4.1,6,1.2,'하나의 지출\n직업훈련 사업의 강사료')
items=[(.15,'조직별\n누가\n쓰는가'),(2.55,'기능별\n어떤 정책\n기능인가'),(4.95,'사업별\n어느\n사업인가'),(7.35,'품목별\n무엇에\n지불하는가'),(9.75,'경제성질별\n어떤\n거래인가')]
arrow(ax,6,4.05,6,3.25)
ax.plot([1.2,10.8],[3.2,3.2],color='#61717d',lw=1.5)
for x,t in items:
    box(ax,x,.6,2.1,1.95,t,GREEN,'#f2f8f5')
    arrow(ax,x+1.05,3.2,x+1.05,2.6)
save(fig,'fig05_crossclass.png','05-1','06',[2,3,4,11],'assumed_example')

# PPT 06, slide 18. Preserve the teaching activity, avoid inventing official codes.
fig,ax=canvas(7.8)
box(ax,3.3,6.3,5.4,1.1,'정책 목표\n쾌적한 생활환경과 자원순환')
items=[(.3,'생활폐기물 관리','폐기물 수거·처리\n무단투기 감시'),(4.4,'재활용 촉진','재활용품 수집\n음식물류 폐기물 자원화'),(8.5,'청소행정 기반','차량·장비 관리\n현장 인력 지원')]
for x,unit,activities in items:
    box(ax,x,4.0,3.2,1.25,unit)
    box(ax,x,1.7,3.2,1.5,activities,GREEN,'#f2f8f5')
    arrow(ax,6,6.25,x+1.6,5.3)
    arrow(ax,x+1.6,3.95,x+1.6,3.25)
label(ax,6,.65,'예시',15)
save(fig,'fig05_program_example.png','05-2','06',[18],'adapted_teaching_example')

# PPT 08, slide 4. Explicitly non-empirical cycle, no fabricated observed GDP.
t=np.linspace(0,12,400)
trend=2+.27*t
actual=trend+.6*np.sin((t-1)*np.pi/3)
fig,ax=plt.subplots(figsize=(11,6.4))
ax.plot(t,actual,color=BLUE,lw=3,label='경기 변동을 포함한 산출')
ax.plot(t,trend,color='#777777',lw=2,ls='--',label='장기 추세')
ax.set(xlim=(0,12),ylim=(1.2,6.2),xlabel='시간',ylabel='실질 산출 수준')
ax.set_xticks([]);ax.set_yticks([])
for x,word,y in [(1,'회복',2.6),(3.1,'확장',3.8),(5.6,'수축',3.25),(7.1,'회복',4.5),(9.2,'확장',5.8)]:
    ax.text(x,y,word,ha='center',fontsize=16,color=DARK)
ax.legend(loc='upper left',fontsize=14,frameon=False)
ax.spines[['top','right']].set_visible(False)
ax.xaxis.label.set_size(16);ax.yaxis.label.set_size(16)
fig.tight_layout()
save(fig,'fig07_cycle.png','07-1','08',[4],'conceptual_curve')

# PPT 09, slide 12, updated from fixed money-target chain to flexible inflation targeting.
fig,ax=canvas(8.2)
rows=[(6.6,'정책수단','기준금리\n공개시장운영·대출제도·지급준비제도'),
      (4.65,'운영목표','단기시장금리 등을\n정책 의도에 맞게 유도'),
      (2.7,'전달경로','시장금리·신용·자산가격·환율·기대\n→ 소비·투자·총수요'),
      (.75,'최종목표','물가안정\n금융안정에 유의')]
for y,title,body in rows:
    box(ax,.4,y,2.65,1.2,title,PURPLE,'#f7f4fa')
    box(ax,3.75,y,7.75,1.2,body)
for y,_,_ in rows[:-1]: arrow(ax,7.625,y-.05,7.625,y-.7)
save(fig,'fig09_transmission.png','09-2','09',[12],'source_diagram_updated')

# PPT 13, slide 4. Multiple paths; arrows are explanatory, not estimates.
fig,ax=canvas(5.7)
for x,tit in [(0.15,'환경'),(3.25,'예산결정\n과정'),(6.35,'참여자의\n개별 전략'),(9.45,'예산 결과')]:
    box(ax,x,2.05,2.4,1.65,tit)
for x in [2.6,5.7,8.8]: arrow(ax,x,2.875,x+.6,2.875)
ax.plot([1.35,1.35,7.55],[3.75,4.45,4.45],color='#61717d',lw=1.5)
arrow(ax,7.55,4.45,7.55,3.75)
ax.plot([1.35,1.35,10.65],[4.45,5.05,5.05],color='#61717d',lw=1.5)
arrow(ax,10.65,5.05,10.65,3.75)
ax.plot([4.45,4.45,10.65],[2.0,.8,.8],color='#61717d',lw=1.5)
arrow(ax,10.65,.8,10.65,2.0)
save(fig,'fig12_paths.png','12-1','13',[4],'source_diagram')

# PPT 16, slides 27-28. Values transcribed from the supplied lecture example.
packages=['A-1','B-1','C-1','D-1','B-2','C-2','A-2','C-3','D-2','B-3','A-3','D-3']
amounts=[70,130,100,150,50,50,20,30,40,30,20,50]
cumulative=np.cumsum(amounts)
fig,ax=plt.subplots(figsize=(11,7))
y=np.arange(12)
colors=[GREEN if v<=600 else '#bdc6cd' for v in cumulative]
ax.barh(y,cumulative,color=colors,height=.67)
ax.axvline(600,color=PURPLE,ls='--',lw=2,label='예산 한도 600억 원')
for i,(v,a) in enumerate(zip(cumulative,amounts)):
    ax.text(v+8,i,f'{v}  (+{a})',va='center',fontsize=13,bbox=dict(fc='white',ec='none',pad=1))
ax.set_yticks(y,[f'{i+1}순위  {p}' for i,p in enumerate(packages)],fontsize=13)
ax.invert_yaxis()
ax.set_xlim(0,900)
ax.set_xlabel('누적 예산액 (억 원), 괄호 안은 패키지별 증분',fontsize=14)
ax.spines[['top','right']].set_visible(False)
ax.legend(loc='lower right',fontsize=13,frameon=False)
fig.tight_layout()
save(fig,'fig13_zbb_packages.png','13-1','16',[27,28],'source_educational_data')

# Highway cash flow: keep the manuscript's explicitly assumed 30 operating years.
# Original PPT uses years 5-30. Manuscript uses 5-34, so recalculate, not transcribe.
def cashflows(rate,last_year=34):
    benefit=sum(30.5/(1+rate)**year for year in range(5,last_year+1))
    cost=90/(1+rate)+sum(100/(1+rate)**year for year in [2,3,4])+sum(.5/(1+rate)**year for year in range(5,last_year+1))
    return dict(rate=rate,benefit=benefit,cost=cost,npv=benefit-cost,bc=benefit/cost)
financial=[cashflows(r) for r in [.04,.06,.08]]
lo,hi=.01,.15
for _ in range(70):
    mid=(lo+hi)/2
    if cashflows(mid)['npv']>0: lo=mid
    else: hi=mid
irr=(lo+hi)/2
(VERIFY/'calculation_results.json').write_text(json.dumps(dict(highway=financial,irr=irr,zbb=dict(packages=packages,amounts=amounts,cumulative=cumulative.tolist(),selected_total=int(cumulative[7]))),indent=2),encoding='utf-8')
fig,ax=plt.subplots(figsize=(11,6.5))
x=np.arange(3);w=.32
ax.bar(x-w/2,[r['benefit'] for r in financial],w,color=BLUE,label='편익의 현재가치')
ax.bar(x+w/2,[r['cost'] for r in financial],w,color='#d8e5df',edgecolor=GREEN,hatch='//',label='비용의 현재가치')
for i,r in enumerate(financial):
    for dx,v in [(-w/2,r['benefit']),(w/2,r['cost'])]:
        ax.text(i+dx,v+7,f'{v:.1f}',ha='center',fontsize=14)
ax.set_xticks(x,['4%','6%','8%'],fontsize=15)
ax.set_xlabel('할인율',fontsize=16)
ax.set_ylabel('현재가치 (백만 달러)',fontsize=16)
ax.set_ylim(0,550)
ax.legend(loc='upper right',fontsize=14,frameon=False)
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
save(fig,'fig13_highway.png','13-2','14',[31],'recomputed_manuscript_example')
print('HIGHWAY',json.dumps(financial));print('IRR',irr)

# PPT 15, slide 18. Keep cross-criterion comparisons to every alternative.
fig,ax=canvas(7.4)
box(ax,3.75,6,4.5,1,'목표: 주택 선택의 만족')
for x,criterion in [(.4,'주거 비용'),(4.4,'교통 접근성'),(8.4,'주거 환경')]:
    box(ax,x,3.6,3.2,1.2,criterion)
    arrow(ax,6,5.95,x+1.6,4.85)
for x,house in [(.4,'주택 A'),(4.4,'주택 B'),(8.4,'주택 C')]:
    box(ax,x,.5,3.2,1.2,house,GREEN,'#f2f8f5')
for a in [2,6,10]:
    for b in [2,6,10]: arrow(ax,a,3.55,b,1.75)
save(fig,'fig14_house.png','14-1','15',[18],'simplified_source_diagram')

# PPT 17, slides 17 and 28. Add fund and subsidy questions to the existing 3-tier chart.
fig,ax=canvas(8.6)
rows=[('재정사업','목표 달성·사업 효과','목표관리·성과평가'),
      ('국고보조사업','계속 지원할 타당성','보조사업 연장평가'),
      ('기금의 여유자금','자산운용의 위험·성과','기금운용평가'),
      ('기금 자체','별도 기금의 존치 필요','기금존치평가')]
for x,w,t in [(.25,2.9,'평가 대상'),(3.6,4.7,'확인하는 질문'),(8.75,3,'관련 평가')]:
    label(ax,x+w/2,8.05,t,18)
for i,(a,b,c) in enumerate(rows):
    y=6.3-i*1.8
    box(ax,.25,y,2.9,1.3,a)
    box(ax,3.6,y,4.7,1.3,b,GREEN,'#f2f8f5')
    box(ax,8.75,y,3,1.3,c,PURPLE,'#f7f4fa')
    arrow(ax,3.2,y+.65,3.55,y+.65)
    arrow(ax,8.35,y+.65,8.7,y+.65)
save(fig,'fig14_eval_questions.png','14-2','17',[17,28],'source_diagram')

(VERIFY/'new_figure_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
(VERIFY/'figure_text_bounds.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
failed=[c for c in checks if not c['inside']]
print('Saved',len(manifest),'figures; labels outside boxes:',len(failed))
for c in failed: print(c)
