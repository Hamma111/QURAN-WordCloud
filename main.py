# coding=utf8
# DO NOT remove the above comment



#### Following libraries are required for the code to work:
# pandas
# matplotlib
# arabic_reshaper
# python-bidi
# wordcloud
## You can install these libraries by using the pip command in cmd. For example, pip install pandas.




###########################
#####  lIBRARIES IMPORT  ##
###########################
from pandas import read_csv
import arabic_reshaper
from bidi.algorithm import get_display
from wordcloud import WordCloud, STOPWORDS
from matplotlib.pyplot import figure, axis, imshow, savefig, style
from matplotlib.pyplot import title as Title
from time import sleep
from os.path import exists
from os import mkdir, system, getcwd


###################################
#####  GENERATE OUTPUT FOLDERS   ##
###################################
if not exists('misc'):
    mkdir('misc')
if not exists('arabic'):
    mkdir('arabic')
if not exists('english'):
    mkdir('english')
    


#########################################
#####  DATA CREATION AND MANIPULATION  ##
#########################################

# Load quran in english
df = read_csv('en.yusufali.csv')
eng_corpus = []
for num in range(1,115):
    full_surah = ""
    for aya in df[df.Surah==num].Text:
        full_surah +=  aya + " "
    eng_corpus.append(full_surah)

# Load quran in arabic
dff = read_csv('Quran-clean-without-aarab.csv', index_col=None)
arabic_corpus = []
for num in range(1,115):
    full_surah = ""
    for aya in dff[dff.SurahNum==num].Ayah:
        full_surah +=  aya + " "
    arabic_corpus.append(full_surah)

# Acquiring meccan and medinan portion of quran
mec_surah_list = [96, 68, 73, 74, 1, 111, 81, 87, 92, 89,
                    93, 94, 103, 100, 108, 102, 107, 109, 105, 113,
                    114, 112, 53, 80, 97, 91, 85, 95, 106, 101,
                    75, 104, 77, 50, 90, 86, 54, 38, 7, 72,
                    36, 25, 35, 19, 20, 56, 26, 27, 28, 17,
                    10, 11, 12, 15, 6, 37, 31, 34, 39, 40,
                    41, 42, 43, 44, 45, 46, 51, 88, 18, 16,
                    71, 14, 21, 23, 32, 52, 67, 69, 70, 78,
                    79, 82, 84, 30, 29, 83]

eng_meccan_corp, eng_medinan_corp = "", ""
arabic_meccan_corp, arabic_medinan_corp = "", ""
for i in range(114):
        if i+1 in mec_surah_list:
            eng_meccan_corp += eng_corpus[i]
            arabic_meccan_corp += arabic_corpus[i]
        else:
            eng_medinan_corp += eng_corpus[i]
            arabic_medinan_corp += arabic_corpus[i]            

            
# Entire quran in eng and arab
all_eng = ' '.join(eng_corpus)
all_arabic = ' '.join(arabic_corpus)



#####################
##### SURAH NAMES  ##
#####################

surahs = """0 -> Al-Fatihah -> الفاتحة
1 -> Al-Baqarah -> البقرة
2 -> Aalimran -> آل عمران
3 -> An-Nisa’ -> النساء
4 -> Al-Ma’idah -> المائدة
5 -> Al-An’am -> الأنعام
6 -> Al-A’raf -> الأعراف
7 -> Al-Anfal -> الأنفال
8 -> At-Taubah -> التوبة
9 -> Yunus -> يونس
10 -> Hud -> هود
11 -> Yusuf -> يوسف
12 -> Ar-Ra’d -> الرعد
13 -> Ibrahim -> إبراهيم
14 -> Al-Hijr -> الحجر
15 -> An-Nahl -> النحل
16 -> Al-Isra’ -> الإسراء
17 -> Al-Kahf -> الكهف
18 -> Maryam -> مريم
19 -> Ta-Ha -> طه
20 -> Al-Anbiya’ -> الأنبياء
21 -> Al-Haj -> الحج
22 -> Al-Mu’minun -> المؤمنون
23 -> An-Nur -> النّور
24 -> Al-Furqan -> الفرقان
25 -> Ash-Shu’ara’ -> الشعراء
26 -> An-Naml -> النّمل
27 -> Al-Qasas -> القصص
28 -> Al-Ankabut -> العنكبوت
29 -> Ar-Rum -> الرّوم
30 -> Luqman -> لقمان
31 -> As-Sajdah -> السجدة
32 -> Al-Ahzab -> الأحزاب
33 -> Saba’ -> سبأ
34 -> Al-Fatir -> فاطر
35 -> Ya-Sin -> يس
36 -> As-Saffah -> الصافات
37 -> Sad -> ص
38 -> Az-Zumar -> الزمر
39 -> Ghafar -> غافر
40 -> Fusilat -> فصّلت
41 -> Ash-Shura -> الشورى
42 -> Az-Zukhruf -> الزخرف
43 -> Ad-Dukhan -> الدّخان
44 -> Al-Jathiyah -> الجاثية
45 -> Al-Ahqaf -> الأحقاف
46 -> Muhammad -> محمد
47 -> Al-Fat’h -> الفتح
48 -> Al-Hujurat -> الحجرات
49 -> Qaf -> ق
50 -> Adz-Dzariyah -> الذاريات
51 -> At-Tur -> الطور
52 -> An-Najm -> النجم
53 -> Al-Qamar -> القمر
54 -> Ar-Rahman -> الرحمن
55 -> Al-Waqi’ah -> الواقعة
56 -> Al-Hadid -> الحديد
57 -> Al-Mujadilah -> المجادلة
58 -> Al-Hashr -> الحشر
59 -> Al-Mumtahanah -> الممتحنة
60 -> As-Saf -> الصف
61 -> Al-Jum’ah -> الجمعة
62 -> Al-Munafiqun -> المنافقون
63 -> At-Taghabun -> التغابن
64 -> At-Talaq -> الطلاق
65 -> At-Tahrim -> التحريم
66 -> Al-Mulk -> الملك
67 -> Al-Qalam -> القلم
68 -> Al-Haqqah -> الحاقة
69 -> Al-Ma’arij -> المعارج
70 -> Nuh -> نوح
71 -> Al-Jinn -> الجن
72 -> Al-Muzammil -> المزّمّل
73 -> Al-Mudaththir -> المدّثر
74 -> Al-Qiyamah -> القيامة
75 -> Al-Insan -> الإنسان
76 -> Al-Mursalat -> المرسلات
77 -> An-Naba’ -> النبأ
78 -> An-Nazi’at -> النازعات
79 -> ‘Abasa -> عبس
80 -> At-Takwir -> التكوير
81 -> Al-Infitar -> الإنفطار
82 -> Al-Mutaffifin -> المطفّفين
83 -> Al-Inshiqaq -> الإنشقاق
84 -> Al-Buruj -> البروج
85 -> At-Tariq -> الطارق
86 -> Al-A’la -> الأعلى
87 -> Al-Ghashiyah -> الغاشية
88 -> Al-Fajr -> الفجر
89 -> Al-Balad -> البلد
90 -> Ash-Shams -> الشمس
91 -> Al-Layl -> الليل
92 -> Adh-Dhuha -> الضحى
93 -> Al-Inshirah -> الشرح
94 -> At-Tin -> التين
95 -> Al-‘Alaq -> العلق
96 -> Al-Qadar -> القدر
97 -> Al-Bayinah -> البينة
98 -> Az-Zalzalah -> الزلزلة
99 -> Al-‘Adiyah -> العاديات
100 -> Al-Qari’ah -> القارعة
101 -> At-Takathur -> التكاثر
102 -> Al-‘Asr -> العصر
103 -> Al-Humazah -> الهمزة
104 -> Al-Fil -> الفيل
105 -> Quraish -> قريش
106 -> Al-Ma’un -> الماعون
107 -> Al-Kauthar -> الكوثر
108 -> Al-Kafirun -> الكافرون
109 -> An-Nasr -> النصر
110 -> Al-Masad -> المسد
111 -> Al-Ikhlas -> الإخلاص
112 -> Al-Falaq -> الفلق
113 -> An-Nas -> النّاس"""
surah_name = [x.split('->')[1].strip() for x in surahs.split('\n')]
surah_name_arabic = [x.split('->')[2].strip() for x in surahs.split('\n')]




######################
##### STOPWORDS CELL##
######################

# to get redundant words(pronouns etc) so we can omit them later on
SW = list(STOPWORDS) + ['ye', 'verily', 'will', 'said', 'say', 'us', 'thy', 'thee', 'thou',
                        'the', 'and', 'of', 'to', 'is', 'in', 'they', 'a', 'that', 'for', 
                        'ye', 'who', 'their', 'not', 'them', 'He', 'be', 
                        'We', 'those', 'with', 'have', 'are', 'And', 'from', 'it', 'but', 
                        'on', 'you', 'your', 'all', 'as', 'he', 'shall', 'if', 'thou', 'no',
                        'which', 'But', 'do', 'his', 'what', 'I', 'or', 'when', 'we', 'by', 
                        'His', 'said:', 'thy', 'has', 'this', 'They', 'there', 
                        'then', 'one', 'my', 'him', 'were', 'was', 'thee', 'them,', 'may', 'any',
                        'had', 'sent', 'before', 'nor', 'among', 'whom', 'Day', 'hath', 'made', 
                        'did', '(of', 'Who', 'would', '(in', 'out', 'Say:', 'our', 'indeed',
                        'so', 'If', '(to', '(the', 'against', 'been', 'an', 'For', 'you,', 
                        'us', 'The', 'Then', 'fear', 'than', 'give', '-', 'should', 'such', 'Most',
                        'down', 'men', 'So', 'say:', '"O', 'Our', 'It', 'come', 'can', 'after', 'O', 
                        'me', 'some', 'turn', '', 'over', 'up', 'things', 'make', 'know',
                        'reject', 'When', 'unto', 'into', 'its', 'see', 'Those', 'only', 
                        'them:','good', 'own', 'doth', 'of)', 'most', 'other', 
                        'except', '(for', 'Thou', 'at', '(and', 'between', 'take', 'away',
                        'given', 'every', 'back', 'say,', 'verily', 'never', 'That', 'said'
                       'whose', 'where', 'which', 'how', 'when']

# arabic redundant words
s = ['من', 'في', 'ما',
       'إن', 'لا', 'على', 'إلا', 'ولا', 'وما', 'أن', 'قال', 'إلى', 'لهم', 'يا', 'ومن', 'ثم', 'لكم', 'به', 'كان', 'بما'
       , 'قل', 'ذلك', 'أو', 'له', 'الذي', 'هو',  'هم', 'وإن', 'قالوا', 'كل', 'فيها', 'كانوا', 'عن', 'إذا',  'عليهم', 
       'شيء', 'هذا', 'كنتم',  'لم', 'وهو', 'فإن', 'إذ',  'عليكم',  'إنا', 'فلا', 'منهم',  'أيها', 'إنه','بعد', 'عليه',
       'حتى', 'وهم', 'وإذا', 'أولئك', 'أم', 'إني', 'ولقد', 'فيه', 'بل', 'قد', 'عند', 'إنما', 'ولكن', 'ولو',
       'مما',  'منكم', 'فلما', 'ألا', 'لمن',  'دون', 'فمن', 'منه', 'فإذا', 'فما', 'منها', 'كذلك', 'وقال', 'وكان']
ASW1 = [get_display(arabic_reshaper.reshape(x)) for x in s]

## fetched this list of stopwords of arabic from https://github.com/mohataher/arabic-stop-words/blob/master/list.txt
s = "ء,ءَ,آ,آب,آذار,آض,آل,آمينَ,آناء,آنفا,آه,آهاً,آهٍ,آهِ,أ,أبدا,أبريل,أبو,أبٌ,أجل,أجمع,أحد,أخبر,أخذ,أخو,أخٌ,أربع,أربعاء,أربعة,أربعمئة,أربعمائة,أرى,أسكن,أصبح,أصلا,أضحى,أطعم,أعطى,أعلم,أغسطس,أفريل,أفعل به,أفٍّ,أقبل,أكتوبر,أل,ألا,ألف,ألفى,أم,أما,أمام,أمامك,أمامكَ,أمد,أمس,أمسى,أمّا,أن,أنا,أنبأ,أنت,أنتم,أنتما,أنتن,أنتِ,أنه,أنًّ,أنّى,أهلا,أو,أوت,أوشك,أول,أولئك,أولاء,أولالك,أوّهْ,أى,أي,أيا,أيار,أيضا,أيلول,أين,أيّ,أيّان,أُفٍّ,ؤ,إذ,إذا,إذاً,إذما,إذن,إزاء,إلى,إلي,إليكم,إليكما,إليكنّ,إليكَ,إلَيْكَ,إلّا,إمّا,إن,إنَّ,إى,إياكم,إياكما,إياكن,إيانا,إياه,إياها,إياهم,إياهما,إياهن,إياي,إيهٍ,ئ,ا,ا?,ا?ى,االا,االتى,ابتدأ,ابين,اتخذ,اثر,اثنا,اثنان,اثني,اثنين,اجل,احد,اخرى,اخلولق,اذا,اربعة,اربعون,اربعين,ارتدّ,استحال,اصبح,اضحى,اطار,اعادة,اعلنت,اف,اكثر,اكد,الآن,الألاء,الألى,الا,الان,الاولى,التى,التي,الحالي,الذاتي,الذى,الذي,الذين,السابق,الف,اللاتي,اللتان,اللتيا,اللتين,اللذان,اللذين,اللواتي,الماضي,المقبل,الوقت,الى,الي,اليه,اليها,اما,امام,امس,امسى,ان,انبرى,انقلب,انه,انها,او,اول,اي,ايار,ايام,ايضا,ب,بؤسا,بإن,بئس,باء,بات,باسم,بان,بخٍ,بد,بدلا,برس,بسبب,بسّ,بشكل,بضع,بطآن,بعد,بعدا,بعض,بغتة,بل,بلى,بن,به,بها,بهذا,بيد,بين,بَسْ,بَلْهَ,ة,ت,تاء,تارة,تاسع,تانِ,تانِك,تبدّل,تجاه,تحوّل,تخذ,ترك,تسع,تسعة,تسعمئة,تسعمائة,تسعون,تسعين,تشرين,تعسا,تعلَّم,تفعلان,تفعلون,تفعلين,تكون,تلقاء,تلك,تم,تموز,تينك,تَيْنِ,تِه,تِي,ث,ثاء,ثالث,ثامن,ثان,ثاني,ثلاث,ثلاثاء,ثلاثة,ثلاثمئة,ثلاثمائة,ثلاثون,ثلاثين,ثم,ثمان,ثمانمئة,ثمانون,ثماني,ثمانية,ثمانين,ثمنمئة,ثمَّ,ثمّ,ثمّة,ج,جانفي,جدا,جعل,جلل,جمعة,جميع,جنيه,جوان,جويلية,جير,جيم,ح,حاء,حادي,حار,حاشا,حاليا,حاي,حبذا,حبيب,حتى,حجا,حدَث,حرى,حزيران,حمدا,حمو,حمٌ,حوالى,حول,حيث,حيثما,حين,حيَّ,حَذارِ,خ,خاء,خاصة,خال,خامس,خلا,خلافا,خلال,خلف,خمسة,خمسمئة,خمسمائة,خمسون,خمسين,خميس,د,دال,درهم,درى,دواليك,دولار,دون,دونك,ديسمبر,دينار,ذ,ذا,ذات,ذاك,ذال,ذانك,ذانِ,ذلك,ذهب,ذو,ذيت,ذينك,ذَيْنِ,ذِه,ذِي,ر,رأى,راء,رابع,راح,رجع,رزق,رويدك,ريال,ريث,ز,زاي,زعم,زود,زيارة,س,ساء,سادس,سبت,سبتمبر,سبحان,سبعة,سبعمئة,سبعمائة,سبعون,سبعين,ست,ستة,ستكون,ستمئة,ستمائة,ستون,ستين,سحقا,سرا,سرعان,سقى,سمعا,سنتيم,سنوات,سوف,سوى,سين,ش,شباط,شبه,شتانَ,شخصا,شرع,شيكل,شين,شَتَّانَ,ص,صاد,صار,صباح,صبر,صبرا,صدقا,صراحة,صفر,صهٍ,صهْ,ض,ضاد,ضحوة,ضد,ضمن,ط,طاء,طاق,طالما,طرا,طفق,طَق,ظ,ظاء,ظل,ظلّ,ظنَّ,ع,عاد,عاشر,عام,عاما,عامة,عجبا,عدا,عدة,عدد,عدم,عدَّ,عسى,عشر,عشرة,عشرون,عشرين,عل,علق,علم,على,علي,عليك,عليه,عليها,علًّ,عن,عند,عندما,عنه,عنها,عوض,عيانا,عين,عَدَسْ,غ,غادر,غالبا,غدا,غداة,غير,غين,ـ,ف,فإن,فاء,فان,فانه,فبراير,فرادى,فضلا,فقد,فقط,فكان,فلان,فلس,فهو,فو,فوق,فى,في,فيفري,فيه,فيها,ق,قاطبة,قاف,قال,قام,قبل,قد,قرش,قطّ,قلما,قوة,ك,كأن,كأنّ,كأيّ,كأيّن,كاد,كاف,كان,كانت,كانون,كثيرا,كذا,كذلك,كرب,كسا,كل,كلتا,كلم,كلَّا,كلّما,كم,كما,كن,كى,كيت,كيف,كيفما,كِخ,ل,لأن,لا,لا سيما,لات,لازال,لاسيما,لام,لايزال,لبيك,لدن,لدى,لدي,لذلك,لعل,لعلَّ,لعمر,لقاء,لكن,لكنه,لكنَّ,للامم,لم,لما,لمّا,لن,له,لها,لهذا,لهم,لو,لوكالة,لولا,لوما,ليت,ليرة,ليس,ليسب,م,مئة,مئتان,ما,ما أفعله,ما انفك,ما برح,مائة,ماانفك,مابرح,مادام,ماذا,مارس,مازال,مافتئ,ماي,مايزال,مايو,متى,مثل,مذ,مرّة,مساء,مع,معاذ,معه,مقابل,مكانكم,مكانكما,مكانكنّ,مكانَك,مليار,مليم,مليون,مما,من,منذ,منه,منها,مه,مهما,ميم,ن,نا,نبَّا,نحن,نحو,نعم,نفس,نفسه,نهاية,نوفمبر,نون,نيسان,نيف,نَخْ,نَّ,ه,هؤلاء,ها,هاء,هاكَ,هبّ,هذا,هذه,هل,هللة,هلم,هلّا,هم,هما,همزة,هن,هنا,هناك,هنالك,هو,هي,هيا,هيهات,هيّا,هَؤلاء,هَاتانِ,هَاتَيْنِ,هَاتِه,هَاتِي,هَجْ,هَذا,هَذانِ,هَذَيْنِ,هَذِه,هَذِي,هَيْهات,و,و6,وأبو,وأن,وا,واضاف,واضافت,واكد,والتي,والذي,وان,واهاً,واو,واوضح,وبين,وثي,وجد,وراءَك,ورد,وعلى,وفي,وقال,وقالت,وقد,وقف,وكان,وكانت,ولا,ولايزال,ولكن,ولم,وله,وليس,ومع,ومن,وهب,وهذا,وهو,وهي,وَيْ,وُشْكَانَ,ى,ي,ياء,يفعلان,يفعلون,يكون,يلي,يمكن,ين,يناير,يوان,يورو,يوليو,يونيو,ّأيّان,".split(',')
ASW2 = [get_display(arabic_reshaper.reshape(x)) for x in s]

### Obtained new combined corpus of redundant words
ASW = ASW1 + ASW2


#######################################
#######################################
#######################################
##  FUNCTION TO GENERATE WORDCLOUDS  ##
#######################################
####  FOCAL PART OF THIS CODE  ########
#######################################
#######################################
style.use('dark_background')
def generateWordCloud(surah=None, corpus=None, title=None, isArabic=False):
    figure(figsize=(17,10))
    
    if not isArabic:
        wc = WordCloud(stopwords=SW, max_words=80, width=800, height=400,
                       background_color='black')
        if surah is None:
            wc.generate(corpus)
            Title(title+'\n', fontdict={'fontsize':40})
            fileName = f'misc/{title}.png'
        else:
            wc.generate(eng_corpus[surah])
            Title(surah_name[surah]+'\n', fontdict={'fontsize':40})
            fileName = f'english/{surah+1}-{surah_name[surah]}.png'

    if isArabic:
        wc = WordCloud(font_path='arial.ttf', #relative_scaling=1,
                       stopwords=ASW, max_words=80, width=800, height=400,
                       background_color='black')
        if surah is None:
            wc = wc.generate_from_text(get_display(arabic_reshaper.reshape(corpus))) 
            Title(get_display(arabic_reshaper.reshape(title))+'\n', fontdict={'fontsize':40})
            fileName = f'misc/{title}.png'
        else:
            wc = wc.generate_from_text(get_display(arabic_reshaper.reshape(arabic_corpus[surah])))
            Title(get_display(arabic_reshaper.reshape(surah_name_arabic[surah])) +'\n', fontdict={'fontsize':40})
            fileName = f'arabic/{surah+1}-{surah_name[surah]}.png'
    
    imshow(wc)
    axis('off')
    
    savefig(fileName, dpi=200, bbox_inches='tight', pad_inches=0)



#####################
#To display progress#
#####################
def prog(b1, b2, corp):
    _ = system('cls')
    temp = '=='*b1 + '>' + '..'*b2
    print(f'[{temp}]  PROGRESS OF CORPUS {corp}/3')
    

################
## FULL QURAN ##
################
prog(0,12,1)
generateWordCloud(corpus=all_eng, title='Entire Quran')
prog(2,10,1)
generateWordCloud(corpus=all_arabic, title='Entire Quran Arabic', isArabic=True)
prog(4,8,1)


################################
## MECCAN AND MEDINAN CORPUS ###
################################
# in eng
generateWordCloud(corpus=eng_meccan_corp, title="Meccan(Makki) Surahs English")
prog(6,6,1)
generateWordCloud(corpus=eng_medinan_corp, title="Medinan(Madni) Surahs English")
prog(8,4,1)

# in arab
generateWordCloud(corpus=arabic_meccan_corp, title="Meccan(Makki) Surahs Arabic", isArabic=True)
prog(10,2,1)
generateWordCloud(corpus=arabic_medinan_corp, title="Medinan(Madni) Surahs Arabic", isArabic=True)
prog(12,0,1)

print('CORPUS 1 complete')
sleep(2)
try:
    system('explorer.exe '+ getcwd() +'\\misc')
except Exception as ex:
    print(f'{ex}  - it occured but code wont stope.')





################################
## QURAN CHAPTERS ENGLISH #####
################################
end = len(eng_corpus)
for i in range(end):
    generateWordCloud(i, eng_corpus)
    prog(i+1, end-i-2, 2)
    print('might take couple of minutes')
    
print('CORPUS 2 complete')
sleep(2)
try:
    system('explorer.exe '+ getcwd() +'\\english')
except Exception as ex:
    print(f'{ex}  - it occured but code wont stope.')

open('challenge.txt', 'w').writelines('Find the connection of words and conviction of words that appear in the images to surah names.\n'
                                      'Can you derive insights from that? \nHint: Check https://www.kaggle.com/hammaadali/quran-word-cloud/notebook ')




################################
## QURAN SURAHS ARABIC ########
################################
end = len(arabic_corpus)
for i in range(end):
    generateWordCloud(i, arabic_corpus, isArabic=True)
    prog(i+1, end-i-2, 3)
    print('might take couple of minutes')

print('CORPUS 3 complete')
sleep(2)
try:
    system('explorer.exe '+ getcwd() +'\\arabic')
except Exception as ex:
    print(f'{ex}  - it occured but code wont stope.')

_ = system('cls')
print('Thanks if you made it this far. Have a good day.')
sleep(100)
