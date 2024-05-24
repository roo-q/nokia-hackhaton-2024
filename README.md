# Nokia Hackathon (early 2024)

**Általános információk:**

Minden feladatnak megvan a saját „munkaterülete” (workspace), saját feladatmappája. Kérjük, maradjatok ezekben a mappákban, amikor a megoldásokon dolgoztok. Ha valamilyen dependency-re szükségetek van, írjátok a _requirements.txt_ fájlba, és az automatikusan telepítve lesz, ha nem üres.
A pontokat először az alapján adjuk, hogy a feladatok helyesen és teljesen vannak-e megoldva. Ezután a megvalósítást, a funkcionalitást, a kód szépségét és olvashatóságát is figyelembe vesszük. Több fájlban is dolgozhattok, és használhattok absztrakciót is. A pontozásnál a harmadik és a negyedik feladat nehezebb, ezért ezek dupla pontot érnek.

Mappastruktúra:

- _input.txt_
- _main.py_, amely az automatizált tesztfuttató fő belépési pontja. Kérjük, ne távolítsátok el ezt a fájlt, és ne legyenek benne kötelező paraméterek. Kérjük, minden feladat megoldását printeljétek ki a console-ra.

**Figyelem:**

- A megoldások futási ideje nem haladhatja meg az 5 másodpercet. Ha egy kód ennél tovább fut, automatikusan leállítjuk.
- Figyeljetek arra, hogy ne módosítsátok a .github mappát.
- Ne nevezzétek át és ne töröljétek a main.py fájlt.
- A leaderboard nem a végleges állást mutatja, csak a szórakoztatás céljából van ott. Minden eredményt egyénileg végig náünk és pontozunk a fentiekben meghatározottak alapján.

## 1. Palindróma-e

**Feladatmappa:**

palindrome_checker

**Leírás:**

A feladatotok egy olyan program fejlesztése, amely ellenőrzi, hogy egy adott karakterlánc palindróma-e, miközben csak az alfanumerikus karaktereket [a-zA-Z0-9] veszi figyelembe, és figyelmen kívül hagyja a nagy- és kisbetűk közötti különbségeket. Emellett a programnak meg kell számolnia az egyedi karakterek számát a karakterláncban.

**Bemenet:**

A bemenet egy karakterláncokból álló lista, amely betűket, számjegyeket, írásjeleket, szimbólumokat és szóközöket tartalmazhat. A karakterlánc nagy- és kisbetűk kombinációja lehet.

**Kimenet:**

A programnak a következőket kell biztosítania:

1. Hogy a bemeneti karakterlánc palindróma-e.
2. Az egyedi alfanumerikus karakterek számát a karakterláncban.

**Példa:**

_input.txt_

```
racecar
hello
1232112321
worldmadamhelloworld
1234567890
!racecar
CivIC
```

_console printout:_

```
YES, 4
NO, -1
YES, 3
NO, -1
NO, -1
YES, 4
YES, 3
```

## 2. Útvesztő

**Feladatmappa:**

maze_solver

**Leírás:**

A feladatotok egy olyan program fejlesztése, amely képes egy 2D útvesztő rácson keresztül navigálni, egy kijelölt ponttól elindulva elérni a célt, miközben elkerüli az akadályokat. Az útvesztő rács folyosókból, falakból, egy startól és a célból áll. A programnak meg kell találnia a legrövidebb és leggyorsabb utat a startól a célig.

**Bemenet:**

A bemenet egy 2D rács, amely az útvesztőt ábrázolja. Karaktereket tartalmaz az útvesztő elemeinek jelölésére.

- 'S' a start jelölésére
- 'G' a cél jelölésére
- '.' a nyitott útvonalak jelölésére
- '#' a falak vagy akadályok jelölésére

**Kimenet:**

A programnak meg kell adnia az utat a startól a célig. Ezt az utat a mozgás irányaival kell ábrázolni, mint például: 'U' felfelé, 'D' lefelé, 'L' balra, 'R' jobbra, és tartalmaznia kell a startot 'S' és a célt 'G'.

**Példa:**

_input.txt_

```
A
# # # # # # #
# S . . . . #
# # . # # . #
# . . # . . #
# . . . # # #
# . # G . . #
# # # # # # #

B
*****
```

A programnak meg kell mutatnia az utat a starttól a célig. Ezt az utat a mozgás irányaival kell jelölni, például: 'U' felfelé, 'D' lefelé, 'L' balra, 'R' jobbra, és tartalmaznia kell a startot 'S' és a célt 'G'.

_console printout:_

```
A
S R D D D R D G

B
*****
```

A program a mozgások sorrendjét adja meg: jobbra (R), lefelé (D), balra (L) és felfelé (U).

**Megjegyzés:**

Győződjetek meg arról, hogy a program helyesen navigál az útvesztőben, elkerülve az akadályokat, és megtalálva az utat a célhoz.

## 3. Mátrix Műveletek

**Feladatmappa:**

matrix_operations

**Leírás:**

A feladatotok egy olyan program fejlesztése, amely különböző méretű mátrixokon képes műveleteket végrehajtani. Ezek a műveletek magukban foglalják a mátrixok összeadását és szorzását. A programnak elég rugalmasnak kell lennie ahhoz, hogy különböző méretű mátrixokkal is dolgozni tudjon.

**Bemenet:**

A bemenet egy mátrixokat tartalmazó lista értékekkel és a műveletek listája.

**Kimenet:**

A programnak a megadott mátrix műveleteket kell megoldanija.

**Példa:**

_input.txt_

```
matrices

A
2 1
3 4

B
1 0
5 6

operations

A + B
A * B
```

_console printout:_

```
A + B
3 1
8 10

A * B
7 6
23 24
```

**Megjegyzés:**

Győződjön meg arról, hogy a program helyesen kezeli a különböző méretű mátrixokat, és pontosan végzi a műveleteket.

## 4. Matematika kvíz

**Feladatmappa:**

math_quiz

**Leírás:**

9 alfeladat van, amelyet meg kell oldanotok, ezek az alfeladatok egymástól függetlenek.
Található egy _thinking.txt_ a feladat mappájában, kérünk titeket hogy amennyire tudjátok vezessétek le a megoldásotokat ott.

1. Egy vonat állandó sebességgel halad át egy alagúton. 20 másodpercig tart, amíg a 300 m hosszú alagúton átér, onnantól, hogy az eleje eléri az alagút elejét, addig, amíg a vége el nem hagyja. Egy lámpa az alagútban pont 5 másodpercen át van a vonat felett. Milyen hosszú a vonat (méterben)?

2. Egy cukrász két 2 cm, egy 6 cm és egy 8 cm oldalélű marcipánkocka összeragasztásával egy nagyobb testet épített úgy, hogy egy-egy illesztésnél az egyik marcipánkocka teljes oldala ráfeküdt a másik kocka egy lapjára. A kész testből kivághatunk magunknak egy téglatestet, de csak olyan sík mentén vághatunk, amely illeszkedik valamelyik kocka lapjára. Mekkora a legnagyobb térfogatú marcipántégla, amit így kaphatunk (köbcentiméterben)?

3. Jancsi és Juliska a tőlük 20 km-re levő mézeskalácsházhoz igyekszik. Kettejüknek van egy biciklijük, amin egyszerre csak egyikük tud ülni. Elhatározták, hogy először Jancsi fog gyalogolni, és Juliska biciklizik valameddig, ott leteszi a biciklit, majd gyalog megy tovább. Amikor Jancsi odaér, felszáll a biciklire, és elmegy vele a mézeskalácsházig. Jancsi 5 km/h sebességgel gyalogol és 12 km/h sebességgel biciklizik, Juliska 4 km/h sebességgel gyalogol, és 10 km/h sebességgel biciklizik. Hány km-t kell Juliskának bicikliznie, hogy egyszerre érjenek a mézeskalácsházhoz, ha egyszerre is indulnak el?

4. Egy koordinátarendszerben megrajzoltuk az origó középpontú, 5 egység sugarú kört. Hány rácspont esik erre a körvonalra? (Rácspontnak nevezzük azokat a pontokat, melyeknek mindkét koordinátája egész szám.)

5. A koordináta-rendszerben az ABC háromszög csúcspontjai: A(0;4), B(3;0), C(c;6). A háromszög területe 7. Mekkora a c, ha tudjuk, hogy 0<c<3 ?

6. Néhányan paintball-ütközetet vívnak egymással. Egy adott helyzetben egymástól való távolságaik mind különbözők. Ekkor mindenki rálő a hozzá legközelebb álló emberre. Legfeljebb hányan lőhetnek ugyanarra az emberre?

7. Egy dobozban 30 egyforma nagyságú golyó van: pirosak, kékek és zöldek, mindegyikből különböző mennyiségű, zöldből van a legtöbb. Becsukott szemmel legalább 23 golyót kell kivennünk ahhoz, hogy biztosan legyen mindhárom színű golyó a kihúzottak között; illetve legalább 21 golyót, hogy biztosan legyen piros golyónk. Hány piros golyó van?

8. 1 cm oldalú kis négyzetekből összeraktunk egy nagyobbat. A nagy négyzet átlóiban álló kis négyzetek területének összege 85 négyzetcentiméter. Mekkora a nagy négyzet területe négyzetcentiméterben megadva?

9. Egy angol-magyar találkozó végén minden résztvevő elköszönt mindegyik másik résztvevőtől: az angolok mindenkinek egyesével ezt mondták: ,,Goodbye!'', míg a magyarok ezt: ,,Viszlát!'' Hányan angol vett részt a találkozón, ha 198-szor hangzott el az, hogy ,,Goodbye!'' és 308-szor az, hogy ,,Viszlát!''?

**Bemenet Formátum:**

Nincs bemenet ehhez a feladathoz, csak a leírás.

**Kimenet:**

**Példa:**

```
1.: 450
2.: 1943
...
8.: 123
9.: 1.5
```
