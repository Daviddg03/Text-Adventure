
zähler=0

zähler_01=0 

Raumschiff_Leben=100

Tank_Reserven=0

Team_Motivation=10


while True:

	if zähler>0:
		print("SPIEL ENDE")
		break	
	print("ANWEISUNGEN: \nSie müssen die antworten genau so eintippen wie sie im Titel geschrieben sind\nDas Ziel ist es die meisten punkte in den vorhanden kategorien zu bekommen \nViel Spaß!")
	print("----------------------------------------------------NEUES SPIEL----------------------------------------------------")
	print("----------------------------------------------------DIE MISSION-----------------------------------------------------")
	print("----------------------------------------------KAPITEL 1: PRÄSENTATION----------------------------------------------")

	print("Bitte geben Sie ihren Namen ein:")


	Player=input("")

	print("Es ist das Jahr 2122, Sie sind Kapitän der “Novus Domum” auf einer Mission nach Alpha Centauri, \nvier Lichtjahre von der Erde entfernt. Es ist erst das zweite mal dass die menschheit zu ihrem \nnächstgelegenen Stern aufbricht. In der ersten mission wurde eine atmosphäre bestätigt die mikrobielles \nleben enthält. Jetzt wurden Sie und ihre Crew auf die Reise geschickt um dieses Leben zu Studieren. \nIhre aufgabe ist es die richtigen entscheidungen zu treffen während der 8 Jährigen reise.") 
	

	print("-------------------------------------------KAPITEL 2: MOND ODER JUPITER--------------------------------------------")

	print((Player), "die erste entscheidung ist ob sie beim Mond Ihren fusions reaktor mit Deuterium auftanken wollen oder im Jupiter.")
	r=input("")
	
	
	
	while True:
		if zähler>0:
			break
		if r == ("Mond"):
			print("")
			print("Wir sollten lieber auf dem", r ,"auftanken, sagst du\n")
			Tank_Reserven+=100
			Raumschiff_Leben-=0

			print("Dank der internationalen Mondbasis konnte euer Team ganz in ruhe und ohne probleme die Tanks auffüllen.")
			print("Das Raumschif leben ist auf", Raumschiff_Leben, "{%} und deine Tanks sind", Tank_Reserven, "{%} voll \n")

			print("Willst du was interesantes erfahren?")
			
			Antwort=input("Ja / Nein: ")

			while True:
				if zähler_01>0:
					break

				if Antwort=="Ja":
					print("Die Fusions reaktoren sind die grosse hoffnung des Klimaschutzes sie kontaminieren kaum\nund brauchen sehr wenig ressourcen um viel energie zu produzieren, das problem ist\ndas noch niemand einen funktionalen reaktor dieser klasse gebaut hat und dass der treibstoff den\ner braucht nicht so viel auf der Erde vorhanden ist. Dafür glauben aber wissenschaftler dass es auf der Mondoberfläche\nsehr großen vorkommen gibt. Außerdem könnte man diesen reaktor auf zukünftige weltraummissionen verwenden.\n")
					Z=input("Drücken Sie eine beliebige Taste und drücken Sie die Eingabetaste: ")
					zähler_01+=1
				
				elif Antwort=="Nein":
					print("OK")
					zähler_01+=1
				
				else:
					print("Option nicht verfügbar")
					Antwort=input("Versuchen Sie es nochmal:  \n")

			print("")



			print("")
			print("-------------------------------------KAPITEL 3: ZEIT DEIN TEAM ZU MOTIVIEREN--------------------------------------------\n")
			print("Nach dem Tanken stellt ihr den “gravitations ring” an, dieser ring ist im durchmesser\n76 meter breit und dreht sich mit drei umdrehungen pro minute. Damit erzeugt es genügend\nzentrifugalkraft um die hälfte der Erdschwerkraft simulieren zu können. Du setzt dich\nso in dein Stuhl und fängst an...")
			print("A) Eine Motivationsrede an dein Team zu schreiben. \nB) Das Raumschiff zu Checken. ")
			r2=input("A / B: ")
			while True:

				if zähler>0:
					break
				
				if r2=="A":
					Team_Motivation+=3
					Raumschiff_Leben-=2
					print("Du gibst eine sehr motivierende rede vor der großen beschleunigung aber dein Team hat ein leck im Raumschiff nicht bemerckt.\n")
					print("Deine Team motivation steigt um", Team_Motivation, "aber dein Raumschiffs Leben sinckt", Raumschiff_Leben )
					break
						
				elif r2 =="B":
					print("Du checkst das Raumschiff und entdeckst paar fehler aber deine Crew ist sehr Nervös")
					print("Dein Raumschiffs Leben steigt", Raumschiff_Leben, "aber die Team motivation sinckt", Team_Motivation)
					break
					
				else:
					print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
					r2=input("")
				
			Z=input("Drücken Sie die Eingabetaste: \n")
			print("-------------------------------------KAPITEL 4: ABREISE NACH APLPHA CENTAURI--------------------------------------------\n")
			print("Euer Schiff fängt an zu beschleunigen, immer schneller und schneller nach kurzer Zeit spürt\nman es kaum noch und wenn man aus dem fenster schaut sieht man nur Schwärze und ein paar Sterne. Wenn man es nicht besser wüsste könnte\nman glauben das man still steht . Deine funktion als Kapitän ist es in dieser \nschweren Zeit die Crew motiviert zu halten alle wichtigen entscheidungen \nzu treffen und mit hilfe deiner kameraden das Raumschiff flott zu halten. Nach zwei jahren passiert nochts besonderes")
			Z=input("Drücken Sie die Eingabetaste:")
			print("-------------------------------------KAPITEL 5: INNERE KONFLICKTE--------------------------------------------\n")

			print("Nach zwei Jahren im All und immer wieder die gleichen Menschen zu\nsehen wird die Luft zwischen den Crew mitgliedern immer dünner. Am 13 Tag des \n5 monats des 2 Jahres rastet die Biologin Emma Smith aus. Sie fängt \nan sachen um sich zu schmeißen und ihre kollegen zu attackieren. Was tust du?")
			print("A) Du versuchst auf sie ein zu reden und sie beruhigen. \nB) Du gibst ihr ein Depressor in form einer Spritze gegen ihren willen damit sie die anderen nicht verletzt und nochts kaput macht")

				
			r3=input("A / B: ")
			while True:
				
				if zähler>1:
					break				
				if r3 == "A":
					Team_Motivation+=4
					Raumschiff_Leben-=20
					print("Sie beruhigt sich und fängt an medikamente zu nehmen aber\ndas Schiff hat schaden zu genommen. Deine Crew sieht das man dir vertrauen \nkann aber das Schiff wurde ziemlich beschädigt.")
					print("Die Team motivation liegt bei", Team_Motivation, "und das Raumschiffs leben bei ", Raumschiff_Leben, "%")
					break
						

				elif r3=="B":
					Team_Motivation-=1
					Raumschiff_Leben+=0
					print("Sie schläft ein. Manche teammitglieder finden gut was du getan hast\n aber die meisten denken das du vorher lieber hättest versuchen sollen \nmit ihr zu reden.")
					print("Die Team motivation liegt bei", Team_Motivation, "und das Raumschiffs leben bei ", Raumschiff_Leben, "%")
					break
				else: 
					print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
					r3=input("")
			Z=input("Drücken Sie eine beliebige Taste und drücken Sie die Eingabetaste: \n")
			print("-------------------------------------KAPITEL 6: DIE ANKUNFT--------------------------------------------\n")
			print("Ihr steht kurz vor der ankunft, der pilot schaltet die brems düsen an damit das Schiff die geschwindigkeit\nreduzieren kann um in eine Stabile Umlaufbahn um den Planeten zu bekommen. Nach paar Tagen \nsteht das Schiff im perfekten orbit. Die Wissenschafts crew verlässt das Schiff in einem \nlander um den Planeten zu inspizieren… Paar Stunden danach meldet es sich und benachrichtigt \nüber ein Problem. Und zwar hat sich ein motor überhitzt und ist kaput gegangen. Du schickst \nein rettungsteam runter aber die sind abgestürzt. Du hast nur noch ein Schiff übrig \nund du weißt das wenn noch jemand da unten stecken bleibt ihr nicht genug personal für den \nrückflug habt. Außerdem weißt du dass die wahrscheinlichkeit das es wieder \npassiert zu 80" "%" "sind. Was tust du?")
			print("Ich lasse meine Crew zurück / Ich versuche meine Crew zu retten")
			r4=input("")
			while True:
		
				if r4=="Ich lasse meine Crew zurück":
					Team_Motivation-=10
					print("Die hälfte deiner Crew stirbt, und der rest fliegt zurück. \nAlle sind aber so traurig und unmotiviert das als es zu einer kollision mit einem \nkleinen Asteroiden gab sie nicht schnell genug reagieren konnten. \nDie mission scheitert und alle sterben.")
					print("Deine punkte sind: Raumschiff Leben", Raumschiff_Leben, "Team Motivation", Team_Motivation, "Tankreserven", Tank_Reserven)
					if zähler==0:
						zähler+=1
						print("SPIEL ENDE")
						Z=input("Drücken Sie die Eingabetaste:")

						break
				elif r4=="Ich versuche meine Crew zu retten":
					Team_Motivation+=10
					print("Du startest den letzten versuch, damit nichts schief läuft fliegst du selber. Du schaffst es deine Crew zu retten, alle Feiern dich und ihr fliegt mit den proben wieder zur Erde. Als ihr ankommt wird dir für deine Tapferkeit eine Medaille vergeben und ", Player, "geht in die geschichte als der größte Kapitän aller Zeiten ein.")
					print("Deine punkte sind:", Raumschiff_Leben, Team_Motivation, Tank_Reserven)
					if zähler==0:
						zähler+=1
						print("SPIEL ENDE")
						Z=input("Drücken Sie die Eingabetaste:")
						break
				else:
					print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
					r4=input("")

		elif r == "Jupiter":
				print("")
				print("Wir sollten lieber auf dem", r ,"auftanken, sagst du\n")
				
				Tank_Reserven+=80
				Raumschiff_Leben-=30

				print("Die starke schwerkraft vom Jupiter hat euer Raumschiff ziemlich durchgerüttelt und die Deuterium vorkommen sind nicht so groß gewesen deswegen...")
				print("Ist das Raumschiffs leben auf", Raumschiff_Leben, "%" " gesuncken und deine Tank nur auf", Tank_Reserven, "% voll \n")

				print("Willst du was interesantes erfahren?")
				Antwort=input("Ja / Nein: ")
				while True:

					if zähler_01>0:
						break
					
					if Antwort=="Ja":
						print("Die Fusions reaktoren sind die grosse hoffnung des Klimaschutzes sie kontaminieren kaum\nund brauchen sehr wenig ressourcen um viel energie zu produzieren, das problem ist\ndas noch niemand einen funktionalen reaktor dieser klasse gebaut hat und dass der treibstoff den\ner braucht nicht so viel auf der Erde vorhanden ist. Dafür glauben aber wissenschaftler dass es auf der Mondoberfläche\nsehr großen vorkommen gibt. Außerdem könnte man diesen reaktor auf zukünftige weltraummissionen verwenden.\n")
						Z=input("Drücken Sie die Eingabetaste:")
						zähler_01+=1		
					elif Antwort=="Nein":
						print("OK")
						zähler_01+=1
					else:
						print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
						Antwort=input("\n")


				print("")
				print("-------------------------------------KAPITEL 3: ZEIT DEIN TEAM ZU MOTIVIEREN--------------------------------------------\n")
				print("Nach dem Tanken stellt ihr den “gravitations ring” an, dieser ring ist im durchmesser\n76 meter breit und dreht sich mit drei umdrehungen pro minute. Damit erzeugt es genügend\nzentrifugalkraft um die hälfte der Erdschwerkraft simulieren zu können. Du setzt dich\nso in dein Stuhl und fängst an...")
				print("A) Eine Motivationsrede an dein Team zu schreiben. \nB) Das Raumschiff zu Checken. ")
				r5=input("A / B: ")
				
				while True:
					
					if zähler>0:
						break
					
					if r5=="A":
						Team_Motivation+=3
						Raumschiff_Leben-=2
						print("Du gibst eine sehr motivierende rede vor der großen beschleunigung aber dein Team hat ein leck im Raumschiff nicht bemerckt.\n")
						print("Deine Team motivation steigt um", Team_Motivation, "aber dein Raumschiffs Leben sinckt", Raumschiff_Leben )
						Z=input("Drücken Sie die Eingabetaste:")
						

						while True:
							if zähler>0:
								break
							print("-------------------------------------KAPITEL 4: ABREISE NACH APLPHA CENTAURI--------------------------------------------\n")
							print("Euer Schiff fängt an zu beschleunigen, immer schneller und schneller nach kurzer Zeit spürt\nman es kaum noch und wenn man aus dem fenster schaut sieht man nur Schwärze und ein paar Sterne. Wenn man es nicht besser wüsste könnte\nman glauben das man still steht . Deine funktion als Kapitän ist es in dieser \nschweren Zeit die Crew motiviert zu halten alle wichtigen entscheidungen \nzu treffen und mit hilfe deiner kameraden das Raumschiff flott zu halten. \nNach 4 Monaten gibt es eine störung bei einer Wand des raumschiffes es ertönt ein alarm \nrasch macht sich dein ganzes Team auf den Weg. Der ingenieur des Teams sagt dass es höchstwahrscheinlich an dem Tag \nliegt wo wir beim Jupiter aufgetankt haben, es könnte gefährlich sein. Du sagst:")
							r2=input("A) Ach ist nicht so schlimm / B) Repariert es so schnell wie möglich.")
							if r2=="B":
								print("Das raumschiff wird von dem ingenieur repariert und ihr fliegt weiter\n")
								print("-------------------------------------KAPITEL 5: INNERE KONFLICKTE--------------------------------------------\n")
								print("Nach zwei Jahren im All und immer wieder die gleichen Menschen zu\nsehen wird die Luft zwischen den Crew mitgliedern immer dünner. Am 13 Tag des \n5 monats des 2 Jahres rastet die Biologin Emma Smith aus. Sie fängt \nan sachen um sich zu schmeißen und ihre kollegen zu attackieren. Was tust du?")
								print("A) Du versuchst auf sie ein zu reden und sie beruhigen. \nB) Du gibst ihr ein Depressor in form einer Spritze gegen ihren willen damit sie die anderen nicht verletzt und nochts kaput macht")

								r3=input("A / B: ")

								while True:
									if zähler>0:
										break				
									if r3 == "A":
										Team_Motivation+=4
										Raumschiff_Leben-=20
										print("Sie beruhigt sich und fängt an medikamente zu nehmen aber\ndas Schiff hat schaden zu genommen. Deine Crew sieht das man dir vertrauen \nkann aber das Schiff wurde ziemlich beschädigt.")

										print("Die Team motivation liegt bei", Team_Motivation, "und das Raumschiffs Leben bei ", Raumschiff_Leben, "%")
									elif r3=="B":
										Team_Motivation-=1
										Raumschiff_Leben+=0
										print("Sie schläft ein. Manche teammitglieder finden gut was du getan hast\n aber die meisten denken das du vorher lieber hättest versuchen sollen \nmit ihr zu reden.")
										print("Die Team motivation liegt bei", Team_Motivation, "und das Raumschiffs Leben bei ", Raumschiff_Leben, "%")
									else: 
										print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
										r3=input("")

									print("-------------------------------------KAPITEL 6: DIE ANKUNFT--------------------------------------------\n")
									print("Ihr steht kurz vor der ankunft, der pilot schaltet die brems düsen an damit das Schiff die geschwindigkeit\nreduzieren kann um in eine Stabile Umlaufbahn um den Planeten zu bekommen. Nach paar Tagen \nsteht das Schiff im perfekten orbit. Die Wissenschafts crew verlässt das Schiff in einem \nlander um den Planeten zu inspizieren… Paar Stunden danach meldet es sich und benachrichtigt \nüber ein Problem. Und zwar hat sich ein motor überhitzt und ist kaput gegangen. Du schickst \nein rettungsteam runter aber die sind abgestürzt. Du hast nur noch ein Schiff übrig \nund du weißt das wenn noch jemand da unten stecken bleibt ihr nicht genug personal für den \nrückflug habt. Außerdem weißt du dass die wahrscheinlichkeit das es wieder \npassiert zu 80" "%" "sind. Was tust du?")
									print("Ich lasse  meine Crew zurück / Ich versuche meine Crew zu retten")
									r4=input("")
									if r4=="Ich lasse  meine Crew zurück":
										Team_Motivation-=10
										print("Die hälfte deiner Crew stirbt, und der rest fliegt zurück. \nAlle sind aber so traurig und unmotiviert das als es zu einer kollision mit einem \nkleinen Asteroiden gab sie nicht schnell genug reagieren konnten. \nDie mission scheitert und alle sterben.")
										print("Deine punkte sind: Raumschiff Leben", Raumschiff_Leben, " Team Motivation", Team_Motivation, "Tank reserven ", Tank_Reserven)
										if zähler==0:
											zähler+=1
											Z=input("Drücken Sie die Eingabetaste:")
											break
									elif r4=="Ich versuche meine Crew zu retten":
										Team_Motivation+=10
										print("Du startest den letzten versuch, damit nichts schief läuft fliegst du selber. Du schaffst es deine Crew zu retten, alle Feiern dich und ihr fliegt mit den proben wieder zur Erde. Als ihr ankommt \nwird dir für deine Tapferkeit eine Medaille vergeben und ", Player, "geht in die geschichte als der größte Kapitän aller Zeiten ein.")
										print("Deine punkte sind: Raumschiff Leben", Raumschiff_Leben, " Team Motivation", Team_Motivation, "Tank reserven ", Tank_Reserven)
										if zähler==0:
											zähler+=1
											print()
											Z=input("Drücken Sie die Eingabetaste:")
											break
									else:
										print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
										r4=input("")
							elif r2=="A":
									print("Das raumschiff fliegt auseinander und Ihr alle stirbt")
									zähler=+1
									break
							else:
								print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
								r=input("")

										
					elif r5 =="B":
						Team_Motivation-=1
						Raumschiff_Leben+=20
						print("Du checkst das Raumschiff und entdeckst paar fehler aber deine Crew ist sehr Nervös")
						print("Dein Raumschiffs Leben steigt", Raumschiff_Leben, "aber die Team motivation sinckt", Team_Motivation)
						Z=input("Drücken Sie die Eingabetaste:")


						while True:
							if zähler>0:
								break
							print("-------------------------------------KAPITEL 4: ABREISE NACH APLPHA CENTAURI--------------------------------------------\n")

							print("Euer Schiff fängt an zu beschleunigen, immer schneller und schneller nach kurzer Zeit spürt\nman es kaum noch und wenn man aus dem fenster schaut sieht man nur Schwärze und ein paar Sterne. Wenn man es nicht besser wüsste könnte\nman glauben das man still steht . Deine funktion als Kapitän ist es in dieser \nschweren Zeit die Crew motiviert zu halten alle wichtigen entscheidungen \nzu treffen und mit hilfe deiner kameraden das Raumschiff flott zu halten. \nDank dem gute Raumschiff lebens gibt es in den nächsten Jahren kein großen zwischenfall.")
							Z=input("Drücken Sie die Eingabetaste:")
							print("-------------------------------------KAPITEL 5: INNERE KONFLICKTE--------------------------------------------\n")

							print("Nach zwei Jahren im All und immer wieder die gleichen Menschen zu\nsehen wird die Luft zwischen den Crew mitgliedern immer dünner. Am 13 Tag des \n5 monats des 2 Jahres rastet die Biologin Emma Smith aus. Sie fängt \nan sachen um sich zu schmeißen und ihre kollegen zu attackieren. Was tust du?")
							print("A) Du versuchst auf sie ein zu reden und sie beruhigen. \nB) Du gibst ihr ein Depressor in form einer Spritze gegen ihren willen damit sie die anderen nicht verletzt und nochts kaput macht")

							r3=input("A / B: ")

							while True:
								if zähler>0:
									break				
								if r3 == "A":
									Team_Motivation+=4
									Raumschiff_Leben-=20
									print("Sie beruhigt sich und fängt an medikamente zu nehmen aber\ndas Schiff hat schaden zu genommen. Deine Crew sieht das man dir vertrauen \nkann aber das Schiff wurde ziemlich beschädigt.")

									print("Die Team motivation liegt bei", Team_Motivation, "und das Raumschiffs Leben bei ", Raumschiff_Leben, "%")
								elif r3=="B":
									Team_Motivation-=1
									Raumschiff_Leben+=0
									print("Sie schläft ein. Manche teammitglieder finden gut was du getan hast\n aber die meisten denken das du vorher lieber hättest versuchen sollen \nmit ihr zu reden.")
									print("Die Team motivation liegt bei", Team_Motivation, "und das Raumschiffs Leben bei ", Raumschiff_Leben, "%")
								else: 
									print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
									r3=input("")

								print("-------------------------------------KAPITEL 6: DIE ANKUNFT--------------------------------------------\n")
								print("Ihr steht kurz vor der ankunft, der pilot schaltet die brems düsen an damit das Schiff die geschwindigkeit\nreduzieren kann um in eine Stabile Umlaufbahn um den Planeten zu bekommen. Nach paar Tagen \nsteht das Schiff im perfekten orbit. Die Wissenschafts crew verlässt das Schiff in einem \nlander um den Planeten zu inspizieren… Paar Stunden danach meldet es sich und benachrichtigt \nüber ein Problem. Und zwar hat sich ein motor überhitzt und ist kaput gegangen. Du schickst \nein rettungsteam runter aber die sind abgestürzt. Du hast nur noch ein Schiff übrig \nund du weißt das wenn noch jemand da unten stecken bleibt ihr nicht genug personal für den \nrückflug habt. Außerdem weißt du dass die wahrscheinlichkeit das es wieder \npassiert zu 80" "%" "sind. Was tust du?")
								print("Ich lasse meine Crew zurück / Ich versuche meine Crew zu retten")
								r4=input("")
								if r4=="Ich lasse meine Crew zurück":
									Team_Motivation-=10
									print("Die hälfte deiner Crew stirbt, und der rest fliegt zurück. \nAlle sind aber so traurig und unmotiviert das als es zu einer kollision mit einem \nkleinen Asteroiden gab sie nicht schnell genug reagieren konnten. \nDie mission scheitert und alle sterben.")
									print("Deine punkte sind: Raumschiff Leben", Raumschiff_Leben, " Team Motivation", Team_Motivation, "Tank reserven ", Tank_Reserven)
									if zähler==0:
										zähler+=1
										print("SPIEL ENDE")
										Z=input("Drücken Sie die Eingabetaste:")
										break
								elif r4=="Ich versuche meine Crew zu retten":
									Team_Motivation+=10
									print("Du startest den letzten versuch, damit nichts schief läuft fliegst du selber. Du schaffst es deine Crew zu retten, alle Feiern dich und ihr fliegt mit den proben wieder zur Erde. Als ihr ankommt \nwird dir für deine Tapferkeit eine Medaille vergeben und ", Player, " geht in die geschichte als der größte Kapitän aller Zeiten ein.")
									print("Deine punkte sind: Raumschiff Leben", Raumschiff_Leben, " Team Motivation", Team_Motivation, "Tank reserven ", Tank_Reserven)
									if zähler==0:
										zähler+=1
										print("SPIEL ENDE")
										Z=input("Drücken Sie die Eingabetaste:")
										break
								else:
									print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
						
									r4=input("")
					else:
						print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
						r5=input("")	

		else:
			print("Aktion nicht durchfürbar, wiederhole deine Entscheidung", end=" ")
			r=input("")
