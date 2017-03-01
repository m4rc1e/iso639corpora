# iso639 Corpora
sqlite3 database for languages specified in iso639 with Wikipedia sample text.


### Using the db with [peewee](https://github.com/coleifer/peewee):
```
>>>from models import db, Languages
>>>db.connect()
>>> # row with iso639-1 codes
>>>hindi = Language.get(Languages.part1 == 'hi')
>>>hindi.text
'**वीर्य** एक जैविक तरल पदार्थ है, जिसे _बीजीय या वीर्य तरल_ भी कहते हैं, जिसमे सामान्यतः शुक्राणु होते हैं। यह जननग्रन्थि (यौन ग्रंथियां) तथा नर या उभयलिंगी प्राणियों के अन्य अंगों द्वारा स्रावित होता है और मादा अंडाणु को निषेचित कर सकता है। इंसानों में, शुक्राणुओं के अलावा बीजीय तरल में अनेक घटक होते हैं: बीजीय तरल के प्रोटियोलिटिक और अन्य एंजाइमों के साथ-साथ फलशर्करा तत्व शुक्राणुओं के अस्तित्व की रक्षा करते हैं और उन्हें एक ऐसा माध्यम प्रदान करते हैं जहां वे चल-फिर सकें या "तैर" सकें. वो प्रक्रिया जिसके परिणामस्वरूप वीर्य का प्रवाह होता है उसे _स्खलन_ कहा जाता है।'

>>> # row with iso639-2 codes
>>> bengali = Languages.get(Languages.part2 == 'ben')
>>> bengali.text
'**হোসাবেত্তু** (ইংরেজি:Hosabettu), ভারতের কেরালা রাজ্যের কসরগোদ জেলার একটি শহর ।'

>>> # acessing all rows which contain sample text
>>> all_texts = Languages.select().where(~(Languages.text >> None))
>>> for language in languages:
>>>     language.text
```

### Installation
```
git clone https://github.com/m4rc1e/iso639corpora
cd iso639corpora
virtualenv --python==python3.5 env
source env/bin/activate
pip install -r requirements.txt

```

### Generate your own db
```
python build.py
```

### caveats
Random pages are used for each language. The db will be unique for each time it is generated.