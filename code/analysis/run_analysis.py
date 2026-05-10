#!/usr/bin/env python3
"""Analysis pipeline for HIM-15: Trust Calibration Dynamics"""
import os, warnings, numpy as np, pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_RAW = os.path.join(BASE, 'data', 'raw')
DATA_PROC = os.path.join(BASE, 'data', 'processed')
RESULTS = os.path.join(BASE, 'results')
for d in [DATA_PROC, os.path.join(RESULTS,'figures'), os.path.join(RESULTS,'tables'), os.path.join(RESULTS,'statistical-output')]:
    os.makedirs(d, exist_ok=True)

print("HIM-15 Analysis Pipeline")

df1 = pd.read_csv(os.path.join(DATA_RAW, 'study1_longitudinal_trust.csv'))

# Session summaries
summary = df1.groupby(['session','condition_reliability','transparency']).agg({
    'trust_score':['mean','std','sem'],
    'brier_score':['mean','std'],
    'detection_accuracy':['mean','std'],
    'nasa_tlx':'mean',
    'subject_id':'count'
}).round(4)
summary.to_csv(os.path.join(DATA_PROC, 'session_summary_study1.csv'))

# Figure 1: Trust trajectories
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
reliability_labels = ['Very High', 'High', 'Moderate', 'Low', 'Variable']
ax = axes[0]
for rel in reliability_labels:
    for trans in ['Low', 'High']:
        sub = df1[(df1['condition_reliability']==rel) & (df1['transparency']==trans)]
        sess_mean = sub.groupby('session')['trust_score'].mean()
        ls = '--' if trans == 'High' else '-'
        ax.plot(sess_mean.index, sess_mean.values, ls, linewidth=2, label=f'{rel} ({trans})', alpha=0.8)
ax.set_xlabel('Session'); ax.set_ylabel('Trust Score'); ax.set_title('A. Trust Trajectories', fontweight='bold')
ax.legend(fontsize=7); ax.set_xlim(1,10); ax.set_ylim(1,7)

ax = axes[1]
for rel in reliability_labels:
    sub = df1[df1['condition_reliability']==rel]
    sess_brier = sub.groupby('session')['brier_score'].mean()
    ax.plot(sess_brier.index, sess_brier.values, linewidth=2, label=rel)
ax.set_xlabel('Session'); ax.set_ylabel('Brier Score (Lower=Better)')
ax.set_title('B. Calibration Trajectories', fontweight='bold'); ax.legend(fontsize=8); ax.set_xlim(1,10)
plt.tight_layout()
fig.savefig(os.path.join(RESULTS, 'figures', 'trust_trajectories.png'), dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig)

# Figure 2: Meta-analysis forest plot
df3 = pd.read_csv(os.path.join(DATA_RAW, 'study3_meta_analysis.csv'))
fig, ax = plt.subplots(figsize=(10, 8))
study3_plot = df3.sort_values('effect_size_calibration')
colors = ['#dc2626' if s=='AI-Assisted' else '#2563eb' if s=='Fully Automated' else '#059669' for s in study3_plot['automation_type']]
y_pos = range(len(study3_plot))
ax.scatter(study3_plot['effect_size_calibration'], y_pos, c=colors, s=30, zorder=5)
for i, (_, row) in enumerate(study3_plot.iterrows()):
    ax.plot([row['ci_lower'], row['ci_upper']], [i, i], 'k-', linewidth=1, alpha=0.5)
    ax.annotate(f"{row['domain'][:4]}({row['automation_type'][:3]})", xy=(row['ci_upper'], i), fontsize=6, va='center')
overall_effect = np.average(df3['effect_size_calibration'], weights=1/df3['se']**2)
ax.axvline(x=0, color='black', linewidth=1, ls='--'); ax.axvline(x=overall_effect, color='red', linewidth=2)
ax.set_xlabel("Effect Size (d) — Negative = Poor Calibration"); ax.set_title('C. Meta-Analysis', fontweight='bold')
legend_elements = [plt.Line2D([0],[0],marker='o',color='w',markerfacecolor='#dc2626',markersize=8,label='AI-Assisted'),
    plt.Line2D([0],[0],marker='o',color='w',markerfacecolor='#2563eb',markersize=8,label='Fully Automated'),
    plt.Line2D([0],[0],marker='o',color='w',markerfacecolor='#059669',markersize=8,label='Semi-Automated')]
ax.legend(handles=legend_elements, fontsize=9); ax.set_yticks(y_pos)
ax.set_yticklabels([f"Study {row['study_id']}" for _, row in study3_plot.iterrows()], fontsize=7)
plt.tight_layout()
fig.savefig(os.path.join(RESULTS, 'figures', 'meta_analysis_forest.png'), dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig)

# Stats
s = []
s.append("STATISTICAL ANALYSIS: HIM-15 Trust Calibration\n")
s.append(f"N (Study1) = {len(df1)} across 10 sessions, 150 subjects\n")
# Trust by condition at session 10
s.append("Final session trust by condition (Study 1):")
for rel in reliability_labels:
    for trans in ['Low','High']:
        sub = df1[(df1['condition_reliability']==rel)&(df1['transparency']==trans)]
        s.append(f"  {rel}/{trans}: M_trust={sub['trust_score'].iloc[-10:].mean():.2f}, M_brier={sub['brier_score'].iloc[-10:].mean():.4f}")
# Meta-analysis
s.append(f"\nMeta-Analysis (Study 3): k={len(df3)}")
s.append(f"Pooled effect: d={overall_effect:.3f} (SE={1/np.sqrt(np.sum(1/df3['se']**2)):.4f})")
s.append(f"95% CI: [{overall_effect-1.96/np.sqrt(np.sum(1/df3['se']**2)):.4f}, {overall_effect+1.96/np.sqrt(np.sum(1/df3['se']**2)):.4f}]")
for dom in df3['domain'].unique():
    d = df3[df3['domain']==dom]; w=1/d['se']**2; e=np.average(d['effect_size_calibration'],weights=w)
    s.append(f"  {dom}: k={len(d)}, pooled d={e:.3f}")
with open(os.path.join(RESULTS, 'statistical-output', 'complete_stats.txt'), 'w') as f:
    f.write('\n'.join(s))

# Table
table = df3.groupby('domain').agg({'effect_size_calibration':['mean','std'],'n_participants':'sum','se':'mean'}).round(4)
table.to_csv(os.path.join(RESULTS, 'tables', 'meta_analysis_table.csv'))
print("✓ HIM-15 analysis complete")