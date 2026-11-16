---
name: thesis-persian-terminology
description: >-
  Audits and enforces the standardized Persian academic terminology across all thesis chapters and LaTeX files. Use when checking for banned terms (e.g. سامانه, زمان واقعی, مینی‌بچ, حیاتی, مکانیسم), harmonizing vocabulary, or reviewing new or edited Persian paragraphs.
---

# Persian Academic Terminology Enforcement Skill

This skill enforces the standardized, mandatory Persian technical vocabulary across all chapters of the doctoral dissertation (`thesis_full_toc_persian_v3.tex`, `chapters/*.tex`).

## Core Rules

Any deviation from the standardized terminology is strictly prohibited across all chapters, abstracts, appendices, and front matter.

### Mandatory Equivalents (Summary Table)

| Concept | Mandatory Persian Term | Strictly Banned / Avoided |
| :--- | :--- | :--- |
| **System** | **`سیستم`** | ❌ `سامانه` (100% strictly purged) |
| **Real-Time** | **`بلادرنگ`** | ❌ `زمان‌حقیقی`, `زمان واقعی`, `بی‌درنگ` |
| **Self-Adaptive Systems** | **`سیستم‌های خودوفق`** | ❌ `سیستم‌های خودتطبیق‌پذیر`, `سامانه‌های خودسازگار` |
| **Self-Adaptation (Capability)** | **`خودوفقی`** | ❌ `خودتطبیقی`, `خودسازگاری` |
| **Adaptation (Process / Space)** | **`انطباق`** | ❌ `تطبیق` (in this context) |
| **Conformance / Verification** | **`انطباق با مشخصه‌ها`** | ❌ `تطابق` |
| **Comparative Analysis** | **`تحلیل تطبیقی`** | ❌ `تحلیل انطباقی` |
| **Context / Testbed** | **`بستر / زمینه`** | ❌ `بافتار` |
| **Asynchronous** | **`ناهمگام`** | ❌ `غیرهمگام` |
| **Thread** | **`ریسمان`** | ❌ `نخ` |
| **Process / Workflow** | **`فرآیند`** | ❌ `پردازه` (unless OS process) |
| **Critical** | **`بحرانی` (Strictly disciplined)** | ❌ Casual rhetorical intensifiers |
| **Speed & Latency** | **`بلادرنگ / کم‌تأخیر / زیر میلی‌ثانیه‌ای`** | ❌ `سریع` (as casual intensifier), `فوق‌سریع` |
| **Immediate Reward** | **`پاداش آنی`** | ❌ `پاداش لحظه‌ای` |
| **Vital / Crucial** | **`کلیدی / بنیادین / تعیین‌کننده`** | ❌ `حیاتی` |
| **Batch & Mini-batch** | **`دسته / دسته‌های کوچک داده`** | ❌ `بچ`, `مینی‌بچ` |
| **Static** | **`ایستا`** | ❌ `استاتیک` |
| **Mechanism** | **`سازوکار`** | ❌ `مکانیسم` |
| **Platform** | **`بستر / سکو`** | ❌ `پلتفرم` |
| **Factor / Multiplier** | **`ضریب`** | ❌ `فاکتور` |
| **Replay Buffer** | **`بافر بازپخش`** | ❌ `میانگیر بازپخش` |
| **Candidate Actions** | **`کاندیداها / گزینه‌های کاندید`** | ❌ `گزینه‌های نامزد` |
| **Offline / Online** | **`غیربرخط / برخط`** | ❌ `آفلاین / آنلاین`, `برون‌خط` |
| **Operational Logs** | **`سوابق عملیاتی / سوابق غیربرخط`** | ❌ `لاگ`, `وقایع‌نگاشت` |
| **Formal Verification** | **`اعتبارسنجی صوری`** | ❌ Mixed `راستی‌آزمایی صوری` |
| **Model Checking** | **`وارسی مدل (آماری)`** | ❌ `مدل‌چکینگ` |
| **Fallback** | **`پشتیبان (شاخه / قاعده)`** | ❌ `فال‌بک` |
| **Gate** | **`دروازه (تنش / حاشیه)`** | ❌ `گیت` |
| **Atomic** | **`تجزیه‌ناپذیر`** | ❌ `اتمیک` |
| **Scalar** | **`نرده‌ای`** | ❌ `اسکالر` |
| **Frequency** | **`بسامد` (کنترلی) / `تواتر` (به‌روزرسانی)** | ❌ `فرکانس` |
| **Isolate / Isolation** | **`مجزا / جدا کردن / جداسازی`** | ❌ `ایزوله / ایزوله‌سازی` |
| **Theoretical** | **`نظری / به صورت نظری`** | ❌ `تئوریک` |
| **Formulation** | **`فرمول‌بندی`** | ❌ `فرمولاسیون` |
| **Avionics** | **`الکترونیک پروازی`** | ❌ `اویونیک` |

For full details and technical rationales, see [terminology_dictionary.md](./references/terminology_dictionary.md).

---

## Automated Terminology Audit Runbook

To scan the entire dissertation for prohibited terms:
```powershell
python .agents/skills/thesis-persian-terminology/scripts/audit_terms.py
```

To automatically preview or replace simple violations:
```powershell
python .agents/skills/thesis-persian-terminology/scripts/audit_terms.py --fix
```

