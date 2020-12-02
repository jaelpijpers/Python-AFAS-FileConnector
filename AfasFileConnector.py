import requests
import base64
import json
import os

# functie:  zet token inclusief xml om tot base64 encoded string.
# input:    token string inclusief XML-strings. (let op: geen BASE64!)
def token_str_to_base64(token):
    return "AfasToken " + str(base64.b64encode(bytes(token, 'utf-8')))[2:][:-1]

# functie:  genereert het correcte endpoint om de metainfo (json) te verkrijgen d.m.v. de meegeleverde variabelen. (alleen genereren! geen aanroep!)
# input:    voorbeeld: getRESTConnMetainfoEndpoint(33608, "Bestanden_uit_dossieritem", 0, 10) 
def getRESTConnMetainfoEndpoint(omgeving, getconnector_naam, skip, take):
    return "https://{}.rest.afas.online/ProfitRestServices/connectors/{}?skip={}&take={}".format(str(omgeving), getconnector_naam, str(skip), str(take))


# functie:  (url)encode de meegeleverde string volgens w3school standaard (https://www.w3schools.com/tags/ref_urlencode.ASP) 
#           inclusief uitzonderingen volgens AFAS standaard. (https://help.afas.nl/help/NL/SE/App_Cnr_Rest_FileCn.htm#o87737)
def urlencode(text):
        return requests.utils.quote(str(text).strip()).replace("_", "_5f").replace("%", "_").replace("_20", "%20") 


# functie:   doet een request naar de metainfo door middel van de bovenstaande functies. 
# LET OP:   Als het argument "write_to_file" True is, schrijft deze functie de output als metainfo.json in de directory waar het script draait!
# input:     voorbeeld: getRESTConnMetainfo('<token><version>1</version><data>TOKEN_PLACEHOLDER</data></token>', 33608, "Bestanden_uit_dossieritem", 0, 10, False)
def getRESTConnMetainfo(token, omgeving, getconnector_naam, skip, take, write_to_file):
    token_base64 = token_str_to_base64(token)
    endpoint_metainfo = getRESTConnMetainfoEndpoint(omgeving, getconnector_naam, skip, take)

    response = requests.get(
        endpoint_metainfo,
        headers={'Authorization': token_base64},
    )
    response.raise_for_status()

    data = response.json()
    if write_to_file == True:
        with open('metainfo.json', 'w') as fp:
            json.dump(data, fp)
    return data



# functie:  hiermee wordt 1 bestand gedownload naar de aangewezen folder door middel van de meegeleverde argumenten.
#           het idee hierachter is dat deze functie iedere keer aangeroepen wordt door de functie download_files()
# input:    download_file('<token><version>1</version><data>TOKEN_PLACEHOLDER</data></token>', 33608,'60C5AAGE45C82E5FCA121DB4D49F7FAE', 'Image (1).jpeg', '/home/gebruiker/Documents/git/Python-AFAS-FileConnector/afas_output')
def download_file(token, omgeving, guid, filename, save_path):
    token_base64 = token_str_to_base64(token)
    filename_urlencoded = urlencode(filename)
    endpoint = "https://{}.rest.afas.online/profitrestservices/fileconnector/{}/{}".format(str(omgeving), guid, filename_urlencoded)
    print("Filename (URLENCODED): {}".format(filename_urlencoded))
    print("Endpoint: {}".format(endpoint))

    with requests.get(endpoint, timeout=(300,300), headers={'Authorization': token_base64}, stream=True) as r:
        r.raise_for_status()
        r = r.json()
            
        # converteert base64 encoded filedata naar .. normale data? meer info: https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
        file_base64 = r['filedata']
        file_base64_bytes = file_base64.encode('utf-8')
        file_decoded_data = base64.decodebytes(file_base64_bytes)

        with open(os.path.join(save_path, filename), 'wb') as f:
            f.write(file_decoded_data)


    return filename


# functie:  pakt de metainfo (inclusief skip en take) van de connector en maakt een loop voor het aantal rows in de metainfo.
#           uit iedere row pakt het de GUID en de bestandsnaam, vervolgens genereert het een endpoint en doet het een GET request.

# debugging:    wanneer een bestand niet correct wordt opgehaald, wordt dit in de console weergeven (e.g. status 404 of 500)
#               hier moet per omgeving correct gekeken worden naar guid = row['bijlage'] et cetera, er is een goede kans dat deze veldnamen niet overeenkomen, je kan de veldnamen die voor jou van toepassing zijn terugvinden in de metainfo.json of connect.afas.nl

# input:        download_files('<token><version>1</version><data>TOKEN_PLACEHOLDER</data></token>', 33608,'Bestanden_bij_dossier', 0, 10, '/home/gebruiker/Documents/git/AFASPython/afas_output')
def download_files(token, omgeving, getconnector_naam, guid_kolomveld, bestandsnaam_kolomveld, skip, take, save_path):
    endpoint_metainfo = getRESTConnMetainfo(token, omgeving, getconnector_naam, skip, take, True) # only use True here for debugging metainfo

    for row in endpoint_metainfo['rows']:
        # verschilt per omgeving!
        guid = row[str(guid_kolomveld)]
        filename = row[str(bestandsnaam_kolomveld)]

        print("GUID: {}".format(guid))
        print("Bestandsnaam: {}".format(filename))
        download_file(token, omgeving, guid, filename, save_path)
