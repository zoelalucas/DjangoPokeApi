from django.shortcuts import render
import requests


def pokemon(request, pk):
             
   try:
          
          data=requests.get('https://pokeapi.co/api/v2/pokemon/'+pk).json()
          
          id = str(data["id"])
          urlimg= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/' + id + '.svg'
          Nombre          = data["name"].capitalize()
          Vida            = data["stats"][0]["base_stat"]
          Experiencia     = data["base_experience"]
          Ataque          = data["stats"][1]["base_stat"]
          AtaqueEspecial  = data["stats"][3]["base_stat"]
          Defensa         = data["stats"][2]["base_stat"]
          Habilidad1      = data["abilities"][0]["ability"]["name"].capitalize()
          Habilidad2      = data["abilities"][1]["ability"]["name"].capitalize()
          Peso            = data["weight"]
          Altura          = data["height"]
          Tipo            = data["types"][0]["type"]["name"].capitalize()
          
          url1 = data["species"]["url"]
          data1 = requests.get(url1) 
          data1 = data1.json()    
          
          url2 = data1["evolution_chain"]["url"]
          data2 = requests.get(url2)
          data2 = data2.json()
          
          nombrepokemon = data2["chain"]["species"]["name"]
   except:
    return render(request, 'pokedex/falla.html')
       
   try:
     evolucion1 = data2["chain"]["evolves_to"][0]["species"]["name"]    
   except:
        try:
            evolucion2 = data2["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]

        except:
         evolucion2 = print("No tiene Evolucion")
   try:
        evolucion2 = data2["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]

   except:
        evolucion1 = print("No tiene Evolucion")
        evolucion2 = print("No tiene Evolucion")

    
   context = {'Nombre': Nombre, 'Vida': Vida, 'Experiencia': Experiencia,
                    'Ataque': Ataque, 'AtaqueEspecial':AtaqueEspecial, 'Defensa':Defensa,
                    "Habilidad1": Habilidad1, "Habilidad2": Habilidad2, "imagen":urlimg, 
                    "Pokemon": nombrepokemon, "PrimerEvolucion": evolucion1, "SegundaEvolucion": evolucion2,
                    "Peso": Peso, "Altura": Altura, "Tipo": Tipo}
            
   return render(request, 'pokedex/index.html', context)


def pokemonhome(request):
     return render(request, 'pokedex/falla.html')