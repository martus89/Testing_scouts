<meta charset="UTF-8">
<h1>Podzadanie 1: konfiguracja oprogramowania.</h1>
<h2>Podzadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?</h2>

<p>Hej, zdecydowałam się na ten kurs, żeby poszerzyć swoje
kompetencje. Jestem na urlopie macierzyńskim, ale bardzo chętnie, zamiast wieczornego
Netflixa, siadam przed komputer i się uczę. IT miałam w planach już bardzo dawno,
ale nigdy nie mogłam nabrać odwagi, żeby odejść z pracy i zacząć się uczyć. Nie pomagał
fakt, że jestem w wieku geriatrycznym na zmiany - mam 34 lata. &#128517

Od pierwszego UAT w pracy wiedziałam, że chcę iść właśnie w tym kierunku. Do tej
pory, robiłam UAT bez żadnej wiedzy w temacie i przygotowania merytorycznego z wyjątkiem
zwykłej znajomości procesów biznesowych i podstaw UX. Odkryłam wtedy, że 
psucie i szukanie błędów wciąga. 

Wielką szansą okazała się dla mnie pandemia, która uziemiła lotnictwo cywilne i dała
mi szansę na dogadanie się z pracodawcą. Chciałam odejść z pracy na ochotnika a 
część odprawy przeznaczyć na bootcamp. Niestety, ciąża pokrzyżowała moje plany, ale
nie poddałam się! Na bootcamp iść nie mogłam, ale zaczełam się uczyć na własną rękę.
Trochę grzebie w Django, stawiam prymitywne apki a dzięki tej 
przygodzie będę mieć doświadczenie i wiedzę. Kto wie, może nawet zdecyduje się
na ISTQB.</p>

<p style="text-align:right"><strong>Marta &#128526</strong></p>

<h2>Subtask 4:</h2>
<p>Mój wynik purpowego testu: <p1 style="color: red">10/14</p1>
<br>

<hr style="height:4px;background-color:red">
<h1>ZADANIE 2: selektory</h1>

<hr style="height:1px;background-color:gray">
<h2>Subtask 2: Wyszukiwanie selektorów na stronie logowania. Wymień wszystkie elementy, które znajdują się na stronie 
logowania.</h2>
<p>
Nasza strona logowania jest bardzo minimalistyczna, co złe nie jest. Nie widzę tam żadnych elementów
typu menu, czy stopki, jedynie formularz.

Elementy formularza:
<ul><b>Pole loginu:</b></ul>
login_field_xpath
<li>//child::div/*[@id="login"]</li>
<li>//*[@id='login']</li>
<li>//input[@id="login"]</li>

<ul><b>Hasło:</b></ul>
password_field_xpath
<li>//input[contains(@id, "password")]</li>
<li>//*[@id="password"]</li>
<li>//child::div/*[@id="password"]</li>

<ul><b>Przypominajka hasła:</b></ul>
password_reminder_xpath
<li>//child::div/a[contains(@class, "MuiTypography-root MuiLink-root")]</li>
<li>//a[contains(@class, "MuiTypography-root MuiLink-root")]</li>
<li>//a[text()="Remind password" or text()="Przypomnij hasło"]</li>

[//]: # (Last one IMHO is discussable due to diacritics [polish letters] present 
in xpath, but no other idea how to chain it creatively anymore)

<ul><b>Język:</b></ul>
language_choice_xpath
<li>//div[contains(@class, "MuiSelect-selectMenu")]</li>
<li>//child::div/*[contains(@class, "MuiSelect-selectMenu")]</li>
<li>//div[@role="button"]</li>

[//]: # ([//]: # So far we have only one role=button, so why not)

<ul><b>Przycisk logowania:</b></ul>
login_button_xpath
<li>//span[@class="MuiTouchRipple-root"]</li>
<li>//child::button/span[2]</li>
<li>//span[text()="Sign in" or text()="Zaloguj"]</li>
