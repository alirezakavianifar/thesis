import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def create_knowledge_repository(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    fig, ax = plt.subplots(figsize=(15.5, 11.0), dpi=300)
    ax.set_xlim(0, 22.0)
    ax.set_ylim(0, 15.5)
    ax.axis('off')

    # Color palette
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

    c_purple_border = '#7C3AED'
    c_purple_fill = '#F5F3FF'
    c_purple_title = '#4C1D95'

    c_rose_border = '#E11D48'
    c_rose_fill = '#FFF1F2'
    c_rose_title = '#881337'

    def draw_card(x, y, w, h, fill, border, r=0.20, lw=1.5):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=fill, edgecolor=border, linewidth=lw
        )
        ax.add_patch(box)

    # Title
    ax.text(11.0, 14.8, "Shared Knowledge Repository Architecture & Concurrent Access Model",
            ha='center', va='center', fontsize=14.0, fontweight='bold', color=c_slate_dark)

    # -------------------------------------------------------------
    # Central Shared Knowledge Base Container (x: [6.8, 15.2], y: [1.0, 13.6])
    # Center x = 11.0, w = 9.2, h = 12.8
    # -------------------------------------------------------------
    kb_box = patches.FancyBboxPatch(
        (6.4, 0.8), 9.2, 13.0,
        boxstyle="round,pad=0,rounding_size=0.4",
        facecolor='#FFFBEB', edgecolor=c_amber_border, linewidth=2.0
    )
    ax.add_patch(kb_box)
    ax.text(11.0, 13.3, "SHARED KNOWLEDGE REPOSITORY", ha='center', va='center',
            fontsize=12.0, fontweight='bold', color=c_amber_title)
    ax.text(11.0, 12.85, "Centralized Thread-Safe In-Memory Data Structures (Validating Table 4.3)",
            ha='center', va='center', fontsize=7.8, color=c_slate_muted)

    # -------------------------------------------------------------
    # 6 Internal Shared Data Stores inside Knowledge Base
    # y positions: 11.6, 9.6, 7.6, 5.6, 3.6, 1.8
    # -------------------------------------------------------------
    stores = [
        (11.0, 11.7, 8.2, 1.5, "1. System Topology & Active Configuration",
         r"Active parameters $\mathbf{CF}$, network routing tables, channel states",
         "[Read-Dominant, Infrequent Sync Write]", c_blue_fill, c_blue_border, c_blue_title),

        (11.0, 9.7, 8.2, 1.5, "2. Real-Time Telemetry Ring Buffer",
         r"Sliding window of state observations: $\mathbf{s}_t = \langle cf, of \rangle \in \mathcal{S}$",
         "[Lock-Free Single-Producer Multiple-Consumer]", c_blue_fill, c_blue_border, c_blue_title),

        (11.0, 7.7, 8.2, 1.5, "3. Deep Policy Neural Weights (Double Buffer)",
         r"Active weights $\theta_{\mathrm{active}}$ & Shadow buffer $\theta_{\mathrm{train}}$",
         r"[Atomic Pointer Swap $\cdot$ Zero Reader Lock]", c_emerald_fill, c_emerald_border, c_emerald_title),

        (11.0, 5.7, 8.2, 1.5, "4. Experience Replay Buffer D",
         r"Historical transitions: $\mathcal{D} = \{ (s, a, r, s^\prime) \}_{i=1}^N$ (Capacity: $10^5$)",
         r"[Thread-Safe Append-Only $\cdot$ Batch Sample]", c_amber_fill, c_amber_border, c_amber_title),

        (11.0, 3.7, 8.2, 1.5, "5. Formal Models & Verification Specifications",
         r"Stochastic Timed Automata (STA) templates, UPPAAL-SMC queries $\psi$",
         r"[Read-Only by SMC Thread $\cdot$ Pre-calibrated]", c_purple_fill, c_purple_border, c_purple_title),

        (11.0, 1.7, 8.2, 1.5, "6. QoS Contracts & Safety Threshold Bounds",
         r"Quality thresholds $\tau_k$, hazard limits $\epsilon_{\mathrm{threshold}}$, margin offsets",
         "[Immutable Operational Contract]", c_rose_fill, c_rose_border, c_rose_title)
    ]

    for sx, sy, sw, sh, s_title, s_desc, s_badge, s_fill, s_border, s_tcol in stores:
        draw_card(sx, sy, sw, sh, s_fill, s_border, r=0.18, lw=1.3)
        ax.text(sx, sy + 0.40, s_title, ha='center', va='center', fontsize=8.6, fontweight='bold', color=s_tcol)
        ax.text(sx, sy - 0.05, s_desc, ha='center', va='center', fontsize=7.6, color=c_slate_dark)
        ax.text(sx, sy - 0.45, s_badge, ha='center', va='center', fontsize=7.0, fontweight='bold', color=c_slate_muted)

    # -------------------------------------------------------------
    # Surrounding Interacting Autonomic Components
    # Left Side: Monitor (top), Analyze (mid), Formal Verifier (bottom)
    # Right Side: Executor (top), Planner (mid), Background Learner (bottom)
    # -------------------------------------------------------------

    # A. MONITOR (Top Left: x = 3.2, y = 10.7)
    draw_card(3.2, 10.7, 5.0, 2.2, c_blue_fill, c_blue_border, lw=1.5)
    ax.text(3.2, 11.35, "MONITOR COMPONENT", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_blue_title)
    ax.text(3.2, 10.75, "Continuous Telemetry Ingestion\nConstructs State Vector $s_t$\nWrites to Telemetry Buffer",
            ha='center', va='center', fontsize=7.8, color=c_slate_dark, linespacing=1.3)
    ax.text(3.2, 10.00, "[Writer to Store 2]", ha='center', va='center', fontsize=7.4, fontweight='bold', color=c_blue_border)

    # Arrow: Monitor -> Store 2 (Write Telemetry)
    ax.annotate('', xy=(6.9, 9.9), xytext=(5.7, 10.7),
                arrowprops=dict(facecolor=c_blue_border, edgecolor=c_blue_border, width=1.3, headwidth=5.5, headlength=6.5))
    ax.text(5.85, 11.20, "Append State $s_t$", ha='center', va='center', fontsize=7.5, fontweight='bold', color=c_blue_title,
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#FFFFFF', edgecolor='none', alpha=0.85))

    # B. ANALYZE (Mid Left: x = 3.2, y = 6.7)
    draw_card(3.2, 6.7, 5.0, 2.2, c_blue_fill, c_blue_border, lw=1.5)
    ax.text(3.2, 7.35, "ANALYZE COMPONENT", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_blue_title)
    ax.text(3.2, 6.75, "Reads Recent State Telemetry\nEvaluates Against QoS Targets\nDispatches Adaptation Trigger",
            ha='center', va='center', fontsize=7.8, color=c_slate_dark, linespacing=1.3)
    ax.text(3.2, 6.00, "[Reader of Stores 2 & 6]", ha='center', va='center', fontsize=7.4, fontweight='bold', color=c_blue_border)

    # Arrows: Store 2 -> Analyze & Store 6 -> Analyze
    ax.annotate('', xy=(5.7, 7.2), xytext=(6.9, 9.4),
                arrowprops=dict(facecolor=c_blue_border, edgecolor=c_blue_border, width=1.2, headwidth=5.0, headlength=6.0, linestyle=':'))
    ax.annotate('', xy=(5.7, 6.2), xytext=(6.9, 2.0),
                arrowprops=dict(facecolor=c_rose_border, edgecolor=c_rose_border, width=1.2, headwidth=5.0, headlength=6.0, linestyle=':'))
    ax.text(5.5, 8.4, "Read $s_t$", ha='center', va='center', fontsize=7.2, color=c_blue_title)
    ax.text(5.5, 4.3, "Read Bounds $\\tau$", ha='center', va='center', fontsize=7.2, color=c_rose_title)

    # C. FORMAL VERIFIER (Bottom Left: x = 3.2, y = 2.7)
    draw_card(3.2, 2.7, 5.0, 2.2, c_purple_fill, c_purple_border, lw=1.5)
    ax.text(3.2, 3.35, "FORMAL VERIFIER (SMC)", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_purple_title)
    ax.text(3.2, 2.75, "Async UPPAAL-SMC Thread\nQueries Formal Models $\\mathcal{M}$\nComputes Compound Reward $r$",
            ha='center', va='center', fontsize=7.8, color=c_slate_dark, linespacing=1.3)
    ax.text(3.2, 2.00, "[Reader of 5 $\\cdot$ Writer to 4]", ha='center', va='center', fontsize=7.4, fontweight='bold', color=c_purple_title)

    # Arrows: Store 5 -> Verifier & Verifier -> Store 4
    ax.annotate('', xy=(5.7, 3.0), xytext=(6.9, 3.5),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.2, headwidth=5.0, headlength=6.0, linestyle=':'))
    ax.annotate('', xy=(6.9, 5.4), xytext=(5.7, 2.4),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.3, headwidth=5.5, headlength=6.5,
                               connectionstyle='arc3,rad=-0.12'))
    ax.text(5.45, 4.65, "Append $(s, a^*, r, s^\\prime)$", ha='center', va='center', fontsize=7.4, fontweight='bold', color=c_purple_title,
            bbox=dict(boxstyle='round,pad=0.18', facecolor='#FFFFFF', edgecolor=c_purple_border, lw=0.6, alpha=0.92))

    # D. EXECUTOR (Top Right: x = 18.8, y = 10.7)
    draw_card(18.8, 10.7, 5.0, 2.2, c_emerald_fill, c_emerald_border, lw=1.5)
    ax.text(18.8, 11.35, "EXECUTOR COMPONENT", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_emerald_title)
    ax.text(18.8, 10.75, "Dispatches Adaptation to Actuators\nUpdates Active Configuration\nMaintains Topology Consistency",
            ha='center', va='center', fontsize=7.8, color=c_slate_dark, linespacing=1.3)
    ax.text(18.8, 10.00, "[Writer to Store 1]", ha='center', va='center', fontsize=7.4, fontweight='bold', color=c_emerald_title)

    # Arrow: Executor -> Store 1 (Update Config)
    ax.annotate('', xy=(15.1, 11.5), xytext=(16.3, 10.7),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.3, headwidth=5.5, headlength=6.5))
    ax.text(15.7, 11.45, r"Commit $\mathbf{CF}^*$", ha='center', va='center', fontsize=7.6, fontweight='bold', color=c_emerald_title,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFFFFF', edgecolor=c_emerald_border, lw=0.8, alpha=0.95))

    # E. PLANNER (Mid Right: x = 18.8, y = 6.7)
    draw_card(18.8, 6.7, 5.0, 2.2, c_emerald_fill, c_emerald_border, lw=1.6)
    ax.text(18.8, 7.35, "PLANNER (RS-DRL INFERENCE)", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_emerald_title)
    ax.text(18.8, 6.75, "Sub-millisecond Forward Pass\nDirect Memory Read of $\\theta_{\\mathrm{active}}$\nNon-blocking Fast Path",
            ha='center', va='center', fontsize=7.8, color=c_slate_dark, linespacing=1.3)
    ax.text(18.8, 6.00, "[Atomic Reader of Store 3]", ha='center', va='center', fontsize=7.4, fontweight='bold', color=c_emerald_title)

    # Arrow: Store 3 -> Planner (Read-Only Pointer)
    ax.annotate('', xy=(16.3, 6.9), xytext=(15.1, 7.5),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.4, headwidth=6.0, headlength=7.0))
    ax.text(15.7, 7.45, r"Read $\theta_{\mathrm{active}}$", ha='center', va='center', fontsize=7.6, fontweight='bold', color=c_emerald_title,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFFFFF', edgecolor=c_emerald_border, lw=0.8, alpha=0.95))

    # F. ASYNC LEARNER (Bottom Right: x = 18.8, y = 2.7)
    draw_card(18.8, 2.7, 5.0, 2.2, c_amber_fill, c_amber_border, lw=1.5)
    ax.text(18.8, 3.35, "ASYNC LEARNER THREAD", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_amber_title)
    ax.text(18.8, 2.75, "Samples Minibatches from $\\mathcal{D}$\nReward Shaping ($\\rho$) & TD Loss\nUpdates Shadow Buffer $\\theta_{\\mathrm{train}}$",
            ha='center', va='center', fontsize=7.8, color=c_slate_dark, linespacing=1.3)
    ax.text(18.8, 2.00, "[Reader of 4 $\\cdot$ Swapper of 3]", ha='center', va='center', fontsize=7.4, fontweight='bold', color=c_amber_title)

    # Arrows: Store 4 -> Learner & Learner -> Store 3 (Atomic Pointer Swap)
    ax.annotate('', xy=(16.3, 2.8), xytext=(15.1, 5.2),
                arrowprops=dict(facecolor=c_amber_border, edgecolor=c_amber_border, width=1.2, headwidth=5.0, headlength=6.0, linestyle=':'))
    ax.annotate('', xy=(15.1, 7.2), xytext=(16.3, 3.2),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.5, headwidth=6.0, headlength=7.0,
                               connectionstyle='arc3,rad=-0.14'))
    ax.text(15.7, 4.3, r"Sample $\mathcal{B} \sim \mathcal{D}$", ha='center', va='center', fontsize=7.2, color=c_amber_title,
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#FFFBEB', edgecolor='none', alpha=0.9))
    ax.text(16.5, 5.4, r"Atomic Swap $\theta$", ha='center', va='center', fontsize=7.6, fontweight='bold', color='#059669',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#ECFDF5', edgecolor='#059669', lw=0.8, alpha=0.95))

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade knowledge repository architecture saved to {output_path}")

if __name__ == '__main__':
    create_knowledge_repository('figures/knowledge-flow.png')
