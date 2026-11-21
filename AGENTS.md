# Agent Instructions & Dissertation Scholarly Guidelines

This document serves as the permanent, authoritative master directive for all AI agents, subagents, and automated workflows operating on this doctoral dissertation repository. All future edits across all chapters, abstracts, appendices, and front matter MUST strictly adhere to the guidelines, architectural conventions, and LaTeX disciplines codified herein and within the modular workspace skills in `.agents/skills/`.

> [!IMPORTANT]
> **Living Document & Dynamic Rule Maintenance Protocol**:
> Whenever a new rule is introduced, a term refined, a word banned, a stylistic constraint added, or a workflow updated, the AI agent **MUST proactively and immediately update `AGENTS.md` and the appropriate skill in `.agents/skills/`**.

---

## 1. Modular Workspace Skills & Progressive Disclosure

To prevent context budget overflows and provide automated verification tooling, detailed procedural checklists and audit scripts are organized into progressive workspace skills:

1. **`thesis-latex-typesetting`** (`.agents/skills/thesis-latex-typesetting/`): XePersian BiDi layout, math-mode numeral formatting, table width constraints, and zero-defect log verification.
2. **`thesis-persian-terminology`** (`.agents/skills/thesis-persian-terminology/`): Complete 45+ term Persian technical dictionary and automated regex scanner (`audit_terms.py`).
3. **`thesis-scholarly-writing`** (`.agents/skills/thesis-scholarly-writing/`): Doctoral prose tone, elimination of AI hype words/fillers, and Anti-Bullet Fatigue discipline (`audit_prose.py`).
4. **`thesis-chapter-architect`** (`.agents/skills/thesis-chapter-architect/`): Epistemological scopes, negative boundaries, and guidelines for authoring chapters and appendices.
5. **`thesis-bibliography-manager`** (`.agents/skills/thesis-bibliography-manager/`): BibTeX integrity, `ieeetr-fa` styling, citation resolution, and footnote conventions (`audit_citations.py`).
6. **`thesis-git-discipline`** (`.agents/skills/thesis-git-discipline/`): Safe version control, 100MB file protection, automated push pipeline, and pre-receive hook defense (`safe_push.py`).
7. **`thesis-build-cleanup`** (`.agents/skills/thesis-build-cleanup/`): Post-compilation build hygiene, automated auxiliary file cleanup (`.aux`, `.log`, `.out`, `.toc`, `.bbl`, `.xdv`, etc.), and pristine workspace maintenance (`clean_build.py`).

---

## 2. Git Remote & Automated Push Workflow

### 2.1 Remote Repository & Size Limit
- Remote: **`https://github.com/alirezakavianifar/thesis.git`**
- GitHub strictly enforces a 100MB file limit. **NEVER** commit large binaries, archives (`.rar`, `.zip`), build dumps, or compiled PDFs.
- Ensure `.gitignore` is verified before staging.

### 2.2 Automated Push on Keyword "push"
When the user uses the keyword **"push"** in a request, you **MUST proactively execute**:
```powershell
python .agents/skills/thesis-git-discipline/scripts/safe_push.py
```
This automatically verifies file sizes, stages changes, generates an inferred semantic commit message, commits, and pushes.

---

## 3. Scholarly Tone, Humanization & Anti-AI Hype Discipline

1. **Authoritative Scholarly Persian**: Evaluate prose from the perspective of an external doctoral examiner. Avoid conversational throat-clearing, run-on sentences, and breathless rhetoric.
2. **Strictly Purged Hype Words (100% Banned)**:
   - `نوین` $\rightarrow$ Use `پیشنهادی`, `مدرن`, `پیشرفته`, or `جدید`.
   - `انقلابی`, `شگفت‌انگیز`, `دگرگون‌ساز`.
   - `چشمگیر` $\rightarrow$ Use `به طور قابل‌ملاحظه‌ای`, `شدید`, or report exact quantitative deltas ($23.22\%$).
   - `فوق‌العاده` $\rightarrow$ Use `با رواداری محدود`, `بسیار باریک`, or state the quantitative bound.
   - Casual prefix `فوق` (`فوق‌سریع`, `فوق‌العاده`).
3. **Elimination of Conversational Fillers**:
   - ❌ Banned: `شایان ذکر است که`, `لازم به یادآوری است که`, `بدیهی است که`, `همان‌طور که می‌دانیم`, `نکته جالب توجه این است که`.
   - ✔️ Use direct, assertive declarative sentences.
4. **Anti-Bullet Fatigue**:
   - Do NOT use fragmented `itemize` / `enumerate` lists for standard expository descriptions or taxonomies.
   - Restructure descriptive lists into flowing narrative paragraphs with bold inline headings: `\paragraph{عنوان مشخص:}`.
   - Bullet lists are strictly reserved for: Research Questions (`RQ1`--`RQ6`), Core Innovations (1--6), formal mathematical proofs, and validity threats.

---

## 4. Persian Technical Terminology Standards

The mandatory vocabulary is strictly enforced. The full table and rationale are in [terminology_dictionary.md](.agents/skills/thesis-persian-terminology/references/terminology_dictionary.md).

- **Core Invariants**:
  - `سیستم` (mandatory) vs ❌ `سامانه` (100% strictly banned).
  - `بلادرنگ` (mandatory) vs ❌ `زمان‌حقیقی`, `زمان واقعی`, `بی‌درنگ`.
  - `سیستم‌های خودوفق` (صفت مرکب برای سیستم‌ها و کنترل‌کننده‌ها) vs ❌ `سیستم‌های خودتطبیق‌پذیر`, `سامانه‌های خودسازگار`.
  - `خودوفقی` (اسم مصدر/قابلیت/پارادایم کلان: `قابلیت خودوفقی`) vs ❌ `خودتطبیقی`, `خودسازگاری`.
  - `انطباق` (اسم مصدر برای چرخه، مراحل، فرامین و انطباق با مشخصه‌ها: `چرخه انطباق`, `فرآیند انطباق`, `طرح انطباق`, `فرمان انطباق`, `انطباق با مشخصه‌ها`, `بردار انطباق`) vs ❌ `تطبیق`.
  - `وفقی` (صفت نسبی برای فضاها، گزینه‌ها، اقدامات و اهداف: `فضای وفقی`, `اقدام وفقی`, `گزینه وفقی`, `اهداف وفقی`, `استنتاج وفقی`) vs ❌ `اقدام انطباقی`, `گزینه‌های انطباقی`, `اهداف انطباقی`, `استنتاج انطباقی`.
  - `تحلیل تطبیقی` vs ❌ `تحلیل انطباقی` (`تطبیق` صرفاً برای ارزیابی مقایسه‌ای).
  - `سازگار با قیود` ($\mathcal{N}_{\text{sat}}$) vs ❌ `سیستم‌های خودسازگار`.
  - `ناهمگام` vs ❌ `غیرهمگام`.
  - `ریسمان` vs ❌ `نخ`.
  - `فرآیند` vs ❌ `پردازه`.
  - `سازوکار` vs ❌ `مکانیسم`.
  - `ایستا` vs ❌ `استاتیک`.
  - `دسته / دسته‌های کوچک داده` vs ❌ `بچ / مینی‌بچ`.
  - `کلیدی / بنیادین` vs ❌ `حیاتی`.
  - `بافر بازپخش` vs ❌ `میانگیر بازپخش`.
  - `کاندیداها / گزینه‌های کاندید` vs ❌ `گزینه‌های نامزد`.
  - `غیربرخط / برخط` vs ❌ `آفلاین / آنلاین`، `برون‌خط`.
  - `سوابق عملیاتی / سوابق غیربرخط` vs ❌ `لاگ`, `وقایع‌نگاشت`.
  - `اعتبارسنجی صوری` vs ❌ mixed `راستی‌آزمایی صوری`.
  - `وارسی مدل (آماری)` vs ❌ `مدل‌چکینگ`.
  - `نمودار` vs ❌ `دیاگرام`.
  - `راه‌انداز` vs ❌ `درایور`؛ و تفکیک مفهومی درایور سخت‌افزاری (`واسط‌های راه‌انداز سخت‌افزاری`) از مفهوم یادگیری تقویتی: `تخمین خودراه‌انداز متوالی\LTRfootnote{Bootstrapping}` vs ❌ خلط معنایی با راه‌انداز سخت‌افزار؛ و پرهیز از ساختار نامأنوس `اعمال بر راه‌اندازها` (استفاده از `صدور فرامین به محرک‌ها / لایه محرک‌ها و اجزای اجرایی`).
  - `انضباط واژگانی محرک‌ها (\lr{Actuators}) در برابر عملگرها (\lr{Operators})`: تحدید کاربرد واژه «عملگر» به عملگرهای ریاضیاتی و منطقی (نظیر `عملگر بیشینه‌سازی`)؛ و الزام استفاده از `محرک‌ها`، `محرک‌های کنترلی / مکانیکی` یا `لایه محرک‌ها و اجزای اجرایی` در لایه فیزیکی سیستم‌های خودوفق و پهپادها vs ❌ کاربرد مبهم واژه «عملگرها» بدون قرینه که موجب خلط با اپراتور انسانی یا فرآیندهای محاسباتی می‌گردد.
  - `انضباط واژگانی کمیت عددی در برابر نرده‌ای (\lr{Scalar})`: در یادگیری تقویتی، استفاده از `مقدار عددی پاداش`، `پاداش عددی` یا حذف صفت در صورت وضوح سیاق متن vs ❌ واژه نامأنوس و بیگانه‌ساز `نرده‌ای` (که در فارسی معاصر حصار و نرده پله را تداعی می‌کند).
  - `تفکیک بازه و محدوده مقادیر (\lr{Interval / Value Range}) از دامنه (\lr{Domain})`: استفاده از `بازه مقادیر`، `بازه بهینه`، `محدوده مقادیر` برای پارامترهای عددی (مانند $\rho \in [0, 1]$) و نرمال‌سازی بردار حالت vs ❌ کاربرد نادرست «دامنه» برای فواصل عددی و برد ویژگی‌ها؛ تحدید کاربرد «دامنه» به اصطلاحات مستقر علوم کامپیوتر (`دانش دامنه`، `مستقل از دامنه`، `انتقال بین‌دامنه‌ای`)؛ استفاده از `قلمرو عملیاتی` (\lr{Operational Envelope}) vs ❌ `دامنه عملیاتی`؛ و استفاده از `خبرگان حوزه کاربرد / متخصصان دامنه مسئله` vs ❌ گرته‌برداری ناشیانه `مهندسان دامنه`.
  - `سناریوهای عددی مرجع / مثال‌های اجرایی عددی` vs ❌ ترکیب مقلوب و مبهم `سناریوهای مرجع عددی`.
  - `سطح اول کنترل برخط / مسیر مستقیم کنترل برخط` vs ❌ کاربرد گمراه‌کننده `لایه مقدماتی` برای حلقه استنتاج بلادرنگ شبکه عصبی؛ و `شبیه‌سازی‌های اولیه` vs ❌ `شبیه‌سازی‌های مقدماتی`.
  - `انضباط و مهار تورم واژه «بنیادین»`: کاربرد واژه «بنیادین» منحصراً در مفاهیم اصیل زیربنایی، نظری و معرفت‌شناختی مجاز است (نظیر `کارهای بنیادین IBM`، `مسئله بنیادین رساله`، `تفاوت بنیادین پارادایم`، `فرض بنیادین فرآیند مارکوف`، `تناقض بنیادین با پارادایم خودوفقی`) vs ❌ ممنوعیت تکرار چندباره در یک بند واحد، و ممنوعیت تعمیم حشوآمیز آن به فراپارامترهای محاسباتی (استفاده از `فراپارامترهای کلیدی/اصلی`)، محورهای پژوهش (استفاده از `محورهای اصلی`)، علل همگرایی (استفاده از `علت اصلی`) یا قیود عملیاتی مسئله (استفاده از `قیود عملیاتی`).
  - `پشتیبان` vs ❌ `فال‌بک`.
  - `الکترونیک پروازی` vs ❌ `اویونیک`.
  - `کنترل همروندی بدون قفل` vs ❌ `مدیریت همزمانی بدون قفل`.
  - `شرایط رقابتی / وضعیت رقابتی` (\lr{Race Conditions}) vs ❌ `شرایط مسابقه`.
  - `نوسان تأخیر` (\lr{Latency Jitter}) vs ❌ `تأخیر نوسانی`.
  - `اشاره‌گر / تبادل تجزیه‌ناپذیر` (\lr{Atomic Pointer Swap}) vs ❌ `اشاره‌گر اتمیک`، `جابه‌جایی تجزیه‌ناپذیر`؛ و تحدید کاربرد «تجزیه‌ناپذیر» به عملیات همروندی و دسترسی به حافظه vs ❌ کاربرد گمراه‌کننده آن برای فازهای کلان اجرا در \lr{MAPE-K} (استفاده از `مرحله اجرا و اعمال فرمان‌های انطباق` به جای `مرحله اجرای تجزیه‌ناپذیر`).
  - `تله ایمنی ناشی از انفعال / رفتار انفعالی` (\lr{Safety through Inaction Trap}) vs ❌ ترکیب حشوآمیز `سیاست‌های محافظه‌کارانه منفعل` یا `محافظه‌کارانه انفعالی`.
  - `انضباط واژگانی مهندسی`: استفاده از `مهندسان` vs ❌ جمع مکسر نامأنوس `مهندسین`؛ پرهیز از تکرار مجاور واژه «مهندسی» در یک جمله واحد (مانند ❌ `در طراحی مهندسی ... چالش‌های مهندسی` $\rightarrow$ `در طراحی سیستم‌های خودوفق مدرن ... چالش‌های پیچیده مهندسی`)؛ و جایگزینی عبارات مبهم نظیر `سازوکار مهندسی` با اصطلاحات دقیق فنی (`سازوکار همروندی` یا `مزیت معماری`).
  - `پرهیز از ساختارهای فعلی سنگین با «فعال»`: پرهیز از ساختار حشوآمیز `فعال بوده و وظیفه ... را بر عهده دارد` (استفاده مستقیم از `وظیفه دریافت بردار حالت جاری ... را بر عهده دارد`)؛ و پرهیز از فعل ضعیف `فعالیت دارد` برای ریسمان‌های کنترلی (استفاده از `اجرا می‌شود` یا `عمل می‌کند`).
  - `ریسمان‌امن` (\lr{Thread-Safe}) vs ❌ `نخ‌امن`.
  - `صف وظایف ناهمگام` (\lr{Asynchronous Task Queue}) vs ❌ `صف کاربری ناهمگام`.
  - `قفل انحصار متقابل` (\lr{Mutex}) vs ❌ `قفل انحصاری`.
  - `تزاحم بر سر قفل` (\lr{Lock Contention}) vs ❌ `رقابت بر سر قفل`.
  - `سنتز کنترل‌کننده / سنتز خط‌مشی / سنتز صوری` (\lr{Controller/Policy Synthesis}): مجاز و استاندارد در روش‌های صوری، مهندسی نرم‌افزار خودکار و الگوی معماری \sgos vs ❌ تعمیم به «سنتز داده» (از `تلفیق داده / تجمیع شواهد` استفاده شود)، «سنتز مؤلفه‌ها» (از `ترکیب مؤلفه‌ها / ترکیب‌بندی` استفاده شود)، یا «سنتز ادبیات / سنتز به پرسش‌ها» (از `تلفیق پیشینه پژوهش / تلفیق یافته‌ها` استفاده شود).
  - `تفکیک فاز اجرا از دیرند و تأخیر زمانی`: استفاده از `تأخیر کل تصمیم‌گیری / بدترین حالت تأخیر تصمیم‌گیری / تأخیر کل برنامه‌ریزی` vs ❌ ترکیب حشوآمیز `تأخیر کل زمان اجرا`؛ و پرهیز از تکرار چندباره `زمان اجرا` در یک بند یا جمله واحد (جایگزینی متناسب با `برخط`، `حین اجرا` یا حذف واژه زاید در صورت ووضوح بافت موضوعی).
  - `پرهیز از کاربرد حشوآمیز صفت مرکب «کم‌تأخیر»` (\lr{Low-Latency}):
    - ❌ ممنوعیت همنشینی «کم‌تأخیر» با «بلادرنگ» (مانند `تصمیم‌گیری بلادرنگ و کم‌تأخیر` یا `استنتاج بلادرنگ کم‌تأخیر` $\rightarrow$ استفاده مستقیم از `تصمیم‌گیری بلادرنگ میلی‌ثانیه‌ای` یا `استنتاج بلادرنگ سیاست`).
    - ❌ ممنوعیت ذکر همزمان صفت کیفی مبهم «کم‌تأخیر» در کنار سنجه‌های کمّی صریح (مانند `استنتاج کم‌تأخیر زیر نیم میلی‌ثانیه‌ای` $\rightarrow$ `استنتاج در مقیاس زیر نیم میلی‌ثانیه‌ای`؛ `مستقیم و کم‌تأخیر ($0.2\,\text{ms}$)` $\rightarrow$ `مستقیم با دیرند $0.2\,\text{ms}$`).
    - ❌ ممنوعیت کاربرد «کم‌تأخیر» در عناوین گام‌ها و خط لوله به جای نقش فنی متغیر (مانند `استنتاج کم‌تأخیر ($a^*$):` $\rightarrow$ استفاده از `استنتاج اقدام نامی ($a^*$):`).
    - ✔️ در سایر زمینه‌ها، ترجیح اکید بر استفاده از اصطلاحات معیار مهندسی نظیر `بلادرنگ`، `با کمترین تأخیر` یا بیان صریح کران زمانی/دیرند است.
  - `کاربرد دقیق واژه «استنتاج»` (\lr{Inference}): مجاز و استاندارد صرفاً به عنوان اصطلاح تخصصی یادگیری ماشین و شبکه‌های عصبی عمیق (\lr{Inference} در برابر \lr{Training}: «زمان استنتاج»، «تأخیر استنتاج»، «مسیر استنتاج»، «استنتاج وفقی») vs ❌ کاربردهای حشوآمیز و نامأنوس نظیر `استنتاج تصمیم` (استفاده از `تصمیم‌گیری / اتخاذ تصمیم`)، انباشت مترادف‌های زاید `برنامه‌ریزی، استنتاج و تولید` (استفاده از `برنامه‌ریزی و تولید`)، یا تحمیل ساختار سنگین `با استنتاج مستقیم ... پیشنهاد را ارائه داده` در چکیده (استفاده مستقیم از `ارائه پیشنهاد اولیه (نامی) در مقیاس زیر میلی‌ثانیه‌ای`).
  - `زوج‌های حالت-عمل / زوج‌های متناظر / زوج‌های ناهمخوان`: کاربرد استاندارد واژه ریاضی و آماری «زوج» (\lr{Pair / Paired}) برای چندگانه‌ها، تاپل‌ها و آزمون‌های آماری زوجی vs ❌ کاربرد عامیانه `جفت‌های عمل-حالت / جفت‌های ناهمخوان / جفت‌های متناظر` (و پرهیز از وارونگی ترتیب مؤلفه‌ها در $s, a$)؛ و حفظ اصطلاح تخصصی تثبیت‌شده هوافضا: `جفت‌شدگی‌های آیرودینامیکی` (\lr{Aerodynamic Couplings}).
  - `انضباط واژگانی «عملیاتی»، «تحمیلی» و «معنایی»`:
    - ❌ ممنوعیت گرته‌برداری نامأنوس و غیرفنی `تحمیلی` در ترکیباتی نظیر `جهت‌دهی‌های معنایی تحمیلی`؛ الزام استفاده از `تزریق سوگیری‌های صریح دامنه` یا `فرمول‌بندی توابع پتانسیل دستی`؛ و پرهیز اکید از تکرار مجاور ریشه «تحمیل» در یک جمله واحد (`تحمیلی ... بدون تحمیل بار`).
    - ❌ مهار تورم واژگانی «عملیاتی» در چکیده و بخش‌های مقدماتی: تحدید کاربرد آن به اصطلاحات مصوب رساله (`سوابق عملیاتی` برای \lr{Operational Logs}، `قلمرو عملیاتی` برای \lr{Operational Envelope}، `قیود عملیاتی` برای \lr{Operational Constraints})؛ و پرهیز از افزودن حشوآمیز آن به عنوان صفت زاید برای مشوق مطلوبیت (استفاده از `مشوق‌های مطلوبیت اقدام` به جای `مشوق‌های مطلوبیت عملیاتی اقدام وفقی`) یا واریانس عملکرد مأموریت (استفاده از `واریانس عملکرد` به جای `واریانس عملیاتی`).
    - ❌ پرهیز از کاربرد حشوآمیز و مبهم «معنایی» در ترکیباتی نظیر `مفاهیم معنایی اهداف` (استفاده از `ساختار و مشخصه‌های صریح اهداف`)؛ و تحدید آن به اصطلاحات مستقر نظیر `فضای معنایی` (\lr{Semantic Space}) در بستر \lr{DARTSim}، `نگاشت معنایی` و اصطلاح استاندارد آماری `معناداری آماری` ($p < 0.05$).
  - `انضباط واژگانی دستی`: پرهیز از ترکیب نامأنوس `توابع پتانسیل دستی` (استفاده از `توابع پتانسیل دست‌ساز / وابسته به خبره`)؛ مهار تراکم نامتعارف واژه «دستی» در یک بند یا جمله واحد؛ و جایگزینی عبارت دارای بار منفی `ویژگی‌های دستکاری‌شده` با `ابعاد متغیر در پالایش موضعی / متغیرهای تصمیم تحت مداخله`.
  - `دقت معنایی در سطوح رواداری دالان پروازی DARTSim`: تفکیک دقیق سه سطح `رواداری ملایم ($v_1$)`، `متوسط ($v_2$)` و `سخت‌گیرانه ($v_3$)` vs ❌ تعمیم متناقض و ناصحیح صفت به کل سطوح نظیر `سه سطح رواداری سخت‌گیرانه $v_1$، $v_2$ و $v_3$`.
  - `تثبیت مرز مفهومی وفقی و انطباق`: کاربرد صریح و الزامی `چرخه انطباق` (\lr{Adaptation Cycle})، `طرح انطباق` (\lr{Adaptation Plan})، `فرآیند انطباق` (\lr{Adaptation Process})، `سیاست انطباق` (\lr{Adaptation Policy})، `تصمیمات انطباق` (\lr{Adaptation Decisions}) vs ❌ صفت‌سازی نسبی نامأنوس نظیر `چرخه وفقی`، `طرح وفقی`، `فرآیند وفقی`، `سیاست وفقی`، `تصمیمات وفقی`؛ و پرهیز از کاربرد جمع مکسر مبهم `اعمال وفقی` (استفاده قطعی از `اقدامات وفقی` برای تفکیک از مصدر «اِعمال»).
  - `انضباط واژگانی «فاز»، «فرآیند» و «مؤلفه»`:
    - `فاز` (\lr{Phase}): وام‌واژه غیرضروری در چرخه‌های مهندسی نرم‌افزار و یادگیری؛ ممنوعیت `فاز برنامه‌ریزی` (استفاده از `مرحله برنامه‌ریزی` یا بیان فعلی `هنگام برنامه‌ریزی`)، `فاز آموزش` (استفاده از `آموزش` یا `مرحله آموزش`)، و `فاز پیش‌پرواز` (استفاده از `مرحله پیش‌پرواز`). حفظ «فاز» صرفاً در پدیده‌های فیزیکی و امواج.
    - `فرآیند` (\lr{Process}): ممنوعیت انباشت و حشو اسمی پیش از مصادر و افعال (`فرآیند اعتبارسنجی صوری` $\rightarrow$ `اعتبارسنجی صوری`؛ `گردش فرآیندی` $\rightarrow$ `جریان کاری`). التزام قطعی به حفظ «فرآیند» منحصراً در اشیای ریاضی صوری تثبیت‌شده نظیر `فرآیند تصمیم‌گیری مارکوف (\lr{MDP})`، `فرآیند تصمیم‌گیری مارکوف بخشاً مشاهده‌پذیر (\lr{POMDP})`، و `فرآیندهای تصادفی/پواسون/گوسی`.
    - `مؤلفه` (\lr{Component}): حفظ دقیق در درایه‌ها و ابعاد بردار در جبر خطی (`مؤلفه‌های بردار حالت`, `مؤلفه j-ام بردار عمل`) و موجودیت‌های رسمی معماری نرم‌افزار مبتنی بر مؤلفه (\lr{CBSE})؛ ممنوعیت حشو اسمی و انباشت زنجیره‌ای اضافات (نظیر ❌ `فرآیند تفصیلی مؤلفه پایش و ساخت بردار حالت` $\rightarrow$ `سازوکار تفصیلی پایش و ساخت بردار حالت`).
  - `فرمان‌ها / فرمان‌های کنترلی / فرمان‌های بازپیکربندی / فرمان‌های انطباق`: استفاده از ساختار اصیل زبان فارسی با نشانه جمع «ها» vs ❌ جمع مکسر نامأنوس و اداری/دیوانی `فرامین` (مشابه قاعده ۹۸ برای `مهندسان` vs `مهندسین`).
  - `دقت مفهومی در واژه «مفروض»`: پرهیز از کاربرد مبهم `وضعیت مفروض` در ارزیابی و استنتاج (استفاده از `وضعیت ارزیابی‌شده / حالت جاری سیستم`)؛ شکستن زنجیره اضافه‌های سنگین نظیر `توزیع مفروض زمان طراحی` $\rightarrow$ `توزیع فرضی داده‌ها در زمان طراحی`؛ و ترجیح واژگان روان فارسی نظیر `پیش‌فرض‌ها و محدودیت‌ها` بر ترکیب عربی `مفروضات و محدودیت‌ها`.
  - `انضباط در کاربرد اصطلاح «بازخورد»` (\lr{Feedback}):
    - ✔️ حفظ قطعی، اصیل و ۱۰۰ درصدی اصطلاحات پایه‌ای و معماری کنترل خودکار و حلقه خودمختار نظیر `حلقه بازخورد` (\lr{Feedback Loop}) و `مسیر بازخورد` (\lr{Feedback Path}) به عنوان ارکان بنیادین مهندسی سیستم‌های خودوفق.
    - ❌ ممنوعیت صفت‌سازی نامأنوس نظیر `حلقه‌های بازخوردی` (استفاده مستقیم از ترکیب اضافی `حلقه‌های بازخورد`).
    - ❌ ممنوعیت حشو در یادگیری تقویتی نظیر `پاداش بازخوردی` (استفاده از `پاداش` یا `سیگنال پاداش`).
    - ❌ پرهیز از ترکیب‌های مقلوب و گمراه‌کننده نظیر `اعتبارسنجی صوری بازخورد` (استفاده دقیق از `اعتبارسنجی صوری در مسیر بازخورد`).
    - ❌ پرهیز از تکرار مجاور و حشوآمیز «بازخورد» در یک جمله واحد.
  - `انضباط واژگانی «نامی»، «مجانبی» و «زمان اجرا»`:
    - ❌ **نامی** (\lr{Nominal}): ممنوعیت صفت‌سازی «نامی» در بافت‌های روایی و توصیفی سیاست، عمل و کاندیداها به دلیل دلالت غالب فارسی بر «مشهور/سرشناس»؛ الزام استفاده از **`پیشنهاد پایه سیاست / پیشنهاد اولیه سیاست`** (\lr{Baseline / Initial Policy Proposal}) برای $a_0$، **`اقدام پایه / گزینه پایه`** برای کاندیدای مبدأ، و **`مقدار مبنا / مقدار اسمی`** برای پارامترها ($\rho=0.3$).
    - ❌ **اقدام زمان اجرا**: ممنوعیت ترکیب اضافی سه‌تایی نامأنوس؛ الزام تفکیک با حرف اضافه (**`اقدام در زمان اجرا`**) یا کاربرد اصطلاح استاندارد سیستم‌های خودوفق (**`اقدام وفقی`** / **`انتخاب برخط اقدام وفقی`**).
    - ⚖️ **مجانبی** (\lr{Asymptotic}): حفظ قطعی و دقیق در تعاریف ریاضی و سرستون جداول سنجه‌های یادگیری تقویتی برای $R_\infty$ (**`عملکرد مجانبی`**، **`پاداش مجانبی`**، **`همگرایی مجانبی`**) vs ❌ گرته‌برداری‌های غلیظ و ثقیل در نثر روایی نظیر `برتری مجانبی` (استفاده از **`برتری در عملکرد پایدار بلندمدت`**) یا `ارزش مجانبی` (استفاده از **`پاداش در حالت پایدار`**). پرهیز از ورود آن به چکیده رساله.
- **Audit & Extraction Tools**:
  - Run `python .agents/skills/thesis-persian-terminology/scripts/audit_terms.py` for mandatory rule violations.
  - Run `python .agents/skills/thesis-persian-terminology/scripts/extract_term_context.py --term "<term>"` (powered by `ripgrep`) to extract surrounding context for nuanced terminology arbitration against literature (see [disambiguation_guide.md](.agents/skills/thesis-persian-terminology/references/disambiguation_guide.md)).

---

## 5. Architectural Scopes & Chapter Negative Boundaries

Each chapter has an immutable scientific nature. For detailed contracts, see [chapter_boundaries.md](.agents/skills/thesis-chapter-architect/references/chapter_boundaries.md).

- **فصل ۱ (کلیات و تبیین مسئله)**: Research Contract, Trilemma, Sub-problems 1--3, \lr{RQ1}--\lr{RQ6}, 6 Innovations, Alignment Matrix. ❌ NO code, NO mathematical proofs, NO empirical result tables, NO physical domain kinematics.
- **فصل ۲ (مبانی نظری و مدل‌سازی)**: Mathematical Foundations (MDP, DRL, SMC), Ground Truth Testbed Models (DeltaIoT DAG, DARTSim 6-DOF). ❌ NO novel proposed algorithms (\lr{RS-DRL}, \rsdrlplus), NO empirical results, NO literature critiques.
- **فصل ۳ (پیشینه پژوهش و کارهای مرتبط)**: 5-Dimensional Critical Taxonomy, Synthesis Matrix (Table 3.1), Tripartite Gap. ❌ NO passive textbook summaries, NO proposed algorithm mechanics, NO thesis experimental data.
- **فصل ۴ (روش پیشنهادی و معماری دوسطحی)**: **100% DOMAIN-AGNOSTIC**. Baseline \lr{RS-DRL}, \rsdrlplus, Patterns \sgos & \caepv (\pgalr), Propositions 1 & 2. ❌ NO testbed-specific numbers/topologies in definitions, NO inlined code function names in prose, NO empirical tables.
- **فصل ۵ (ارزیابی تجربی و تحلیل نتایج)**: DeltaIoT & DARTSim benchmarks, 2,000 flights, ablation studies, Wilcoxon/Cohen's $d$ tests. ❌ NO mathematical re-derivations, NO unsupported assertions, NO missing baselines.
- **فصل ۶ (بحث، نتیجه‌گیری و کارهای آتی)**: Mechanistic theorization, Pareto trade-offs, SE guidelines, 4-dimensional validity threats, 3 future horizons. ❌ NO new empirical figures/tables, NO algorithm re-derivations, NO superficial summaries.
- **پیوست‌ها (ضمائم)**: Appendix A: Full UML Workflows; Appendix B: Full Algorithm Listings; Appendix C: Extended Benchmark Logs; Appendix D: Reproducibility Package.

---

## 6. LaTeX, XePersian & BiDi Typography Guidelines

1. **BiDi Math Mode for Numerals & Metrics**: Under XePersian, bare Persian numbers containing decimals, fractions, thousands commas, decibels, or units reverse digit order. Always typeset in math mode with thin space:
   - `$70.5\%$`, `$137/200$`, `$2{,}000$`, `$0.485\,\text{ms}$`, `$-40\,\text{dB}$`.
2. **Heading Safety (`\texorpdfstring`)**: Wrap math symbols or Latin algorithm macros in `\texorpdfstring{$...$}{...}` in headings to guarantee 0 hyperref token warnings.
3. **Strict Ban on Wrapping Cross-References in `\lr{...}`**:
   - Cross-references must remain bare: `شکل \ref{fig:...}`, `جدول \ref{tab:...}`, `بخش \ref{sec:...}`. Wrapping in `\lr{...}` forces Latin numbers and breaks Persian layout.
4. **Table Sizing**: Always use explicit column widths (`p{...}`), `\small` or `\footnotesize`, preventing overfull `\hbox`.
5. **Footnotes**: Move non-acronym English equivalents to `\LTRfootnote{...}` on first chapter mention. Strip redundant parentheticals on later mentions. Never place `\LTRfootnote` inside headings, captions, or tables.
6. **Zero-Defect Verification Command**:
   ```powershell
   python .agents/skills/thesis-latex-typesetting/scripts/verify_build.py thesis_full_toc_persian_v3.log
   ```
   Acceptable build criteria:
   - `Undefined references: 0`
   - `Undefined citations: 0`
   - `Hyperref warnings: 0`
   - `Overfull \hbox > 10pt: 0` (max overfull bounded strictly $< 10\,\text{pt}$)
   - `Total PDF pages: 164-165`
7. **Mandatory Post-Compilation Cleanup Protocol**:
   - Immediately after each XeLaTeX PDF compilation and verification of `thesis_full_toc_persian_v3.log`, the agent **MUST ALWAYS clean up all intermediate build files**:
     ```powershell
     python .agents/skills/thesis-build-cleanup/scripts/clean_build.py
     ```
   - No PDF generation turn is considered complete until all auxiliary artifacts (`.aux`, `.log`, `.out`, `.toc`, `.lof`, `.lot`, `.bbl`, `.blg`, `.idx`, `.xdv`, etc.) have been purged.

---

## 7. Dynamic Rule Synchronization Protocol

Whenever the author in any session introduces a new rule, refines a term, or adjusts a constraint, the agent must:
1. Apply the requested change to the target dissertation files.
2. Concurrently update `AGENTS.md` and the appropriate skill in `.agents/skills/`.
3. Commit and push the updated files when the user triggers a push.
