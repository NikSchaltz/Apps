from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import os

class MainApp(App):

    def build(self):
        self.data_file = "money.txt"
        self.players = [
            {'name': 'Player 1', 'money': 0, 'money_label': None, 'money_update': None},
            {'name': 'Player 2', 'money': 0, 'money_label': None, 'money_update': None},
            {'name': 'Player 3', 'money': 0, 'money_label': None, 'money_update': None},
            {'name': 'Player 4', 'money': 0, 'money_label': None, 'money_update': None},
            {'name': 'Player 5', 'money': 0, 'money_label': None, 'money_update': None},
            {'name': 'Player 6', 'money': 0, 'money_label': None, 'money_update': None},
        ]

        self.load_money_values()

        self.box = BoxLayout(orientation='vertical')

        for i, player in enumerate(self.players):
            player_layout = BoxLayout(orientation='horizontal')

            player_name_label = Label(text=player['name'])
            player['money_label'] = Label(text=str(player['money']))
            player['money_update'] = TextInput(input_filter='int')

            plus_button = Button(text='+')
            plus_button.bind(on_press=lambda instance, p=player: self.addMoney(p))

            minus_button = Button(text='-')
            minus_button.bind(on_press=lambda instance, p=player: self.substractMoney(p))

            player_layout.add_widget(player_name_label)
            player_layout.add_widget(player['money_label'])
            player_layout.add_widget(player['money_update'])
            player_layout.add_widget(plus_button)
            player_layout.add_widget(minus_button)

            self.box.add_widget(player_layout)

        return self.box

    def load_money_values(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i < len(self.players):
                        self.players[i]['money'] = int(line.strip())

    def save_money_values(self):
        with open(self.data_file, 'w') as file:
            for player in self.players:
                file.write(f"{player['money']}\n")

    def addMoney(self, player):
        try:
            update_amount = int(player['money_update'].text)
            player['money'] += update_amount
            player['money_label'].text = str(player['money'])
            player['money_update'].text = ""  # Clear the text box after adding money
            self.save_money_values()
        except ValueError:
            pass  # handle the error if necessary

    def substractMoney(self, player):
        try:
            update_amount = int(player['money_update'].text)
            player['money'] -= update_amount
            player['money_label'].text = str(player['money'])
            player['money_update'].text = ""  # Clear the text box after adding money
            self.save_money_values()
        except ValueError:
            pass  # handle the error if necessary


if __name__ == '__main__':
    MainApp().run()
