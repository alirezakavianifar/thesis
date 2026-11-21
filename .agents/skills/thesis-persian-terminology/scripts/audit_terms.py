#!/usr/bin/env python3
"""
Comprehensive Persian Terminology Audit Script for Thesis Source Files.
Scans chapters/*.tex and thesis_full_toc_persian_v3.tex for prohibited terms
according to the comprehensive Persian terminological dictionary.
"""

import sys
import re
from pathlib import Path

# Mapping of prohibited regex pattern to (mandatory replacement, explanation)
TERM_RULES = [
    (r"\bسامانه\b", "سیستم", "سامانه 100% strictly banned; use سیستم"),
    (r"\bسامانه‌ها\b", "سیستم‌ها", "سامانه‌ها 100% strictly banned; use سیستم‌ها"),
    (r"\bسامانه‌های\b", "سیستم‌های", "سامانه‌های 100% strictly banned; use سیستم‌های"),
    (r"زمان[- ]واقعی", "بلادرنگ", "زمان واقعی banned; use بلادرنگ"),
    (r"زمان[- ]حقیقی", "بلادرنگ", "زمان حقیقی banned; use بلادرنگ"),
    (r"\bبی‌درنگ\b", "بلادرنگ", "بی‌درنگ avoided; use بلادرنگ"),
    (r"\bمکانیسم\b", "سازوکار", "مکانیسم banned; use سازوکار"),
    (r"\bمکانیسم‌ها\b", "سازوکارها", "مکانیسم‌ها banned; use سازوکارها"),
    (r"\bمکانیسم‌های\b", "سازوکارهای", "مکانیسم‌های banned; use سازوکارهای"),
    (r"\bاستاتیک\b", "ایستا", "استاتیک banned; use ایستا"),
    (r"\bمینی[ -]?بچ\b", "دسته‌های کوچک داده", "مینی‌بچ banned; use دسته‌های کوچک داده"),
    (r"\bحیاتی\b", "کلیدی / بنیادین / تعیین‌کننده", "حیاتی banned due to journalistic tone"),
    (r"\bنوین\b", "پیشنهادی / پیشرفته / مدرن / جدید", "نوین 100% banned; use پیشنهادی or modern"),
    (r"\bانقلابی\b", "مؤثر / پیشرفته", "انقلابی banned hype word"),
    (r"\bشگفت‌انگیز\b", "اثبات‌شده / مؤثر", "شگفت‌انگیز banned hype word"),
    (r"\bدگرگون‌ساز\b", "اثرگذار / توسعه‌یافته", "دگرگون‌ساز banned hype word"),
    (r"\bچشمگیر\b", "به طور قابل‌ملاحظه‌ای / شدید", "چشمگیر banned; report quantitative delta"),
    (r"\bفوق‌العاده\b", "بسیار / با رواداری محدود", "فوق‌العاده banned hype intensifier"),
    (r"\bفوق‌سریع\b", "بلادرنگ / زیر میلی‌ثانیه‌ای", "فوق‌سریع banned; state exact latency bound"),
    (r"\bلاگ\b", "سوابق", "لاگ banned; use سوابق عملیاتی / سوابق غیربرخط"),
    (r"\bلاگ‌ها\b", "سوابق", "لاگ‌ها banned; use سوابق عملیاتی"),
    (r"\bتئوریک\b", "نظری", "تئوریک banned; use نظری"),
    (r"\bفرمولاسیون\b", "فرمول‌بندی", "فرمولاسیون banned; use فرمول‌بندی"),
    (r"\bپلتفرم\b", "بستر / سکو", "پلتفرم banned; use بستر پیاده‌سازی / سکو"),
    (r"\bفال‌بک\b", "پشتیبان", "فال‌بک banned; use پشتیبان"),
    (r"\bاتمیک\b", "تجزیه‌ناپذیر", "اتمیک banned; use تجزیه‌ناپذیر"),
    (r"\bاسکالر\b", "نرده‌ای", "اسکالر banned; use نرده‌ای"),
    (r"\bکالیبراسیون\b", "واسنجی", "کالیبراسیون banned; use واسنجی"),
    (r"\bکاتالوگ\b", "فهرست جامع", "کاتالوگ banned; use فهرست جامع"),
    (r"\bفرکانس\b", "بسامد / تواتر", "فرکانس banned; use بسامد (کنترلی) or تواتر (به‌روزرسانی)"),
    (r"\bایزوله\b", "مجزا / جداسازی", "ایزوله banned; use مجزا / جداسازی"),
    (r"\bمدل‌چکینگ\b", "وارسی مدل", "مدل‌چکینگ banned; use وارسی مدل"),
    (r"\bدیاگرام\b", "نمودار", "دیاگرام banned; use نمودار"),
    (r"\bدرایور\b", "راه‌انداز", "درایور banned; use راه‌انداز"),
    (r"\bاویونیک\b", "الکترونیک پروازی", "اویونیک banned; use الکترونیک پروازی"),
    (r"\bغیرهمگام\b", "ناهمگام", "غیرهمگام banned; use ناهمگام"),
    (r"\bبافتار\b", "بستر / زمینه", "بافتار banned calque; use بستر / زمینه"),
    (r"\bخودتطبیق‌پذیر\b", "خودوفق", "خودتطبیق‌پذیر banned; use خودوفق"),
    (r"\bخودتطبیقی\b", "خودوفقی", "خودتطبیقی banned; use خودوفقی"),
    (r"\bاقدام[‌های]* انطباقی\b", "اقدام وفقی", "اقدام انطباقی banned; use اقدام وفقی"),
    (r"\bگزینه[‌های]* انطباقی\b", "گزینه‌های وفقی", "گزینه‌های انطباقی banned; use گزینه‌های وفقی"),
    (r"\bاهداف انطباقی\b", "اهداف وفقی", "اهداف انطباقی banned; use اهداف وفقی"),
    (r"\bاستنتاج انطباقی\b", "استنتاج وفقی", "استنتاج انطباقی banned; use استنتاج وفقی"),
    (r"\bگزینه‌های انطباق\b", "گزینه‌های وفقی", "گزینه‌های انطباق banned; use گزینه‌های وفقی"),
    (r"\bسیستم‌های خودوفقی\b", "سیستم‌های خودوفق", "سیستم‌های خودوفقی banned; use سیستم‌های خودوفق"),
    (r"\bگزینه‌های نامزد\b", "گزینه‌های کاندید", "نامزد banned in optimization; use کاندید"),
    (r"\bمیانگیر بازپخش\b", "بافر بازپخش", "میانگیر banned in RL; use بافر بازپخش"),
    (r"شرایط مسابقه", "شرایط رقابتی", "شرایط مسابقه banned; use شرایط رقابتی"),
    (r"ت[اأ]خیر نوسانی", "نوسان تأخیر", "تأخیر نوسانی banned; use نوسان تأخیر"),
    (r"نخ[- ]?امن", "ریسمان‌امن", "نخ‌امن banned; use ریسمان‌امن"),
    (r"صف کاربری ناهمگام", "صف وظایف ناهمگام", "صف کاربری ناهمگام banned; use صف وظایف ناهمگام"),
    (r"مدیریت همزمانی بدون قفل", "کنترل همروندی بدون قفل", "مدیریت همزمانی بدون قفل avoided; use کنترل همروندی بدون قفل"),
]

COMPILED_RULES = [(re.compile(p), repl, desc) for p, repl, desc in TERM_RULES]

def audit_file(file_path: Path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    violations = []
    for line_idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("%"):
            continue
        # Strip \lr{...} blocks to avoid flagging English references or package names
        clean_line = re.sub(r"\\lr\{[^}]*\}", "", line)
        # Strip comment tails
        clean_line = re.sub(r"(?<!\\)%.*$", "", clean_line)

        for pattern, repl, desc in COMPILED_RULES:
            for match in pattern.finditer(clean_line):
                violations.append({
                    "line": line_idx,
                    "matched": match.group(0),
                    "replacement": repl,
                    "desc": desc,
                    "context": stripped[:120]
                })
    return violations

def main():
    apply_fix = "--fix" in sys.argv
    root_dir = Path("e:/projects/thesis")
    tex_files = sorted(list(root_dir.glob("chapters/*.tex")) + [root_dir / "thesis_full_toc_persian_v3.tex"])

    total_violations = 0
    all_reports = {}

    for f in tex_files:
        if not f.exists():
            continue
        v_list = audit_file(f)
        all_reports[f.name] = v_list
        total_violations += len(v_list)

    print("=" * 70)
    print(" " * 15 + "PERSIAN TERMINOLOGY AUDIT REPORT")
    print("=" * 70)

    for fname, violations in all_reports.items():
        if violations:
            print(f"\n[X] {fname}: {len(violations)} violation(s)")
            for v in violations:
                print(f"  Line {v['line']}: `{v['matched']}` -> `{v['replacement']}` ({v['desc']})")
        else:
            print(f"[PASS] {fname}: 100% Compliant (0 violations)")

    print("\n" + "=" * 70)
    print(f"TOTAL VIOLATIONS FOUND: {total_violations}")
    print("=" * 70)

    return 1 if total_violations > 0 else 0

if __name__ == "__main__":
    sys.exit(main())

