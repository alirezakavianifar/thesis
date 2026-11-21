import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def create_system_architecture(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    # Dimensions: 16.8 x 11.8 inches
    fig, ax = plt.subplots(figsize=(16.8, 11.8), dpi=300)
    ax.set_xlim(0, 22.0)
    ax.set_ylim(0, 15.6)
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

    c_indigo_border = '#4F46E5'
    c_indigo_fill = '#EEF2FF'
    c_indigo_title = '#312E81'

    def draw_card(x, y, w, h, fill, border, r=0.18, lw=1.4):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=fill, edgecolor=border, linewidth=lw
        )
        ax.add_patch(box)

    # =============================================================
    # 1. TOP CONTAINER: Managed System & Operational Environment
    # y in [13.30, 14.90] (height 1.60)
    # =============================================================
    # Managed System Box (x: [0.8, 14.6], y: [13.30, 14.90])
    draw_card(7.7, 14.10, 13.8, 1.60, c_indigo_fill, c_indigo_border, lw=1.6)
    ax.text(7.7, 14.52, "Managed Autonomous / Cyber-Physical System",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=c_indigo_title)
    ax.text(7.7, 14.06, "Controllable Features $\\mathbf{CF} = \\{cf_1, \\dots, cf_m\\} \\in \\mathcal{A} \\quad \\cdot \\quad$ Dependability & QoS Targets: $\\{R_0, \\dots, R_{K-1}\\}$",
            ha='center', va='center', fontsize=8.2, color=c_slate_dark)
    ax.text(7.7, 13.62, "Instantiations: Aerial Robotics (6-DOF Flight Dynamics) & Distributed WSN (Multi-hop Topological Routing)",
            ha='center', va='center', fontsize=7.5, color=c_slate_muted)

    # Operational Environment Box (x: [15.2, 21.4], y: [13.30, 14.90])
    draw_card(18.3, 14.10, 6.2, 1.60, c_rose_fill, c_rose_border, lw=1.5)
    ax.text(18.3, 14.52, "Operational Environment",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color=c_rose_title)
    ax.text(18.3, 13.98, "Observable Features $\\mathcal{OF}$:\nEnvironmental Context $\\cdot$ Disturbances $\\cdot$ Noise",
            ha='center', va='center', fontsize=7.8, color=c_slate_dark, linespacing=1.2)

    # Arrow: Environment -> Managed System (Hazards & Disturbances)
    ax.annotate('', xy=(14.6, 14.10), xytext=(15.2, 14.10),
                arrowprops=dict(facecolor=c_rose_border, edgecolor=c_rose_border, width=1.3, headwidth=5.5, headlength=6.0))
    ax.text(14.9, 14.48, "Hazards", ha='center', va='center', fontsize=7.0, fontweight='bold', color=c_rose_title)

    # =============================================================
    # INTER-CONTAINER GAP 1: y in [12.40, 13.30] (height 0.90 units)
    # Holds Telemetry and Actuation buses with zero border overlap!
    # =============================================================
    y_bus_top = 12.85

    # Arrow: Managed System -> Monitor
    ax.annotate('', xy=(2.1, 11.10), xytext=(2.1, 13.30),
                arrowprops=dict(facecolor=c_indigo_border, edgecolor=c_indigo_border, width=1.4, headwidth=5.5, headlength=6.5))
    draw_card(2.1, y_bus_top, 2.6, 0.42, '#EEF2FF', c_indigo_border, r=0.10, lw=1.0)
    ax.text(2.1, y_bus_top, "Telemetry Stream $s = \\langle cf, of \\rangle$", ha='center', va='center',
            fontsize=7.2, fontweight='bold', color=c_indigo_title)

    # Arrow: Executor -> Managed System (Actuation Control Commands)
    path_act = [
        (Path.MOVETO, (20.0, 10.80)),
        (Path.LINETO, (20.0, y_bus_top)),
        (Path.LINETO, (13.8, y_bus_top)),
        (Path.LINETO, (13.8, 13.30))
    ]
    codes_act, verts_act = zip(*path_act)
    ax.add_patch(patches.PathPatch(Path(verts_act, codes_act), facecolor='none', edgecolor=c_emerald_border, lw=1.5))
    ax.annotate('', xy=(13.8, 13.30), xytext=(13.8, 13.05),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.4, headwidth=5.5, headlength=6.5))

    # Flow chevrons on actuation path
    ax.annotate('', xy=(15.2, y_bus_top), xytext=(15.5, y_bus_top),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.1, headwidth=4.5, headlength=4.5))

    draw_card(17.2, y_bus_top, 3.4, 0.42, '#ECFDF5', c_emerald_border, r=0.10, lw=1.0)
    ax.text(17.2, y_bus_top, "Actuation Control Commands ($a^*$)", ha='center', va='center',
            fontsize=7.4, fontweight='bold', color=c_emerald_title)

    # =============================================================
    # 2. MIDDLE CONTAINER: MANAGING SYSTEM (ONLINE MAPE-K LOOP)
    # y in [4.75, 12.40] (height 7.65)
    # =============================================================
    box_online = patches.FancyBboxPatch(
        (0.6, 4.75), 20.8, 7.65,
        boxstyle="round,pad=0,rounding_size=0.35",
        facecolor='#F8FAFC', edgecolor=c_blue_border, linewidth=1.8
    )
    ax.add_patch(box_online)

    # Title centered at the top of the Managing System (Zero collision with any arrow!)
    ax.text(11.0, 12.05, "MANAGING SYSTEM (Online Runtime MAPE-K Feedback Loop)",
            ha='center', va='center', fontsize=11.0, fontweight='bold', color=c_blue_title)

    # -------------------------------------------------------------
    # 1. MONITOR (x = 2.1, y = 9.8) - Width 2.6 -> [0.8, 3.4]
    # -------------------------------------------------------------
    draw_card(2.1, 9.80, 2.6, 2.40, c_blue_fill, c_blue_border)
    ax.text(2.1, 10.60, "1. MONITOR", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_blue_title)
    ax.text(2.1, 9.95, "Telemetry Ingestion\nState Normalization:\n$s = \\langle cf, of \\rangle \\in [0, 1]^d$",
            ha='center', va='center', fontsize=7.5, color=c_slate_dark, linespacing=1.2)
    ax.text(2.1, 9.15, "Sensory Probes", ha='center', va='center', fontsize=7.0, fontweight='bold', color=c_blue_border)

    # Arrow: Monitor -> Analyze
    ax.annotate('', xy=(2.1, 7.70), xytext=(2.1, 8.60),
                arrowprops=dict(facecolor=c_blue_border, edgecolor=c_blue_border, width=1.3, headwidth=5.5, headlength=6.0))
    ax.text(1.5, 8.15, "State $s$", ha='center', va='center', fontsize=7.4, color=c_blue_title)

    # -------------------------------------------------------------
    # 2. ANALYZE (x = 2.1, y = 6.4) - Width 2.6 -> [0.8, 3.4]
    # -------------------------------------------------------------
    draw_card(2.1, 6.40, 2.6, 2.40, c_blue_fill, c_blue_border)
    ax.text(2.1, 7.20, "2. ANALYZE", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_blue_title)
    ax.text(2.1, 6.55, "Surrogate Compliance\nQuery $M_k(s) \\; \\forall k$\nConfidence $\\tau_k$",
            ha='center', va='center', fontsize=7.5, color=c_slate_dark, linespacing=1.2)
    ax.text(2.1, 5.75, r"Trigger if $\min_k M_k(s) < \tau_k$", ha='center', va='center', fontsize=7.0, fontweight='bold', color='#991B1B')

    # -------------------------------------------------------------
    # SHARED KNOWLEDGE BASE (x = 5.7, y = 8.10) - Width 2.6 -> [4.4, 7.0]
    # -------------------------------------------------------------
    draw_card(5.7, 8.10, 2.6, 5.50, c_amber_fill, c_amber_border, r=0.25, lw=1.5)
    ax.text(5.7, 10.35, "SHARED\nKNOWLEDGE", ha='center', va='center', fontsize=9.0, fontweight='bold', color=c_amber_title, linespacing=1.2)
    kb_summary = (
        "• Calibrated Surrogates\n"
        "  $\\{M_k\\}_{k=0}^{K-1}$\n\n"
        "• Trained DRL Policy\n"
        "  Weights $\\theta_{\\mathrm{active}}$\n\n"
        "• Safety Thresholds\n"
        "  $(\\tau_k, \\epsilon_{\\mathrm{threshold}})$\n\n"
        "• Operational Telemetry\n"
        "  Ring Buffer"
    )
    ax.text(5.7, 7.80, kb_summary, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.1)

    # -------------------------------------------------------------
    # Knowledge Interactions (Gap 1: [3.4, 4.4], Gap 2: [7.0, 8.4])
    # -------------------------------------------------------------
    # Monitor -> Knowledge (Store Telemetry)
    ax.annotate('', xy=(4.4, 9.80), xytext=(3.4, 9.80),
                arrowprops=dict(facecolor=c_blue_border, edgecolor=c_blue_border, width=1.1, headwidth=4.5, headlength=5.0))
    # Analyze -> Knowledge (Log Violation)
    ax.annotate('', xy=(4.4, 6.40), xytext=(3.4, 6.40),
                arrowprops=dict(facecolor='#DC2626', edgecolor='#DC2626', width=1.1, headwidth=4.5, headlength=5.0))
    draw_card(3.9, 6.75, 0.8, 0.32, '#FEF2F2', '#DC2626', r=0.08, lw=0.8)
    ax.text(3.9, 6.75, "Violation", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#DC2626')

    # Knowledge -> Plan (Trigger Adaptation) at y = 6.40 in Gap 2 [7.0, 8.4]
    ax.annotate('', xy=(8.4, 6.40), xytext=(7.0, 6.40),
                arrowprops=dict(facecolor='#DC2626', edgecolor='#DC2626', width=1.3, headwidth=5.5, headlength=6.0))
    draw_card(7.7, 6.80, 1.20, 0.40, '#FEF2F2', '#DC2626', r=0.10, lw=0.9)
    ax.text(7.7, 6.80, "Trigger\nAdaptation", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#991B1B', linespacing=1.1)

    # Knowledge -> Plan (Read Active Policy Weights) at y = 9.80 in Gap 2 [7.0, 8.4]
    ax.annotate('', xy=(8.4, 9.80), xytext=(7.0, 9.80),
                arrowprops=dict(facecolor=c_amber_border, edgecolor=c_amber_border, width=1.2, headwidth=5.0, headlength=5.5))
    draw_card(7.7, 10.20, 1.20, 0.40, '#FEF3C7', c_amber_border, r=0.10, lw=0.9)
    ax.text(7.7, 10.20, "Read Active\nPolicy $\\theta_{\\mathrm{active}}$", ha='center', va='center', fontsize=6.2, fontweight='bold', color=c_amber_title, linespacing=1.1)

    # -------------------------------------------------------------
    # 3. PLAN: RS-DRL+ 3-STAGE ANYTIME ENGINE (x = 12.9, y = 8.10)
    # Box width: 9.0 -> [8.4, 17.4], height: 6.40 -> [4.90, 11.30]
    # -------------------------------------------------------------
    box_plan = patches.FancyBboxPatch(
        (8.4, 4.90), 9.0, 6.40,
        boxstyle="round,pad=0,rounding_size=0.3",
        facecolor='#FFFFFF', edgecolor=c_emerald_border, linewidth=1.6
    )
    ax.add_patch(box_plan)
    ax.text(12.9, 10.98, "3. PLAN (RS-DRL$^+$ 3-Stage Anytime Adaptation Engine)",
            ha='center', va='center', fontsize=9.6, fontweight='bold', color=c_emerald_title)

    # Stage 1 Card (width 8.4 -> [8.7, 17.1])
    draw_card(12.9, 9.90, 8.4, 1.30, c_purple_fill, c_purple_border, lw=1.3)
    ax.text(12.9, 10.22, r"Stage 1: RS-DRL$^+$ Compiled Policy Proposal",
            ha='center', va='center', fontsize=8.6, fontweight='bold', color=c_purple_title)
    ax.text(12.9, 9.75, r"Nominal Action: $a_0 = \arg\max_{a \in \mathcal{A}} Q(s, a; \theta_{\mathrm{active}}) \quad \cdot \quad \mathcal{O}(1)$ Inference ($0.485\,\mathrm{ms}$)",
            ha='center', va='center', fontsize=7.4, color=c_slate_dark)

    # Arrow Stage 1 -> Stage 2
    ax.annotate('', xy=(12.9, 8.85), xytext=(12.9, 9.25),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.1, headwidth=4.5, headlength=5.5))

    # Stage 2 Card (width 8.4 -> [8.7, 17.1])
    draw_card(12.9, 8.15, 8.4, 1.30, c_amber_fill, c_amber_border, lw=1.3)
    ax.text(12.9, 8.47, "Stage 2: Threat-Aware Margin Gate",
            ha='center', va='center', fontsize=8.6, fontweight='bold', color=c_amber_title)
    ax.text(12.9, 8.00, r"$\Delta_{\min}(s, a_0) \geq 0 \quad \wedge \quad \mathcal{E}(of) \leq \epsilon_{\mathrm{threshold}}$ ?",
            ha='center', va='center', fontsize=7.8, fontweight='bold', color=c_slate_dark)

    # Arrow Stage 2 -> Stage 3 (Violated / Threat)
    ax.annotate('', xy=(12.9, 6.95), xytext=(12.9, 7.50),
                arrowprops=dict(facecolor='#DC2626', edgecolor='#DC2626', width=1.1, headwidth=4.5, headlength=5.5))
    ax.text(12.9, 7.22, "Violated / High Threat", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#DC2626',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#FEF2F2', edgecolor='none'))

    # Stage 3 Card (width 8.4 -> [8.7, 17.1])
    draw_card(12.9, 5.95, 8.4, 1.55, c_emerald_fill, c_emerald_border, lw=1.4)
    ax.text(12.9, 6.45, "Stage 3: Targeted 1-Hop Refiner / Shield (PG-ALR)",
            ha='center', va='center', fontsize=8.6, fontweight='bold', color=c_emerald_title)
    ax.text(12.9, 5.98, r"Micro-Neighborhood $\mathcal{N}(a_0)$ along Top-$m$ SHAP Features ($|\mathcal{N}| \leq 2m + 1$)",
            ha='center', va='center', fontsize=7.2, color=c_slate_dark)
    ax.text(12.9, 5.50, "Surrogate Compliance Check $\\cdot$ Margin-Maximizing Fallback Barrier ($< 3.5\\,\\mathrm{ms}$)",
            ha='center', va='center', fontsize=7.0, fontweight='bold', color='#065F46')

    # -------------------------------------------------------------
    # Exits from 3. PLAN to 4. EXECUTE (Gap 3: [17.4, 19.0], width 1.6)
    # -------------------------------------------------------------
    # Fast Path Arrow (leaving Stage 2 at 17.1, entering Exec at 19.0)
    ax.annotate('', xy=(19.0, 8.15), xytext=(17.1, 8.15),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.3, headwidth=5.5, headlength=6.0))
    draw_card(18.2, 8.55, 1.20, 0.40, '#ECFDF5', '#059669', r=0.10, lw=0.9)
    ax.text(18.2, 8.55, "Fast Path\n(< 0.5 ms)", ha='center', va='center', fontsize=6.5, fontweight='bold', color='#059669', linespacing=1.1)

    # Refined Path Arrow (leaving Stage 3 at 17.1, entering Exec at 19.0)
    ax.annotate('', xy=(19.0, 5.95), xytext=(17.1, 5.95),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.3, headwidth=5.5, headlength=6.0))
    draw_card(18.2, 6.35, 1.20, 0.40, '#ECFDF5', '#065F46', r=0.10, lw=0.9)
    ax.text(18.2, 6.35, "Refined $a^*$\n(< 3.5 ms)", ha='center', va='center', fontsize=6.5, fontweight='bold', color='#065F46', linespacing=1.1)

    # -------------------------------------------------------------
    # 4. EXECUTOR (x = 20.0, y = 8.10) - Width 2.0 -> [19.0, 21.0]
    # -------------------------------------------------------------
    draw_card(20.0, 8.10, 2.0, 5.40, c_emerald_fill, c_emerald_border, lw=1.5)
    ax.text(20.0, 10.35, "4. EXECUTE", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_emerald_title)
    exec_body = (
        "Effector Dispatch\n\n"
        "Dispatches Verified\n"
        "Adaptation\n"
        "$a^* \\in \\mathcal{A}$\n"
        "to System Actuators\n\n"
        "Deterministic\n"
        "Latency $< 0.5\\,\\mathrm{ms}$"
    )
    ax.text(20.0, 8.20, exec_body, ha='center', va='center', fontsize=7.0, color=c_slate_dark, linespacing=1.2)
    ax.text(20.0, 5.75, "Real-Time", ha='center', va='center', fontsize=7.0, fontweight='bold', color='#059669')

    # =============================================================
    # 3. BOTTOM CONTAINER: OFFLINE SG-OS OPTIMIZATION PIPELINE
    # y in [0.60, 3.90] (height 3.30)
    # =============================================================
    box_offline = patches.FancyBboxPatch(
        (0.6, 0.60), 20.8, 3.30,
        boxstyle="round,pad=0,rounding_size=0.35",
        facecolor='#FDF4FF', edgecolor=c_purple_border, linewidth=1.8
    )
    ax.add_patch(box_offline)
    ax.text(1.2, 3.62, "OFFLINE SPECIFICATION-GUIDED REWARD RESHAPING & REPLAY PIPELINE (SG-OS PATTERN)",
            ha='left', va='center', fontsize=10.0, fontweight='bold', color=c_purple_title)

    # Card 1: Experience Buffer (Left)
    draw_card(4.2, 2.05, 6.4, 2.10, '#FFFFFF', c_purple_border)
    ax.text(4.2, 2.70, "Pre-Indexed Experience Replay Buffer", ha='center', va='center', fontsize=8.8, fontweight='bold', color=c_purple_title)
    ax.text(4.2, 2.10, "Offline Transitions: $(s, a, r_{\\mathrm{base}}, s^\\prime, d) \\sim \\mathcal{D}$\nSevere Failure Regime (Over 90% Constraints Violated)",
            ha='center', va='center', fontsize=7.2, color=c_slate_dark, linespacing=1.2)
    ax.text(4.2, 1.40, "Catastrophic & Near-Miss Records", ha='center', va='center', fontsize=6.8, color=c_slate_muted)

    # Arrow: Buffer -> Reshaping Engine
    ax.annotate('', xy=(7.9, 2.05), xytext=(7.4, 2.05),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.3, headwidth=5.0, headlength=6.0))

    # Card 2: Guided Reward Reshaping Engine (Center)
    draw_card(12.3, 2.05, 8.2, 2.10, c_amber_fill, c_amber_border, lw=1.5)
    ax.text(12.3, 2.78, "Guided Reward Reshaping Engine (MU-RS-DRL / CM-RS-DRL)",
            ha='center', va='center', fontsize=8.6, fontweight='bold', color=c_amber_title)
    reshaping_summary = (
        r"• Near-Miss Recoverability: $\mathcal{M}(s, a) = (n_{\mathrm{sat}}/K)^\alpha \exp(-\bar{\Delta}_{\mathrm{def}}/\sigma_\Delta)$" "\n"
        r"• Utility Incentive: $\mathcal{U}_{\mathrm{inc}}(a) = (u(a)/u^{\max})^\beta \quad \cdot \quad$ Target: $\tilde{r}_{\mathrm{opt}} = r_{\mathrm{base}} + \mu \mathcal{U}_{\mathrm{inc}}$" "\n"
        r"• Confidence Buffer Cushion: $\bar{\mathcal{B}}(s, a) \in [0, 1]$ (Absorbs Reality Gap)"
    )
    ax.text(12.3, 1.90, reshaping_summary, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # Arrow: Reshaping -> DQN Policy Learning
    ax.annotate('', xy=(16.9, 2.05), xytext=(16.4, 2.05),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.3, headwidth=5.0, headlength=6.0))

    # Card 3: DQN Policy Learning (Right)
    draw_card(19.1, 2.05, 3.8, 2.10, '#FFFFFF', c_purple_border)
    ax.text(19.1, 2.70, "DQN Policy Learning", ha='center', va='center', fontsize=8.6, fontweight='bold', color=c_purple_title)
    ax.text(19.1, 2.10, "TD-Loss Optimization:\n$\\mathcal{L}(\\theta)$ over mini-batches\nOptimistic Re-labeling",
            ha='center', va='center', fontsize=7.2, color=c_slate_dark, linespacing=1.2)
    ax.text(19.1, 1.40, "Updates Shadow Weights $\\theta_{\\mathrm{train}}$", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#059669')

    # =============================================================
    # OFFLINE POLICY DEPLOYMENT BUS TO SHARED KNOWLEDGE
    # Rises from Card 3 top at (19.1, 3.10) to horizontal corridor y = 4.32
    # Runs left along y = 4.32 to x = 5.7, rises directly into Shared Knowledge bottom at (5.7, 5.35)
    # ZERO intersections with any other lines!
    # =============================================================
    y_bus_offline = 4.32
    path_deploy = [
        (Path.MOVETO, (19.1, 3.10)),
        (Path.LINETO, (19.1, y_bus_offline)),
        (Path.LINETO, (5.7, y_bus_offline)),
        (Path.LINETO, (5.7, 5.35))
    ]
    codes_dep, verts_dep = zip(*path_deploy)
    ax.add_patch(patches.PathPatch(Path(verts_dep, codes_dep), facecolor='none', edgecolor=c_purple_border, lw=1.5, linestyle='--'))
    ax.annotate('', xy=(5.7, 5.35), xytext=(5.7, 5.00),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.4, headwidth=5.5, headlength=6.5))

    # Flow chevrons on deployment bus
    ax.annotate('', xy=(16.8, y_bus_offline), xytext=(17.1, y_bus_offline),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.1, headwidth=4.5, headlength=4.5))
    ax.annotate('', xy=(7.2, y_bus_offline), xytext=(7.5, y_bus_offline),
                arrowprops=dict(facecolor=c_purple_border, edgecolor=c_purple_border, width=1.1, headwidth=4.5, headlength=4.5))

    draw_card(12.0, y_bus_offline, 8.4, 0.42, '#F5F3FF', c_purple_border, r=0.10, lw=1.0)
    ax.text(12.0, y_bus_offline, "Deploy Converged Policy Checkpoint & Surrogates into Shared Knowledge",
            ha='center', va='center', fontsize=7.4, fontweight='bold', color=c_purple_title)

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade full system architecture saved to {output_path}")

if __name__ == '__main__':
    create_system_architecture('figures/fig_system_architecture.png')
