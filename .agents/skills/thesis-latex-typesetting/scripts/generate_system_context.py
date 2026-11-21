import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def create_system_context(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    fig, ax = plt.subplots(figsize=(14.2, 10.2), dpi=300)
    ax.set_xlim(0, 20.0)
    ax.set_ylim(0.5, 14.6)
    ax.axis('off')

    # Color palette - Refined Academic Style (IEEE / ACM / NeurIPS)
    c_slate_dark = '#0F172A'
    c_slate_mid = '#334155'
    c_slate_muted = '#475569'
    c_slate_light = '#F8FAFC'
    c_border_gray = '#CBD5E1'

    c_blue_border = '#2563EB'
    c_blue_fill = '#EFF6FF'
    c_blue_title = '#1E3A8A'

    c_emerald_border = '#059669'
    c_emerald_fill = '#ECFDF5'
    c_emerald_title = '#065F46'

    c_amber_border = '#D97706'
    c_amber_fill = '#FEF3C7'
    c_amber_title = '#78350F'

    c_rose_border = '#E11D48'
    c_rose_fill = '#FFF1F2'
    c_rose_title = '#881337'

    c_indigo_border = '#4F46E5'
    c_indigo_fill = '#EEF2FF'
    c_indigo_title = '#312E81'

    def draw_card(x, y, w, h, fill, border, r=0.22, lw=1.5):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=fill, edgecolor=border, linewidth=lw
        )
        ax.add_patch(box)

    # -------------------------------------------------------------
    # 0. Title Banner
    # -------------------------------------------------------------
    ax.text(10.0, 14.1, "RS-DRL System Context & Architectural Boundaries",
            ha='center', va='center', fontsize=14.5, fontweight='bold', color=c_slate_dark)

    # -------------------------------------------------------------
    # 1. Managed System (Top-Left to Mid-Right)
    # Span: x in [1.2, 13.2] (center 7.2, width 12.0, height 1.9, center y=12.5)
    # -------------------------------------------------------------
    draw_card(7.2, 12.5, 12.0, 1.9, c_indigo_fill, c_indigo_border, r=0.25, lw=1.6)
    ax.text(7.2, 13.0, "Managed Autonomous System", ha='center', va='center',
            fontsize=12.2, fontweight='bold', color=c_indigo_title)
    ax.text(7.2, 12.45, "Target Software / Cyber-Physical Infrastructure (Controllable Parameters & Probes)",
            ha='center', va='center', fontsize=8.8, color=c_slate_muted)
    
    # Internal port badges inside Managed System
    # Left port: Sensory Probes (Centered at x=3.8, width=4.2 -> spans [1.7, 5.9])
    draw_card(3.8, 11.85, 4.2, 0.44, '#E0E7FF', c_indigo_border, r=0.12, lw=1.0)
    ax.text(3.8, 11.85, "Sensory Probes: State $s_t = (cf_t, of_t)$", ha='center', va='center',
            fontsize=7.4, fontweight='bold', color=c_indigo_title)
    
    # Right port: Actuators (Centered at x=10.6, width=4.2 -> spans [8.5, 12.7], margin to 13.2 is 0.5)
    # Text is "Actuators: Reconfiguration ($a^*$)" which fits with generous padding inside 4.2 units!
    draw_card(10.6, 11.85, 4.2, 0.44, '#DCFCE7', c_emerald_border, r=0.12, lw=1.0)
    ax.text(10.6, 11.85, "Actuators: Reconfiguration Controls ($a^*$)", ha='center', va='center',
            fontsize=7.0, fontweight='bold', color=c_emerald_title)

    # -------------------------------------------------------------
    # 2. Operational Environment (Top-Right)
    # Span: x in [15.6, 19.4] (center 17.5, width 3.8, height 1.9, center y=12.5)
    # -------------------------------------------------------------
    draw_card(17.5, 12.5, 3.8, 1.9, c_rose_fill, c_rose_border, r=0.25, lw=1.6)
    ax.text(17.5, 13.0, "Operational Environment", ha='center', va='center',
            fontsize=11.0, fontweight='bold', color=c_rose_title)
    ax.text(17.5, 12.35, "Stochastic Disturbances,\nDynamic Context ($of$)",
            ha='center', va='center', fontsize=8.4, color=c_slate_muted, linespacing=1.2)

    # Gap between boxes is [13.2, 15.6] -> 2.4 units wide!
    # Arrow: Environment -> Managed System (Disturbances & Context)
    ax.annotate('', xy=(13.2, 12.5), xytext=(15.6, 12.5),
                arrowprops=dict(facecolor=c_rose_border, edgecolor=c_rose_border, width=1.4, headwidth=6.0, headlength=7.0))
    # Dedicated Pill Badge for Disturbance Label (Centered at 14.4, width 2.0 -> spans [13.4, 15.4] cleanly)
    draw_card(14.4, 13.15, 2.0, 0.48, '#FFF1F2', c_rose_border, r=0.10, lw=0.9)
    ax.text(14.4, 13.15, "Stochastic\nDisturbances", ha='center', va='center',
            fontsize=7.4, fontweight='bold', color=c_rose_title, linespacing=1.1)

    # -------------------------------------------------------------
    # 3. Autonomic Controller Boundary (MAPE-K Loop Container)
    # -------------------------------------------------------------
    box_controller = patches.FancyBboxPatch(
        (1.2, 1.2), 18.0, 9.2,
        boxstyle="round,pad=0,rounding_size=0.35",
        facecolor='#F8FAFC', edgecolor=c_border_gray, linewidth=2.0, linestyle='--'
    )
    ax.add_patch(box_controller)

    # Dedicated Header Badge for Controller
    # Positioned at (7.4, 10.4), width=5.4 -> spans x in [4.7, 10.1]
    # Clean clearance: Sensory arrow is at x=3.8 (gap=0.9), Actuation arrow is at x=10.6 (gap=0.5)
    draw_card(7.4, 10.4, 5.4, 0.52, '#F1F5F9', c_border_gray, r=0.15, lw=1.3)
    ax.text(7.4, 10.4, "AUTONOMIC CONTROLLER (MAPE-K LOOP)", ha='center', va='center',
            fontsize=9.0, fontweight='bold', color=c_slate_mid)

    # -------------------------------------------------------------
    # MAPE-K Elements Inside Controller
    # -------------------------------------------------------------
    # A. Monitor (Top-Left of Controller)
    draw_card(3.8, 8.4, 4.4, 1.9, c_blue_fill, c_blue_border, lw=1.5)
    ax.text(3.8, 8.9, "1. MONITOR", ha='center', va='center', fontsize=11.0, fontweight='bold', color=c_blue_title)
    ax.text(3.8, 8.25, "Telemetry Ingestion &\nState Vector Construction $s_t$",
            ha='center', va='center', fontsize=8.8, color=c_slate_dark)

    # B. Analyze (Bottom-Left of Controller)
    draw_card(3.8, 4.5, 4.4, 1.9, c_blue_fill, c_blue_border, lw=1.5)
    ax.text(3.8, 5.0, "2. ANALYZE", ha='center', va='center', fontsize=11.0, fontweight='bold', color=c_blue_title)
    ax.text(3.8, 4.35, "SLA / QoS Compliance Evaluation &\nAdaptation Symptom Detection",
            ha='center', va='center', fontsize=8.6, color=c_slate_dark)

    # C. Shared Knowledge Base (Center)
    draw_card(10.2, 6.4, 5.4, 3.8, c_amber_fill, c_amber_border, r=0.28, lw=1.6)
    ax.text(10.2, 7.9, "SHARED KNOWLEDGE", ha='center', va='center', fontsize=11.5, fontweight='bold', color=c_amber_title)
    knowledge_lines = (
        "• Replay Buffer $\\mathcal{D}$ (Transitions $(s, a, r, s'))$\n"
        "• Neural Weights $\\theta, \\theta'$ (Atomic Pointer Swap)\n"
        "• Formal Models & Specs ($\\psi \\in \\mathrm{PCTL}$)\n"
        "• SLA Targets & QoS Thresholds $\\tau$\n"
        "• Operational Telemetry & State History"
    )
    ax.text(10.2, 6.2, knowledge_lines, ha='center', va='center', fontsize=8.3, color=c_slate_dark, linespacing=1.35)

    # D. Plan (Bottom-Right of Controller)
    draw_card(16.6, 4.5, 4.6, 2.2, c_emerald_fill, c_emerald_border, lw=1.6)
    ax.text(16.6, 5.2, "3. PLAN (RS-DRL)", ha='center', va='center', fontsize=11.0, fontweight='bold', color=c_emerald_title)
    ax.text(16.6, 4.4, "Deep Policy Inference ($< 0.5\\,\\mathrm{ms}$)\n+ Asynchronous Non-blocking\nSMC Feedback Guidance",
            ha='center', va='center', fontsize=8.4, color=c_slate_dark, linespacing=1.3)

    # E. Execute (Top-Right of Controller)
    draw_card(16.6, 8.4, 4.6, 1.9, c_blue_fill, c_blue_border, lw=1.5)
    ax.text(16.6, 8.9, "4. EXECUTE", ha='center', va='center', fontsize=11.0, fontweight='bold', color=c_blue_title)
    ax.text(16.6, 8.25, "Effector Dispatch &\nRuntime Adaptation Execution",
            ha='center', va='center', fontsize=8.8, color=c_slate_dark)

    # -------------------------------------------------------------
    # Connecting Arrows Inside Controller
    # -------------------------------------------------------------
    # Monitor -> Analyze (Vertical Downward)
    ax.annotate('', xy=(3.8, 5.45), xytext=(3.8, 7.45),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.3, headwidth=5.5, headlength=6.5))
    ax.text(2.7, 6.45, "State $s_t$", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_slate_dark)

    # Analyze -> Plan (Routed Cleanly BELOW Shared Knowledge - Zero Intersect)
    path_data = [
        (Path.MOVETO, (3.8, 3.55)),
        (Path.LINETO, (3.8, 2.2)),
        (Path.LINETO, (16.6, 2.2)),
        (Path.LINETO, (16.6, 3.4))
    ]
    codes, verts = zip(*path_data)
    arrow_path = Path(verts, codes)
    patch_arrow = patches.PathPatch(arrow_path, facecolor='none', edgecolor='#DC2626', linewidth=1.5)
    ax.add_patch(patch_arrow)

    # Arrow head on Plan entry (pointing up at 16.6, 3.4)
    ax.annotate('', xy=(16.6, 3.4), xytext=(16.6, 3.0),
                arrowprops=dict(facecolor='#DC2626', edgecolor='#DC2626', width=1.5, headwidth=6.0, headlength=7.0))

    # Badge for Adaptation Trigger along bottom bus
    draw_card(10.2, 2.2, 7.2, 0.45, '#FEF2F2', '#DC2626', r=0.10, lw=1.0)
    ax.text(10.2, 2.2, "Adaptation Trigger (SLA Violation / Margin Depletion)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='#991B1B')

    # Plan -> Execute (Vertical Upward)
    ax.annotate('', xy=(16.6, 7.45), xytext=(16.6, 5.6),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.3, headwidth=5.5, headlength=6.5))
    ax.text(18.0, 6.5, "Selected\nAction $a^*$", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_emerald_title)

    # -------------------------------------------------------------
    # Two-Way Knowledge Connections (Dashed Amber <->)
    # -------------------------------------------------------------
    # Monitor <-> Knowledge
    ax.annotate('', xy=(7.5, 7.4), xytext=(6.0, 7.9),
                arrowprops=dict(arrowstyle='<->', lw=1.3, color=c_amber_border, linestyle=':'))
    # Analyze <-> Knowledge
    ax.annotate('', xy=(7.5, 5.4), xytext=(6.0, 4.9),
                arrowprops=dict(arrowstyle='<->', lw=1.3, color=c_amber_border, linestyle=':'))
    # Plan <-> Knowledge
    ax.annotate('', xy=(12.9, 5.4), xytext=(14.3, 4.9),
                arrowprops=dict(arrowstyle='<->', lw=1.3, color=c_amber_border, linestyle=':'))
    # Execute <-> Knowledge
    ax.annotate('', xy=(12.9, 7.4), xytext=(14.3, 7.9),
                arrowprops=dict(arrowstyle='<->', lw=1.3, color=c_amber_border, linestyle=':'))

    # -------------------------------------------------------------
    # Boundary Crossings (Telemetry Ingestion & Effector Actuation)
    # -------------------------------------------------------------
    # 1. Managed System -> Monitor (Sensory Probes: Clean Straight Vertical at x=3.8)
    ax.annotate('', xy=(3.8, 9.35), xytext=(3.8, 11.55),
                arrowprops=dict(facecolor=c_indigo_border, edgecolor=c_indigo_border, width=1.4, headwidth=6.0, headlength=7.0))
    # Label badge on the left of arrow (Centered at x=2.2, y=10.45)
    draw_card(2.2, 10.45, 2.6, 0.60, '#EEF2FF', c_indigo_border, r=0.10, lw=0.9)
    ax.text(2.2, 10.45, "Sensory Probes\n(Telemetry Stream $s_t$)", ha='center', va='center',
            fontsize=7.6, fontweight='bold', color=c_indigo_title)

    # 2. Execute -> Managed System (Effector Actuation: Clean Orthogonal Bus)
    # From top of Execute (16.6, 9.35) -> up to y=10.85 -> left to x=10.6 -> up to Managed System (10.6, 11.55)
    path_actuation = [
        (Path.MOVETO, (16.6, 9.35)),
        (Path.LINETO, (16.6, 10.85)),
        (Path.LINETO, (10.6, 10.85)),
        (Path.LINETO, (10.6, 11.55))
    ]
    codes_act, verts_act = zip(*path_actuation)
    act_path = Path(verts_act, codes_act)
    patch_act = patches.PathPatch(act_path, facecolor='none', edgecolor=c_emerald_border, linewidth=1.5)
    ax.add_patch(patch_act)

    # Arrow head entering Managed System at (10.6, 11.55)
    ax.annotate('', xy=(10.6, 11.55), xytext=(10.6, 11.25),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.5, headwidth=6.0, headlength=7.0))

    # Badge on horizontal actuation segment (Centered at x=13.6, y=10.85)
    draw_card(13.6, 10.85, 3.8, 0.45, '#ECFDF5', c_emerald_border, r=0.10, lw=0.9)
    ax.text(13.6, 10.85, "Effector Actuation (Reconfiguration $a^*$)", ha='center', va='center',
            fontsize=7.6, fontweight='bold', color=c_emerald_title)

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade system context saved to {output_path}")

if __name__ == '__main__':
    create_system_context('figures/system-context.png')
