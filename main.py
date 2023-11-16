# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv('netflix_data.csv')
netflix_subset = netflix_df[netflix_df['type']=="Movie"]
netflix_movies = netflix_subset.loc[:,["title", "country", "genre", "release_year", "duration"]]
short_movies = netflix_movies.loc[netflix_movies["duration"]<=60]
colors=[]

for lab,row in short_movies.iterrows():
    genre = row['genre']

    if genre == 'Children':
        colors.append('Red')
    elif genre == 'Documentaries':
        colors.append('Blue')
    elif genre == 'Stand-Up':
        colors.append('Green')
    else:
        colors.append('Yellow')

scatter_plot = plt.scatter(short_movies["release_year"],short_movies["duration"], c=colors)

plt.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='Red', markersize=10, label='Children'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='Blue', markersize=10, label='Documentaries'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='Green', markersize=10, label='Stand-Up'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='Yellow', markersize=10, label='Other')
])

plt.title("Scatter Plot of Movie Durations Over Years by Genre.")
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")
plt.grid(True)

plt.show()