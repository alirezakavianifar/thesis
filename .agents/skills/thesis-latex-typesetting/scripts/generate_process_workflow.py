import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def create_process_workflow(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    # Canvas dimensions: wide landscape format for 6 clear swimlanes
    fig, ax = plt.subplots(figsize=(16.0, 11.5), dpi=300)
    ax.set_xlim(0, 23.0)
    ax.set_ylim(0, 16.0)
    ax.axis('off')

    # Palette - Refined Academic
    c_slate_dark = '#0F172A'
    c_slate_mid = '#334155'
    c_slate_muted = '#475569'
    c_slate_light = '#F8FAFC'
    c_lane_bg_even = '#FFFFFF'
    c_lane_bg_odd = '#F8FAFC'
    c_lane_border = '#CBD5E1'

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

    def draw_card(x, y, w, h, fill, border, r=0.18, lw=1.4):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=fill, edgecolor=border, linewidth=lw
        )
        ax.add_patch(box)

    # -------------------------------------------------------------
    # 6 Swimlanes Definitions
    # Y-bounds: from y=0.8 to y=14.6 (each lane h=2.3)
    # Header width 4.6 with multi-line formatted subtitles
    # -------------------------------------------------------------
    lanes = [
        ("1. Monitor", "Continuous Telemetry Ingestion\n& State Construction $s_t$", 12.3, 14.6, c_lane_bg_even, c_blue_title),
        ("2. Analyze", "SLA & QoS Compliance Evaluation\n& Adaptation Triggering", 10.0, 12.3, c_lane_bg_odd, c_blue_title),
        ("3. Planner (RS-DRL)", "Deterministic DQN Policy Inference\nSub-millisecond ($< 0.5\\,\\mathrm{ms}$)", 7.7, 10.0, c_lane_bg_even, c_emerald_title),
        ("4. Executor", "Immediate Effector Dispatch\n& Runtime Actuation", 5.4, 7.7, c_lane_bg_odd, c_emerald_title),
        ("5. Formal Verifier", "Non-Blocking Statistical Model\nChecking (UPPAAL-SMC)", 3.1, 5.4, c_lane_bg_even, c_purple_title),
        ("6. Shared Knowledge", "Async Experience Replay &\nLock-Free Weight Sync", 0.8, 3.1, c_lane_bg_odd, c_amber_title)
    ]

    header_w = 4.6
    body_w = 17.2
    x_header = 0.6
    x_body = x_header + header_w  # 5.2

    for name, desc, y_bot, y_top, bg_color, title_color in lanes:
        h = y_top - y_bot
        # Swimlane Header Box
        box_hdr = patches.Rectangle((x_header, y_bot), header_w, h, facecolor='#E2E8F0', edgecolor=c_lane_border, lw=1.2)
        ax.add_patch(box_hdr)
        ax.text(x_header + header_w/2, y_bot + h*0.64, name, ha='center', va='center', fontsize=10.2, fontweight='bold', color=title_color)
        ax.text(x_header + header_w/2, y_bot + h*0.28, desc, ha='center', va='center', fontsize=7.2, color=c_slate_muted, linespacing=1.2)

        # Swimlane Body Box
        box_body = patches.Rectangle((x_body, y_bot), body_w, h, facecolor=bg_color, edgecolor=c_lane_border, lw=1.2)
        ax.add_patch(box_body)

    # -------------------------------------------------------------
    # Boundary Divider: Online Real-Time vs. Asynchronous Background
    # Boundary between Executor (bottom at y=5.4) and Formal Verifier (y=5.4)
    # -------------------------------------------------------------
    ax.plot([x_body, x_body + body_w], [5.4, 5.4], color='#DC2626', linestyle='--', linewidth=2.2)
    ax.text(x_body + body_w - 0.5, 5.68, "▲ ONLINE REAL-TIME CRITICAL PATH (< 0.5 ms) ▲",
            ha='right', va='center', fontsize=8.6, fontweight='bold', color='#DC2626')
    ax.text(x_body + body_w - 0.5, 5.12, "▼ ASYNCHRONOUS BACKGROUND THREADS (NON-BLOCKING) ▼",
            ha='right', va='center', fontsize=8.6, fontweight='bold', color='#7C3AED')

    # -------------------------------------------------------------
    # 1. Lane: Monitor (y in [12.3, 14.6], center y=13.45)
    # -------------------------------------------------------------
    # Initial Start Node
    start_circle = patches.Circle((6.2, 13.45), 0.22, facecolor=c_slate_dark, edgecolor=c_slate_dark)
    ax.add_patch(start_circle)

    # Arrow -> Sense
    ax.annotate('', xy=(7.1, 13.45), xytext=(6.45, 13.45),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=6.0))

    # Action 1: Sense & Construct State
    draw_card(8.8, 13.45, 3.2, 1.25, c_blue_fill, c_blue_border)
    ax.text(8.8, 13.68, "Sense Environment", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_blue_title)
    ax.text(8.8, 13.25, "Construct State $s_t \\in \\mathcal{S}$", ha='center', va='center', fontsize=8.0, color=c_slate_dark)

    # Arrow Monitor -> Analyze
    ax.annotate('', xy=(8.8, 11.85), xytext=(8.8, 12.82),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=6.0))

    # -------------------------------------------------------------
    # 2. Lane: Analyze (y in [10.0, 12.3], center y=11.15)
    # -------------------------------------------------------------
    # Decision Diamond
    diamond = patches.Polygon([[8.8, 11.85], [9.9, 11.15], [8.8, 10.45], [7.7, 11.15]], closed=True,
                              facecolor=c_amber_fill, edgecolor=c_amber_border, lw=1.4)
    ax.add_patch(diamond)
    ax.text(8.8, 11.30, "QoS Violation?", ha='center', va='center', fontsize=8.2, fontweight='bold', color=c_amber_title)
    ax.text(8.8, 10.95, r"$\min_k M_k(s) < \tau$ ?", ha='center', va='center', fontsize=7.8, color=c_amber_title)

    # NO Branch (Loop back to Monitor)
    ax.text(10.2, 11.35, "NO", ha='left', va='center', fontsize=8.0, fontweight='bold', color='#059669')
    # Loopback line
    ax.plot([9.9, 11.0, 11.0], [11.15, 11.15, 13.45], color='#059669', lw=1.3)
    ax.annotate('', xy=(10.42, 13.45), xytext=(11.0, 13.45),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.2, headwidth=5.0, headlength=6.0))

    # YES Branch (Down to Planner)
    ax.text(9.15, 10.25, "YES", ha='left', va='center', fontsize=8.0, fontweight='bold', color='#DC2626')
    ax.annotate('', xy=(8.8, 9.48), xytext=(8.8, 10.45),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=6.0))

    # -------------------------------------------------------------
    # 3. Lane: Planner (y in [7.7, 10.0], center y=8.85)
    # -------------------------------------------------------------
    draw_card(8.8, 8.85, 3.4, 1.25, c_emerald_fill, c_emerald_border)
    ax.text(8.8, 9.10, "DQN Policy Forward Pass", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_emerald_title)
    ax.text(8.8, 8.65, r"$a^* = \arg\max_a Q(s_t, a; \theta_{\mathrm{active}})$", ha='center', va='center', fontsize=8.2, color=c_slate_dark)

    # Down to FORK BAR
    ax.annotate('', xy=(8.8, 7.95), xytext=(8.8, 8.22),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.3, headwidth=5.0, headlength=5.0))

    # -------------------------------------------------------------
    # UML FORK NODE (Horizontal Thick Bar)
    # Splitting into Branch A (Immediate Execution) & Branch B (Async Feedback)
    # -------------------------------------------------------------
    fork_bar = patches.Rectangle((6.8, 7.82), 6.6, 0.14, facecolor=c_slate_dark, edgecolor=c_slate_dark)
    ax.add_patch(fork_bar)
    ax.text(10.2, 8.05, "UML Concurrent Fork", ha='left', va='center', fontsize=7.5, fontweight='bold', color=c_slate_muted)

    # -------------------------------------------------------------
    # 4. Lane: Executor (y in [5.4, 7.7], center y=6.55)
    # Branch 1 (Immediate Execution Path)
    # -------------------------------------------------------------
    # Arrow from Fork Bar down to Executor
    ax.annotate('', xy=(7.8, 7.18), xytext=(7.8, 7.82),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.4, headwidth=5.5, headlength=6.0))
    ax.text(7.0, 7.50, "Fast Path\n(< 0.5 ms)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#059669')

    draw_card(7.8, 6.55, 3.2, 1.25, c_emerald_fill, c_emerald_border)
    ax.text(7.8, 6.80, "Execute Action $a^*$", ha='center', va='center', fontsize=9.0, fontweight='bold', color=c_emerald_title)
    ax.text(7.8, 6.35, "Dispatch to Actuators", ha='center', va='center', fontsize=8.0, color=c_slate_dark)

    # Arrow to Final Activity Node for Execution
    ax.annotate('', xy=(10.7, 6.55), xytext=(9.42, 6.55),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=6.0))

    # Bullseye Activity Final Node
    out_circle = patches.Circle((11.0, 6.55), 0.26, facecolor='none', edgecolor=c_slate_dark, lw=1.5)
    in_circle = patches.Circle((11.0, 6.55), 0.16, facecolor=c_slate_dark, edgecolor=c_slate_dark)
    ax.add_patch(out_circle)
    ax.add_patch(in_circle)
    ax.text(11.0, 6.05, "Actuation Completed\n(No Latency Injected)", ha='center', va='center', fontsize=7.4, color='#059669')

    # -------------------------------------------------------------
    # Branch 2: Asynchronous Formal Verification & Knowledge Loop
    # Arrow from Fork Bar down across Red Boundary into Formal Verifier
    # -------------------------------------------------------------
    ax.plot([12.6, 12.6], [7.82, 4.88], color='#7C3AED', lw=1.4, linestyle='-')
    ax.annotate('', xy=(12.6, 4.88), xytext=(12.6, 5.0),
                arrowprops=dict(facecolor='#7C3AED', edgecolor='#7C3AED', width=1.3, headwidth=5.5, headlength=6.5))
    ax.text(14.2, 6.55, "Asynchronous Fork\nFeedback Signal\n(Non-blocking)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color='#7C3AED')

    # -------------------------------------------------------------
    # 5. Lane: Formal Verifier (y in [3.1, 5.4], center y=4.25)
    # -------------------------------------------------------------
    draw_card(12.6, 4.25, 4.2, 1.25, c_purple_fill, c_purple_border)
    ax.text(12.6, 4.50, "UPPAAL-SMC Verification", ha='center', va='center', fontsize=9.0, fontweight='bold', color=c_purple_title)
    ax.text(12.6, 4.05, r"Simulate $(s_t, a^*) \rightarrow r_{\mathrm{smc}} \in [0, 1]$", ha='center', va='center', fontsize=8.2, color=c_slate_dark)

    # Arrow Verifier -> Composite Reward Synthesizer
    ax.annotate('', xy=(17.4, 4.25), xytext=(14.72, 4.25),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=6.0))

    draw_card(19.2, 4.25, 3.4, 1.25, c_purple_fill, c_purple_border)
    ax.text(19.2, 4.50, "Synthesize Reward", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_purple_title)
    ax.text(19.2, 4.05, r"$r = r_{\mathrm{env}} \cdot r_{\mathrm{smc}}$", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#4C1D95')

    # -------------------------------------------------------------
    # 6. Lane: Shared Knowledge (y in [0.8, 3.1], center y=1.95)
    # -------------------------------------------------------------
    # Arrow from Synthesize Reward down to Replay Buffer
    ax.annotate('', xy=(19.2, 2.58), xytext=(19.2, 3.62),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=6.0))

    # Replay Buffer Storage Card
    draw_card(19.2, 1.95, 3.4, 1.25, c_amber_fill, c_amber_border)
    ax.text(19.2, 2.20, "Store Transition", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_amber_title)
    ax.text(19.2, 1.75, r"Append $(s, a^*, r, s^\prime)$ to $\mathcal{D}$", ha='center', va='center', fontsize=8.0, color=c_slate_dark)

    # Arrow Replay Buffer -> Training Pipeline
    ax.annotate('', xy=(15.7, 1.95), xytext=(17.48, 1.95),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=6.0))

    # Background Training Card
    draw_card(13.6, 1.95, 4.0, 1.25, c_amber_fill, c_amber_border)
    ax.text(13.6, 2.20, "Off-Policy DRL Update", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_amber_title)
    ax.text(13.6, 1.75, r"Shaping ($\rho$) + Batch Loss $\mathcal{L}(\theta)$", ha='center', va='center', fontsize=8.0, color=c_slate_dark)

    # Arrow Training -> Atomic Swap
    ax.annotate('', xy=(10.0, 1.95), xytext=(11.58, 1.95),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=6.0))

    # Atomic Pointer Swap Card (Centered at x=8.2, width=3.4 -> spans [6.5, 9.9])
    draw_card(8.2, 1.95, 3.4, 1.25, c_emerald_fill, c_emerald_border)
    ax.text(8.2, 2.20, "Atomic Pointer Swap", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_emerald_title)
    ax.text(8.2, 1.75, r"$\theta_{\mathrm{active}} \leftarrow \theta_{\mathrm{train}}$ (Lock-Free)", ha='center', va='center', fontsize=7.8, color='#065F46')

    # Arrow Atomic Swap looping back up to Policy Forward Pass in Planner lane
    # Routed vertically at x=5.8 in the dedicated corridor between divider (5.2) and card (6.5)
    ax.plot([6.5, 5.8, 5.8, 7.08], [1.95, 1.95, 8.85, 8.85], color='#059669', lw=1.4, linestyle=':')
    ax.annotate('', xy=(7.08, 8.85), xytext=(6.8, 8.85),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.2, headwidth=5.0, headlength=6.0))
    
    # Reload badge placed cleanly above the horizontal entry segment in Planner lane (x=6.4, y=9.35)
    # Completely within Lane 3, zero overlap with any divider or line
    draw_card(6.4, 9.35, 1.4, 0.42, '#ECFDF5', '#059669', r=0.10, lw=0.9)
    ax.text(6.4, 9.35, "Atomic Reload\n(Lock-Free)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#065F46', linespacing=1.1)

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade process workflow saved to {output_path}")

if __name__ == '__main__':
    create_process_workflow('figures/process-workflow.png')
