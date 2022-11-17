Robot slouží k vyplnění jednoduchého formuláře pro přidání známky studentovi v 
daném předmětu. Je to pouze první část z projektu VUT FEKT Bezpečnost ICT2 - 
"Návrh a testování nástroje k detekci bota na webové stránce". 

Před spuštěním bota je nutné nainstalovat všechny dependencies, které robot využívá. V příkazové řádce 
se přesuňte se do složky s robotem. Příkazem: <code>pip install -r requirements.txt</code> je všechny
nainstalujete.


Dalším důležitým krokem je vložení cesty k webovému ovladači (ChromeDriver), který robot využívá pro práci v prohlížeci Chrome. 
Stáhněte si tento ovladač na odkazu -  https://chromedriver.chromium.org/ a uložte do složky: <code>C:\webdrivers</code>.

Tuto cestu poté uložte do systémových proměnných systému Windows.

1. Do vyhledávacího okna napiště: "Upravit proměnné prosředí systému",
2. Dále v "Proměnné prostředí",
3. Kde v sekci "Systémové proměnné" přidáte či upravíte proměnnou jménem **Path**,
4. Jako hodnotu proměnné nastavte <code>C:\webdrivers</code> v případě, že jste proměnnou vytvořili,
5. Pokud již vytvořená byla, cestu přidáte pomocí tlačítka "Nový". 

Jako testovací stránka nám poslouží - https://230914.9e.cz/, v případě nedostupnosti stránek či pro jiné účely, můžeme využívat localhost. 
Zdrojový kód včetně databáze naleznete zde: https://github.com/amax45/web_robot.
