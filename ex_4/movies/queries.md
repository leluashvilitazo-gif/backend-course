# Django ORM urtiertobebis shemowmeba

# 1. filmis direqtoris migeba


from movies.models import Movie

m = Movie.objects.get(slug="mimino")

m.director
# <Director: giorgi danelia>

m.director.name
# 'giorgi danelia'


> Ganmarteba: ForeignKey-is sashualebit shegvidzlia filmis dakavshirebuli direqtoris migheba.

# 2. filmis janrebis migeba


m.genres.all()
# <QuerySet [<Genre: drama>, <Genre: comedy>]>


> Ganmarteba: ManyToManyField sashualebas gvadzlevs, rom ert films ramdenime janri hqondes.

# 3. filmis msaxiobebis migheba


m.cast.all()
# <QuerySet [<Actor: vaxtang kikabidze>, <Actor: frunzik mkrtchiani>]>


> Ganmarteba: Cast akavshirebs pilmebs da msaxiobebs Role modelis sashualebit.

# 4. Msaxiobebisa da mati personajebis migeba


m.roles.all()

for role in m.roles.all():
    print(role.actor.name, "-", role.character_name)

# vaxtang kikabidze - valiko mizandari
# frunzik mkrtchiani - rubik xachikani


> Ganmarteba: Role modeli inaxavs damatebit informacias msaxiobisa da filmis urtiertobaze, magalitad, romel personajs asrulebs msaxiobi.

# 5. filmis salaros informaciis migeba


m.box_office.tickets_sold
# 20106


> Ganmarteba: OneToOneField sashualebas gvadzlevs, rom films mxolod erti salaros chanaweri hqondes.

# 6. Direqtoris yvela filmis migheba


from movies.models import Director

d = Director.objects.get(name="tengiz abuladze")

d.movies.all()
# <QuerySet [<Movie: monanieba (1984)>, <Movie: natvris xe (1976)>]>


> Ganmarteba: related_name="movies" sashualebas gvadzlevs, rom direqtoridan misi yvela filmi mivigot.

# 7. Direqtoris filmebis raodenobis gamotvla


d.movies.count()
# 2


> Ganmarteba: count() abrunebs direqtortan dakavshirebuli filmebis raodenobas.

# 8. Drama janris filmebis raodenobis gamotvla


from movies.models import Genre

g = Genre.objects.get(name="drama")
g.movies.count()
# 4


> Ganmarteba: ManyToMany urtiertobis reverse mimartulebit shegvidzlia konkretuli janris yvela filmis migeba.

# 9. filmis migheba, romelsac salaros chanaweri ar aqvs


p = Movie.objects.get(slug="pirosmani")
p.box_office


> Shedegi:


# RelatedObjectDoesNotExist: Movie has no box_office.


> Ganmarteba: Tu films BoxOffice chanaweri ar aqvs, reverse OneToOneField urtiertobis mimartvisas Django abrunebs RelatedObjectDoesNotExist shecdomas da ara cariel QuerySet-s.