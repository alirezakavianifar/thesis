import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def create_planner_internal(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    # Canvas Dimensions: 16.5 x 12.0 inches
    fig, ax = plt.subplots(figsize=(16.5, 12.0), dpi=300)
    ax.set_xlim(0, 22.0)
    ax.set_ylim(0, 15.6)
    ax.axis('off')

    # Color palette - Refined Academic
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

    def draw_card(x, y, w, h, fill, border, r=0.18, lw=1.4):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=fill, edgecolor=border, linewidth=lw
        )
        ax.add_patch(box)

    # Title
    ax.text(11.0, 15.05, "RS-DRL Planner Three-Path Concurrency & Internal Architecture",
            ha='center', va='center', fontsize=14.0, fontweight='bold', color=c_slate_dark)

    # -------------------------------------------------------------
    # 3 Main Vertical Lanes with Dedicated Inter-Lane Channels
    # Lane 1: x in [1.6, 6.6] (center 4.1, width 5.0) -> Inference
    # Channel 1-2: x in [6.6, 8.6] (center 7.6, width 2.0)
    # Lane 2: x in [8.6, 13.6] (center 11.1, width 5.0) -> Feedback & SMC
    # Channel 2-3: x in [13.6, 15.6] (center 14.6, width 2.0)
    # Lane 3: x in [15.6, 20.6] (center 18.1, width 5.0) -> Training & Optimization
    # -------------------------------------------------------------
    cx1, cx2, cx3 = 4.1, 11.1, 18.1
    ch1_x, ch2_x = 7.6, 14.6
    w_lane = 5.0
    w_card = 4.0
    y_lane_bottom = 1.20
    h_lane = 13.10  # y from 1.20 to 14.30

    lane_data = [
        (cx1, w_lane, "PATH 1: INFERENCE", "(Read-Only, < 0.5 ms Critical Path)", '#EFF6FF', c_blue_border, c_blue_title),
        (cx2, w_lane, "PATH 2: FEEDBACK", "(Async Verification & Reward Synthesis)", '#F5F3FF', c_purple_border, c_purple_title),
        (cx3, w_lane, "PATH 3: TRAINING", "(Async Gradient Descent & Lock-Free Sync)", '#FEF3C7', c_amber_border, c_amber_title)
    ]

    for cx, w, title, subtitle, bg_color, border_color, title_color in lane_data:
        # Lane Background Box (y from y_lane_bottom to 14.30)
        box = patches.FancyBboxPatch(
            (cx - w/2, y_lane_bottom), w, h_lane,
            boxstyle="round,pad=0,rounding_size=0.3",
            facecolor=bg_color, edgecolor=border_color, linewidth=1.5
        )
        ax.add_patch(box)
        # Lane Header Box
        hdr_box = patches.FancyBboxPatch(
            (cx - w/2, 13.0), w, 1.3,
            boxstyle="round,pad=0,rounding_size=0.2",
            facecolor='#FFFFFF', edgecolor=border_color, linewidth=1.4
        )
        ax.add_patch(hdr_box)
        ax.text(cx, 13.72, title, ha='center', va='center', fontsize=10.2, fontweight='bold', color=title_color)
        ax.text(cx, 13.25, subtitle, ha='center', va='center', fontsize=7.2, color=c_slate_muted)

    # =============================================================
    # PATH 1: INFERENCE (x = 4.1)
    # =============================================================
    # 1. State Vector
    draw_card(cx1, 11.60, w_card, 1.30, '#FFFFFF', c_blue_border)
    ax.text(cx1, 11.95, "Normalized State Vector", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_blue_title)
    ax.text(cx1, 11.40, r"$s_t = \langle cf_t, of_t \rangle \in \mathcal{S} \subset [0, 1]^d$",
            ha='center', va='center', fontsize=8.5, color=c_slate_dark)

    # Arrow -> Active Policy Network
    ax.annotate('', xy=(cx1, 9.95), xytext=(cx1, 10.95),
                arrowprops=dict(facecolor=c_blue_border, edgecolor=c_blue_border, width=1.3, headwidth=5.5, headlength=6.0))

    # 2. Active Policy Network (Double Buffer Slot A)
    draw_card(cx1, 8.60, w_card, 2.70, c_emerald_fill, c_emerald_border, lw=1.6)
    ax.text(cx1, 9.55, "ACTIVE POLICY NETWORK", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_emerald_title)
    ax.text(cx1, 9.15, r"$\theta_{\mathrm{active}}$ (Read-Only Double Buffer)", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#065F46')
    ax.text(cx1, 8.50, "Forward Pass Execution:\n$\\mathcal{O}(1)$ Matrix Multiplications\nDeterministic Latency $< 0.5\\,\\mathrm{ms}$",
            ha='center', va='center', fontsize=7.8, color=c_slate_dark, linespacing=1.3)
    ax.text(cx1, 7.55, r"$Q(s_t, a; \theta_{\mathrm{active}}), \;\; \forall a \in \mathcal{A}$",
            ha='center', va='center', fontsize=8.2, fontweight='bold', color=c_emerald_title)

    # Arrow -> Selected Action
    ax.annotate('', xy=(cx1, 5.45), xytext=(cx1, 7.25),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.3, headwidth=5.5, headlength=6.0))

    # 3. Selected Action Card
    draw_card(cx1, 4.60, w_card, 1.70, c_emerald_fill, c_emerald_border, lw=1.5)
    ax.text(cx1, 5.10, "Selected Adaptation Action", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_emerald_title)
    ax.text(cx1, 4.60, r"$a^* = \arg\max_{a \in \mathcal{A}} Q(s_t, a; \theta_{\mathrm{active}})$",
            ha='center', va='center', fontsize=8.8, fontweight='bold', color='#065F46')
    ax.text(cx1, 4.10, "Dispatched to Actuators (< 0.5 ms)", ha='center', va='center', fontsize=7.4, color=c_slate_muted)

    # Arrow from Selected Action to Fast Actuation Badge
    ax.annotate('', xy=(cx1, 2.71), xytext=(cx1, 3.75),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.4, headwidth=5.5, headlength=6.0))

    # Badge on Actuation Exit
    draw_card(cx1, 2.50, 2.40, 0.42, '#ECFDF5', '#059669', r=0.10, lw=1.0)
    ax.text(cx1, 2.50, "Fast Actuation Path", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#059669')

    # Arrow from Badge to Terminal Node (Generous clearance!)
    ax.annotate('', xy=(cx1, 1.83), xytext=(cx1, 2.29),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.4, headwidth=5.5, headlength=6.0))

    # Terminal node (Cleanly centered at y=1.65, bottom at 1.47, lane bottom is 1.20 -> 0.27 padding!)
    term_circle_out = patches.Circle((cx1, 1.65), 0.18, facecolor='none', edgecolor='#059669', lw=1.5)
    term_circle_in = patches.Circle((cx1, 1.65), 0.11, facecolor='#059669', edgecolor='#059669')
    ax.add_patch(term_circle_out)
    ax.add_patch(term_circle_in)

    # =============================================================
    # ASYNC FORK (Action a* -> Path 2 Telemetry Ingestion)
    # Leaves RIGHT edge of Card 3 at (cx1 + w_card/2, 4.60) -> into Channel 1-2 (x=ch1_x)
    # -> up to y=11.60 -> into left edge of Telemetry (cx2 - w_card/2, 11.60)
    # =============================================================
    x_fork_start = cx1 + w_card / 2
    x_fork_end = cx2 - w_card / 2
    path_fork = [
        (Path.MOVETO, (x_fork_start, 4.60)),
        (Path.LINETO, (ch1_x, 4.60)),
        (Path.LINETO, (ch1_x, 11.60)),
        (Path.LINETO, (x_fork_end, 11.60))
    ]
    codes_fork, verts_fork = zip(*path_fork)
    fork_patch = patches.PathPatch(Path(verts_fork, codes_fork), facecolor='none', edgecolor=c_purple_border, lw=1.4, linestyle='--')
    ax.add_patch(fork_patch)

    # Small junction dot at fork origin on Card 3 right edge
    ax.add_patch(patches.Circle((x_fork_start, 4.60), 0.06, facecolor=c_purple_border, edgecolor=c_purple_border))

    ax.annotate('', xy=(x_fork_end, 11.60), xytext=(x_fork_end - 0.4, 11.60),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.4, headwidth=5.5, headlength=6.0))

    # Badge in Channel 1-2 (width 1.4, height 0.60, perfectly inside 2.0 channel with 0.3 margin!)
    draw_card(ch1_x, 7.80, 1.40, 0.60, '#F5F3FF', c_purple_border, r=0.10, lw=1.0)
    ax.text(ch1_x, 7.80, "Async Fork\nAction $a^*$", ha='center', va='center', fontsize=7.2, fontweight='bold', color=c_purple_title, linespacing=1.15)

    # =============================================================
    # PATH 2: FEEDBACK & VERIFICATION (x = 11.1)
    # =============================================================
    # 1. Feedback Telemetry
    draw_card(cx2, 11.60, w_card, 1.30, '#FFFFFF', c_purple_border)
    ax.text(cx2, 11.95, "Operational Telemetry", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_purple_title)
    ax.text(cx2, 11.40, r"$(s_t, a^*, r_{\mathrm{env}}, s_{t+1})$",
            ha='center', va='center', fontsize=8.5, color=c_slate_dark)

    # Arrow -> UPPAAL-SMC
    ax.annotate('', xy=(cx2, 9.85), xytext=(cx2, 10.95),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.3, headwidth=5.5, headlength=6.0))

    # 2. UPPAAL-SMC Verification Module
    draw_card(cx2, 8.60, w_card, 2.50, c_purple_fill, c_purple_border, lw=1.5)
    ax.text(cx2, 9.45, "UPPAAL-SMC VERIFIER", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_purple_title)
    ax.text(cx2, 8.90, "Parallel Background Thread\n$N_{\\mathrm{sim}} = 4{,}612$ via Chernoff Bound\nNon-blocking Execution",
            ha='center', va='center', fontsize=7.6, color=c_slate_dark, linespacing=1.3)
    ax.text(cx2, 7.75, r"Returns $r_{\mathrm{smc}} = \mathbb{I}[\hat{P}(\mathrm{□}_{\leq T}\, \phi) \geq 1-\alpha] \in \{0, 1\}$",
            ha='center', va='center', fontsize=7.6, fontweight='bold', color='#4C1D95')

    # Arrow -> Composite Reward
    ax.annotate('', xy=(cx2, 6.15), xytext=(cx2, 7.35),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.3, headwidth=5.5, headlength=6.0))

    # 3. Composite Reward Synthesizer
    draw_card(cx2, 5.50, w_card, 1.30, c_purple_fill, c_purple_border)
    ax.text(cx2, 5.85, "Composite Reward Synthesis", ha='center', va='center', fontsize=8.5, fontweight='bold', color=c_purple_title)
    ax.text(cx2, 5.25, r"$r = r_{\mathrm{env}} \cdot r_{\mathrm{smc}}$",
            ha='center', va='center', fontsize=9.2, fontweight='bold', color='#4C1D95')

    # Arrow -> Shared Replay Buffer
    ax.annotate('', xy=(cx2, 3.65), xytext=(cx2, 4.85),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.3, headwidth=5.5, headlength=6.0))

    # 4. Shared Replay Buffer Card
    draw_card(cx2, 2.80, w_card, 1.70, c_amber_fill, c_amber_border, r=0.25, lw=1.6)
    ax.text(cx2, 3.25, "SHARED REPLAY BUFFER", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_amber_title)
    ax.text(cx2, 2.75, r"$\mathcal{D} = \{ (s_i, a_i, r_i, s^\prime_i) \}_{i=1}^{N}$",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color=c_slate_dark)
    ax.text(cx2, 2.25, "Thread-Safe Ring Buffer Storage", ha='center', va='center', fontsize=7.5, color=c_slate_muted)

    # =============================================================
    # ORTHOGONAL BATCH SAMPLING BUS (Path 2 Buffer -> Path 3 Sampler)
    # Leaves RIGHT edge of Buffer at (cx2 + w_card/2, 2.80) -> into Channel 2-3 (x=ch2_x)
    # -> up to y=11.60 -> into left edge of Sampler (cx3 - w_card/2, 11.60)
    # =============================================================
    x_batch_start = cx2 + w_card / 2
    x_batch_end = cx3 - w_card / 2
    path_batch = [
        (Path.MOVETO, (x_batch_start, 2.80)),
        (Path.LINETO, (ch2_x, 2.80)),
        (Path.LINETO, (ch2_x, 11.60)),
        (Path.LINETO, (x_batch_end, 11.60))
    ]
    codes_batch, verts_batch = zip(*path_batch)
    batch_patch = patches.PathPatch(Path(verts_batch, codes_batch), facecolor='none', edgecolor=c_amber_border, lw=1.4)
    ax.add_patch(batch_patch)

    ax.annotate('', xy=(x_batch_end, 11.60), xytext=(x_batch_end - 0.4, 11.60),
                arrowprops=dict(facecolor=c_amber_border, edgecolor=c_amber_border, width=1.4, headwidth=5.5, headlength=6.0))

    # Badge in Channel 2-3 (width 1.4, height 0.60, perfectly inside 2.0 channel with 0.3 margin!)
    draw_card(ch2_x, 7.20, 1.40, 0.60, '#FEF3C7', c_amber_border, r=0.10, lw=1.0)
    ax.text(ch2_x, 7.20, "Sample Batch\n$\\mathcal{B} \\sim \\mathcal{D}$", ha='center', va='center',
            fontsize=7.2, fontweight='bold', color=c_amber_title, linespacing=1.15)

    # =============================================================
    # PATH 3: TRAINING & LOCK-FREE SYNC (x = 18.1)
    # =============================================================
    # 1. Batch Sampling
    draw_card(cx3, 11.60, w_card, 1.30, '#FFFFFF', c_amber_border)
    ax.text(cx3, 11.95, "Transition Batch Sampling", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_amber_title)
    ax.text(cx3, 11.40, r"$\mathcal{B} = \{ (s, a, r, s^\prime) \}_{k=1}^{B}$",
            ha='center', va='center', fontsize=8.5, color=c_slate_dark)

    # Arrow -> Reward Shaping
    ax.annotate('', xy=(cx3, 9.90), xytext=(cx3, 10.95),
                arrowprops=dict(facecolor=c_amber_border, edgecolor=c_amber_border, width=1.3, headwidth=5.5, headlength=6.0))

    # 2. Reward Shaping Module
    draw_card(cx3, 9.10, w_card, 1.60, c_amber_fill, c_amber_border, lw=1.5)
    ax.text(cx3, 9.60, "Reward Shaping Engine", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_amber_title)
    ax.text(cx3, 9.15, r"$\tilde{r} = 1$ if $r=0 \wedge \mathrm{rand} < \rho$",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#B45309')
    ax.text(cx3, 8.65, r"Else $\tilde{r} = r$ (Stochastic Guidance)", ha='center', va='center', fontsize=7.6, color=c_slate_muted)

    # Arrow -> Gradient Descent & Shadow Update
    ax.annotate('', xy=(cx3, 7.10), xytext=(cx3, 8.30),
                arrowprops=dict(facecolor=c_amber_border, edgecolor=c_amber_border, width=1.3, headwidth=5.5, headlength=6.0))

    # 3. Off-Policy Gradient Update
    draw_card(cx3, 6.30, w_card, 1.60, c_amber_fill, c_amber_border, lw=1.5)
    ax.text(cx3, 6.80, "Gradient Descent Optimization", ha='center', va='center', fontsize=8.5, fontweight='bold', color=c_amber_title)
    ax.text(cx3, 6.30, r"$\mathcal{L}(\theta) = \mathbb{E} [ (y - Q(s, a; \theta_{\mathrm{train}}))^2 ]$",
            ha='center', va='center', fontsize=7.8, color=c_slate_dark)
    ax.text(cx3, 5.75, r"$\theta_{\mathrm{train}} \leftarrow \theta_{\mathrm{train}} - \alpha \nabla \mathcal{L}$",
            ha='center', va='center', fontsize=8.2, fontweight='bold', color='#B45309')

    # Arrow -> Target Network Update
    ax.annotate('', xy=(cx3, 4.68), xytext=(cx3, 5.50),
                arrowprops=dict(facecolor=c_amber_border, edgecolor=c_amber_border, width=1.3, headwidth=5.5, headlength=6.0))

    # 4. Target Network Periodic Update Card
    draw_card(cx3, 4.10, w_card, 1.15, '#FFFFFF', c_amber_border)
    ax.text(cx3, 4.35, "Target Network Sync (Every $C$ Steps)", ha='center', va='center', fontsize=8.3, fontweight='bold', color=c_amber_title)
    ax.text(cx3, 3.85, r"$\theta^\prime \leftarrow \tau_{\mathrm{soft}}\theta_{\mathrm{train}} + (1{-}\tau_{\mathrm{soft}})\theta^\prime$ ($\tau_{\mathrm{soft}}{=}1.0$)",
            ha='center', va='center', fontsize=7.6, color=c_slate_dark)

    # Arrow -> Atomic Pointer Swap Box
    ax.annotate('', xy=(cx3, 2.73), xytext=(cx3, 3.52),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.3, headwidth=5.5, headlength=6.0))

    # 5. Lock-Free Atomic Pointer Swap Card
    draw_card(cx3, 2.15, w_card, 1.15, c_emerald_fill, c_emerald_border, lw=1.6)
    ax.text(cx3, 2.40, "Atomic Pointer Swap", ha='center', va='center', fontsize=9.0, fontweight='bold', color=c_emerald_title)
    ax.text(cx3, 1.95, r"$\mathrm{AtomicSwap}(\theta_{\mathrm{active}}, \theta_{\mathrm{train}})$ (Lock-Free)",
            ha='center', va='center', fontsize=7.8, fontweight='bold', color='#065F46')

    # =============================================================
    # ATOMIC SWAP RETURN LINE TO PATH 1 ACTIVE NETWORK
    # Drops straight from Card 5 bottom at (cx3, 1.575) down to y=0.55
    # Runs horizontally across to (0.70, 0.55) -> rises to (0.70, 8.60)
    # -> enters Card 2 at (cx1 - w_card/2, 8.60)
    # =============================================================
    x_swap_start = cx3
    y_card5_bottom = 2.15 - 1.15 / 2
    x_swap_end = cx1 - w_card / 2
    y_bus = 0.55
    badge_w = 6.6
    badge_left = cx2 - badge_w / 2
    badge_right = cx2 + badge_w / 2

    # Drop from Card 5 bottom straight down to bottom corridor, then to badge right
    path_swap_drop = [
        (Path.MOVETO, (x_swap_start, y_card5_bottom)),
        (Path.LINETO, (x_swap_start, y_bus)),
        (Path.LINETO, (badge_right, y_bus))
    ]
    codes_drop, verts_drop = zip(*path_swap_drop)
    ax.add_patch(patches.PathPatch(Path(verts_drop, codes_drop), facecolor='none', edgecolor='#059669', lw=1.6))

    # Directional chevron on right horizontal segment (placed cleanly at midpoint x=16.25)
    ax.annotate('', xy=(16.10, y_bus), xytext=(16.40, y_bus),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.2, headwidth=5.0, headlength=5.0))

    # Return bus badge (Floating cleanly in bottom corridor, perfectly centered at cx2=11.1, y=0.55)
    draw_card(cx2, y_bus, badge_w, 0.46, '#ECFDF5', '#059669', r=0.10, lw=1.1)
    ax.text(cx2, y_bus, r"Lock-Free Weight Bus: $\mathrm{AtomicSwap}(\theta_{\mathrm{active}}, \theta_{\mathrm{train}})$ (Zero Reader Lock)",
            ha='center', va='center', fontsize=7.8, fontweight='bold', color='#065F46')

    # Path from badge left to Lane 1 entrance
    path_swap_return = [
        (Path.MOVETO, (badge_left, y_bus)),
        (Path.LINETO, (0.70, y_bus)),
        (Path.LINETO, (0.70, 8.60)),
        (Path.LINETO, (x_swap_end, 8.60))
    ]
    codes_ret, verts_ret = zip(*path_swap_return)
    ax.add_patch(patches.PathPatch(Path(verts_ret, codes_ret), facecolor='none', edgecolor='#059669', lw=1.6))

    # Directional chevron on left horizontal segment (placed cleanly at midpoint x=4.25)
    ax.annotate('', xy=(4.10, y_bus), xytext=(4.40, y_bus),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.2, headwidth=5.0, headlength=5.0))

    # Directional chevron on vertical rise segment (placed cleanly at midpoint y=4.80)
    ax.annotate('', xy=(0.70, 4.95), xytext=(0.70, 4.65),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.2, headwidth=5.0, headlength=5.0))

    # Final entry arrow into Active Policy Network
    ax.annotate('', xy=(x_swap_end, 8.60), xytext=(x_swap_end - 0.45, 8.60),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.4, headwidth=6.0, headlength=7.0))

    # Entry label placed cleanly above entry arrow in the left margin (No border collision!)
    ax.text(0.70, 9.05, "Atomic Reload", ha='center', va='center',
            fontsize=7.2, fontweight='bold', color='#065F46')

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade planner internal architecture saved to {output_path}")

if __name__ == '__main__':
    create_planner_internal('figures/planner-internal.png')
