# FiltreGmic
Un script python pour manipuler (CRUD) les filtres dans un fichier Gmic

Appel Gmic
gmic -m fichier.gmic input_image.png  -filtre3 -o output_image.png

**fichier.gmic**
```
filtre3 :
fx_voronoi 120,1,0.5
fx_lightglow 15,0.2

filtre893 :
fx_voronoi 120,1,0.5
fx_lightglow 15,0.2
```
**Exemple basic d'usage**
```
filtres = FiltreGmic("fichier.gmic")
code = """
fx_voronoi 120,1,0.5
fx_lightglow 15,0.2
"""
filtres.add("filtre3", code)
filtres.remove("filtre4")
filtres.isin("filtre4")
print(filtres.liste)
```


