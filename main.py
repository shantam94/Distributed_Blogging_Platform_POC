import os
import json
import pandas as pd
from src.initialize_nodes import *
from src.distance_calc import *
from src.cities import city_coordinates
from src.generate_dates import *
from src.generate_titles import *
from tqdm import tqdm
import string
import random

# Nodes with simulated locations
top_10_keys = list(city_coordinates.keys())[:5]

# Creating a new dictionary with only the top 10 keys
selected_cities = {key: city_coordinates[key] for key in top_10_keys}
NODES_LOCATIONS = selected_cities
print(NODES_LOCATIONS)

# Function to generate a random alphanumeric ID
def generate_random_alphanumeric_id(length=10):
    characters = string.ascii_letters + string.digits  # Combination of letters and digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id


def generate_random_author_name():
    first_names = ["Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack",
                   "Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan", "Sophia", "Mason", "Isabella", "Logan",
                   "Mia", "Lucas", "Amelia", "Jacob", "Charlotte", "Aiden", "Evelyn", "Daniel", "Abigail", "Matthew"]

    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
                  "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
                  "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall"]

    # Randomly select one first name and one last name
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # Combine them to form a full name
    author_name = f"{first_name} {last_name}"

    return author_name

# Function to insert data based on proximity and horizontal fragmentation
def insert_data(data, random_city):
    data_location =  city_coordinates.get(random_city)
    location_based_node = find_closest_node(data_location, NODES_LOCATIONS)
    print("The closest node to the requestor is: ", location_based_node)
    
    # Choose the node based on location based attribute
    target_node = location_based_node
    print(target_node)
    filepath = os.path.join("nodes",target_node, f"{target_node}.csv")
    print(filepath)
    data_transformed = pd.DataFrame(data, index = [0])
    
    if os.path.exists(filepath):   
        node_data = pd.read_csv(filepath)
        node_data = node_data._append(data_transformed, ignore_index=True)
        node_data.to_csv(filepath, index = False)
    else:
        data_transformed.to_csv(filepath, index = False)

    print(f"Data with ID {data['Blog_ID']} inserted into {target_node}.")


# Main function
def main():
    
    for i in tqdm(range(50)):
        
        initialize_nodes(NODES_LOCATIONS)
        
        sample_blogs = pd.read_csv("src/model_blogs.csv")
        
        # Example insert
        data_to_insert = {
            'Blog_ID': generate_random_alphanumeric_id(),
            'Author': generate_random_author_name(),
            'Author_ID':generate_random_alphanumeric_id(),
            "Title" : generate_random_title(),
            "Publication_Date" : generate_random_date().strftime("%Y-%m-%d"),
            "Blog Text" :  sample_blogs.sample(1)['Blog'].unique()
        }
        # Simulated location for the data
        
        random_city= random.choice(list(city_coordinates.keys()))

        print("The city from where the data is getting inserted is: ", random_city)
        insert_data(data_to_insert, random_city)
        

if __name__ == "__main__":
    main()
