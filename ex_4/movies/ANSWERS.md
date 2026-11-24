---
> დავალება 4: ქართული კინო, თეორიული კითხვები
---

------
> ნაწილი 1: თეორია

# 1. რა განსხვავებაა null=True -სა და blank=True -ს შორის? TextField -ისთვის
რომელს გამოიყენებდი და რატომ?

blank=True gansazgvravs sheidzleba tu ara veli carieli iyos validaciis dros, da null=True gansazgvravs sheidzleba tu ara bazashi velis mnishvneloba NULL iyos. TextField istvis mxolod blank=True s viyenebt radgan carieli teqsti cariel striqonad inaxeba

# 2. რატომ არის ფულისთვის DecimalField უკეთესი, ვიდრე FloatField ?

FloatField binary base 2 s iyenebs ris gamoc patara shecdomebs ushvebs magalitad 0.1 + 0.2 = 0.30000000000000004 da DecimalField i atobit sizustes inaxavs amitom fulis gamosatvlelad uketesia

# 3. რატომ არ ვწერთ model-ში id ველს? საიდან ჩნდება ის ცხრილში?

Django titoeul models tavisit uwers tavis unique id vels, is iqmneba migrationis shesrulebisas tu primary key ravad ar gangvimartavs

# 4. რა განსხვავებაა auto_now_add=True -სა და auto_now=True -ს შორის? რომელს გამოიყენებდი „შექმნის თარიღისთვის“ და რომელს „ბოლო ცვლილებისთვის“?

auto_now_add=True s gamoviyenebt sheqmnis tarigistvis radgan is tarigs inaxavs mxolod mashin rodesac obieqti pirvelad sheiqmnda da auto_now=True s gamoviyenebt bolo cvlilebistvis radgan dros anaxlebs yovel axal save ze

# 5. რას აკეთებს makemigrations და რას migrate ? რა მოხდება, თუ model-ს შეცვლი, მაგრამ მხოლოდ migrate -ს გაუშვებ?

makemigrations cvlilebebs adetectebs da migration filebs qmnis
migrate makemigrations is mier sheqmnil migration filebidan instruqciebs asrulebs da cvlilebebs axorcielebs database shi

tu mxolod migrates gavushvebt databasei aranair cvlilebas ar miigebs sanam makemigrations da mere migrates ar gavushvebt

# 6. slug = models.SlugField(unique=True) . რა მოხდება, თუ ორ ფილმს ერთნაირ slug-ს მისცემ? რა ფორმით აღიწერება ეს წესი ბაზაში?

radganac slug unique aris djangos databasei meore films daarejectebs

# 7. რატომ ტვირთავ git-ში migration ფაილებს, მაგრამ db.sqlite3 -ს არა?

migrationis failebi xsnian rogor unda sheiqmnas da sheicvalos sheni database struktura rac sxva developerebs swirdebat rom databasei sheqmndan
db.sqlite3 ar vtvirtavt radgan chven databazas da shignit informacias sheicavs rac localze unda darches

# 8. age_rating ველი TextChoices -ით: რა ინახება ბაზაში და რა ჩანს admin-ში?

bazashi inaxeba magalitad "G" da adminshi chans "yvelastvis"

------
> შეკითხვა 4: წესების შემოწმება

# 1. ახალი ფილმი slug-ით mimino , რომელიც უკვე არსებობს.

dublirebul slugs ar inaxavs radgan Movie is slug wels aqvs unique=True

# 2. ახალი ჟანრი სახელით დრამა.

dublirebuli janri ar sheinaxa radgan Genre is name vels aqvs unique=True

# 3. ფილმი ცარიელი description -ით და ცარიელი budget -ით

carieli description da budget warmatebid sheinaxa radgan orive vels aqvs blank=True

# 4. ფილმი ცარიელი release_year -ით.

carieli release_year ar sheinaxa radgan vels blank=True ar aqvs da savaldebuloa


> ------
> # დავალება 5 "4-ის გაგრძელება": თეორია
> ------

# 1. რას ნიშნავს abstract = True? რამდენი ცხრილი შეიქმნება TimeStampedModel-ისთვის და მისი სამი შვილისთვის?

abstract = True nishnavs rom TimeStampedModel i template modelia romlis velebsac memkvidreobit shtamomavali modelebi igeben

sheiqmneba sami cxrili - Genre, Director da Movie, da titoeuli moicavs memkvidreobit migebul created_at da updated_at velebs

# 2. ფილმს ერთი რეჟისორი ჰყავს, რეჟისორს ბევრი ფილმი. რომელ model-ში იწერება ForeignKey და რა სვეტი ჩნდება ბაზაში?

FK iwereba Movie model shi radgan one to many kavshiria, bazashi movies_movie cxrils daemateba director_id sveti

# 3. რატომ ვერ გამოვხატავთ „ფილმი ↔ ჟანრი“ კავშირს ერთი ForeignKey-ით? რას ქმნის Django ManyToManyField-ისთვის?

films da ganrs shoris kavshiri many to many a radgan ert films sheidzleba bevri ganri qondes da piriqitac

ManyToManyField istvis django mesame shualedur cxrils qmnis

# 4. რით განსხვავდება OneToOneField ForeignKey-სგან ბაზის დონეზე?

orive foreign key svets qmnis magram OneToOneField UNIQUE constraint sac amatebs rac uzrunvelyofs rom ert chanawers mxolod erti dakavshirebuli chanaweri sheesabamebodes

# 5. აირჩიე on_delete და დაასაბუთე:
   ># ა) რეჟისორი, რომელსაც ფილმები აქვს, არ უნდა წაიშალოს
   ># ბ) ფილმი წაიშალა: მისი სალაროს მონაცემიც უნდა გაქრეს
   ># გ) ფესტივალი წაიშალა: ფილმი უნდა დარჩეს, უბრალოდ პრემიერის ფესტივალი აღარ ეცოდინება

ა) .PROTECT
ბ) .CASCADE
გ) .SET_NULL

# 6. რას აკეთებს related_name="movies"? რა სახელით მივწვდებოდით რეჟისორის ფილმებს მის გარეშე?

related_name="movies" sashualebas gvadzlevs regisoris obieqtidan mivigot mastan dakavshirebuli filmebi director.movies.all() is gamoyenebit. related_name is gareshe Django gamoiyenebda director.movie_set.all()

# 7. როდის გვჭირდება through model ჩვეულებრივი ManyToManyField-ის ნაცვლად?

through model gvwirdebaa mashin roca MTM Field s damatebiti informacia unda davukavshirot

# 8. რატომ არ სჭირდება ManyToManyField-ს on_delete?

MTMF s on_delete ar swirdeba radgan Django avtomaturad martavs shualedur cxrils.
dakavshirebuli obieqtis washlisas shesabamisi kavshiris chanawerebi ishleba, xolo meore obieqti rcheba

# 9. Movie ცხრილში უკვე 4 ფილმია. რა პრობლემა წარმოიქმნება, თუ დავამატებთ სავალდებულო director ველს?

Django avtomaturad ver gansazgvravs tu romel regisors unda miabas titoeuli filmi, amitom migration is sheqmnisas sawiro gaxdeba arsebuli chanawerebistvis mnishvnelobebis mititeba