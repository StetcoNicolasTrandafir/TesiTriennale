# Crea i protitipi per le singole canzoni

import json
from Song import Song

with open('data.txt') as json_file:
    data = json.load(json_file)
    for s in data['songs']:
        if "comedy" not in s["genre"]:
            song = Song(str(s["title"]).replace('"', " ").replace('/', '_').replace('?', '').replace(':', ''),
                        str(s["performer"]).replace('"', "").replace('/', '_').replace('?', '').replace(':', ''),
                        s["genre"], s["attributes"])
            song.toPercent()
        else:
            print("abc")



# {"title": "Idalah-Abal",
# "performer": "Bar Kokhba", 
# "genre": "avant-garde-ma0000012170", 
# "attributes": ["Jewish Music (8)", "World Fusion (8)", "Post-Bop (7)", "Chamber Jazz (6)", "Nocturnal (9)", 
# "Passionate (8)", "Uncompromising (8)", "Dreamy (7)", "Laid-Back/Mellow (7)", "Relaxed (7)", "Late Night (9)", "The Creative Side (9)"]}