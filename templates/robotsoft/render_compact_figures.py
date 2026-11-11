"""Compose the six-page figures from frozen analyses, using the original style.

No fitting, sampling exclusions, or statistical reanalysis occurs here. Statistical
intervals are copied from the original summaries; strips show every network.
"""
from pathlib import Path
import hashlib
import json
import shutil
import sys
import os
os.environ["DSH_PALETTE"] = "light"
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ORIGINAL = ROOT / '03_REPRODUCIBLE_WORKSPACE/outputs/endpoint_revision'
DATA = ROOT / '03_REPRODUCIBLE_WORKSPACE/work/recording_extensions'
sys.path.insert(0, str(ORIGINAL))
import figure_style as fs
from render_figures import pct

OUT = HERE / 'figures'
SOURCES = {}
QA = {}

def remember(path):
    SOURCES[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()

def load(rel):
    path = DATA / rel
    remember(path)
    return json.loads(path.read_text())

def finish(cv, name):
    # All five main figures keep the Canvas 1:1 mm geometry. The earlier
    # 80 mm override stretched Figures 1-2 vertically by 14 % without
    # changing type size, which opened the gaps and made markers elliptical.
    QA[name] = fs.save(cv, OUT / name)

def endpoint():
    a = load('round2/analysis/endpoint_summary.json')
    b = load('round2/analysis/validation_summary.json')
    c = fs.Canvas(70)
    c.header(2, 65, 'a', 'The prediction task')
    # Schematic: node locations and curves illustrate the protocol, not data.
    xs, ys = np.meshgrid(np.linspace(8, 48, 10), np.linspace(32, 52, 10))
    c.base.scatter(xs, ys, s=3, color=fs.LIGHT_GREY)
    c.marker(8, 43.1, fs.GOLD, size=5)
    for y in [36.4, 43.1, 49.8]:
        c.marker(48, y, fs.ROSE, size=4.7)
    c.note(8, 55.5, 'Known connectivity; uncertain gains')
    c.text(4, 28, 'Stimulus', 6, color=fs.GOLD_DARK)
    c.text(39, 28, 'Readouts', 6, color=fs.ROSE_LINE)
    c.base.annotate('', xy=(44, 43), xytext=(12, 43), arrowprops=dict(arrowstyle='->', color=fs.PLUM, lw=.8, shrinkA=0, shrinkB=0))
    # The label sits inside the node field just above the flow arrow. The 10x10
    # grid has a 2.22 mm row pitch and the label is 1.77 mm tall, so resting on a
    # node row is intended rather than avoided.
    c.text(28, 44.0, 'Recurrent dynamics', 6, ha='center')
    c.text(28, 22.25, 'Choose 5 calibration recordings', 6.3, ha='center')
    c.text(28, 14.35, 'Fit gains; predict a held-out pulse', 6.3, ha='center')
    # Centre the final line on the lowest readout-marker row (y = 7).
    c.text(28, 7.0, 'Integrate response; forecast arm motion', 6.3, ha='center', va='center')
    # annotate() shrinks 2 pt off each end of a FancyArrowPatch by default, which
    # consumed more than half of the old 3 mm arrows, so shrink is disabled. Each
    # arrow is 2.65 mm, centred between the lines with an even ~1.2 mm of ink
    # clearance, which
    # keeps the stack low enough to leave 3.7 mm of air under the node field.
    for y_top, y_bottom in [(20.40, 17.75), (12.50, 9.85)]:
        c.base.annotate('', xy=(28, y_bottom), xytext=(28, y_top),
                        arrowprops=dict(arrowstyle='->', color=fs.MUTED, lw=.6,
                                        shrinkA=0, shrinkB=0))
    policies = ['neither', 'stim_only', 'readouts_only', 'both']
    colors = [fs.GREY, fs.GOLD, fs.READOUT, fs.ROSE]
    for x, d, letter, title, seed in [(62, a, 'b', 'First 40 networks', 7), (123, b, 'c', 'Independent 40 networks', 8)]:
        c.header(x, 65, letter, title)
        ax = c.ax(x+13, 19, 42, 39)
        values = [d['network_means'][p] for p in policies]
        assert all(len(v)==40 for v in values)
        fs.strip(ax, values, colors, seed=seed, size=5.6, width=.16)
        fs.log_axis(ax.yaxis, 1e-9, 1e-1, every=2)
        ax.set_ylabel('Response MSE')
        c.categories(ax, ['Neither', 'Stim.', 'Readouts', 'Both'], 16.3, size=6.1)
        for k in range(4):
            xx = c.x_of(ax, k)
            c.marker(xx, 10.7, fs.GOLD, filled=k in (1,3), size=3.6, edge=fs.GOLD_DARK if k in (1,3) else fs.LIGHT_GREY)
            for j in range(3):
                c.marker(xx+(j-1)*2, 7, fs.ROSE, filled=k in (2,3), size=2.7, edge=fs.ROSE_LINE if k in (2,3) else fs.LIGHT_GREY)
    finish(c, 'endpoint_compact')

def mechanism():
    p = load('round3/analysis/profile_summary.json')
    v = load('round4/analysis/mechanism_validation_summary.json')
    o = load('round4/analysis/oracle_data_fit_audit_summary.json')
    r = load('round5/analysis/summary.json')
    c = fs.Canvas(70)
    for x,l,t in [(1,'a','Response ambiguity'),(47,'b','Recording precision'),(94,'c','Error factors'),(139,'d','Recurrent information')]:
        c.header(x,65,l,t)
    ax = c.ax(13,20,29,37)
    x=np.array(p['metrics']['neither']['width2']); y=np.array(p['metrics']['both']['width2'])
    assert len(x)==len(y)==40
    ax.plot([1e-7,1],[1e-7,1], color=fs.MUTED, lw=.6, ls=(0,(2,2)))
    ax.scatter(x,y,s=8,c=fs.ROSE,edgecolors=fs.ROSE_LINE,linewidths=.3)
    fs.log_axis(ax.xaxis,1e-7,1,2);fs.log_axis(ax.yaxis,1e-7,1,2)
    ax.set_xlabel('Internal sites');ax.set_ylabel('Joint endpoints')
    fs.clean(ax)
    c.note(27,6.5,'Squared response-range width',ha='center')
    ax=c.ax(59,20,29,37)
    pol=['neither','both','both_noise4','both_noise16']
    fs.strip(ax,[p['metrics'][k]['mse'] for k in pol],[fs.GREY,fs.ROSE,fs.READOUT,fs.PALE_ROSE],seed=31,size=4.7,width=.14)
    fs.log_axis(ax.yaxis,1e-10,1e-1,3);ax.set_ylabel('Response MSE')
    c.categories(ax,['Int.','Ends','4x','16x'],17,size=6.2)
    c.note(73,6.5,'Endpoint noise SD multiplier',ha='center')
    ax=c.ax(113,20,22,37)
    fs.ratio_axis(ax,.003,3,[.01,.1,1],'Change, %')
    ax.set_ylim(2.65,-.65)
    for i,(k,color,label) in enumerate([('input',fs.GOLD,'Input'),('recurrence',fs.PLUM,'Recur.'),('readout',fs.ROSE,'Readout')]):
        est,lo,hi,*_=pct(v['component_comparisons'][k])
        fs.interval(ax,i,est,lo,hi,color,filled=True)
        c.text(95,c.y_of(ax,i),label,6.2,va='center')
    c.note(115,6.5,'Mean squared contribution',ha='center')
    ax=c.ax(146,20,31,37)
    fs.ratio_axis(ax,.003,1.5,[.01,.1,1],'Change in MSE, %')
    ax.set_ylim(1.7,-.65)
    initial=o['comparisons']['endpoints_recurrence8_vs_endpoint_ordinary8']
    valid=r['primary']['response_mse/oracle_combinations_vs_oracle_ordinary']
    for i,(d,lab,filled) in enumerate([(initial,'First 40 (added)',False),(valid,'Independent 40',True)]):
        est,lo,hi,*_=pct(d)
        fs.interval(ax,i+.20,est,lo,hi,fs.PLUM,filled=filled,adjusted=d.get('ci_family_three'))
        c.text(145,c.y_of(ax,i-.21),lab,6.2)
    c.note(160,6.5,'Equal information dimension',ha='center')
    finish(c,'mechanism_compact')

def fifth():
    r=load('round6/analysis/summary.json')
    c=fs.Canvas(72)
    c.header(2,67,'a','Fifth-site allocation, 80 networks')
    ax=c.ax(15,20,48,39)
    pol=['endpoints4','random5','combination5','response5']
    values=[r['metrics']['response_mse'][k] for k in pol]
    assert all(len(v)==80 for v in values)
    fs.strip(ax,values,[fs.LIGHT_GREY,fs.GREY,fs.PLUM,fs.ROSE],seed=51,size=4.5,width=.16)
    assert all(1e-10 < min(v) <= max(v) < 1e-3 for v in values)
    fs.log_axis(ax.yaxis,1e-10,1e-3,2);ax.set_ylabel('Response MSE')
    c.categories(ax,['Four\nends','+\nrandom','+\ncomb.','+\nresponse'],17,size=6.2)
    c.note(39,4,'All five-site policies retain the four endpoints',ha='center')
    c.header(73,68,'b','Information acquired and response prediction')
    ax=c.ax(115,21,24,39)
    fs.ratio_axis(ax,.4,2.1,[.5,1,2],'Change, %')
    ax.set_ylim(4.5,-.65)
    ds=r['diagnostic_contrasts'];ss=r['secondary']
    rows=[('Combination target',ds['combination_mse/combination5_vs_random5'],fs.PLUM,False),
          ('Response target',ds['combination_mse/response5_vs_random5'],fs.PLUM,False),
          ('Combination target',ss['combination5_vs_random5'],fs.ROSE,False),
          ('Response target',r['primary'],fs.ROSE,True),
          ('Random fifth site vs four endpoints',ss['random5_vs_endpoints4'],fs.GREY,False)]
    for i,(lab,d,color,filled) in enumerate(rows):
        est,lo,hi,*_=pct(d)
        fs.interval(ax,i,est,lo,hi,color,filled=filled)
        c.text(74,c.y_of(ax,i),lab,6.2,va='center')
        c.mono(141,c.y_of(ax,i),fs.ci_text(est,lo,hi,1),size=5.8,va='center')
    c.note(74,64,'Fifth-site policy / outcome');c.note(141,64,'Change, % [95% CI]')
    # Outcome labels are separated from rows by horizontal group rules.
    y=c.y_of(ax,1.5)
    c.rule(74,177,y)
    y=c.y_of(ax,3.5)
    c.rule(74,177,y)
    c.marker(77,10.2,fs.PLUM);c.note(80,9.5,'Combination MSE (top two)')
    c.marker(124,10.2,fs.ROSE);c.note(127,9.5,'Response MSE (next two)')
    c.note(74,4,'Last row: response MSE, increased recording budget.')
    finish(c,'fifth_compact')

if __name__=='__main__':
    OUT.mkdir(exist_ok=True)
    remember(ORIGINAL/'figure_style.py')
    remember(ORIGINAL/'render_figures.py')
    endpoint();mechanism();fifth()
    # This original main figure is already compact; preserve it byte for byte.
    for ext in ['pdf','png']:
        path=ORIGINAL/f'figures/structure_robustness.{ext}'
        remember(path);shutil.copyfile(path,OUT/path.name)
    (OUT/'compact_source_data.json').write_text(json.dumps({'source_sha256':SOURCES,'figure_checks':QA,'analysis_change':'none','independent_unit':'network','style':'Original figure_style.py; default light palette'},indent=2)+'\n')
    print(json.dumps(QA,indent=2))
