### Functionaliteiten

```python
> token_str_to_base64(token)
```
**functie**<br/>
zet token inclusief xml om tot base64 encoded string.

**input**<br/>
token string inclusief XML-strings. (let op: geen BASE64!)
<br/><br/>
```python
> getRESTConnMetainfoEndpoint(omgeving, getconnector_naam, skip, take)
```
**functie**<br/>
genereert het correcte endpoint (URL) om de metainfo (json) te verkrijgen d.m.v. de meegeleverde variabelen. (alleen URL genereren! geen aanroep!)

**input**<br/>
getRESTConnMetainfoEndpoint(33608, "Bestanden_uit_dossieritem", 0, 10) 
<br/><br/>
```python
> token_str_to_base64(token)
```
**functie**<br/>
zet token inclusief xml om tot base64 encoded string.

**input**<br/>
token string inclusief XML-strings. (let op: geen BASE64!)
<br/><br/>

```python
> getRESTConnMetainfo(token, omgeving, getconnector_naam, skip, take, write_to_file)
```
**functie**<br/>
doet een request naar de metainfo door middel van de bovenstaande functies. 
**LET OP**:   Als het argument "write_to_file" True is, schrijft deze functie de output als metainfo.json in de directory waar het script draait!

**input**<br/>
getRESTConnMetainfo('TOKEN_PLACEHOLDER', 33608, "Bestanden_uit_dossieritem", 0, 10, False)
<br/><br/>

```python
> download_file(token, omgeving, guid, filename, save_path)
```
**functie**<br/>
hiermee wordt 1 bestand gedownload naar de aangewezen folder door middel van de meegeleverde argumenten.
**het idee hierachter is dat deze functie iedere keer aangeroepen wordt door de functie download_files()**

**input**<br/>
download_file('TOKEN_PLACEHOLDER', 33608,'60C5AAGE45C82E5FCA121DB4D49F7FAE', 'Image (1).jpeg', '/home/gebruiker/Documents/git/Python-AFAS-FileConnector/afas_output')
<br/><br/>

```python
> urlencode(text)
```
**functie**<br/>
(url)encode de meegeleverde string volgens w3school standaard (https://www.w3schools.com/tags/ref_urlencode.ASP) 
inclusief uitzonderingen volgens AFAS standaard. (https://help.afas.nl/help/NL/SE/App_Cnr_Rest_FileCn.htm#o87737)

**input**<br/>
token string inclusief XML-strings. (let op: geen BASE64!)
<br/><br/>
```python
> download_files(token, omgeving, getconnector_naam, guid_kolomveld, bestandsnaam_kolomveld, skip, take, save_path)
```
**functie**<br/>
pakt de metainfo (inclusief skip en take) van de connector en maakt een loop voor het aantal rows in de metainfo.
uit iedere row pakt het de GUID en de bestandsnaam, vervolgens genereert het een endpoint en doet het een GET request.

**Let op**:wanneer een bestand niet correct wordt opgehaald, wordt dit in de console weergeven (e.g. status 404 of 500)

**Let op**:hier moet per omgeving correct gekeken worden naar guid = row['bijlage'] et cetera, er is een goede kans dat deze veldnamen niet overeenkomen, je kan de veldnamen die voor jou van toepassing zijn terugvinden in de metainfo.json of connect.afas.nl

**input**<br/>
download_files('TOKEN_PLACEHOLDER', 33608,'Bestanden_bij_dossier', 'Bijlage', 'Naam', 0, 10, '/home/gebruiker/Documents/git/AFASPython/afas_output')
<br/><br/>
