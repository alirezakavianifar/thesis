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
    (r"\bفاز برنامه‌ریزی\b", "مرحله برنامه‌ریزی", "فاز برنامه‌ریزی contains loanword; use مرحله برنامه‌ریزی"),
    (r"\bفاز پیش[ -]?پرواز\b", "مرحله پیش‌پرواز", "فاز پیش‌پرواز contains loanword; use مرحله پیش‌پرواز"),
    (r"\bگردش فرآیندی\b", "جریان کاری", "گردش فرآیندی awkward calque; use جریان کاری"),
    (r"\bفرآیند اعتبارسنجی صوری\b", "اعتبارسنجی صوری", "فرآیند اعتبارسنجی صوری is pleonastic; use اعتبارسنجی صوری"),
    (r"شرایط مسابقه", "شرایط رقابتی", "شرایط مسابقه banned; use شرایط رقابتی"),
    (r"ت[اأ]خیر نوسانی", "نوسان تأخیر", "تأخیر نوسانی banned; use نوسان تأخیر"),
    (r"نخ[- ]?امن", "ریسمان‌امن", "نخ‌امن banned; use ریسمان‌امن"),
    (r"صف کاربری ناهمگام", "صف وظایف ناهمگام", "صف کاربری ناهمگام banned; use صف وظایف ناهمگام"),
    (r"مدیریت همزمانی بدون قفل", "کنترل همروندی بدون قفل", "مدیریت همزمانی بدون قفل avoided; use کنترل همروندی بدون قفل"),
    (r"مرجع عددی", "سناریوهای عددی مرجع / مثال‌های اجرایی عددی", "مرجع عددی ambiguous/inverted; use سناریوهای عددی مرجع"),
    (r"لایه مقدماتی", "سطح اول کنترل برخط", "لایه مقدماتی misleading for real-time inference; use سطح اول کنترل برخط"),
    (r"شبیه‌سازی‌های مقدماتی", "شبیه‌سازی‌های اولیه", "شبیه‌سازی‌های مقدماتی avoided; use شبیه‌سازی‌های اولیه"),
    (r"اعمال بر راه‌اندازها", "صدور فرمان‌ها به عملگرها", "اعمال بر راه‌اندازها defective phrasing; use صدور فرمان‌ها به عملگرها"),
    (r"فراپارامترهای بنیادین", "فراپارامترهای کلیدی", "بنیادین inflation on parameters; use فراپارامترهای کلیدی"),
    (r"\bمهندسین\b", "مهندسان", "مهندسین non-standard plural in academic Persian; use مهندسان"),
    (r"محافظ[هە][\u200c\s]?کارانه\s+منفعل|محافظ[هە][\u200c\s]?کارانه\s+انفعالی", "رفتار انفعالی (تله ایمنی ناشی از انفعال)", "محافظه‌کارانه منفعل awkward compound; use رفتار انفعالی"),
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
    (r"رگرسیون[\s\u200c]*راهزن[\s\u200c]*زمین[هە][\s\u200c]*آگاه", "مسئله راهزن زمینه‌آگاه", "رگرسیون راهزن زمینه‌آگاه heavy compound calque; disentangle formulation from model"),
    (r"احتمال[\s\u200c]*هدایت[\s\u200c]*شده", "احتمال شکل‌دهی هدایت‌شده", "احتمال هدایت‌شده awkward calque; use احتمال شکل‌دهی هدایت‌شده"),
    (r"ماژول\s+\\pgalr|ماژول\s+PG-ALR|ماژول[\s\u200c]+پالایش\s+محلی", "سازوکار \\pgalr / پالایش محلی", "ماژول PG-ALR contains loanword and incorrect acronym translation; use سازوکار \\pgalr"),
    (r"اعتبارسنجی\s+در\s+هر\s+زمان", "اعتبارسنجی هرزمانی", "اعتبارسنجی در هر زمان misleadingly suggests continuous monitoring; use اعتبارسنجی هرزمانی"),
    (r"پالایش\s+(?:محلی\s+)?در\s+هر\s+زمان", "پالایش محلی هرزمانی", "پالایش در هر زمان misleading; use پالایش هرزمانی / پالایش محلی هرزمانی"),
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

