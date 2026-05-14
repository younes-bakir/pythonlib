import matplotlib.pyplot as plt
import requests
import numpy as np

all_data = []

pokemon_num = int(input("How many Pokémon would you like to compare? "))

for i in range(pokemon_num):
    pokemon = input("Enter a Pokémon you'd like to compare (type 'exit' if you'd like to quit): ")
    if pokemon == "exit": break

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
    # print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        stats = [s['base_stat'] for s in data['stats']]
        labels = [s['stat']['name'] for s in data['stats']]
        all_data.append((data['name'].capitalize(), stats, labels))
    else:
        print("Pokémon not found!")

if len(all_data) > 0:
    labels = all_data[0][2]
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    for name, stats, _ in all_data:
        plot_stats = stats + stats[:1] 
        ax.plot(angles, plot_stats, label=name)
        ax.fill(angles, plot_stats, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.title("Pokémon-Comparisonatron-3000")
    plt.show()
