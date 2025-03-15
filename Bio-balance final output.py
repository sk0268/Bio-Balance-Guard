from PIL import Image
import tensorflow as tf
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox

import mysql.connector


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Senthil@0804",
        database="dbms_project"
    )


def load_model():
    return tf.keras.applications.MobileNetV2(
        weights='imagenet', 
        input_shape=(224, 224, 3),  
        include_top=True  
    )


def recognize_animal(image_path, model):
    img = Image.open(image_path)
    img = img.resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    predictions = model.predict(img_array)
    predicted_class = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0][0][1]
   
    predicted_class = predicted_class.replace('_', ' ').title()
    return predicted_class


def get_animal_info(animal_name, db_connection):
    cursor = db_connection.cursor()
    query = "SELECT * FROM animals WHERE Animal = %s"
    cursor.execute(query, (animal_name,))
    return cursor.fetchone() 
def select_image():
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename()
    return image_path

def main():
    db_connection = connect_to_database()
    model = load_model()
    image_path = select_image()
    animal_name = recognize_animal(image_path, model)
    print(animal_name)
    animal_info = get_animal_info(animal_name, db_connection)
    if animal_info:
        print("Animal Information:")
        print("Name:", animal_info[0]) 
        print("Habitat:", animal_info[1])
        print("Diet:", animal_info[2])
       
    else:
        print("Animal not found in the database.")
    db_connection.close()

    
    def create_result_window(animal_info):
        window = tk.Tk()
        window.title("Animal Information")
        
       
        name_label = tk.Label(window, text="Name: " + animal_info[0])
        name_label.pack()
        
        height_label = tk.Label(window, text="Height (cm): " + str(animal_info[1]))
        height_label.pack()
        
        weight_label = tk.Label(window, text="Weight (kg): " + str(animal_info[2]))
        weight_label.pack()
        
        color_label = tk.Label(window, text="Color: " + animal_info[3])
        color_label.pack()
        
        lifespan_label = tk.Label(window, text="Lifespan (years): " + str(animal_info[4]))
        lifespan_label.pack()
        
        diet_label = tk.Label(window, text="Diet: " + animal_info[5])
        diet_label.pack()
        
        habitat_label = tk.Label(window, text="Habitat: " + animal_info[6])
        habitat_label.pack()
        
        predators_label = tk.Label(window, text="Predators: " + animal_info[7])
        predators_label.pack()
        
        speed_label = tk.Label(window, text="Average Speed (km/h): " + str(animal_info[8]))
        speed_label.pack()
        
        countries_label = tk.Label(window, text="Countries Found: " + animal_info[9])
        countries_label.pack()
        
        conservation_label = tk.Label(window, text="Conservation Status: " + animal_info[10])
        conservation_label.pack()
        
        family_label = tk.Label(window, text="Family: " + animal_info[11])
        family_label.pack()
        
        gestation_label = tk.Label(window, text="Gestation Period (days): " + str(animal_info[12]))
        gestation_label.pack()
        
        top_speed_label = tk.Label(window, text="Top Speed (km/h): " + str(animal_info[13]))
        top_speed_label.pack()
        
        social_structure_label = tk.Label(window, text="Social Structure & Offspring per Birth: " + animal_info[14])
        social_structure_label.pack()
        
        window.mainloop()

   

    def main():
       
        
        if animal_info:
            create_result_window(animal_info)
        else:
            messagebox.showinfo("Animal not found", "Animal not found in the database.")
        
        db_connection.close()

    if __name__ == "__main__":
        main()
if __name__ == "__main__":
    main()