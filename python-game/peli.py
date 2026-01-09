# Sepon seikkailu - tektiseikkailupeli
# Tekijä Ilona Nikulina. 24TIKOOT2
# Yksi tiedosto: peli.py
# Suunnat: pohjoinen, etelä, itä, länsi
# Käännöshaaste: suomekielinen esinenimi -> kirjoita englanniksi (3 yritystä)
# Coin - järjestelmä: jokaisesta oikein käännetystä esineestä +1 coin 
# Tehtävä: avain Kruunuhuoneesta -> avaa Salahuone 

import sys
import textwrap

def wrap(s, width = 80):
    return "\n".join(textwrap.wrap(s, width=width))

def print_rules():
    rules = """

    ============================================
                  SEPON SEIKKAILU
    ============================================

    Olet apina viidakossa. Löydät hylätyn linnan, matkustat sinne 
    viidakon läpi ja matkalla on paljon seikkailua, ennen kun pääsee
    liinnaan ja tutkit sen huoneita.
    Kerää esineitä kääntämällä niiden nimet englanniksi oikein.
    Jokaisesta onnistuneesta käännöksestä saat 1 coin.

    PÄÄTEHTÄVÄT:
1) Etsi avain kirjastosta
2) Avaa salahuone avaimella
3) Löydä kruunu ja sauva
4) Aseta ne salahuoneessa

KOMENNOT:
- mene [suunta]
- katsele / tutki
- ota [esine]
- käytä [esine]
- mukana
- anna vinkki
- avaa salahuone avain
- aseta
- lopeta

MAKSIMI KOLIKOT: 280

    Vinkkejä:
    - Tutki huoneita rauhassa. Jos jokin on lukossa, ehkä avain on jossain.
    - Banaani Miksu ystävällisesti antaa vihjeitä.

    Onnea matkaan, apina!
    ============================================
    """   
    print(rules)


sijainti = "viidakkopolku"
inventaario = []
coins = 0
huoneet = {
    "viidakkopolku": {
          "kuvaus": (
            "Seisot kapealla viidakkopolulla. Korkeat puut kaartuvat yllesi ja "
            "kostea ilma tuntuu turkissasi. Linnut huutavat jossain kauempana ja "
            "lehdet kahisevat tuulessa. Polku jatkuu useaan suuntaan."
        ),
        "käyty": False,
        "reitit": {"itä": "vesiputousranta", "länsi": "kallionaukko", "etelä":"banaanimetsä"},
        "esineet":["reppu"]
    },
    "vesiputousranta": {
        "kuvaus": (
            "Saavut vesiputouksen rannalle. Vesi syöksyy alas kallioilta "
            "voimalla ja viilentää ilman. Aurinko heijastuu pisaroihin ja "
            "muodostaa sateenkaaren."
        ),
        "käyty": False,
        "reitit": {"länsi": "kallionaukko", "etelä":"banaanimetsä", "pohjoinen":"viidakkopolku"},
        "esineet":["vesipullo"]
    },
    "kallionaukko": {
        "kuvaus": (
            "Edessäsi on kallioon hakattu aukko. Se on pimeä ja viileä, "
            "ja sisältä kuuluu kaikuvaa hiljaisuutta. Tunnet, että tämä "
            "paikka kätkee jotain vanhaa."
        ),
        "käyty": False,
        "reitit": {"itä": "vesiputousranta", "etelä":"banaanimetsä", "pohjoinen":"viidakkopolku"},
        "esineet":["kartta"]
    },
    "banaanimetsä": {
        "kuvaus": (
            "Banaanimetsä levittäytyy ympärillesi. Puut ovat täynnä "
            "kypsiä banaaneja ja ilma tuoksuu makealta. Tunnet olosi "
            "iloiseksi."
        ),
        "käyty": False,
        "reitit": {"etelä":"lian siltareitti", "pohjoinen":"vesiputousranta"},
        "esineet":["banaani"]
    },
    "lian siltareitti": {
        "kuvaus": (
            "Kapea lianasilta heiluu jalkojesi alla. Sen alla avautuu "
            "syvä rotko. Jokainen askel vaatii keskittymistä."
        ),
        "käyty": False,
        "reitit": {"etelä":"linnan crupina", "pohjoinen":"banaanimetsä"},
        "esineet":["köynnös"]
    },
    "linnan crupina": {
        "kuvaus": (
            "Seisot linnan raunioituneella sisäpihalla. Kiviseinät ovat osittain sortuneet "
            "ja köynnökset kiipeilevät niiden pinnalla. Maassa lojuu irtokiviä ja vanhoja "
            "rakennusjäänteitä. Hiljaisuus on painostava, kuin paikka tarkkailisi sinua."
),
        "käyty": False,
        "reitit": {"itä": "romahdettu muuri", "etelä":"raurioportaat", "pohjoinen":"lian siltareitti"},
        "esineet":["taskulamppu"]
    },
    "romahdettu muuri": {
        "kuvaus": (
            "Saavut romahdetun muurin luo. Suuret kivipaadet ovat kaatuneet toistensa päälle "
            "ja muodostavat vaikeakulkuisen esteen. Muurin takana häämöttää linnan sisäosia, "
            "ja tunnet viileän ilman virtaavan kivien välistä."
),
        "käyty": False,
        "reitit": {"länsi": "linnan crupina", "etelä":"raurioportaat","pohjoinen":"lian siltareitti"},
        "esineet":["jalokivi"]
    },
    "raurioportaat": {
       "kuvaus": (
            "Saavut linnan raunioille. Kiviseinät ovat sortuneet ja "
            "köynnökset peittävät niitä. Tämä paikka huokuu historiaa."
        ),
        "käyty": False,
        "reitit": {"etelä":"ruosteinen käytävä", "pohjoinen":"linnan crupina"},
        "esineet":["kompassi"]
    },
    "ruosteinen käytävä": {
        "kuvaus": (
            "Käytävä on kapea ja seinät ovat ruosteen peitossa. "
            "Askeleesi kaikuvat metallisesti ja ilma tuntuu raskaalta."
        ),
        "käyty": False,
        "reitit": {"itä": "banaanihalli", "länsi": "pyhäskäytävä", "pohjoinen":"raurioportaat"},
        "esineet":[]
    },
    "banaanihalli": {
       "kuvaus": (
            "Astut suureen halliin, jossa kasvaa villejä banaanipuita. Katto on osittain "
            "romahtanut, ja auringonvalo pääsee sisään. Banaanit roikkuvat raskaasti oksilla "
            "ja ilma tuoksuu makealta ja kypsältä."
),
        "käyty": False,
        "reitit": {"länsi": "ruosteinen käytävä", "etelä":"rumppuhuone"},
        "esineet":["voileipä"]
    },
    "pyhäskäytävä": {
       "kuvaus": (
            "Kävelet pyhässä käytävässä. Seinillä on haalistuneita symboleja ja kaiverruksia, "
            "joiden merkitys on ajan saatossa unohtunut. Paikka tuntuu hiljaiselta ja "
            "kunnioitusta herättävältä."
),
        "käyty": False,
        "reitit": {"itä": "ruosteinen käytävä","etelä":"varasto"},
        "esineet":["suklaa"]
    },
    "rumppuhuone": {
        "kuvaus": (
           "Huoneessa on vanhoja rumpuja ja lyömäsoittimia. Osa niistä on rikki, mutta "
            "toiset näyttävät yhä käyttökelpoisilta. Kuvittelet, kuinka täällä on joskus "
            "soinut rytmikäs musiikki."
),
        "käyty": False,
        "reitit": {"länsi": "ruosteinen käytävä", "etelä":"kirjasto", "pohjoinen":"banaani halli"},
        "esineet":["rummut"]
    },
    "varasto": {
       "kuvaus": (
           "Varasto on täynnä pölyisiä laatikoita ja rikkinäisiä hyllyjä. Täällä on "
           "säilytetty ruokaa ja tarvikkeita linnan loiston aikoina. Nyt paikka on "
           "hylätty, mutta ehkä jotain hyödyllistä on jäänyt jäljelle."
),
        "käyty": False,
        "reitit": {"itä": "ruosteinen käytävä", "etelä":"kruunuhuone", "pohjoinen":"pyhäskäytävä"},
        "esineet":["energiajuoma"]
    },
    "kruunuhuone": {
        "kuvaus": (
            "Astut kruunuhuoneeseen. Keskellä huonetta seisoo valtaistuin, "
            "jonka ympärillä on hajonneita koristeita. Tunnet, että "
            "tämä huone on linnan sydän."
        ),
        "käyty": False,
        "reitit": {"itä": "ruosteinen käytävä", "etelä":"aateliskammio", "pohjoinen":"varasto"},
        "esineet":["kruunu"]
    },
    "kirjasto": {
        "kuvaus": (
           "Saavut vanhaan kirjastoon. Kirjahyllyt ovat kaatuneet ja kirjat lojuvat "
           "lattialla. Osa sivuista on repeytynyt tai homeessa, mutta tunnet että "
           "täällä on säilynyt linnan historia."
),
        "käyty": False,
        "reitit": {"länsi": "ruosteinen käytävä", "etelä":"kookoshuone", "pohjoinen":"rumppuhuone"},
        "esineet":["avain"]
    },
    "aateliskammio": {
        "kuvaus": (
            "Aateliskammio on koristellumpi kuin muut huoneet. Seinillä on rikkinäisiä "
            "koristeita ja lattialla pehmeitä, mutta pölyisiä mattoja. Tämä huone on "
            "selvästi ollut tärkeä linnan asukkaille."
),
        "käyty": False,
        "reitit": {"itä": "ruosteinen käytävä", "etelä":"kasvihuone", "pohjoinen":"kruunuhuone"},
        "esineet":["sauva"]
    },
    "kookoshuone": {
        "kuvaus": (
           "Huone on täynnä kookospähkinöitä ja kuivuneita kasveja. Ilma on hieman tunkkainen, "
           "ja lattialla on murskautuneita kuoria. Tässä huoneessa kaikki huonekalut "
           "tehty kookospähkinöistä ja seinällä on taulu, jossa on maalattu kookospähkinä."
),
        "käyty": False,
        "reitit": {"länsi":"ruosteinen käytävä", "etelä":"teatterihuone", "pohjoinen":"kirjasto"},
        "esineet":["kookospähkinä"]
    },
    "kasvihuone": {
       "kuvaus": (
           "Kasvihuoneessa kasvaa villiintyneitä kasveja ja köynnöksiä. Lasikatto on "
           "haljennut, mutta valo ja lämpö pitävät kasvuston elossa. Paikka tuntuu "
           "yllättävän rauhoittavalta."
),
        "käyty": False,
        "reitit": {"itä": "ruosteinen käytävä", "etelä":"pinkki huone", "pohjoinen":"aateliskammio"},
        "esineet":["ruusu"]
    },
    "teatterihuone": {
        "kuvaus": (
           "Teatterihuoneessa on pieni lava ja rikkinäisiä istuimia. Kuvittelet, kuinka "
           "täällä on joskus esitetty näytelmiä linnan väelle. Nyt huone on hiljainen, "
           "ja vain askeleesi rikkovat rauhan."
),
        "käyty": False,
        "reitit": {"länsi": "ruosteinen käytävä", "etelä":"salahuone", "pohjoinen":"kookoshuone"},
        "esineet":[]
    },
    "pinkki huone": {
        "kuvaus": (
           "Huoneen seinät ovat yhä hennon vaaleanpunaiset, vaikka maali on kulunut. "
           "Huone tuntuu oudolta verrattuna muihin linnan tiloihin, melkein kuin se "
           "kuuluisi toiseen maailmaan."
),
        "käyty": False,
        "reitit": {"itä": "ruosteinen käytävä","etelä":"kellari", "pohjoinen":"kasvihuone"},
        "esineet":["mekko"]
    },
    "salahuone": {
       "kuvaus": (
           "Olet salahuoneessa. Huone on pieni ja hämärä, ja huoneen keskellä on  "
           "valoistettu ständi josta puuttuu kruunu, ja tunnet että tämä paikka on piilotettu "
           "tarkoituksella."
),
        "käyty": False,
        "reitit": {"länsi": "ruosteinen käytävä", "etelä":"takapiha", "pohjoinen":"teatterihuone"},
        "esineet":[]
    },
    "kellari": {
        "kuvaus": (
           "Laskeudut kellariin. Ilma on kylmää ja kosteaa, ja seinät tihkuvat vettä. "
           "Täällä on säilytetty asioita, joita ei haluttu pitää näkyvillä."
),
        "käyty": False,
        "reitit": {"itä": "ruosteinen käytävä", "pohjoinen":"pinkkihuone"},
        "esineet":[]
    },
    "takapiha": {
        "kuvaus": (
            "Saavut linnan takapihalle. Kasvillisuus on vallannut alueen, ja luonto "
            "on ottanut paikan takaisin itselleen. Täältä linnan rauniot näyttävät "
            "vieläkin vaikuttavammilta."
),
        "käyty": False,
        "reitit": {"pohjoinen":"salahuone"},
        "esineet":["mitali"]
    },
}


# Esineet

esineet = {
    "avain": {"englanti": "key", "pisteet": 20},
    "sauva": {"englanti": "staff", "pisteet": 20},
    "kruunu": {"englanti": "crown", "pisteet": 30},
    "energiajuoma": {"englanti": "energy drink", "pisteet": 10},
    "banaani": {"englanti": "banana", "pisteet": 10},
    "kookospähkinä": {"englanti": "coconut", "pisteet": 10},
    "köynnös": {"englanti": "vine", "pisteet": 10},
    "taskulamppu": {"englanti": "flashlight", "pisteet": 10},
    "reppu": {"englanti": "backpack", "pisteet": 10},
    "kartta": {"englanti": "map", "pisteet": 10},
    "jalokivi": {"englanti": "gem", "pisteet": 10},
    "rummut": {"englanti": "drums", "pisteet": 10},
    "vesipullo": {"englanti": "bottle of water", "pisteet": 10},
    "suklaa": {"englanti": "chocolate", "pisteet": 10},
    "kompassi": {"englanti": "compass", "pisteet": 10},
    "voileipä": {"englanti": "sandwich", "pisteet": 10},
    "ruusu": {"englanti": "rose", "pisteet": 10},
    "mekko": {"englanti": "dress", "pisteet": 10},
    "mitali": {"englanti": "medal", "pisteet": 10}
}

# Funktio: Pikku banaani antaa vinkkejä
def huonekuvaus(sijainti):
    if not huoneet[sijainti]["käyty"]:
        print(wrap(huoneet[sijainti]["kuvaus"]))
        huoneet[sijainti]["käyty"] = True

    if huoneet[sijainti]["esineet"]:
        print("\nNäet täällä seuraavat esineet:")
        for esine in huoneet[sijainti]["esineet"]:
            print(f"- {esine}")
        print("\nVoit ottaa esineen komennolla: ota [esine]")
        print("Saat esineen vain, jos käännät sen englanniksi oikein!")
    else:
        print("\nTäällä ei näytä olevan mitään hyödyllistä.")

def pikku_banaani_vinkki():
    print("🍌 Banaani Miksu sanoo: 'Etsi kruunuhuone, siellä on avain!'")

def ota_esine(esine, sijainti, inventaario, coins):
    if esine not in huoneet[sijainti]["esineet"]:
        print("Täällä ei ole sitä esinettä.")
        return coins

    yritykset = 3
    while yritykset > 0:
        vastaus = input("Kirjoita esine englanniksi: ").lower()
        if vastaus == esineet[esine]["englanti"]:
            inventaario.append(esine)
            huoneet[sijainti]["esineet"].remove(esine)
            coins += esineet[esine]["pisteet"]
            print(f"✅ Oikein! +{esineet[esine]['pisteet']} kolikkoa")
            return coins
        else:
            yritykset -= 1
            print("❌ Väärin.")

    print("Et saanut kolikoita.")
    return coins

def käytä_esine(esine, inventaario, energia):
    if esine not in inventaario:
        print(f"Sinulla ei ole {esine} inventaariossa.")
        return energia

    if esine == "energiajuoma":
        energia += 50
        inventaario.remove(esine)
        print(f"💪 Juot energiajuoman! Energia nyt: {energia}/100")
    elif esine == "suklaa":
        energia += 20
        inventaario.remove(esine)
        print(f"🍫 Syöt suklaata! Energia nyt: {energia}/100")
    elif esine == "vesipullo":
        energia += 50
        inventaario.remove(esine)
        print(f"Juot vesipulloa! Energia nyt: {energia}/100")
    elif esine == "voileipä":
        energia += 30
        inventaario.remove(esine)
        print(f"🥪 Syöt voileivän! Energia nyt: {energia}/100")
    elif esine == "banaani":
        energia += 30
        inventaario.remove(esine)
        print(f"Syöt banaanin! Energia nyt: {energia}/100")
    elif esine == "kookospähkinä":
        energia += 30
        inventaario.remove(esine)
        print(f"Syöt kookospähkinän! Energia nyt: {energia}/100")
    else:
        print(f"Et voi käyttää {esine} tässä.")

    if energia > 100:
        energia = 100

    return energia



# -------------------------
# PELI
# -------------------------

def peli():
    print_rules()
    nimi = input("Anna hahmollesi nimi: ")
    print(f"Tervetuloa seikkailuun, {nimi}!\n")

    sijainti = "viidakkopolku"
    inventaario = []
    coins = 0
    energia = 100
    salahuone_avattu = False

    huonekuvaus(sijainti)

    while True:
        komento = input("> ").lower().split()

        if not komento:
            continue

        if komento[0] == "lopeta":
            print("Kiitos pelaamisesta!")
            sys.exit()

        elif komento[0] in ["katsele", "tutki"]:
            huonekuvaus(sijainti)

        elif komento[0] == "mene" and len(komento) > 1:
            suunta = komento[1]

            # Tarkistetaan onko suunta mahdollinen
            if suunta in huoneet[sijainti]["reitit"]:
                seuraava_huone = huoneet[sijainti]["reitit"][suunta]

                # Erityistapaus: salahuone
                if seuraava_huone == "salahuone" and "avain" not in inventaario:
                    print("🚪 Salahuone on lukossa. Tarvitset avaimen päästäksesi sinne.")
                else:
                    sijainti = seuraava_huone
                    print(f"Siirryit huoneeseen: {sijainti}")

                    # Energia vähenee tietyissä huoneissa
                    if sijainti in ["kirjasto", "kookoshuone", "banaanimetsä", "teatterihuone"]:
                        energia -= 30
                        if energia <= 0:
                            energia = 0
                            print("💤 Olet liian väsynyt jatkaaksesi. Tarvitset energiajuoman!")

                    huonekuvaus(sijainti)
                    print(f"🔋 Energia: {energia}/100")
            else:
                print("Et voi mennä siihen suuntaan.")

        elif komento[0] == "käytä" and len(komento) > 1:
                esine = komento[1]
                energia = käytä_esine(esine, inventaario, energia)

        elif komento[0] == "ota" and len(komento) > 1:
            coins = ota_esine(komento[1], sijainti, inventaario, coins)

        elif komento[0] == "avaa":
            if "avain" in inventaario:
                salahuone_avattu = True
                coins += 30
                print("🔓 Salahhuone avattu! +30 kolikkoa")
            else:
                print("Sinulla ei ole avainta.")
        elif komento[0] == "aseta":
            if sijainti == "salahuone" and "kruunu" in inventaario and "sauva" in inventaario:
                coins += 50
                print("🏆 VOITIT PELIN!")
                print(f"Lopulliset kolikot: {coins} / 150")
                sys.exit()
            else:
                print("Et voi asettaa vielä.")


        elif komento[0] == "mukana":
            print("Inventaario:", inventaario)
            print(f"Kolikot: {coins} / 280")
            print(f"energia: {energia} / 100")


        elif komento[0] == "anna" and len(komento) > 1 and komento[1] == "vinkki":
            pikku_banaani_vinkki()

        elif komento[0] == "apua":
            print("Komennot: mene, katsele, ota, mukana, juo, syö, anna vinkki, lopeta")

        else:
            print("Tuntematon komento.")

# Käynnistetään peli
if __name__ == "__main__":
    peli()
