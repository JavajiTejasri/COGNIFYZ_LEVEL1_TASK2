import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Show columns
print(df.columns)

# Count restaurants by city
city_counts = df['City'].value_counts()

print("\nTop Cities by Number of Restaurants:")
print(city_counts.head())

# Average ratings by city
average_ratings = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

print("\nTop Rated Cities:")
print(average_ratings.head())

# Plot graph
top5 = city_counts.head(5)

top5.plot(kind='bar')

plt.title("Top 5 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")

plt.tight_layout()

# Save graph
plt.savefig("city_restaurants.png")

plt.show()