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
    (r"\bنرده‌ای\b", "عددی / مقدار عددی", "نرده‌ای is archaic and misleading in RL; use عددی / مقدار عددی"),
    (r"\bمهندسان دامنه\b", "خبرگان حوزه کاربرد", "مهندسان دامنه is an awkward calque; use خبرگان حوزه کاربرد"),
    (r"\bدامنه عملیاتی\b", "قلمرو عملیاتی", "Use قلمرو عملیاتی for Operational Envelope"),
    (r"\bکالیبراسیون\b", "واسنجی", "کالیبراسیون banned; use واسنجی"),
    (r"\bکاتالوگ\b", "فهرست جامع", "کاتالوگ banned; use فهرست جامع"),
    (r"\bفرکانس\b", "بسامد / تواتر", "فرکانس banned; use بسامد (کنترلی) or تواتر (به‌روزرسانی)"),
    (r"\bایزوله\b", "مجزا / جداسازی", "ایزوله banned; use مجزا / جداسازی"),
    (r"\bمدل‌چکینگ\b", "وارسی مدل", "مدل‌چکینگ banned; use وارسی مدل"),
    (r"\bدیاگرام\b", "نمودار", "دیاگرام banned; use نمودار"),
    (r"\bدرایور(?:ها|های|ی)?\b", "راه‌انداز / راه‌اندازها", "درایور banned; use راه‌انداز"),
    (r"\bاویونیک\b", "الکترونیک پروازی", "اویونیک banned; use الکترونیک پروازی"),
    (r"\bغیرهمگام\b", "ناهمگام", "غیرهمگام banned; use ناهمگام"),
    (r"\bبافتار\b", "بستر / زمینه", "بافتار banned calque; use بستر / زمینه"),
    (r"\bخودتطبیق‌پذیر\b", "خودوفق", "خودتطبیق‌پذیر banned; use خودوفق"),
    (r"\bخودتطبیقی\b", "خودوفقی", "خودتطبیقی banned; use خودوفقی"),
    (r"\bتطبیق[\s\u200c]*پذیر(?:ی)?\b", "وفقی / قابلیت انطباق", "تطبیق‌پذیر/ی banned; use وفقی / قابلیت انطباق"),
    (r"\bاقدام[‌های]* انطباقی\b", "اقدام وفقی", "اقدام انطباقی banned; use اقدام وفقی"),
    (r"\bگزینه[‌های]* انطباقی\b", "گزینه‌های وفقی", "گزینه‌های انطباقی banned; use گزینه‌های وفقی"),
    (r"\bاهداف انطباقی\b", "اهداف وفقی", "اهداف انطباقی banned; use اهداف وفقی"),
    (r"\bاستنتاج انطباقی\b", "استنتاج وفقی", "استنتاج انطباقی banned; use استنتاج وفقی"),
    (r"\bگزینه‌های انطباق\b", "گزینه‌های وفقی", "گزینه‌های انطباق banned; use گزینه‌های وفقی"),
    (r"\bسیستم‌های خودوفقی\b", "سیستم‌های خودوفق", "سیستم‌های خودوفقی banned; use سیستم‌های خودوفق"),
    (r"\bگزینه‌های نامزد\b", "گزینه‌های کاندید", "نامزد banned in optimization; use کاندید"),
    (r"\bمیانگیر بازپخش\b", "بافر بازپخش", "میانگیر banned in RL; use بافر بازپخش"),
    (r"\bفاز برنامه‌ریزی\b", "مرحله برنامه‌ریزی", "فاز برنامه‌ریزی contains loanword; use مرحله برنامه‌ریزی"),
    (r"\bفاز پیش[ -]?پرواز\b", "مرحله پیش‌پرواز", "فاز پیش‌پرواز contains loanword; use مرحله پیش‌پرواز"),
    (r"\bگردش فرآیندی\b", "جریان کاری", "گردش فرآیندی awkward calque; use جریان کاری"),
    (r"\bفرآیند اعتبارسنجی صوری\b", "اعتبارسنجی صوری", "فرآیند اعتبارسنجی صوری is pleonastic; use اعتبارسنجی صوری"),
    (r"شرایط مسابقه", "شرایط رقابتی", "شرایط مسابقه banned; use شرایط رقابتی"),
    (r"ت[اأ]خیر نوسانی|پرش زمانی(?:\s+ت[اأ]خیر)?", "نوسان تأخیر", "تأخیر نوسانی و پرش زمانی تأخیر banned; use نوسان تأخیر"),
    (r"روش‌های مرجع ایستا|پیکربندی مرجع ایستا", "پیکربندی ایستا / روش‌های مقایسه‌ای", "مرجع ایستا ambiguous with bibliography; use پیکربندی ایستا / روش‌های مقایسه‌ای"),
    (r"\bخط(?:وط)?[\s\u200c]+پایه\b", "روش‌های رقیب / روش‌های مقایسه‌ای / مبنای مقایسه", "خط پایه is a literal baseline calque; use روش‌های رقیب / مقایسه‌ای / مبنا"),
    (r"نخ[- ]?امن", "ریسمان‌امن", "نخ‌امن banned; use ریسمان‌امن"),
    (r"صف کاربری ناهمگام", "صف وظایف ناهمگام", "صف کاربری ناهمگام banned; use صف وظایف ناهمگام"),
    (r"مدیریت همزمانی بدون قفل", "کنترل همروندی بدون قفل", "مدیریت همزمانی بدون قفل avoided; use کنترل همروندی بدون قفل"),
    (r"مرجع عددی", "سناریوهای عددی مرجع / مثال‌های اجرایی عددی", "مرجع عددی ambiguous/inverted; use سناریوهای عددی مرجع"),
    (r"لایه مقدماتی", "سطح اول کنترل برخط", "لایه مقدماتی misleading for real-time inference; use سطح اول کنترل برخط"),
    (r"شبیه‌سازی‌های مقدماتی", "شبیه‌سازی‌های اولیه", "شبیه‌سازی‌های مقدماتی avoided; use شبیه‌سازی‌های اولیه"),
    (r"اعمال بر راه‌اندازها", "صدور فرمان‌ها به عملگرها", "اعمال بر راه‌اندازها defective phrasing; use صدور فرمان‌ها به عملگرها"),
    (r"فراپارامترهای بنیادین", "فراپارامترهای کلیدی", "بنیادین inflation on parameters; use فراپارامترهای کلیدی"),
    (r"\bمهندسین\b", "مهندسان", "مهندسین non-standard plural in academic Persian; use مهندسان"),
    (r"محافظ[هە][\u200c\s]?کارانه\s+منفعل|محافظ[هە][\u200c\s]?کارانه\s+انفعالی", "رفتارهای انفعالی (پدیده ایمنی ناشی از انفعال)", "محافظه‌کارانه منفعل awkward compound; use رفتارهای انفعالی"),
    (r"مرحله اجرای تجزی[هە][\u200c\s]?ناپذیر", "مرحله اجرا و اعمال فرمان‌های انطباق", "تجزیه‌ناپذیر misplaced on MAPE-K execute phase; use مرحله اجرا و اعمال فرمان‌های انطباق"),
    (r"جفت[\s\u200c]*های\s+عمل-حالت", "زوج‌های حالت-عمل", "جفت‌های عمل-حالت inverted and informal; use زوج‌های حالت-عمل"),
    (r"جفت[\s\u200c]*های\s+ناهمخوان", "زوج‌های ناهمخوان", "جفت‌های ناهمخوان informal in statistics; use زوج‌های ناهمخوان"),
    (r"جفت[\s\u200c]*(?:های\s+)?متناظر", "زوج‌های متناظر", "جفت‌های متناظر informal in statistics; use زوج‌های متناظر"),
    (r"توابع پتانسیل دستی", "توابع پتانسیل دست‌ساز", "توابع پتانسیل دستی awkward calque; use توابع پتانسیل دست‌ساز"),
    (r"ویژگی‌های[\s\u200c]*دستکاری‌شده", "ابعاد متغیر در پالایش موضعی", "ویژگی‌های دستکاری‌شده pejorative tone; use ابعاد متغیر در پالایش موضعی"),
    (r"چرخه[\s\u200c]*وفقی", "چرخه انطباق", "چرخه وفقی incorrect relative adjective; use چرخه انطباق"),
    (r"طرح[\s\u200c]*وفقی", "طرح انطباق", "طرح وفقی incorrect relative adjective; use طرح انطباق"),
    (r"فرآیند[\s\u200c]*وفقی", "فرآیند انطباق", "فرآیند وفقی incorrect relative adjective; use فرآیند انطباق"),
    (r"تصمیمات[\s\u200c]*وفقی", "تصمیمات انطباق", "تصمیمات وفقی incorrect relative adjective; use تصمیمات انطباق"),
    (r"اعمال[\s\u200c]*وفقی", "اقدامات وفقی", "اعمال وفقی ambiguous Arabic plural; use اقدامات وفقی"),
    (r"سه سطح رواداری سخت‌گیرانه\s+\$v_1\$", "سه سطح رواداری ملایم ($v_1$)، متوسط ($v_2$) و سخت‌گیرانه ($v_3$)", "سه سطح رواداری سخت‌گیرانه contradictory with mild/moderate corridor definitions"),
    (r"\bفرامین\b", "فرمان‌ها / فرمان‌های کنترلی", "فرامین archaic broken plural; use فرمان‌ها / فرمان‌های کنترلی"),
    (r"حلقه‌های بازخوردی", "حلقه‌های بازخورد", "حلقه‌های بازخوردی non-standard; use حلقه‌های بازخورد"),
    (r"پاداش بازخوردی", "پاداش", "پاداش بازخوردی pleonastic; use پاداش / سیگنال پاداش"),
    (r"اعتبارسنجی صوری بازخورد", "اعتبارسنجی صوری در مسیر بازخورد", "اعتبارسنجی صوری بازخورد misleading ezafe; use اعتبارسنجی صوری در مسیر بازخورد"),
    (r"وضعیت مفروض", "وضعیت ارزیابی‌شده / حالت جاری", "وضعیت مفروض ambiguous; use وضعیت ارزیابی‌شده / حالت جاری"),
    (r"غیر[\s\u200c]*انسدادی", "غیرمسدودکننده", "غیرانسدادی non-standard calque; use غیرمسدودکننده / بدون مسدودسازی"),
    (r"فیلتر[\s\u200c]*انسدادی", "فیلتر مسدودکننده", "فیلتر انسدادی non-standard calque; use فیلتر مسدودکننده"),
    (r"مرز[\s\u200c]*عدم[\s\u200c]*انسداد", "مرز تفکیک غیرمسدودکننده", "مرز عدم‌انسداد awkward calque; use مرز تفکیک غیرمسدودکننده"),
    (r"انسداد محاسباتی", "وقفه محاسباتی / توقف محاسباتی", "انسداد محاسباتی literal calque; use وقفه محاسباتی / توقف محاسباتی"),
    (r"محیط[\s\u200c]*سخت[\s\u200c]*گیرانه", "محیط بسیار مقید / با قیود شدید", "محیط سخت‌گیرانه anthropomorphic calque; use محیط بسیار مقید / با قیود شدید"),
    (r"انسداد یا نوسان ت[اآأ]خیر", "توقف مسیر اجرا ... نوسان در تأخیر", "انسداد یا نوسان تأخیر ambiguous false parallelism; decouple blocking from latency jitter"),
    (r"پیشنهاد[‌های]*\s+نامی", "پیشنهاد پایه سیاست / پیشنهاد اولیه سیاست", "پیشنهاد نامی is an ambiguous calque; use پیشنهاد پایه سیاست"),
    (r"مسیر[\s\u200c]+سریع[\s\u200c]+نامی", "مسیر سریع پایه", "مسیر سریع نامی uses banned نامی; use مسیر سریع پایه"),
    (r"اقدام[‌های]*\s+نامی", "اقدام پایه / اقدام وفقی", "اقدام نامی is ambiguous; use اقدام پایه / اقدام وفقی"),
    (r"کاندیدای\s+نامی", "کاندیدای پایه", "کاندیدای نامی is ambiguous; use کاندیدای پایه"),
    (r"گزینه\s+نامی", "گزینه پایه", "گزینه نامی is ambiguous; use گزینه پایه"),
    (r"اقدام\s+زمان[‌ ]اجرا", "اقدام در زمان اجرا / اقدام وفقی", "اقدام زمان اجرا is a broken compound; use اقدام در زمان اجرا or اقدام وفقی"),
    (r"برتری\s+مجانبی", "برتری در عملکرد پایدار بلندمدت", "برتری مجانبی is a stiff narrative calque; use برتری در عملکرد پایدار بلندمدت"),
    (r"گذارای\b", "گذرای / موقت", "گذارای with intrusive alif is an orthographic error; use گذرای or موقت"),
    (r"بهینه[\s\u200c]*بینانه", "پاداش خوش‌بینانه پویا", "بهینه‌بینانه is a malformed portmanteau; use پاداش خوش‌بینانه"),
    (r"\bمدنظر\b", "هدف / انتخابی / مورد بررسی", "مدنظر is bureaucratic padding; use direct active nouns/verbs"),
    (r"رواداری\s+خطای\s+مطلوب", "حاشیه خطای مجاز", "رواداری خطای مطلوب is polysemous/subjective in SMC; use حاشیه خطای مجاز"),
    (r"اثبات\s+صوری\s+گزاره", "اثبات دقیق ریاضی گزاره", "اثبات صوری گزاره risks colloquial ambiguity (superficial/nominal); use اثبات دقیق ریاضی گزاره"),
    (r"رژیم[\s\u200c]*رواداری", "سطح رواداری", "رژیم رواداری contains political/diet loanword; use سطح رواداری or رده رواداری"),
    (r"نوسانات[\s\u200c]*فیزیکی[\s\u200c]*شتابان", "نوسانات سریع فیزیکی", "نوسانات فیزیکی شتابان is anthropomorphic; use نوسانات سریع فیزیکی"),
    (r"بازه‌های[\s\u200c]*زمانی[\s\u200c]*سخت[\s\u200c]*و[\s\u200c]*قطعی", "مهلت‌های زمانی سخت", "بازه‌های زمانی سخت و قطعی mixes intervals with deadlines; use مهلت‌های زمانی سخت"),
    (r"کوری[\s\u200c]*سازوکار", "عدم حساسیت سازوکار", "کوری سازوکار is sensationalist anthropomorphism; use عدم حساسیت سازوکار"),
    (r"پهنا\s+و\s+عم[قث]\s+شکست", "تعداد قیود نقض‌شده و شدت انحراف", "پهنا و عمق شکست is an awkward spatial metaphor; use تعداد قیود نقض‌شده و شدت انحراف"),
    (r"پالایش[\s\u200c]*موضعی", "پالایش محلی", "پالایش موضعی is non-standard; use پالایش محلی to match بهینه‌های محلی"),
    (r"شکل[\s\u200c]*یافته[\s\u200c]*هدایت[\s\u200c]*شده", "پاداش شکل‌دهی‌شده با هدایت مشخصه‌ها", "شکل‌یافته هدایت‌شده double passive participle; use پاداش شکل‌دهی‌شده با هدایت مشخصه‌ها"),
    (r"(?:رگرسیون[\s\u200c]*)?راهزن[\s\u200c]*زمین[هە][\s\u200c]*آگاه", "تصمیم‌گیری تک‌گامی وابسته به زمینه", "راهزن زمینه‌آگاه is a jarring calque of Contextual Bandit; use تصمیم‌گیری تک‌گامی وابسته به زمینه"),
    (r"احتمال[\s\u200c]*هدایت[\s\u200c]*شده", "احتمال شکل‌دهی هدایت‌شده", "احتمال هدایت‌شده awkward calque; use احتمال شکل‌دهی هدایت‌شده"),
    (r"ماژول\s+\\pgalr|ماژول\s+PG-ALR|ماژول[\s\u200c]+پالایش\s+محلی", "سازوکار \\pgalr / پالایش محلی", "ماژول PG-ALR contains loanword and incorrect acronym translation; use سازوکار \\pgalr"),
    (r"اعتبارسنجی\s+در\s+هر\s+زمان", "اعتبارسنجی هرزمانی", "اعتبارسنجی در هر زمان misleadingly suggests continuous monitoring; use اعتبارسنجی هرزمانی"),
    (r"(?:پالایش|اعتبارسنجی|توابع\s+مانع\s+کنترلی)[^\n.،؛:]{0,35}\s+در\s+هر\s+زمان", "پالایش / اعتبارسنجی هرزمانی", "در هر زمان for Anytime algorithms is misleading; use هرزمانی"),
    (r"درون\s+حلقه\s+(?:استاندارد\s+)?\\lr\{MAPE-K\}", "در حلقه \\lr{MAPE-K}", "درون حلقه MAPE-K prepositional calque; use در حلقه MAPE-K"),
    (r"درون\s+بافر\s+بازپخش", "در بافر بازپخش", "درون بافر بازپخش prepositional calque; use در بافر بازپخش"),
    (r"دروازه\s+حاشیه\b", "دروازه اعتبارسنجی حاشیه ایمنی و تنش محیطی", "دروازه حاشیه is an ambiguous truncated calque; use دروازه اعتبارسنجی حاشیه ایمنی و تنش محیطی or omit in abstract"),
    (r"حاشیه\s+مدل\s+جانشین", "حاشیه ارضای قیود در مدل جانشین", "حاشیه مدل جانشین confounds constraint margin with model error; use حاشیه ارضای قیود در مدل جانشین"),
    (r"اغتشاش(?:ات)?\s+(?:۱-سطحی|۱-گامی|چندمحوره|تک[\s\u200c]*محوره|محلی)", "انحراف محلی / جابه‌جایی ۱-گامی", "اغتشاش for coordinate search steps is inappropriate; use انحراف محلی or جابه‌جایی ۱-گامی"),
    (r"گام[\s\u200c]*اغتشاش", "گام انحراف", "گام اغتشاش is inappropriate; use گام انحراف"),
    (r"گستره[\s\u200c]*گسسته", "فضای گسسته با", "گستره گسسته is a category error; use فضای گسسته"),
    (r"استخر\s+(?:ارزیابی|کاندیداها|گزینه‌ها)", "مجموعه گزینه‌های مورد ارزیابی", "استخر for candidate pool is a comical calque; use مجموعه گزینه‌های مورد ارزیابی"),
    (r"قرارداد(?:های)?\s+عام\b", "قراردادهای معماری مستقل از دامنه", "قراردادهای عام carries legalistic/commercial ambiguity; use قراردادهای معماری مستقل از دامنه"),
    (r"ملاحظات[\s\u200c]*بلادرنگ[\s\u200c]*سخت[\s\u200c]*افزاری", "الزامات اجرای بلادرنگ سخت‌افزاری", "ملاحظات بلادرنگ سخت‌افزاری is a weak advisory stack; use الزامات اجرای بلادرنگ سخت‌افزاری"),
    (r"تزاحم\s+بر\s+سر\s+قفل", "وقفه و مسدودسازی ناشی از قفل‌ها", "تزاحم بر سر قفل is non-standard/archaic; use وقفه و مسدودسازی ناشی از قفل‌ها"),
    (r"تزاحم\s+بر\s+سر\s+پهنای\s+باند", "گلوگاه پهنای باند حافظه", "تزاحم بر سر پهنای باند is non-standard; use گلوگاه پهنای باند حافظه"),
    (r"\bمقاصد\b", "اهداف", "مقاصد connotes intentions/destinations; use اهداف"),
    (r"\bترکیبات\b", "نسخه‌های ترکیبی", "ترکیبات evokes chemical compounds; use نسخه‌های ترکیبی"),
    (r"\bالحاق\b", "افزودن به ورودی / جایگذاری", "الحاق evokes annexation/concatenation; use افزودن به ورودی"),
    (r"سازگاری\s+رو\s+به\s+عقب", "اصل شمول معماری / حفظ کامل رفتار چارچوب پایه‌ای", "سازگاری رو به عقب is a literal calque; use اصل شمول معماری"),
    (r"مرتبه[\s\u200c]+اجرایی", "مرتبه زمانی", "مرتبه اجرایی is ambiguous; use مرتبه زمانی"),
    (r"خدمات[\s\u200c]+اجرایی", "کیفیت خدمات", "خدمات اجرایی is administrative pleonasm; use کیفیت خدمات"),
    (r"جزئیات[\s\u200c]+اجرایی", "جزئیات پیاده‌سازی", "جزئیات اجرایی is ambiguous for pseudocode; use جزئیات پیاده‌سازی"),
    (r"فرآیند[\s\u200c]+اجرایی", "ساختار اجرا", "فرآیند اجرایی is pleonastic/administrative; use ساختار اجرا"),
    (r"ارضای[\s\u200c]+(?:یا|مهلت|کیفیت|اهداف|کران|نیازمندی|حقیقی)", "رعایت / تأمین / تحقق / مقدار واقعی شاخص", "ارضای is mismatched on deadlines, QoS, bounds, or real-valued metrics"),
    (r"(?:پویایی‌های|سناریوهای|حالت)[\s\u200c]+نویزی|نویز[\s\u200c]+محیطی", "نوسانات و اختلالات پویا / شرایط پرتداخل", "نویز محیطی/پویایی‌های نویزی are calques; reserve نویز for channel/sensor signals"),
    (r"رفتار[\s\u200c]+(?:مقیاس‌پذیری|همگرایی|تجربی|کاوش|یادگیری)|رویه‌های[\s\u200cِ]+رفتارگونه|شکاف[\s\u200c]+رفتار", "روند / میزان / نتایج تجربی / الگوهای تصمیم‌گیری", "Calqued رفتار on inanimate metrics/trends; use روند / میزان / الگوهای تصمیم‌گیری"),
    (r"(?:هدف|اهداف)[\s\u200c]+صریح|حاشیه[\s\u200c]+اطمینان[\s\u200c]+صریح|مداخله[\s\u200c]+صریح", "هدف‌محور / نقطه هدف مشخص / حاشیه اطمینان کمّی / مداخله مستقیم", "Awkward calque of explicit; use هدف‌محور / نقطه هدف مشخص / حاشیه اطمینان کمّی"),
    (r"\bابلیشن\b", "تحلیل حذفی مؤلفه‌ها / تحلیل حساسیت", "ابلیشن is an unassimilated loanword; use تحلیل حذفی مؤلفه‌ها or تحلیل حساسیت"),
    (r"تفکیک[\s\u200c]+اثر", "تحلیل حذفی مؤلفه‌ها / تحلیل حساسیت", "تفکیک اثر replaced by تحلیل حذفی مؤلفه‌ها or تحلیل حساسیت"),
    (r"قرارداد(?:های)?[\s\u200c]+چند[\s\u200c]*هدفه", "اهداف چندهدفه", "قراردادهای چندهدفه is unclear/legalistic; use اهداف چندهدفه"),
    (r"آستانه[\s\u200c]*ای[\s\u200c]+سخت", "آستانه‌ای مطلق", "آستانه‌ای سخت contradicts Soft-QoS and official TT term (آستانه‌ای مطلق)"),
    (r"هم[\s\u200c]*راستایی", "ارتباط و پیوند", "هم‌راستایی is an awkward alignment calque; use ارتباط و پیوند"),
    (r"\bتحقیق(?:ات|اتی)?\b", "پژوهش / پژوهش‌ها / پژوهشی", "Standardize on پژوهش* across the dissertation instead of تحقیق*"),
    (r"فیزیک[\s\u200c]+مختصاتی", "مختصات نقطه‌ای مشخص", "فیزیک مختصاتی is awkward; use مختصات نقطه‌ای مشخص"),
    (r"فیزیک[\s\u200c]+۶[\s\u200c]+درجه[\s\u200c]+آزادی", "دینامیک ۶ درجه آزادی", "Use دینامیک ۶ درجه آزادی for 6-DOF flight dynamics"),
    (r"اهداف[\s\u200c]+غیر[\s\u200c]*برخط[\s\u200c]+ایستا", "عملکرد ایستای بنچمارک پیشین", "اهداف غیربرخط ایستا is confusing during dynamic evaluation"),
    (r"انتقال[\s\u200c]*های?[\s\u200c]+تجربی", "گذارهای ثبت‌شده", "انتقال تجربی mistranslation of transitions; use گذار ثبت‌شده"),
    (r"شکست[\s\u200c]+در[\s\u200c]+انطباق", "پیامد ناکامی انطباق", "شکست در انطباق awkward in table headers; use پیامد ناکامی انطباق"),
    (r"بازمقیاس[\s\u200c]*بندی[\s\u200c]*شده", "محاسبه‌شده بر حسب درصد", "بازمقیاس‌بندی‌شده unreadable 10-word calque; use محاسبه‌شده بر حسب درصد"),
    (r"بن[\s\u200c]*بست[\s\u200c]+تجربی", "ناکارآمدی عملی در مقیاس بزرگ", "بن‌بست تجربی sensationalist; use ناکارآمدی عملی در مقیاس بزرگ"),
    (r"بن[\s\u200c]*بست[\s\u200c]+یادگیری", "رکود یادگیری", "بن‌بست یادگیری sensationalist; use رکود یادگیری"),
    (r"بن[\s\u200c]*بست[\s\u200c]+زمانی", "تنگنای زمانی", "بن‌بست زمانی sensationalist; use تنگنای زمانی"),
    (r"نسخه[\s\u200c]+مقیاس[\s\u200c]*(?:بزرگ|وسیع)", "بستر مقیاس‌بزرگ", "نسخه مقیاس‌بزرگ awkward for DeltaIoTv2 testbed; use بستر مقیاس‌بزرگ"),
    (r"پاداش[\s\u200c]+خوش[\s\u200c]*بینانه[\s\u200c]+دینامیک", "پاداش خوش‌بینانه پویا", "پاداش خوش‌بینانه دینامیک violates loanword rule; use پاداش خوش‌بینانه پویا"),
    (r"دینامیک[\s\u200c]+شبیه‌سازی", "مدل و ماهیت شبیه‌سازی", "دینامیک شبیه‌سازی awkward in table; use مدل و ماهیت شبیه‌سازی"),
    (r"دینامیک[\s\u200c]+پیوسته[\s\u200c]+تغییر[\s\u200c]+کانال", "تغییرات پیوسته کانال‌های رادیویی", "دینامیک پیوسته تغییر کانال awkward; use تغییرات پیوسته کانال‌های رادیویی"),
    (r"واماندگی[\s\u200c]+دینامیکی", "واماندگی آیرودینامیکی", "واماندگی دینامیکی incorrect aerodynamics term; use واماندگی آیرودینامیکی"),
    (r"الزامات[\s\u200c]+نرم[\s\u200c]+کیفیت[\s\u200c]+خدمات", "نیازمندی‌های نرم کیفیت خدمات", "الزامات نرم oxymoronic; use نیازمندی‌های نرم کیفیت خدمات"),
    (r"الزام[\s\u200c]+به[\s\u200c]+طی[\s\u200c]+مجدد[\s\u200c]+مسیر[\s\u200c]+آموزش", "نیاز به بازآموزی کامل شبکه", "الزام به طی مجدد مسیر آموزش verbose/clunky; use نیاز به بازآموزی کامل شبکه"),
    (r"\bعدم[\s\u200c]+توازن[\s\u200c]+شدید[\s\u200c]+شکست\b", "عدم توازن شدید داده‌های شکست / غلبه شدید داده‌های شکست", "عدم توازن شدید شکست lacks syntactic head; use داده‌های شکست"),
    (r"نوسان‌های[\s\u200c]+شدید", "نوسانات شدید", "Unify on نوسانات for periodic physical fluctuations"),
    (r"\bکیو\b", "مقدار $Q$ / شبکه عصبی عمیق $Q$", "Phonetic کیو banned; use mathematical $Q$ notation"),
    (r"(?<![آ-ی\u200c])برنامه(?![\u200c ]?ریز|[\u200c ]?نویس)(?![آ-ی\u200c])", "زمان‌بندی / طرح", "Standalone برنامه for RL schedules is ambiguous; use زمان‌بندی"),
    (r"\$?\\epsilon\$?[\s\u200c-]*حریصانه|کاوش[\s\u200c]+حریصانه|راهبردهای[\s\u200c]+حریصانه", r"\\lr{$\epsilon$-greedy} / کاوش تصادفی مرسوم / راهبردهای بیشینه‌سازی محلی در هر گام", "Avoid حریصانه in RL exploration/strategies"),
    (r"سقوط[\s\u200c]+(?:ارزش|مقادیر|فاجعه‌بار[\s\u200c]+مقادیر|در[\s\u200c]+شکاف|۱۱[\s\u200c]+درصدی)|دچار[\s\u200c]+سقوط|سقوط[\s\u200c]+کردند|سقوط[\s\u200c]*های[\s\u200c]+مرگبار", "افت شدید مقادیر $Q$ / شکست فاجعه‌بار / تنزل نرخ موفقیت", "Reserve سقوط strictly for literal physical UAV crashes"),
    (r"(?:۱۲|الگوریتم(?:\s*های)?)[\s\u200c]+برنامه‌ریز\b|سه‌گانه[\s\u200c]+برنامه‌ریزی", "الگوریتم تصمیم‌گیری / سه‌گانه تصمیم‌گیری بلادرنگ", "Avoid برنامه‌ریز for decision algorithms and bare سه‌گانه برنامه‌ریزی"),
    (r"شبی[هە][\s\u200c]*سازی[\s\u200c]+فیزیکی", "شبیه‌ساز دینامیک پرواز / شبیه‌سازی دینامیک پرواز", "شبیه‌سازی فیزیکی is an oxymoronic calque banned by AGENTS.md"),
    (r"غربال(?:گری)?\b", "پالایش / ارزیابی و پالایش", "Avoid agricultural sieve metaphor غربال; use پالایش"),
    (r"مصالحه[\s\u200c]+حاکم[\s\u200c]+بر[\s\u200c]+روش", "ویژگی و مصالحه کلیدی", "مصالحه حاکم بر روش is stiff/opaque in table headers; use ویژگی و مصالحه کلیدی"),
    (r"مبنای[\s\u200c]+ثابت", "پیکربندی ایستا و بدون انطباق", "مبنای ثابت is clunky; use پیکربندی ایستا و بدون انطباق"),
    (r"اجرای[\s\u200c]+مستقیم[\s\u200c]+پیشنهاد[\s\u200c]+پایه", "استنتاج مستقیم پیشنهاد پایه سیاست", "اجرای مستقیم پیشنهاد پایه conflates Plan and Execute; use استنتاج مستقیم"),
    (r"حلق[هە]-بست[هە]", "حلقه‌بسته", "Use Persian ZWNJ حلقه‌بسته instead of ASCII-hyphenated حلقه-بسته"),
    (r"بنچ[\s\u200c]*مارک(?:[\s\u200c]*های)?\b", "محک / آزمون‌های محک", "Unassimilated loanword بنچ‌مارک; use محک / آزمون‌های محک"),
    (r"بقای[\s\u200c]+دودویی", "نرخ بقای مأموریت", "بقای دودویی is an awkward literal calque of binary survival; use نرخ بقای مأموریت"),
    (r"مزیت[\s\u200c]+قاطع[\s\u200c]+پایداری", "پایداری پروازی بسیار بالاتر", "مزیت قاطع پایداری is stiff/hyperbolic; use پایداری پروازی بسیار بالاتر"),
    (r"تله[\s\u200c]*متری", "داده‌های دورسنجی / داده‌های ثبت‌شده پروازی", "Unassimilated loanword تله‌متری; use داده‌های دورسنجی / ثبت‌شده پروازی"),
    (r"(?:^|[\s(«])مد(?:ها|های)?(?:\s+تهاجمی)?\b", "حالت / حالت‌ها / پیکربندی‌های پرسرعت و پرریسک", "مد (Mode) is banned by terminology_dictionary.md; use حالت / پیکربندی"),
    (r"دالان[\s\u200c]+(?:پروازی[\s\u200c]+)?ملایم", "سطح رواداری ملایم", "Mildness modifies tolerance level, not flight corridor; use سطح رواداری ملایم"),
    (r"ماتریس[\s\u200c]+(?:ارزیابی[\s\u200c]+\$?2\{?,\}?000|بنچ[\s\u200c]*مارک)", "آزمایش جامع / آزمایش محک اصلی", "Avoid ماتریس for flight experiment suite; reserve ماتریس for math/2D tables"),
    (r"(?:^|[\s(«])(?:در[\s\u200c]+)?حضور(?:$|[\s)».,:;،؛])", "در شرایط / تحت / در مواجهه با / بر روی", "Avoid translationese calque در حضور (in the presence of); use natural Persian"),
    (r"\bسرکوب\w*", "تضعیف یا حذف پاداش خوش‌بینانه / بازدارندگی ایمنی‌بخش", "سرکوب carries political/psychological overtones; use تضعیف یا حذف / بازدارندگی ایمنی‌بخش"),
    (r"چگالی[\s\u200c]*های\w*", "افزایش تراکم / تراکم فزاینده", "Do not pluralize uncountable چگالی; use تراکم فزاینده"),
    (r"\bنگردید\b", "نشد / کاهش نیافت / نقض نکرد", "نگردید is stilted bureaucratic passive; use نشد or direct active verb"),
    (r"کران[\s\u200c]+نظری\b", "کران بالای تحلیلی / کران پایین اثبات‌شده / کران بالای اثبات‌شده", "Specify bound direction (upper/lower) instead of vague کران نظری"),
    (r"مطلوبیت[\s\u200c]+(?:فیزیکی[\s\u200c]+)?عملیاتی", "مطلوبیت مأموریت / مطلوبیت عملکرد / مطلوبیت سیستم", "Operational Inflation rule: avoid مطلوبیت عملیاتی"),
    (r"انحراف[\s\u200c]+معیار[\s\u200c]+عملیاتی", "انحراف معیار عملکرد", "Operational Inflation rule: avoid انحراف معیار عملیاتی"),
    (r"هندسه[\s\u200c]+ترسیم[\s\u200c]*شده", "نمودار فاز-فضا / کران‌های ترسیم‌شده", "Avoid figurative هندسه ترسیم‌شده for 2D phase-space plots"),
    (r"تلاطم[\s\u200c]+ملایم", "تلاطم خفیف باد", "تلاطم ملایم is oxymoronic and collides with سطح رواداری ملایم"),
    (r"(?:مرزهای[\s\u200c]+)?تنگ[\s\u200c]*تر\b", "کران‌های محدودتر مانور / محدودتر شدن کران‌های مانور", "Avoid colloquial تنگ‌تر on maneuver bounds; use کران‌های محدودتر مانور"),
    (r"(?:تهدید(?:ات|های)[\s\u200c]+)?متراکم[\s\u200c]+راداری", "تعداد بالای تهدیدهای راداری", "Misplaced modifier and unit mismatch with >= 40; use تعداد بالای تهدیدهای راداری"),
    (r"\bاکیداً\b", "به طور قطعی / نامساوی اکید", "اکیداً banned by AGENTS.md; express exact mathematical inequality or به طور قطعی"),
    (r"آشفتگی[\s\u200c]*(?:های[\s\u200c]*)?(?:جوی|خفیف[\s\u200c]*باد)\b|آشفتگی[\s\u200c]*ها\b", "تلاطم باد / تلاطم خفیف باد / شرایط تلاطم شدید باد", "Avoid آشفتگی جوی/خفیف باد; use تلاطم باد / تلاطم شدید باد"),
    (r"افت[\s\u200c]+فاجع[هە][\s\u200c]*بار[\s\u200c]+مقادیر", "افت شدید مقادیر $Q$", "Avoid hyperbolic فاجعه‌بار on Q-value drop; use افت شدید مقادیر $Q$"),
    (r"\bمتداول\w*", "مرسوم / رایج / شناخته‌شده", "Avoid colloquial/redundant متداول; use مرسوم / رایج / شناخته‌شده"),
    (r"خود[\s\u200c]*راه[\s\u200c]*انداز[\s\u200c]*ی?[\s\u200c]+متوالی", "برآورد بازگشتی مقادیر آتی (سازوکار خودراه‌اندازی)", "خودراه‌اندازی متوالی is an opaque calque; unpack recursive bootstrapping"),
    (r"برون[\s\u200c]*یابی[\s\u200c]+اقدامات[\s\u200c]+خارج[\s\u200c]+از[\s\u200c]+توزیع", "خطای برآورد برای اقداماتی که در سوابق ثبت‌شده مشاهده نشده‌اند", "Unpack dense OOD action extrapolation calque in prose"),
    (r"غیر[\s\u200c]*مقید[\s\u200c]+به[\s\u200c]+زمان", "بدون محدودیت زمانی", "غیرمقید به زمان is unnatural; use بدون محدودیت زمانی"),
    (r"فضای[\s\u200c]+گسسته[\s\u200c]+مقید", "فضای گسسته کوچک‌تر", "فضای گسسته مقید is ambiguous for small discrete space; use فضای گسسته کوچک‌تر"),
    (r"مقید[\s\u200c]+(?:می[\s\u200c]*سازد|سازد|می[\s\u200c]*گردد|گردید|شده|است|کرده)\b", "محدود می‌سازد / محدود شده / کاهش یافت", "Avoid overusing مقید where محدود or کاهش یافت is expected"),
    (r"برآورد[\s\u200c]+بازگشتی[\s\u200c]+آتی", "حذف وابستگی به برآورد گام بعدی / برآورد بازگشتی مقادیر آتی", "برآورد بازگشتی آتی drops مقادیر and reads awkwardly; unpack or keep مقادیر"),
    (r"جمله[\s\u200c]+بازگشتی[\s\u200c]+آتی", "جمله برآورد ارزش گام بعدی", "جمله بازگشتی آتی drops ارزش/مقادیر; use جمله برآورد ارزش گام بعدی"),
    (r"(?<![آ-ی\u200c])تله[\s\u200c]+انفعال(?![آ-ی\u200c])", "رفتارهای انفعالی و پرهیز از اقدام / پدیده ایمنی ناشی از انفعال", "Bare تله انفعال is an opaque calque; use رفتارهای انفعالی و پرهیز از اقدام"),
    (r"دچار[\s\u200c]+تله", "روی آوردن به رفتارهای انفعالی / گرفتار شدن در", "دچار تله is an awkward collocation; avoid دچار with تله"),
    (r"تله[\s\u200c]+[^\n.،؛:]{0,40}\s+در[\s\u200c]+هم[\s\u200c]+شکسته", "مانع از گرایش به رفتارهای انفعالی شده", "تله ... در هم شکسته is a mixed metaphor; use مانع از گرایش به"),
    (r"تخریب[\s\u200c]+شبکه[\s\u200c]+عصبی", "واگرایی گرادیان و افت شدید مقادیر $Q$ / ناپایداری آموزش شبکه عصبی", "تخریب شبکه عصبی is imprecise/hyperbolic; state exact mathematical failure mode"),
    (r"تخریب[\s\u200c]+تدریجی[\s\u200cِ]+کیفیت", "افت تدریجی کیفیت", "Prefer افت تدریجی کیفیت over تخریب تدریجی کیفیت"),
    (r"جبهه[\s\u200c]+(?:بهینه[\s\u200c]+|مصالحه[\s\u200c]+)?پارتو", "مرز بهینه پارتو / منحنی مصالحه پارتو", "Avoid military-connoting جبهه for Pareto Frontier; use مرز بهینه پارتو or منحنی مصالحه پارتو"),
    (r"حاشیه[\s\u200c]+امن[\s\u200c]+بالا", "فاصله زمانی مطمئن / فاصله اطمینان زیاد از مرز آستانه", "حاشیه امن بالا is vague/colliding; use فاصله زمانی مطمئن or فاصله اطمینان زیاد از مرز آستانه"),
    (r"میانگین[\s\u200c]+(?:کل[\s\u200c]+)?غیر[\s\u200c]*شرطی|میانگین[\s\u200c]+تأخیر[\s\u200c]+(?:شرطی|غیر[\s\u200c]*شرطی[\s\u200c]+ترکیبی)", "میانگین کل تأخیر در مجموع چرخه‌ها / میانگین تأخیر شاخه پالایش", "Unpack opaque conditional/unconditional latency jargon"),
    (r"حافظه[\s\u200c]+هیپ", "حافظه پویا", "هیپ is an unassimilated loanword; use حافظه پویا"),
    (r"تک[\s\u200c-]*تولید[\s\u200c]*کننده|تک[\s\u200c-]*مصرف[\s\u200c]*کننده", "با یک تولیدکننده و یک مصرف‌کننده", "Avoid dense hyphenated compound تک‌تولیدکننده-تک‌مصرف‌کننده"),
    (r"تک[\s\u200c]*نویسنده", "توسط یک ریسمان نویسنده", "Unpack تک‌نویسنده for readability"),
    (r"پردازنده[\s\u200c]*های[\s\u200c]*پروازی", "پردازنده‌های روی برد پهپاد (الکترونیک پروازی)", "پردازنده‌های پروازی is colloquial translationese; use پردازنده‌های روی برد پهپاد"),
    (r"سیاست[\s\u200c]+بدون[\s\u200c]+بافر", "سیاست فاقد بافر حاشیه اطمینان", "سیاست بدون بافر creates severe RL ambiguity (confused with replay buffer); use سیاست فاقد بافر حاشیه اطمینان"),
    (r"پیش‌ازپرواز|پیش‌پرواز\b", "پیش از پرواز", "Prefer fluent prepositional پیش از پرواز over dense compounds"),
    (r"واحد[\s\u200c]*درصدی", "درصد / افتی معادل X درصد", "واحد درصدی is rigid translationese when explicit values are present; rewrite as X درصد"),
    (r"انطباق\s+مدل(?:‌های)?\s+جانشین\s+در\s+برابر\s+موفقیت\s+فیزیکی", "نرخ انطباق پیش‌بینی‌شده در مدل‌های جانشین با نرخ بقای پرواز در شبیه‌ساز ۶ درجه آزادی", "Clarify both compared rates and avoid vague موفقیت فیزیکی"),
    (r"مشخصات\s+بسترها\b", "ویژگی‌های بسترهای ارزیابی", "Specify بسترهای ارزیابی for reader clarity"),
    (r"جاب[ه\u200c]?جایی\s+ملایم\s+داده‌ها", "تغییرات تدریجی توزیع داده‌ها بدون غلبه شکست", "جابجایی ملایم داده‌ها is a misleading calque for distribution shift"),
    (r"(?:ثبت[\s\u200c]*شده|یافته‌های|شواهد\s+تجربی)[^\n]{0,45}مستخرج\s+از", "در پژوهش / به‌دست‌آمده در این رساله", "Avoid heavy passive مستخرج in analytical prose"),
    (r"بهره\s+گرفته\s+شده\s+است", "به‌کار رفته‌اند / انجام شده است", "Avoid wordy, verb-delayed passive بهره گرفته شده است"),
    (r"بستر\s+فیزیکی[-\s\u200c]+سایبری\s+ناوگان\s+پهپادی", "شبیه‌ساز فیزیکی-سایبری DARTSim (ناوگان پهپادی)", "Break 4-level ezafe chain بستر فیزیکی-سایبری ناوگان پهپادی"),
    (r"عملکرد\s+پایدار\s+و\s+همگرایی\s+قابل\s+اطمینان", "جلوگیری از واگرایی آموزش و کاهش نوسان یادگیری در بذرهای تصادفی مختلف", "Replace vague boilerplate with concrete hyperparameter tuning objective"),
    (r"(?:روش(?:[\s\u200c]+|[\s\u200c]*های[\s\u200c]+)|جستجوی[\s\u200c]+)تقلیلی", "روش‌های سنتز غیربرخط سیاست / گونه حذفی / جستجو در زیرفضای محدود", "تقلیلی is ambiguous in Persian; specify offline synthesis / ablated variant or subspace search"),
    (r"محافظت[\s\u200c]+صوری[\s\u200c]+پیرامونی[\s\u200c]+سیاست", "اعمال فیلتر ایمنی صوری بر خروجی سیاست", "محافظت صوری پیرامونی سیاست is an opaque spatial calque; describe the safety filter functionally"),
    (r"بهینه[\s\u200c]*سازی[\s\u200c]+نرم[\s\u200c]*افزاری", "مهندسی نرم‌افزار مبتنی بر جستجو", "بهینه‌سازی نرم‌افزاری mistranslates Search-Based Software Engineering (SBSE)"),
    (r"بیانیه[\s\u200c]+پل", "بند انتقالی روان در پایان خلاصه فصل", "بیانیه پل is a leaked literal calque of Bridge Statement"),
    (r"(?:استقرار[\s\u200c]+بستر[\s\u200c]+نظری|بستر[\s\u200c]+نظری[\s\u200c]+مستحکم|زیربنای[\s\u200c]+مستحکم[\s\u200c]+نظری)", "مبانی نظری و ریاضی / جمع‌بندی پژوهش‌های پیشین", "Avoid deployment/platform metaphors and promotional مستحکم for theoretical foundations"),
    (r"شکاف(?:[\s\u200c]*های)?[\s\u200c]+پیشینه", "شکاف‌های پژوهشی", "شکاف‌های پیشینه is a literal calque; use شکاف‌های پژوهشی"),
    (r"دروازه[\s\u200c]+(?:کیفیت[\s\u200c]+(?:صوری|آماری)|صوری|کیفیت\b)", "سیگنال اعتبارسنجی صوری ($r_{\\text{smc}}$) / سیگنال پاداش صوری", "Reserve دروازه for Gateway and Stress Gate; UPPAAL-SMC outputs a formal verification signal"),
    (r"(?:معماری(?:[\s\u200c]*های)?[\s\u200c]+)?ترادف[\s\u200c]+ناهمگام|معماری(?:[\s\u200c]*های)?[\s\u200c]+ترادف(?:ی)?|رویکردهای[\s\u200c]+ترادف|مدل‌های[\s\u200c]+ترادف|ترادف[\s\u200c]+صوری", "تلفیق ناهمگام / رویکردهای ترکیبی متوالی", "ترادف (synonymy/tandem) is opaque and oxymoronic with ناهمگام; use تلفیق ناهمگام or رویکردهای ترکیبی متوالی"),
    (r"تضمین[\s\u200c]+صوری[\s\u200c]+ایمنی[\s\u200c]+ریاضی|تضمین(?:[\s\u200c]*های)?[\s\u200c]+صوری[\s\u200c]+ریاضی(?:اتی)?|استواری[\s\u200c]+صوری[\s\u200c]+ریاضیاتی", "تضمین‌های صوری ایمنی", "Avoid redundant stacking of صوری + ریاضی + ایمنی"),
    (r"قابلیت[\s\u200c]+انطباق[\s\u200c]+با[\s\u200c]+پویایی[\s\u200c]+زمان[\s\u200c]*اجرا", "انطباق با تغییرات پویای محیط", "Break heavy 5-word abstract nominalization chain"),
    (r"پایداری[\s\u200c]+زمانی(?:[\s\u200c]+تصمیم[\s\u200c]*گیری|[\s\u200c]+سیستم)?", "تأخیر تصمیم‌گیری / مهلت‌های زمانی سیستم", "پایداری زمانی is a false friend for Latency/Timeliness (sounds like temporal stability)"),
    (r"توزیع[\s\u200c]*شده[\s\u200c]+پیشرفته", "توزیع‌شده مقیاس‌بزرگ / توزیع‌شده", "Avoid vague promotional qualifier پیشرفته on distributed networks"),
    (r"برخط[\s\u200c]+(?:در[\s\u200c]+)?زمان[\s\u200c]*اجرا|زمان[\s\u200c]*اجرای[\s\u200c]+برخط", "برخط / در زمان اجرا (از یکی استفاده شود)", "Avoid tautological stacking of برخط and زمان اجرا in one phrase"),
    (r"جستجوی[\s\u200c]+تصادفی[\s\u200c]+زمان[\s\u200c]*اجرا|تغییر[\s\u200c]+مستمر[\s\u200c]+زمان[\s\u200c]*اجرا|پاداش[\s\u200c]+تجمعی[\s\u200c]+زمان[\s\u200c]*اجرا|پاداش[\s\u200c]+شکل[\s\u200c]*دهی[\s\u200c]*شده[\s\u200c]+زمان[\s\u200c]*اجرا|محیط[\s\u200c]*های[\s\u200c]+زمان[\s\u200c]*اجرا|کنترل[\s\u200c]*کننده[\s\u200c]+زمان[\s\u200c]+اجرا|گزینه[\s\u200c]*های[\s\u200c]+وفقی[\s\u200c]+زمان[\s\u200c]+اجرا|گزینه[\s\u200c]*های[\s\u200c]+تصمیم[\s\u200c]*گیری[\s\u200c]+زمان[\s\u200c]+اجرا|تغییرات[\s\u200c]+برخط|اختلالات[\s\u200c]+پویای[\s\u200c]+برخط|سیستم[\s\u200c]*های[\s\u200c]+برخط", "عبارت روان با حرف اضافه «در» یا صفت محیطی/پویا", "Fix unprepositioned زمان اجرا or unnatural برخط collocation"),
    (r"تخصص[\s\u200c]+انسانی[\s\u200c]+زمان[\s\u200c]+توسعه", "دانش خبرگان حوزه کاربرد در زمان طراحی", "Stacked 4-noun Ezafe chain; use دانش خبرگان حوزه کاربرد در زمان طراحی"),
    (r"تله[\s\u200c]*(?:های)?[\s\u200c]+بهینگی[\s\u200c]+محلی", "نقاط بهینه محلی", "تله‌های بهینگی محلی is semantically awkward; use نقاط بهینه محلی"),
    (r"غیر[\s\u200c]*مدل[\s\u200c]*محور", "بدون مدل", "غیرمدل‌محور is a clunky hybrid; standardize on بدون مدل"),
    (r"تپه[\s\u200c]*های[\s\u200c]+متعدد", "قله‌های محلی متعدد (چندمُد)", "تپه‌های متعدد is a literal calque for multimodal functions; use قله‌های محلی متعدد"),
    (r"انتخاب[\s\u200c]+بهینه[\s\u200c]+آنی", "بیشینه‌سازی محلی در هر گام", "انتخاب بهینه آنی contradicts local-optima trapping; use بیشینه‌سازی محلی در هر گام"),
    (r"\bریاضیاتی\b", "ریاضی", "Prefer standard academic adjective ریاضی over double-suffixed ریاضیاتی"),
    (r"(?<![آ-ی\u200c])هرس[\s\u200c]+فضا(?![آ-ی\u200c])", "کاهش فضای وفقی", "Bare هرس فضا is abrupt; standardize on کاهش فضای وفقی"),
    (r"نوسانات[\s\u200c]+تداخل[\s\u200c]+سیگنال", "نوسانات تداخل رادیویی", "3-noun Ezafe calque; use نوسانات تداخل رادیویی"),
    (r"روش[\s\u200c]+مدل[\s\u200c]*سازی[\s\u200c]+ریاضی[\s\u200c]+تصمیم[\s\u200c]*گیری[\s\u200c]+پیاپی", "چارچوب ریاضی برای مدل‌سازی تصمیم‌گیری‌های متوالی", "5-Ezafe stack; break with برای and standardize on تصمیم‌گیری‌های متوالی"),
    (r"محیط[\s\u200c]+تصمیم[\s\u200c]*گیری", "فضای وفقی / فضای تصمیم‌گیری", "Do not conflate adaptation/decision space with environment (محیط)"),
    (r"داده[\s\u200c]*های[\s\u200c]+برچسب[\s\u200c]*دار[\s\u200c]+غیر[\s\u200c]*برخط", "داده‌های آموزشی برچسب‌دار در زمان طراحی", "Avoid colliding design-time supervised data with SG-OS offline operational logs"),
    (r"تصمیمات[\s\u200c]+مخرب", "تصمیم منسوخ‌شده / پاسخ دیرهنگام / اقدامات پرخطا", "Latency-induced stale responses are not destructive decisions; distinguish stale vs hazardous actions"),
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

