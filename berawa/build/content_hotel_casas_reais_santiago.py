# Contenido de la demo Casas Reais (Santiago de Compostela) (es/en/fr/de). Hechos de casasreais.es leidos el 02/11/2026 (ver berawa/sources.json). Sin precios, valoraciones ni resenas.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Habitación doble','Habitación doble superior','Doble deluxe con bañera de hidromasaje','Ático con bañera de hidromasaje'],'en':['Double room','Superior double room','Deluxe double with whirlpool bath','Attic room with whirlpool bath'],'fr':['Chambre double','Chambre double supérieure','Double deluxe avec baignoire balnéo','Chambre sous les toits avec baignoire balnéo'],'de':['Doppelzimmer','Doppelzimmer Superior','Deluxe-Doppelzimmer mit Whirlpool-Badewanne','Dachgeschosszimmer mit Whirlpool-Badewanne']}
RD={
'es':['Cómoda e insonorizada, con cama de 150 cm, Smart TV de 55”, minibar y baño con ducha.','Más amplia y luminosa gracias a su ubicación en esquina, con Smart TV de 55” y minibar.','Amplia y elegante, con cama de 180 cm, Smart TV de 65” y bañera de hidromasaje.','Habitación singular en la planta ático, con vistas sobre Santiago y bañera de hidromasaje.'],
'en':['Comfortable and soundproofed, with a 150 cm bed, 55” Smart TV, minibar and bathroom with shower.','More spacious and bright thanks to its corner location, with a 55” Smart TV and minibar.','Spacious and elegant, with a 180 cm bed, 65” Smart TV and whirlpool bath.','A unique room on the attic floor, with views over Santiago and a whirlpool bath.'],
'fr':['Confortable et insonorisée, avec lit de 150 cm, Smart TV 55”, minibar et salle de bains avec douche.','Plus spacieuse et lumineuse grâce à sa position d’angle, avec Smart TV 55” et minibar.','Spacieuse et élégante, avec lit de 180 cm, Smart TV 65” et baignoire balnéo.','Chambre singulière à l’étage sous les toits, avec vue sur Santiago et baignoire balnéo.'],
'de':['Komfortabel und schallisoliert, mit 150-cm-Bett, 55”-Smart-TV, Minibar und Bad mit Dusche.','Geräumiger und heller dank der Ecklage, mit 55”-Smart-TV und Minibar.','Geräumig und elegant, mit 180-cm-Bett, 65”-Smart-TV und Whirlpool-Badewanne.','Ein besonderes Zimmer im Dachgeschoss mit Blick über Santiago und Whirlpool-Badewanne.']}
ART={
'hero':('skyline',6611,['#1a1c22','#c9a24f','#efe3c6','#5c5355','#3a3436','#16171b']),
'intro':('arches',6612,['#f3efe6','#fbf8f1','#8a6a2e','#5f5354','#2a2526']),
'r1':('columns',6621,['#efeae0','#e3c77f','#8a6a2e','#5f5354','#2a2526']),
'r2':('arches',6622,['#1a1c22','#c9a24f','#efe3c6','#5c5355','#3a3436','#16171b']),
'r3':('waves',6623,['#1a1c22','#d1ad5c','#f1e6cb','#655b5d','#403a3c','#1b1c20']),
'r4':('skyline',6624,['#1a1c22','#c9a24f','#efe3c6','#5c5355','#3a3436','#16171b']),
'g1':('columns',6631,['#f1ece3','#faf6ef','#8a6a2e','#5f5354','#2a2526']),
'g2':('hills',6632,['#e9e5dc','#ece0c2','#d1ad5c','#8f8a7c','#666054','#433f38']),
'g3':('arches',6633,['#f3efe6','#fbf8f1','#8a6a2e','#5f5354','#2a2526']),
'g4':('waves',6634,['#1a1c22','#c9a24f','#efe3c6','#5c5355','#3a3436','#16171b'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3','r4'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Casas Reais · Alojamiento boutique en el casco histórico de Santiago',see_rooms='Ver las habitaciones',hero_k='Santiago · Rúa das Casas Reais, 29',hero_t='Alojamiento boutique a cinco minutos de la Catedral',hero_s='Habitaciones diferentes, camas premium y desayuno artesano, en pleno casco histórico de Santiago.',
 intro_t='Descanso, diseño y atención en cada detalle',intro_p1='Las 11 habitaciones de Casas Reais tienen identidad propia, inspirada en residencias reales de la historia y la cultura popular. Todas son exteriores e insonorizadas.',
 intro_p2='Cada mañana, desayuno artesano: pan, bollería y tarta de Santiago elaborados a mano, con café de alta calidad. En recepción te recomiendan planes y te ayudan con excursiones y traslados al aeropuerto.',
 stats=['5 min a pie de la Catedral','11 habitaciones','WiFi gratuito','Recepción de 8:00 a 22:00'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Todas con colchones premium, Smart TV, escritorio, WiFi gratuito, aire acondicionado, calefacción, minibar y caja fuerte.',
 svcs=['Desayuno artesano','Excursiones a Finisterre y Rías Baixas','Traslados al aeropuerto','Sillón de masaje gratuito para huéspedes','Parking público con carga eléctrica a 150 m','Guarda equipajes gratuito y ascensor'],
 loc_p='Rúa das Casas Reais, 29 · 15704 Santiago de Compostela. Teléfono: 981 555 709 (todos los días, de 8:00 a 22:00). Correo: reservas@casasreais.es.',
 chips=['¿Qué habitaciones tenéis?','¿Cómo es el desayuno?','¿Hay parking?','¿Cómo reservo?']),
'en':dict(title='Casas Reais · Boutique stay in the old town of Santiago',see_rooms='See the rooms',hero_k='Santiago · Rúa das Casas Reais, 29',hero_t='Boutique stay five minutes from the Cathedral',hero_s='Distinctive rooms, premium beds and a homemade breakfast, right in the old town of Santiago.',
 intro_t='Rest, design and care in every detail',intro_p1='Each of the 11 rooms at Casas Reais has its own identity, inspired by royal residences from history and popular culture. All are exterior-facing and soundproofed.',
 intro_p2='Every morning, a homemade breakfast: bread, pastries and Santiago tart made by hand, with high-quality coffee. Reception gives recommendations and helps with excursions and airport transfers.',
 stats=['5 min walk to the Cathedral','11 rooms','Free WiFi','Reception 8:00 to 22:00'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='All with premium mattresses, Smart TV, desk, free WiFi, air conditioning, heating, minibar and safe.',
 svcs=['Homemade breakfast','Excursions to Finisterre and Rías Baixas','Airport transfers','Free massage chair for guests','Public car park with EV charging 150 m away','Free luggage storage and lift'],
 loc_p='Rúa das Casas Reais, 29 · 15704 Santiago de Compostela. Phone: +34 981 555 709 (every day, 8:00 to 22:00). Email: reservas@casasreais.es.',
 chips=['Which rooms do you have?','What is breakfast like?','Is there parking?','How do I book?']),
'fr':dict(title='Casas Reais · Séjour boutique dans la vieille ville de Saint-Jacques',see_rooms='Voir les chambres',hero_k='Santiago · Rúa das Casas Reais, 29',hero_t='Séjour boutique à cinq minutes de la cathédrale',hero_s='Des chambres singulières, des lits premium et un petit-déjeuner artisanal, en pleine vieille ville de Saint-Jacques.',
 intro_t='Repos, design et attention à chaque détail',intro_p1='Les 11 chambres de Casas Reais ont chacune leur identité, inspirée de résidences royales de l’histoire et de la culture populaire. Toutes donnent sur l’extérieur et sont insonorisées.',
 intro_p2='Chaque matin, un petit-déjeuner artisanal : pain, viennoiseries et tarte de Santiago faits main, avec un café de grande qualité. La réception conseille des sorties et aide pour les excursions et les transferts vers l’aéroport.',
 stats=['5 min à pied de la cathédrale','11 chambres','WiFi gratuit','Réception de 8h à 22h'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Toutes avec matelas premium, Smart TV, bureau, WiFi gratuit, climatisation, chauffage, minibar et coffre-fort.',
 svcs=['Petit-déjeuner artisanal','Excursions à Finisterre et aux Rías Baixas','Transferts vers l’aéroport','Fauteuil de massage gratuit pour les clients','Parking public avec recharge électrique à 150 m','Consigne à bagages gratuite et ascenseur'],
 loc_p='Rúa das Casas Reais, 29 · 15704 Saint-Jacques-de-Compostelle. Téléphone : +34 981 555 709 (tous les jours, de 8h à 22h). E-mail : reservas@casasreais.es.',
 chips=['Quelles chambres avez-vous ?','Comment est le petit-déjeuner ?','Où se garer ?','Comment réserver ?']),
'de':dict(title='Casas Reais · Boutique-Unterkunft in der Altstadt von Santiago',see_rooms='Zimmer ansehen',hero_k='Santiago · Rúa das Casas Reais, 29',hero_t='Boutique-Unterkunft fünf Minuten von der Kathedrale',hero_s='Besondere Zimmer, Premium-Betten und handgemachtes Frühstück, mitten in der Altstadt von Santiago.',
 intro_t='Erholung, Design und Aufmerksamkeit im Detail',intro_p1='Die 11 Zimmer von Casas Reais haben jeweils eine eigene Identität, inspiriert von königlichen Residenzen aus Geschichte und Volkskultur. Alle liegen nach außen und sind schallisoliert.',
 intro_p2='Jeden Morgen ein handgemachtes Frühstück: Brot, Gebäck und Santiago-Torte, dazu Kaffee in hoher Qualität. Die Rezeption gibt Empfehlungen und hilft bei Ausflügen und Flughafentransfers.',
 stats=['5 Gehminuten zur Kathedrale','11 Zimmer','Kostenloses WLAN','Rezeption 8:00 bis 22:00'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Alle mit Premium-Matratzen, Smart-TV, Schreibtisch, kostenlosem WLAN, Klimaanlage, Heizung, Minibar und Safe.',
 svcs=['Handgemachtes Frühstück','Ausflüge nach Finisterre und in die Rías Baixas','Flughafentransfers','Kostenloser Massagesessel für Gäste','Öffentliches Parkhaus mit E-Ladestationen in 150 m','Kostenlose Gepäckaufbewahrung und Aufzug'],
 loc_p='Rúa das Casas Reais, 29 · 15704 Santiago de Compostela. Telefon: +34 981 555 709 (täglich 8:00 bis 22:00). E-Mail: reservas@casasreais.es.',
 chips=['Welche Zimmer gibt es?','Wie ist das Frühstück?','Wo kann ich parken?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://casasreais.es/#reservas'
BOOK=dict(mode='engine',url=dict(es=R,en=R,fr=R,de=R))
D=dict(name='Casas Reais',ac='#1a1c22',ac2='#8a6a2e',ac2_a11y='#6e5222',book=BOOK,around=[],foot=FOOT,
 address='Rúa das Casas Reais, 29 · 15704 Santiago de Compostela',phones=['+34 981 555 709'],emails=['reservas@casasreais.es'],maps='Casas Reais, Rúa das Casas Reais 29, 15704 Santiago de Compostela',t=T)
META=dict(repo='demo-hotel-casas-reais-santiago',name='Casas Reais',legal_name='PORTA DO CAMIÑO FRANCÉS, S.L., NIF B70096185 (aviso legal de su web)',registry_ids=['B70096185'],
 url='https://casasreais.es/',domain='casasreais.es',municipality='Santiago de Compostela',province='A Coruña',sector='alojamiento boutique de 11 habitaciones en el casco historico de Santiago',
 read_at='2026-11-02T09:00:00+01:00',created_at='2026-11-02T08:58:00+01:00',built_at='2026-11-02T09:10:00+01:00',audit_date='2026-11-02T09:00:00+01:00',
 rating=dict(value=4.5,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Casas+Reais+P.R./@42.8819041,-8.5404406,17z'),
 book=dict(mode='engine',url=R,note='motor WuBook incrustado en su propia web (seccion #reservas de la portada, widget de WuBook «Casas Reais»; los botones Reservar de su web llevan ahi). Sin URL directa publica del motor: se enlaza su seccion de reservas, HTTP 200 (02/11/2026 09:00). Solo en espanol, mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Hay bañera de hidromasaje?','K02'),('¿Qué tienen las habitaciones?','K03'),('¿Cómo es el desayuno?','K04'),('¿Hay parking?','K05'),('¿Dónde estáis?','K06'),('¿Cómo llego desde el aeropuerto?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Organizáis excursiones?','K09'),('¿Qué ver cerca?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Puedo dejar las maletas?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Are there rooms with a whirlpool bath?','K02'),('What do the rooms include?','K03'),('What is breakfast like?','K04'),('Is there parking?','K05'),('Where are you?','K06'),('How do I get there from the airport?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Do you organise excursions?','K09'),('What is there to see nearby?','K10'),('What is your phone number?','K11'),('Can I leave my luggage?','K12'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Y a-t-il des chambres avec baignoire balnéo ?','K02'),('Que comprennent les chambres ?','K03'),('Comment est le petit-déjeuner ?','K04'),('Y a-t-il un parking ?','K05'),('Où êtes-vous ?','K06'),('Comment venir depuis l’aéroport ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Organisez-vous des excursions ?','K09'),('Que voir à proximité ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Puis-je laisser mes bagages ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es Zimmer mit Whirlpool?','K02'),('Was bieten die Zimmer?','K03'),('Wie ist das Frühstück?','K04'),('Gibt es einen Parkplatz?','K05'),('Wo liegt die Unterkunft?','K06'),('Wie komme ich vom Flughafen hin?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Organisieren Sie Ausflüge?','K09'),('Was kann man in der Nähe besichtigen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Kann ich mein Gepäck abgeben?','K12'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
