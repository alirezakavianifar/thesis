import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_decision_hierarchy(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    fig, ax = plt.subplots(figsize=(14.5, 11.2), dpi=300)
    ax.set_xlim(0, 20.0)
    ax.set_ylim(0, 15.5)
    ax.axis('off')

    # Color palette
    c_slate_dark = '#0F172A'
    c_slate_mid = '#334155'
    c_slate_muted = '#475569'

    c_blue_border = '#2563EB'
    c_blue_fill = '#EFF6FF'
    c_blue_title = '#1E3A8A'

    c_purple_border = '#7C3AED'
    c_purple_fill = '#F5F3FF'
    c_purple_title = '#4C1D95'

    c_emerald_border = '#059669'
    c_emerald_fill = '#ECFDF5'
    c_emerald_title = '#065F46'

    c_amber_border = '#D97706'
    c_amber_fill = '#FEF3C7'
    c_amber_title = '#78350F'

    c_rose_border = '#E11D48'
    c_rose_fill = '#FFF1F2'
    c_rose_title = '#881337'

    c_red_border = '#DC2626'
    c_red_fill = '#FEF2F2'
    c_red_title = '#991B1B'

    def draw_card(x, y, w, h, fill, border, r=0.18, lw=1.5):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=fill, edgecolor=border, linewidth=lw
        )
        ax.add_patch(box)

    # Title
    ax.text(10.0, 15.0, "RS-DRL+ Three-Stage Anytime Decision Hierarchy (CA-EPV Pattern)",
            ha='center', va='center', fontsize=13.5, fontweight='bold', color=c_slate_dark)

    # -------------------------------------------------------------
    # 0. Runtime State Telemetry
    # -------------------------------------------------------------
    draw_card(10.0, 13.8, 14.5, 1.3, c_blue_fill, c_blue_border)
    ax.text(10.0, 14.15, r"Runtime State Telemetry: $s_t = \langle cf, of \rangle \in \mathcal{S}$",
            ha='center', va='center', fontsize=9.6, fontweight='bold', color=c_blue_title)
    ax.text(10.0, 13.60, r"Triggered when any surrogate confidence falls below threshold: $\min_k M_k(s_t) < \tau_k$",
            ha='center', va='center', fontsize=8.2, color=c_slate_dark)

    # Arrow 0 -> Stage 1
    ax.annotate('', xy=(10.0, 12.85), xytext=(10.0, 13.15),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.3, headwidth=5.5, headlength=6.5))

    # -------------------------------------------------------------
    # Stage 1: RS-DRL+ Compiled Policy Proposal
    # -------------------------------------------------------------
    draw_card(10.0, 12.0, 14.5, 1.4, c_purple_fill, c_purple_border, lw=1.6)
    ax.text(10.0, 12.40, r"Stage 1: RS-DRL$^+$ Compiled Policy Proposal",
            ha='center', va='center', fontsize=10.0, fontweight='bold', color=c_purple_title)
    ax.text(10.0, 11.85, r"Single forward pass through neural network: $a_0 = \arg\max_{a \in \mathcal{A}} Q(s_t, a; \theta_{\mathrm{active}})$",
            ha='center', va='center', fontsize=8.5, color=c_slate_dark)

    # Latency badge Stage 1
    ax.text(16.5, 12.45, "0.485 ms", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#DC2626',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FEF2F2', edgecolor='#DC2626', lw=1.0))

    # Arrow Stage 1 -> Stage 2 Diamond
    ax.annotate('', xy=(10.0, 10.75), xytext=(10.0, 11.30),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.3, headwidth=5.5, headlength=6.5))

    # -------------------------------------------------------------
    # Stage 2: Margin & Stress Gate (Diamond)
    # -------------------------------------------------------------
    diamond_s2 = patches.Polygon([[10.0, 10.75], [14.0, 9.85], [10.0, 8.95], [6.0, 9.85]], closed=True,
                                 facecolor='#FFFFFF', edgecolor=c_blue_border, lw=1.8)
    ax.add_patch(diamond_s2)
    ax.text(10.0, 10.15, "Stage 2: Margin & Stress Gate",
            ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_blue_title)
    ax.text(10.0, 9.60, r"$\Delta_{\min}(s_t, a_0) \geq 0 \quad \wedge \quad \mathcal{E}(of) \leq \epsilon_{\mathrm{threshold}}$ ?",
            ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_slate_dark)

    # -------------------------------------------------------------
    # Right Branch: YES (Nominal Safe) -> Fast Path Execution
    # -------------------------------------------------------------
    ax.text(15.2, 10.15, "YES (Nominal Safe)", ha='left', va='center', fontsize=8.8, fontweight='bold', color='#059669')
    ax.plot([14.0, 16.5, 16.5], [9.85, 9.85, 8.70], color='#059669', lw=1.5)
    ax.annotate('', xy=(16.5, 8.70), xytext=(16.5, 8.85),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.3, headwidth=5.5, headlength=6.0))

    # Fast Path Card (Right Side)
    draw_card(16.5, 7.8, 4.4, 1.5, c_emerald_fill, c_emerald_border, lw=1.6)
    ax.text(16.5, 8.25, "Fast-Path Execution", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_emerald_title)
    ax.text(16.5, 7.75, r"Accept Nominal: $a^* = a_0$", ha='center', va='center', fontsize=8.6, fontweight='bold', color='#065F46')
    ax.text(16.5, 7.30, "No Search Latency Injected", ha='center', va='center', fontsize=7.4, color=c_slate_muted)
    ax.text(17.8, 8.25, "< 0.50 ms", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#059669',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#ECFDF5', edgecolor='#059669', lw=0.8))

    # -------------------------------------------------------------
    # Left Branch: NO (Threat / Margin Alert) -> Stage 3 (PG-ALR)
    # -------------------------------------------------------------
    ax.text(4.8, 10.15, "NO (Threat / Alert)", ha='right', va='center', fontsize=8.8, fontweight='bold', color='#DC2626')
    ax.plot([6.0, 4.0, 4.0], [9.85, 9.85, 8.65], color='#DC2626', lw=1.5)
    ax.annotate('', xy=(4.0, 8.65), xytext=(4.0, 8.80),
                arrowprops=dict(facecolor='#DC2626', edgecolor='#DC2626', width=1.3, headwidth=5.5, headlength=6.0))

    # Stage 3 Card
    draw_card(7.0, 7.8, 9.6, 1.5, c_amber_fill, c_amber_border, lw=1.6)
    ax.text(7.0, 8.25, "Stage 3: Policy-Guided Local Refinement (PG-ALR)",
            ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_amber_title)
    ax.text(7.0, 7.78, r"Evaluates 1-Hop Neighborhood $\mathcal{N}(a_0)$ along Top-$m$ SHAP Features",
            ha='center', va='center', fontsize=8.0, color=c_slate_dark)
    ax.text(7.0, 7.35, r"Proposition 1 Bound: $|\mathcal{N}(a_0)| \leq 2m + 1$ (Evaluates only 4–5 micro-actions)",
            ha='center', va='center', fontsize=7.6, fontweight='bold', color='#B45309')
    ax.text(11.0, 8.35, "1.5–3.5 ms", ha='center', va='center', fontsize=7.4, fontweight='bold', color='#B45309',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#FEF3C7', edgecolor='#D97706', lw=0.8))

    # Arrow Stage 3 -> Compliance Check Diamond
    ax.annotate('', xy=(7.0, 6.45), xytext=(7.0, 7.05),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.3, headwidth=5.5, headlength=6.5))

    # -------------------------------------------------------------
    # Compliance Check Diamond (Stage 3 Verification)
    # -------------------------------------------------------------
    diamond_comp = patches.Polygon([[7.0, 6.45], [10.5, 5.65], [7.0, 4.85], [3.5, 5.65]], closed=True,
                                   facecolor='#FFFFFF', edgecolor=c_amber_border, lw=1.6)
    ax.add_patch(diamond_comp)
    ax.text(7.0, 5.90, "Surrogate Compliance Check",
            ha='center', va='center', fontsize=9.0, fontweight='bold', color=c_amber_title)
    ax.text(7.0, 5.40, r"Does any $a \in \mathcal{N}(a_0)$ satisfy $\min_k (M_k(s, a) - \tau_k) \geq 0$ ?",
            ha='center', va='center', fontsize=8.0, fontweight='bold', color=c_slate_dark)

    # Branches from Compliance Diamond
    # YES -> Optimal Safe Action (Left)
    ax.text(2.6, 5.85, "YES", ha='right', va='center', fontsize=8.8, fontweight='bold', color='#059669')
    ax.plot([3.5, 2.2, 2.2], [5.65, 5.65, 4.25], color='#059669', lw=1.4)
    ax.annotate('', xy=(2.2, 4.25), xytext=(2.2, 4.40),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.3, headwidth=5.5, headlength=6.0))

    # Card: Select Optimal Refined Action
    draw_card(3.8, 3.4, 5.2, 1.4, c_emerald_fill, c_emerald_border, lw=1.5)
    ax.text(3.8, 3.80, "Select Optimal Safe Action", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_emerald_title)
    ax.text(3.8, 3.25, r"$a^* = \arg\max_{a \in \mathcal{N}_{\mathrm{sat}}(s, a_0)} \mathcal{J}(s, a)$",
            ha='center', va='center', fontsize=8.8, fontweight='bold', color='#065F46')

    # NO -> Margin-Maximizing Fallback (Right)
    ax.text(11.4, 5.85, "NO", ha='left', va='center', fontsize=8.8, fontweight='bold', color='#DC2626')
    ax.plot([10.5, 10.5], [5.65, 4.25], color='#DC2626', lw=1.4)
    ax.annotate('', xy=(10.5, 4.25), xytext=(10.5, 4.40),
                arrowprops=dict(facecolor='#DC2626', edgecolor='#DC2626', width=1.3, headwidth=5.5, headlength=6.0))

    # Card: Margin-Maximizing Fallback
    draw_card(10.5, 3.4, 6.0, 1.4, c_rose_fill, c_rose_border, lw=1.5)
    ax.text(10.5, 3.80, "Margin-Maximizing Fallback", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_rose_title)
    ax.text(10.5, 3.25, r"$a^* = \arg\max_{a \in \mathcal{N}(a_0)} \sum_{k=0}^{K-1} (M_k(s, a) - \tau_k)$",
            ha='center', va='center', fontsize=8.0, fontweight='bold', color='#991B1B')

    # -------------------------------------------------------------
    # Convergence into Bottom Executor
    # -------------------------------------------------------------
    # From Left (Safe Refined Action): x=3.8, y=2.7 -> down to y=2.1
    ax.plot([3.8, 3.8], [2.7, 2.1], color='#059669', lw=1.4)
    # From Center (Fallback Action): x=10.5, y=2.7 -> down to y=2.1
    ax.plot([10.5, 10.5], [2.7, 2.1], color='#DC2626', lw=1.4)
    # From Right (Fast-Path): x=16.5, y=7.05 -> down to y=2.1
    ax.plot([16.5, 16.5], [7.05, 2.1], color='#059669', lw=1.4)

    # Continuous horizontal convergence bar at y=2.1
    ax.plot([3.8, 16.5], [2.1, 2.1], color=c_slate_mid, lw=1.5)

    # Common entry arrow into Executor
    ax.annotate('', xy=(10.0, 1.65), xytext=(10.0, 2.1),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.4, headwidth=6.0, headlength=6.5))

    # Executor Card (Bottom)
    draw_card(10.0, 0.95, 16.5, 1.3, c_emerald_fill, c_emerald_border, lw=1.8)
    ax.text(10.0, 1.32, r"EXECUTOR: DISPATCH VERIFIED ADAPTATION $a^* \in \mathcal{A}$ TO ACTUATORS",
            ha='center', va='center', fontsize=9.8, fontweight='bold', color=c_emerald_title)
    ax.text(10.0, 0.78, "Applies Verified Control Parameters $\\cdot$ Total Decision Time Strictly Constrained ($< 3.5\\,\\mathrm{ms} \\ll 20\\text{--}50\\,\\mathrm{ms}$)",
            ha='center', va='center', fontsize=8.2, color=c_slate_dark)
    ax.text(17.2, 1.35, "Hard Real-Time", ha='center', va='center', fontsize=7.6, fontweight='bold', color='#059669',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#ECFDF5', edgecolor='#059669', lw=1.0))

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade decision hierarchy flowchart saved to {output_path}")

if __name__ == '__main__':
    create_decision_hierarchy('figures/fig_decision_hierarchy_flowchart.png')
