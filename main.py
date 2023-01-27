from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
import sqlite3
import json

Window.size = 400, 700

with open('settings.json', 'r') as s_d:
    data = json.load(s_d)

with sqlite3.connect('mydb.db') as db:
    sql = db.cursor()

class MyRoot(MDScreenManager):

    def return_settings_data(self, value):
        return data[value]

    def set_settings_data(self, key, value):
        data[key] = value

    def add_tracking_element(self):
        self.ids.mybox.add_widget(MDTextField(hint_text='What will tracking?'))

    def mybox_build(self):
        for i in range(len(data['tracking_elements'])):
            self.ids.mybox.add_widget(MDLabel(text=data['tracking_elements'][i]))

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        value = str(value)
        val: str = value.replace('-', '/')
        self.ids.mydate.text = val

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def ppp(self, *args):
        if '' in args:
            pass
        else:
            self.ids.job.text = self.ids.comment.text = self.ids.price.text = self.ids.odometr.text = self.ids.mydate.text = self.ids.tag_label.text = ''
            sql.execute('INSERT INTO myTable VALUES(?, ?, ?, ?, ?, ?)', args)
            db.commit()
            x = sql.execute('SELECT * FROM myTable WHERE rowid == 3').fetchall()
            print(x)
            self.current = 's1'



class MyApp(MDApp, MyRoot):
    def build(self):
        self.title = 'myapp'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return MyRoot()

    def on_start(self):
        pass

    def on_stop(self):
        with open('settings.json', 'w') as f:
            json.dump(data, f)


if __name__ == "__main__":
    MyApp().run()
