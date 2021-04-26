"""
Source fuer den "glob" teil:
https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/
"""
import glob
import xml.etree.ElementTree as ET  # Modul um xml auszulesen
import file_paths as mod_paths  # file_paths enthaelt alle absoluten pfade zu den benoetigten files
import shutil  # Modul zum dateien kopieren usw.

modFiles = [f for f in glob.glob(mod_paths.modOrdnerPath + "**/*.zip", recursive=True)]  # Mithilfe von glob alle
#                                                                                          Dateien parsen
modNames = []  # Leere Liste fuer die ModNamen ohne pfad und dateiendung

for e in modFiles:
    modNames.append(e.split('\\')[7][:-4])  # Die ModFiles liste splitten und die Strings so slicen das nur der
#                                              modname ueber bleibt

# Hier werden die Aktiven Mods bestimmt
saveGame = ET.parse(mod_paths.saveGamePath)  # XML des Savegames parsen
root = saveGame.getroot()  # Die "wurzel" abspeichern
activeMods = []  # Leere Liste fuer die aktiven mods generieren

for mod in root.iter('mod'):  # Mit einer Schleife ueber die Elemente der XML gehen die "mod" im tag haben
    activeMods.append(mod.get('modName'))  # den Modnamen in die Liste einfuegen

# Test ob ein Element in einer anderen Liste ist
for mod in modNames:
    if mod in activeMods:
        print("Die Mod: " + mod + " gehoert in den Spielstand/Modordner.")
    else:
        print("Die Mod: " + mod + " gehoert NICHT in den Spielstand/Modordner.")
        shutil.move(mod_paths.modOrdnerPath + mod + ".zip", mod_paths.modBackup)  # Datei in anderes verzeichnis
#                                                                                   verschieben

# for mod in modFiles:
#    if any([y in mod for y in activeMods]):
#        print("Die Mod: " + mod + " ist aktiv.")
#    else:
#        print("Die Mod: " + mod + " ist NICHT aktiv.")
#        shutil.move(mod, mod_paths.modBackup)

# Stats
# Die Stats sind nicht 100% akkurat weil die "modNames" liste nicht aktuallisiert wird nachdem evt dateien verschoben
# wurden.
print("")
print("Mods insgesamt im Ordner: " + str(len(modNames)))
print("Mods insgesamt im Spielstand aktiviert: " + str(len(activeMods)))
print("")
