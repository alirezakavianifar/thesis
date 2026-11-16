# Comprehensive Persian Technical Terminology Dictionary

This dictionary defines the mandatory technical vocabulary across all chapters of the doctoral dissertation. Any deviation is strictly prohibited.

| Concept | Mandatory Persian Term | Strictly Banned / Avoided | Specific Rule & Technical Rationale |
| :--- | :--- | :--- | :--- |
| **System** | **`سیستم`** | ❌ `سامانه` | Standardized 100% across the thesis (`سیستم‌های خودوفق`, `سیستم هدف`, `سیستم‌های فیزیکی-سایبری`). The word `سامانه` is completely purged. |
| **Real-Time** | **`بلادرنگ`** | ❌ `زمان‌حقیقی`<br>❌ `زمان واقعی`<br>❌ `بی‌درنگ` | Sole official Academy of Persian Language & Literature & IEEE-Iran term. Never use `زمان واقعی` or call Soft-QoS systems (DeltaIoT 8-min period) real-time. Never stack `برخط بلادرنگ`. |
| **Self-Adaptive Systems** | **`سیستم‌های خودوفق`** | ❌ `سیستم‌های خودتطبیق‌پذیر`<br>❌ `سامانه‌های خودسازگار` | Established academic compound in Iranian computer software engineering. |
| **Self-Adaptation (Capability)** | **`خودوفقی`** | ❌ `خودتطبیقی`<br>❌ `خودسازگاری` | Refers to the architectural property or capability of the system. |
| **Adaptation (Process / Space)** | **`انطباق`** | ❌ `تطبیق` (in this context) | Dynamic action, search, or execution: `فضای وفقی`, `گزینه‌های وفقی`, `اهداف وفقی`, `طرح‌های انطباق`. |
| **Conformance / Verification** | **`انطباق با مشخصه‌ها`** | ❌ `تطابق` | Conformance to formal specifications, SLAs, or contracts. |
| **Comparative Analysis** | **`تحلیل تطبیقی`** | ❌ `تحلیل انطباقی` | `تطبیق` is strictly reserved for comparative cross-evaluation. |
| **Context / Testbed** | **`بستر / زمینه`** | ❌ `بافتار` | `بافتار` is an awkward calque. Use `بستر` for testbeds (DeltaIoT, DARTSim) and `زمینه` for context. |
| **Asynchronous** | **`ناهمگام`** | ❌ `غیرهمگام` | Standard computer systems term for decoupled background operations. |
| **Thread** | **`ریسمان`** | ❌ `نخ` | `ریسمان کنترلی` for execution threads. |
| **Process / Workflow** | **`فرآیند`** | ❌ `پردازه` (unless OS process) | Used for dynamic workflows, MAPE-K phases, MDP processes (`فرآیند تصمیم‌گیری مارکوف`). |
| **Swimlanes** | **`خطوط شناوری`** | ❌ `خطوط شناور` | UML Activity Diagram swimlanes in Figure 4.2. |
| **Critical** | **`بحرانی` (Strictly Disciplined)** | ❌ Rhetorical intensifiers<br>❌ Ambiguous `مسیر بحرانی` | **ONLY** permitted in formal technical terms: `گره‌های بحرانی`, `آستانه‌ها/مرزهای بحرانی`. For system classification, prefer **`سیستم‌های فیزیکی-سایبری حساس و بلادرنگ`** or **`بلادرنگ`** over the clunky calque `مأموریت‌بحرانی`. Never `مهلت بحرانی` (use `مهلت زمانی سخت پروازی`), `چالش‌های بحرانی` (use `چالش‌های بنیادین`), `شرایط بحرانی` (use `شرایط تنش شدید محیطی`), or `تنش بحرانی` (use `فراتر رفتن تنش از آستانه بحرانی`). For systems execution paths, avoid `مسیر بحرانی` and use **`مسیر مستقیم کنترل برخط / مسیر زمان اجرای کنترل (\lr{Critical Path})`**. |
| **Speed & Latency** | **`بلادرنگ / کم‌تأخیر / زیر میلی‌ثانیه‌ای / مسیر سریع (Fast Path)`** | ❌ `سریع` (as casual intensifier)<br>❌ `فوق‌سریع` | Never use `سریع` casually for latency. Always state the quantitative metric directly (`زیر میلی‌ثانیه‌ای`, `$0.485\,\text{ms}$`) or use formal engineering terms (`بلادرنگ`, `کم‌تأخیر`, `مسیر سریع`). `سریع` is strictly permitted ONLY in: (1) formal pattern names (`«مسیر سریع» (\lr{Fast Path})`), (2) empirical speedup ratios (`۲۷۰ برابر سریع‌تر`), (3) learning convergence dynamics (`همگرایی سریع‌تر / تسریع همگرایی`), and (4) physical avionics dynamics (`تخلیه سریع باتری`). |
| **Immediate Reward** | **`پاداش آنی`** | ❌ `پاداش لحظه‌ای` | Standard MDP mathematical translation for $R(s, a, s')$. |
| **Vital / Crucial** | **`کلیدی / بنیادین / تعیین‌کننده`** | ❌ `حیاتی` | `حیاتی` is completely banned due to journalistic exaggeration. |
| **Baseline Method** | **`روش پایه‌ای RS-DRL`** | ❌ `متد`, `الگوریتم کلی` | Foundational single-tier algorithmic formulation. |
| **Generalized Architecture** | **`معماری تعمیم‌یافته RS-DRL+`**| ❌ `روش تعمیم‌یافته` | Two-tier contract-anytime software architecture. |
| **Holistic Framework** | **`چارچوب`** | ❌ `فریم‌ورک` | The overarching theoretical and engineering construct. |
| **Architectural Patterns** | **`الگوهای معماری SG-OS و CAE-PV`** | ❌ `روش‌های SG-OS` | Software engineering design patterns. |
| **Batch & Mini-batch** | **`دسته / دسته‌های کوچک داده`** | ❌ `مینی‌بچ`<br>❌ `بچ` | Standardized across TMU, Sharif, and UT computing documents. Colloquial transliterations (`مینی‌بچ` / `بچ`) are 100% purged. |
| **Static** | **`ایستا`** | ❌ `استاتیک` | Standard Persian computer systems terminology (`سپرهای ایمنی ایستا`, `اهداف غیربرخط ایستا`). |
| **Mechanism** | **`سازوکار`** | ❌ `مکانیسم` | Official Academy term standardized 100% across the thesis (`سازوکارهای شکل‌دهی پاداش`). |
| **Platform** | **`بستر / سکو`** | ❌ `پلتفرم` | Always use `بستر پیاده‌سازی` or `بستر آزمایشگاهی/محک`. |
| **Factor / Multiplier** | **`ضریب`** | ❌ `فاکتور` | Mathematical multipliers ($\gamma, \rho, \beta, \sigma$) must strictly be `ضریب` (`ضریب تنزیل زمانی`, `ضریب شکل‌دهی پاداش`, `ضریب مقیاس`). For environmental conditions, use `عوامل محیطی / متغیرهای کنترلی`. |
| **Replay Buffer** | **`بافر بازپخش`** | ❌ `میانگیر بازپخش` | Established standard term in Iranian AI & DRL departments. |
| **Candidate Actions** | **`کاندیداها / گزینه‌های کاندید`** | ❌ `گزینه‌های نامزد` | In optimization and AI literature, `کاندید` is standard; `نامزد` connotes elections. |
| **Offline / Online** | **`غیربرخط / برخط`** | ❌ `آفلاین / آنلاین`، `برون‌خط` | Standardized across all chapters per Academy/TMU convention. |
| **Operational Logs** | **`سوابق عملیاتی / سوابق غیربرخط`** | ❌ `لاگ`، `لاگ‌ها`، `گزارش` (ambiguous)، `وقایع‌نگاشت` | Standardized formal Persian academic terminology. Anchor with `\LTRfootnote{Operational Logs}` on first chapter mention; reserve `ردپا` exclusively for environmental traces. |
| **Formal Verification** | **`اعتبارسنجی صوری`** | ❌ Inconsistent mixing with `راستی‌آزمایی صوری` | Standardized as `اعتبارسنجی صوری` for formal verification with UPPAAL-SMC. |
| **Model Checking** | **`وارسی مدل (آماری)`** | ❌ `مدل‌چکینگ` | Standardized formal methods terminology. |
| **Diagram** | **`نمودار`** | ❌ `دیاگرام` | Formal Persian academic terminology (`نمودار فعالیت`). |
| **Hardware Driver** | **`راه‌انداز (سخت‌افزاری)`** | ❌ `درایور` | Standard Persian systems engineering term. |
| **Fallback** | **`پشتیبان (شاخه / قاعده / سازوکار)`** | ❌ `فال‌بک` | Formal Persian equivalent for fallback control branches. |
| **Gate** | **`دروازه (تنش / حاشیه)`** | ❌ `گیت` | Formal Persian equivalent for runtime safety gating. |
| **Atomic** | **`تجزیه‌ناپذیر`** | ❌ `اتمیک` | Formal Persian concurrency term (`تبادل تجزیه‌ناپذیر وزن‌ها`). |
| **Scalar** | **`نرده‌ای`** | ❌ `اسکالر` | Official Persian mathematical terminology (`پاداش نرده‌ای`). |
| **Probe** | **`کاوشگر`** | ❌ `پروب` | Standard Persian telemetry term (`کاوشگرهای حسگری / پایش`). |
| **Link** | **`پیوند`** | ❌ `لینک` | Standard Persian networking term (`پیوندهای رادیویی`). |
| **Mode** | **`حالت`** | ❌ `مد` | Unambiguous formal Persian term (`حالت‌های غیرعملیاتی`). |
| **Calibration** | **`واسنجی`** | ❌ `کالیبراسیون` | Official Academy of Persian Language & Literature term. |
| **Catalog** | **`فهرست جامع`** | ❌ `کاتالوگ` | Formal Persian academic equivalent. |
| **Frequency** | **`بسامد` (کنترلی) / `تواتر` (به‌روزرسانی)** | ❌ `فرکانس` | Distinguishing physical rate (`بسامد`) from update rate (`تواتر`). |
| **Isolate / Isolation** | **`مجزا / جدا کردن / جداسازی`** | ❌ `ایزوله / ایزوله‌سازی` | Formal Persian architectural separation terminology. |
| **Theoretical** | **`نظری / به صورت نظری`** | ❌ `تئوریک` | Standard Persian academic writing. |
| **Formulation** | **`فرمول‌بندی`** | ❌ `فرموله / فرمولاسیون` | Consistent Persian academic usage. |
| **Avionics** | **`الکترونیک پروازی`** | ❌ `اویونیک` | Formal Persian aerospace engineering equivalent. |

