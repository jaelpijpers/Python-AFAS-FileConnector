
# Python-AFAS-FileConnector
Functies  voor het gebruik van de AFAS FileConnector.

### Gebruik
Hier onderstaand een voorbeeld van het gebruik van de code.

```python
import os
import AfasFileConnector

## configuration ##
token = "<token><version>1</version><data>TOKEN_HIER_INVOEGEN</data></token>"
omgeving = "25275"
getconnector_naam = "Bestanden_bij_dossier"
guid_kolomveld          = 'Bijlage'
bestandsnaam_kolomveld  = 'Bestand'
save_path               = os.path.join(os.getcwd(),'output') 
# save_path variabel pakt de directory van het script, en voegt de folder 'output' toe aan dit path
###################

download_files(token, omgeving, getconnector_naam, guid_kolomveld, bestandsnaam_kolomveld, 0, 50, save_path)
```


### To Do
- UpdateConnector functionaliteiten toevoegen

### Functionaliteiten
Bekijk alle functionaliteiten [hier](https://github.com/jaelpijpers/Python-AFAS-FileConnector/blob/main/FUNCTIONALITEITEN.md).


