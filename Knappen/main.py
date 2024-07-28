from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import csv
import random

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lines = []
        self.used_indices = set()
        self.current_text = "Press the button to get a line"

    
    def build(self):
        self.load_lines_from_csv("liste.csv")
        self.box = BoxLayout(orientation='vertical')
        self.spilSpillet(self.box)
        return self.box
    
    def skrivNyeLinjer(self, instance):
        self.box.clear_widgets()
        self.tekstBox = TextInput(hint_text='Skriv linjer her')
        upload = Button(text='Tilføj linje')
        spilSpillet = Button(text='Spil spillet', size_hint=(1, 0.20))

        self.box.add_widget(spilSpillet)
        self.box.add_widget(self.tekstBox)
        self.box.add_widget(upload)

        spilSpillet.bind(on_press=self.spilSpillet)
        upload.bind(on_press=self.tilføjTekst)

    def spilSpillet(self, instance):
        self.box.clear_widgets()
        # Load lines from file at the start
        
        spil = BoxLayout(orientation='vertical')
        skrivTekst = Button(text='Skriv ny tekst', size_hint=(1, 0.20))

        
        # One outer box layout that contains the top bar and the lower box layout
        self.tekst = Label(text="Press the button to get a line")
        knappen = Button(text='Click for new')

        knappen.bind(on_press=self.update_text)
        skrivTekst.bind(on_press=self.skrivNyeLinjer)
        
        spil.add_widget(skrivTekst)
        spil.add_widget(self.tekst)
        spil.add_widget(knappen)

        self.box.add_widget(spil)

    def load_lines_from_csv(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                self.lines.append(row['tekst'].strip())

    def nyTekst(self):
        # Check if all lines have been used
        if len(self.used_indices) == len(self.lines):
            self.used_indices.clear()

        # Get a random index that hasn't been used yet
        index = random.randint(0, len(self.lines) - 1)
        while index in self.used_indices:
            index = random.randint(0, len(self.lines) - 1)

        # Mark this index as used
        self.used_indices.add(index)
        self.current_text = self.lines[index]
        
        return self.current_text

    def update_text(self, instance):
        self.tekst.text = self.nyTekst()

    def tilføjTekst(self, instance):
        new_line_text = self.tekstBox.text.strip()
        if new_line_text:
            # Find the next available number
            next_number = len(self.lines) + 1
            new_line = f"{next_number},{new_line_text}\n"
            
            # Append to the CSV file
            with open("liste.csv", 'a', newline='', encoding='utf-8') as file:
                file.write(new_line)
            
            # Update the internal lines list
            self.lines.append(new_line_text)
            
            # Notify user or update UI as needed
            self.tekstBox.text = ""  # Clear TextInput after adding line    



if __name__ == '__main__':
    MainApp().run()
