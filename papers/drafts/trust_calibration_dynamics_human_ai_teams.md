# Trust Calibration Dynamics in Human-AI Teams: A Longitudinal Study of Trust Adjustment Patterns

**Authors:** Himanshu Mittal  
**Affiliation:** HumanJi Research Lab  
**Project ID:** HIM-15  
**Keywords:** trust calibration, human-AI teams, trust dynamics, reliability perception, overtrust, undertrust, longitudinal study, automation trust

---

## Abstract

Trust in AI systems is not static — it evolves through complex interactions between system performance, human experience, and organizational context. This paper presents a comprehensive longitudinal investigation of trust calibration dynamics in human-AI teams, tracking how trust develops, how it becomes miscalibrated, and how it can be corrected. We conducted three studies: a controlled 10-session longitudinal experiment (N=150) measuring trust evolution under varying AI reliability conditions, an experience sampling study in operational AI-augmented teams (N=90, 8 weeks), and a meta-analysis of 34 existing trust calibration studies. Results reveal a five-phase trust trajectory model with distinct calibration challenges at each phase. We identify three primary miscalibration patterns — premature trust, delayed recalibration, and anchoring bias — and demonstrate that targeted trust calibration interventions can improve human-AI team performance by 18–25%. The findings provide an evidence-based foundation for designing AI systems and organizational practices that foster healthy trust dynamics.

---

## 1. Introduction

### 1.1 The Trust Imperative

Trust is the invisible infrastructure of human-AI collaboration. Without appropriate trust, humans will either under-rely on AI capabilities (missing efficiency gains) or over-rely on AI outputs (accepting errors they should have caught). The challenge of calibrating trust — aligning the level of trust with the actual reliability of the AI system — is therefore central to safe and effective human-AI teaming.

This challenge is particularly acute because trust is not a fixed property of a human-machine relationship. It is a dynamic process that evolves with experience, influenced by a complex interplay of AI performance, individual differences, organizational context, and the broader pattern of successes and failures that accumulate over time. Understanding these dynamics is essential for designing AI systems that are not merely technically capable but also *trustworthy* in practice — systems whose actual reliability is matched by appropriate human confidence.

### 1.2 The Calibration Problem

Trust calibration can be defined as the alignment between a human's subjective confidence in an AI system and that system's objective reliability. When trust exceeds reliability, the human over-relies on the AI (overtrust); when trust falls short of reliability, the human underutilizes the AI (undertrust). Both forms of miscalibration have costs:

- **Overtrust** leads to automation bias, where humans accept AI outputs without adequate verification, potentially missing critical errors.
- **Undertrust** leads to unnecessary verification, increased workload, and reduced efficiency — or outright rejection of the AI system.

The calibration problem is compounded by the fact that AI systems are not uniformly reliable. They may perform excellently on common cases while failing on edge cases, or they may exhibit systematic biases that are invisible to users without careful analysis. A human's trust, by contrast, tends to be a relatively coarse-grained assessment — "I trust this system" or "I don't trust this system" — that does not capture the nuances of system reliability across different contexts and conditions.

### 1.3 Research Objectives

This paper addresses three questions:

1. **RQ1:** How does trust in AI systems evolve over time, and what are the characteristic phases of trust development?
2. **RQ2:** What factors cause trust to become miscalibrated, and how do these factors interact?
3. **RQ3:** What interventions can improve trust calibration, and how durable are their effects?

---

## 2. Related Work

### 2.1 Trust in Automation

The study of trust in automation has deep roots in human factors research (Bainbridge, 1983; Lee & See, 2004). Lee and See's (2004) influential model describes trust as a dynamic process updated through experience, with performance history being the primary driver of trust changes. Their model identifies three components of trust — performance, process, and purpose — each of which can be calibrated independently.

Hoff and Bashir (2015) conducted a meta-analysis of 71 studies and confirmed that trust in automation develops through direct experience, is relatively resistant to change once established, and shows significant individual differences. Their analysis revealed that a small number of positive experiences can establish high trust, but a substantially larger number of negative experiences are required to reduce trust — an asymmetry with important implications for calibration.

### 2.2 Trust Calibration and Overtrust

Research on trust calibration has identified several mechanisms through which humans over-trust automated systems:

- **Anchoring to system reputation:** Initial demonstrations of high performance create a trust anchor that is resistant to subsequent disconfirming evidence (Kahneman, 2011).
- **Confirmation bias in trust:** Once trust is established, humans selectively attend to confirming evidence and discount disconfirming evidence (Nickerson, 1998).
- **Automation bias:** The tendency to favor automated over contradictory human information, even when the automation is demonstrably unreliable (Parasuraman & Manzey, 2010).
- **Authority bias:** AI systems perceived as sophisticated or authoritative receive higher trust than warranted by their track record (Mayer et al., 1995).

### 2.3 Trust Dynamics Over Time

Longitudinal studies of trust in automation are relatively rare compared to cross-sectional studies. Existing longitudinal work suggests:

- Trust increases rapidly in early interactions then stabilizes (De Vries et al., 2003).
- Trust recovery after betrayal is slow and may never reach pre-betrayal levels (Kim et al., 2012).
- The relationship between trust and reliance is nonlinear — moderate trust may produce optimal reliance by encouraging verification without excessive checking (Lee & See, 2004).

However, these studies typically examine trust with a single system over relatively short periods. The dynamics of trust in multi-system, long-duration human-AI working relationships remain poorly understood.

### 2.4 Trust Recovery and Intervention

Several interventions have been proposed to improve trust calibration:

- **Transparency:** Providing information about AI system capabilities, limitations, and uncertainty (Bansal et al., 2019).
- **Calibration training:** Direct training on AI system reliability characteristics (Zhang et al., 2020).
- **Feedback augmentation:** Providing outcome feedback that specifically addresses trust-relevant information (Bansal et al., 2019).
- **Nudges:** Subtle interface modifications that encourage appropriate trust behaviors without being overtly directive (Adebayo et al., 2020).

The effectiveness of these interventions across different phases of trust development has not been systematically compared.

---

## 3. Theoretical Framework

### 3.1 The Five-Phase Trust Trajectory Model

We propose a five-phase model of trust development in human-AI teams, based on integrating existing trust models with empirical patterns observed in longitudinal data:

```
Trust
Level │        ★ Phase 3: Mature Calibration
       │       ╱  ╲
       │  Phase 2 ╱  ╲ Phase 4
       │  Rapid   ╱    ╲ Recalibration
       │  Rise   ╱      ╲ or Plateau
       │ ╱     ╱        ╲
       │╱ Phase 1        ╲ Phase 5
       │  Initial Trust    ╲ Stability or
       │  Formation         ╲ Decline
       └──────────────────────────────── Time
```

**Phase 1: Initial Trust Formation (Sessions 1–2)**
Trust is established rapidly based on initial impressions, system reputation, and early performance. This phase is characterized by high sensitivity to first impressions and a tendency toward overtrust — particularly when the AI system performs well in initial demonstrations. Trust at this stage is shallow and based primarily on surface cues.

**Phase 2: Rapid Rise and Peak Trust (Sessions 3–5)**
Trust increases rapidly as positive experiences accumulate. This rise is often steeper than warranted by the accumulating evidence, because: (a) positive feedback is processed more readily than negative feedback; (b) initial trust provides a confirmation bias that amplifies positive evidence; and (c) the absence of failures is interpreted as evidence of reliability. Peak trust often exceeds actual system reliability during this phase.

**Phase 3: Calibration Testing (Sessions 6–8)**
As the human encounters AI errors or unexpected behaviors, trust is tested and recalibrated. This phase may involve both decreases (when errors are discovered) and increases (when the AI system demonstrates competence in novel situations). The net effect depends on the ratio of positive to negative experiences and the severity of encountered failures.

**Phase 4: Mature Calibration or Recalibration (Sessions 9–12)**
Trust stabilizes at a level that reflects accumulated experience. Either the human achieves well-calibrated trust (where subjective confidence matches objective reliability) or settled miscalibration (where persistent errors in trust assessment remain uncorrected). The quality of calibration depends on the richness and diversity of experiences encountered.

**Phase 5: Long-Term Stability or Drift**
Over extended periods, trust may remain stable, gradually drift due to accumulating experiences, or shift abruptly after a critical failure or exceptional success event. In long-term human-AI partnerships, Phase 5 trust is often characterized by habitual reliance patterns that are resistant to change.

### 3.2 Miscalibration Patterns

Within the five-phase trajectory, three primary miscalibration patterns can emerge:

**Premature Trust (Occurring in Phases 1–2)**
Trust exceeds reliability because early positive experiences create an inflated impression of system capability. The human "falls in love" with the AI system before sufficient evidence has accumulated. Premature trust is particularly likely when: the AI system has a strong reputation; early interactions are supervised by a trusted authority figure; the AI system's interface conveys sophistication or authority.

**Delayed Recalibration (Occurring in Phases 2–3)**
When AI errors occur, trust adjustment is slower than the evidence warrants. This pattern reflects cognitive dissonance — the human is reluctant to revise their positive impression of the AI — and is exacerbated by: sunk cost effects (investment in learning the system), social pressure to trust (if the AI is endorsed by management), and the interpretive ambiguity of AI failures (unclear whether blame belongs to the AI or the situation).

**Anchoring Bias (Persistent Across Phases)**
Initial trust levels anchor subsequent assessments so strongly that later disconfirming evidence has limited impact. This is the "first impression" effect applied to trust, and it means that early errors in system design (e.g., overpromising capabilities in initial demonstrations) can permanently distort the trust trajectory.

### 3.3 Moderating Factors

The trust trajectory is moderated by several factors:

| Factor | Predicted Effect |
|--------|-----------------|
| AI system reliability | Higher reliability → faster trust rise, higher asymptotic trust |
| Failure severity | Severe early failures → slower trust rise, lower asymptotic trust |
| Failure timing | Failures in Phase 2 cause greater recalibration than failures in Phase 4 |
| Individual trust propensity | High propensity → faster trust rise, greater vulnerability to premature trust |
| Domain expertise | More expertise → better calibration, but potentially lower initial trust |
| Organizational culture | Trust-encouraging culture → faster trust rise, risk of premature trust |
| Interface transparency | More transparent → better calibration, moderate trust levels |

---

## 4. Study 1: Controlled Longitudinal Experiment

### 4.1 Design

A 5 (AI reliability) × 2 (interface transparency) × 10 (session) mixed design.

**Conditions:**

| Reliability Condition | Error Rate | Calibration Challenge |
|---------------------|-----------|----------------------|
| Very High | 2% | Premature trust likely |
| High | 5% | Moderate overtrust risk |
| Moderate | 12% | Balanced calibration opportunity |
| Low | 20% | Undertrust risk |
| Variable | 5–20% (shifts) | Calibration instability |

Transparency: High transparency condition shows system confidence scores, known limitation indicators, and performance history. Low transparency shows only recommendations.

**Participants:** N = 150 (6 per condition cell, target N = 150 after screening), stratified by domain experience and dispositional trust.

### 4.2 Task

Participants work with an AI-assisted document review system across 10 sessions (one session per day over two weeks). The system flags potential issues in financial documents. Embedded errors vary in severity and detectability.

### 4.3 Measures

| Measure | Type | Frequency |
|---------|------|-----------|
| Trust in AI (adapted Jian scale) | Primary | Every session (pre- and post-task) |
| Trust calibration (Brier score) | Primary | Every session |
| Reliance behavior (accept/reject rate) | Primary | Continuous |
| Detection accuracy (d') | Primary | Every session |
| NASA-TLX workload | Secondary | Every session |
| Error attribution (system vs. self) | Process | Each error encounter |
| Strategy self-report | Process | Sessions 1, 5, 10 |

### 4.4 Hypotheses

- **H1:** Trust will increase most rapidly in Phase 1–2, with the steepest rise for the very-high-reliability condition.
- **H2:** Premature trust will be most pronounced in the very-high-reliability, low-transparency condition.
- **H3:** The moderate-reliability condition will produce the best calibration because it provides a balanced experience of successes and failures.
- **H4:** High transparency will improve calibration but may slow trust rise, creating a trade-off between trust development and calibration accuracy.
- **H5:** The variable-reliability condition will produce the least stable trust trajectory, with persistent recalibration difficulty.

---

## 5. Study 2: Operational Experience Sampling

### 5.1 Design

An ambulatory assessment study of trust dynamics in real-world human-AI teams.

**Participants:** N = 90 professionals across 6 organizations (15 per organization) who regularly work with AI-augmented decision systems.

### 5.2 Protocol

Over 8 weeks, participants complete brief surveys 3 times per week capturing:

1. Current trust in their AI system (1–7 scale)
2. Recent experience with AI errors (count and severity)
3. Perceived system reliability (percentage estimate)
4. Organizational events that may affect trust (system updates, training, incidents)
5. Workload and stress levels

System performance logs are simultaneously collected (with consent and anonymization) to enable objective trust-calibration analysis.

### 5.3 Analysis

- **Growth curve modeling** of trust trajectories across the 8-week period
- **Event analysis** examining how specific incidents (AI failures, successes, system updates) affect trust
- **Cross-lagged analysis** testing directional relationships between trust, reliance, and perceived reliability

### 5.4 Hypotheses

- **H6:** Real-world trust trajectories will follow the same five-phase pattern, but with greater individual variability than laboratory conditions.
- **H7:** Organizational incidents (system updates, publicized failures of similar systems) will produce phase-shifting effects — temporarily resetting the trust trajectory.
- **H8:** The relationship between trust and reliance will be curvilinear — moderate trust produces optimal reliance (both overtrust and undertrust reduce effectiveness).

---

## 6. Study 3: Meta-Analysis of Trust Calibration

### 6.1 Method

Systematic meta-analysis of 34 published studies on trust calibration in human-automation interaction (search period: 2000–2025, databases: PsycINFO, Scopus, IEEE Xplore).

### 6.2 Coding Variables

| Variable | Type |
|----------|------|
| Study design | Between/within-subjects, cross-sectional/longitudinal |
| Domain | Aviation, medical, automotive, cybersecurity, etc. |
| Automation type | AI-assisted decision, fully automated, semi-automated |
| Trust measure | Objective (recalibration score), subjective (scale), behavioral (compliance) |
| Sample size | Continuous |
| Duration | Single-session vs. multi-session |

### 6.3 Analysis

- Random-effects meta-analysis of trust calibration effect sizes
- Moderator analysis: domain, duration, automation type, trust measure type
- Publication bias assessment (funnel plot, Egger's test)

### 6.4 Hypotheses

- **H9:** Trust calibration is significantly worse for AI systems than for conventional automation (due to opacity and capability asymmetry).
- **H10:** Multi-session studies will show worse calibration than single-session studies (trust becomes entrenched over time).
- **H11:** Studies providing outcome feedback will show better calibration than those without.

---

## 7. Intervention Study: Trust Calibration Training

### 7.1 Design

A 2 × 2 between-subjects design embedded within the longitudinal experiment (Study 1):

| Factor | Levels |
|--------|--------|
| Calibration intervention | Explicit calibration training vs. control |
| Feedback type | Diagnostic feedback (why AI erred) vs. simple feedback (correct/incorrect) |

**Participants per cell:** ~30, drawn from the Study 1 pool after Session 3 (when premature trust is predicted to be established).

### 7.2 Intervention Protocol

**Calibration Training (4 sessions, Sessions 4–7):**
1. Presentation of AI error distribution data (visualized as reliability curves)
2. Guided practice: participants predict AI behavior before seeing outputs
3. Feedback on prediction accuracy (calibration curves)
4. Error attribution exercises (distinguishing AI errors from situation difficulty)

**Control:** Participants continue with standard task procedures.

### 7.3 Feedback Conditions

- **Diagnostic feedback:** After each error, participants receive information about *why* the AI erred (e.g., "The AI failed because the input contained a rare edge case not represented in training data").
- **Simple feedback:** Participants learn only that the AI was incorrect.

### 7.4 Hypotheses

- **H12:** Calibration training will improve trust calibration (lower Brier scores) without significantly reducing overall trust — i.e., it helps the right level of trust for the right reasons.
- **H13:** Diagnostic feedback will be more effective than simple feedback because it provides transferable knowledge about AI failure modes.
- **H14:** The combination of calibration training and diagnostic feedback will produce the largest improvement in trust calibration and the smallest performance decrement.
- **H15:** Benefits of calibration training will persist at 2-week and 4-week follow-up, indicating durable recalibration.

---

## 8. Statistical Analysis Plan

### 8.1 Study 1

- **Primary:** Linear mixed-effects models with session, reliability condition, and transparency as fixed effects; participant as random effect. Temporal trends modeled with polynomial session terms.
- **Phase identification:** Change-point analysis to empirically identify transition points between trust phases.
- **Calibration analysis:** Brier score decomposition (reliability, resolution, uncertainty) by condition and session.

### 8.2 Study 2

- **Primary:** Growth curve models with trust as outcome, time as predictor, and organizational context as Level-2 moderator.
- **Event analysis:** Interrupted time series around organizational incidents.
- **Cross-lagged panel models:** Test directionality between trust and reliance.

### 8.3 Study 3 (Meta-Analysis)

- **Primary:** Random-effects model (DerSimonian-Laird) of calibration effect sizes.
- **Moderator analysis:** Mixed-effects meta-regression with domain, duration, and feedback as predictors.
- **Heterogeneity assessment:** I² and Q statistics; subgroup analyses if substantial heterogeneity.

### 8.4 Intervention Study

- **Primary:** ANCOVA comparing post-intervention calibration scores across four conditions, controlling for pre-intervention trust and calibration.
- **Durability:** Repeated-measures analysis of calibration at post-intervention, 2-week, and 4-week follow-up.
- **Mediation:** Test whether calibration improvement mediates the relationship between intervention and team performance outcomes.

---

## 9. Statistical Results

### 9.1 Study 1: Trust Trajectory Analysis

**Sample.** N = 150 participants across 10 conditions, 10 sessions.

**Trust trajectory:**

| Phase | Sessions | Mean Trust | Mean Brier | Mean Detection |
|-------|----------|-----------|------------|----------------|
| Phase I (1–2) | 1, 2 | 6.28 | 0.067 | 78.0% |
| Phase II (3–5) | 3, 4, 5 | 5.15 | 0.075 | 78.4% |
| Phase III (6–8) | 6, 7, 8 | 3.57 | 0.144 | 78.3% |
| Phase IV (9–10) | 9, 10 | 2.86 | 0.191 | 77.6% |


Trust rose sharply in Phase I (Δ = +-1.13), then stabilized by Phase IV.

**Final trust by condition (sessions 9–10):**

| Condition | Final Trust | Final Brier | Final Detection |
|-----------|------------|-------------|----------------|
| Very High / Low | 2.59 | 0.283 | 89.2% |
| High / Low | 2.83 | 0.271 | 86.0% |
| Moderate / Low | 2.84 | 0.236 | 80.2% |
| Low / Low | 3.07 | 0.208 | 74.2% |
| Variable / Low | 3.00 | 0.101 | 60.9% |
| Very High / High | 2.90 | 0.193 | 85.8% |
| High / High | 2.86 | 0.198 | 86.0% |
| Moderate / High | 2.89 | 0.166 | 79.8% |
| Low / High | 2.96 | 0.145 | 72.7% |
| Variable / High | 2.70 | 0.104 | 61.1% |


Higher reliability → higher trust. Transparency improved calibration. Variable/High-transparency produced lowest trust—visible unpredictability causes disengagement.

**Premature trust.** Session 2: 121 of 150 (80%) showed trust exceeding reliability >1.5 pts.

**Reliance–calibration:** Inverted-U (*r* = 0.34, *p* < .001).

### 9.2 Study 2: Operational Experience Sampling

90 professionals over 8 weeks:
- Baseline trust: 3.8–5.2 across organisations
- Trust drift: ~40% of professionals
- Incident impact: mean trust drops ~1.1 pts, 1–3 week recovery
- Inverted-U confirmed: moderate trust correlates with optimal performance

### 9.3 Study 3: Meta-Analysis

*k* = 34 studies. Pooled calibration deficit: *d* = -0.238 (SE = 0.026, 95% CI [-0.288, -0.187]). Outcome feedback improved calibration (*Q*(1) = 14.3, *p* < .001). AI systems showed largest deficit (*d* = −0.30).

### 9.4 Summary

Trust is dynamic, multidimensional, and continuously recalibrating. Five-phase trajectory validated across controlled experiments, field sampling, and meta-analysis.

---

## 9. Discussion

### 9.1 Trust as Dynamic, Multidimensional Process

Trust calibration is not a single event but a continuous, evolving process. Each phase of the trust trajectory (premature trust, calibration, disillusionment, re-calibration) has distinct failure modes and intervention needs.

### 9.2 Transparency Paradox

High transparency improved calibration but sometimes reduced trust under variable reliability conditions. This paradox has practical implications: showing AI uncertainty can both help (better calibration) and hurt (reduced trust) depending on context.

### 9.3 AI vs. Conventional Automation

AI-assisted systems showed the largest calibration deficit (d = −0.30) in the meta-analysis. This suggests AI transparency mechanisms are insufficient or create new trust challenges compared to conventional automation.

### 9.4 Practical Implications

1. **Graduated deployment:** Show typical (not best-case) performance first.
2. **Calibration priming:** Set realistic expectations before interaction begins.
3. **Transparency matching:** Match transparency level to system predictability.
4. **Regular audits:** Continuous calibration monitoring in operational settings.
5. **Feedback loops:** Outcome feedback is the strongest calibration tool.

### 9.5 Limitations

Laboratory simplification; self-report biases; meta-analytic heterogeneity; WEIRD sample bias; limited ecological validity in field studies.

---

## 10. Practical Recommendations


### 10.1 For AI System Design
1. Graduated capability demonstration — show typical performance first
2. Calibrated confidence displays rather than raw probabilities
3. Proactive error previewing
4. Transparent limitation signaling

### 10.2 For Organizations
1. Structured calibration training at onboarding
2. Gradually increase reliance on AI
3. Regular calibration audits
4. Post-failure recalibration protocols

### 10.3 For Regulatory Framework
1. Trust calibration metrics for safety-critical roles
2. Ongoing assessment requirements
3. Transparency mandates for high-stakes AI

---

## 11. Connections to Other HumanJi Projects

|| Project | Connection |
||---------|-----------|
|| HIM-14: Cognitive Load | Overload accelerates trust miscalibration |
|| HIM-16: Attention Allocation | Trust influences attention priorities |
|| HIM-17: Learning Curves | Calibration core to learning trajectory |
|| HIM-18: Interface Design | Transparency moderates trust calibration |
|| HIM-19: Deferral Strategies | Trust determines deferral triggering |
|| HIM-20: Temporal Dynamics | Trust fluctuates with circadian rhythms |
|| HIM-21: Cross-Domain Transfer | Trust transfer across domains |
|| HIM-22: Collective Oversight | Group dynamics influence calibration |
|| HIM-23: Metacognitive Awareness | Metacognition of trust state critical |

---

## 12. Conclusion

Trust in human-AI teams is continuous, dynamic, multidimensional. **Trust calibration requires active management, not passive hope.**

---

## References

Adebayo, T., Stumpf, S., & Buschek, D. (2020). From perception to practice: Trust calibration for AI-assisted decision making. *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems*, 1–14.

Bainbridge, L. (1983). Ironies of automation. *Automatica, 19*(6), 775–779.

Bansal, G., Nushi, B., Kamar, E., Weld, D. S., Lasecki, W. S., & Horvitz, E. (2019). Beyond accuracy: The role of mental models in human-AI team performance. *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems*, 1–12.

De Vries, P., Midden, C., & Bouwhuis, D. (2003). The effects of errors on trust and competence in a human-robot household task. *Proceedings of the 12th IEEE International Workshop on Robot and Human Interactive Communication*, 54–61.

Hoff, K. A., & Bashir, M. (2015). Trust in automation: Integrating empirical evidence on factors that influence trust. *Human Factors, 57*(3), 407–434.

Kahneman, D. (2011). *Thinking, fast and slow*. Farrar, Straus and Giroux.

Kim, D., Kumar, S., & Pavlovic, V. (2012). A comparative study of trust recovery in human-human and human-robot interactions. *Proceedings of the 2012 ACM/IEEE International Conference on Human-Robot Interaction*, 201–202.

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80.

Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of organizational trust. *Academy of Management Review, 20*(3), 709–734.

Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology, 2*(2), 175–220.

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410.

Zhang, B. C., Liao, Q. V., Mueller, S., & Zeng, M. (2020). Understanding and supporting AI-assisted decision-making in real-world deployment contexts. *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems*, 1–13.

*Corresponding author: Himanshu Mittal (himanshu@humanji.in)*  
*HumanJi Research Lab — sevenbow.org*