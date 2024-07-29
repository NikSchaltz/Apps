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
        self.used_inDice = set()
        self.current_text = "Press the button to get a line"

    
    def build(self):
        #self.load_lines_from_txt("dices.txt")

        self.diceNum = 6
        self.showDice = False

        self.box = BoxLayout(orientation='vertical')
        self.DiceBox = BoxLayout(orientation='vertical', size_hint=(1, 0.80))
        self.buttonsBox = BoxLayout(orientation='horizontal', size_hint=(1, 0.20))
        self.changeBox = BoxLayout(orientation='horizontal', size_hint=(1, 0.20))
        self.diceNumLabel = Label(text=str(self.diceNum), font_size=150)

        self.addButton = Button(text='+', font_size=150)
        self.substractButton = Button(text='-', font_size=150)

        self.throwDiceButton = Button(text='Throw Dice', font_size=50)
        self.hideDiceButton = Button(text='Hide/show Dice', font_size=50)

        self.addButton.bind(on_press=self.addDice)
        self.substractButton.bind(on_press=self.substractDice)

        self.throwDiceButton.bind(on_press=self.throwDice)
        self.hideDiceButton.bind(on_press=self.hideShowDice)

        self.changeBox.add_widget(self.diceNumLabel)
        self.changeBox.add_widget(self.substractButton)
        self.changeBox.add_widget(self.addButton)

        self.buttonsBox.add_widget(self.throwDiceButton)
        self.buttonsBox.add_widget(self.hideDiceButton)

        self.box.add_widget(self.changeBox)
        self.box.add_widget(self.DiceBox)
        self.box.add_widget(self.buttonsBox)
        return self.box
    
    def addDice(self, instance):
        self.diceNum += 1
        self.updateDiceNum()

    def substractDice(self, instance):
        if self.diceNum > 1:
            self.diceNum -= 1
        self.updateDiceNum()

    def updateDiceNum(self):
        self.diceNumLabel.text = str(self.diceNum)

    def throwDice(self, instance):
        self.DiceBox.clear_widgets()
        self.clearDice()
        dice_values = [random.randint(1, 6) for _ in range(self.diceNum)]
        dice_values.sort()

        with open("dices.txt", 'w') as file:
            for value in dice_values:
                file.write(str(value) + "\n")

        self.showDice = False
    
    def clearDice(self):
        with open("dices.txt", 'w') as file:
            pass



    def hideShowDice(self, instance):
        #Hides the Dice
        if self.showDice == True:
            self.showDice = False
            self.DiceBox.clear_widgets()


        #Shows the dice
        else:
            self.showDice = True
            with open("dices.txt", 'r') as file:
                for line in file:
                    self.DiceBox.add_widget(Label(text=line.strip(), font_size=75))
   

if __name__ == '__main__':
    MainApp().run()
