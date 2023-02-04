from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ThreeLineRightIconListItem, IconRightWidget
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.tab import MDTabsBase
import sqlite3
import json

Window.size = 400, 700

with open('settings.json', 'r') as s_d:
    data = json.load(s_d)

with sqlite3.connect('mydb.db') as db:
    sql = db.cursor()


class Tab(MDFloatLayout, MDTabsBase):
    pass

class CustomThreeLineRightIconListItem(ThreeLineRightIconListItem):
    row_id = StringProperty()
    tag_icon = StringProperty()
    comment = StringProperty()
    price = StringProperty()
    odometr = StringProperty()
    date = StringProperty()
    tag = StringProperty()
class MyRoot(MDScreenManager):

    @staticmethod
    def return_settings_data(key):
        return data[key]

    @staticmethod
    def set_settings_data(key, value):
        data[key] = value

    def calc_func(self, val):
        return

    def add_tracking_element(self):
        self.ids.mybox.add_widget(MDTextField(hint_text='What will tracking?'))

    def mybox_build(self):
        for i in range(len(data['tracking_elements'])):
            self.ids.mybox.add_widget(MDLabel(text=data['tracking_elements'][i]))

    def on_save(self, instance, value, date_range):
        """
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        """
        value = str(value)
        val: str = value.replace('-', '/')
        self.ids.mydate.text = val

    def on_cancel(self, instance, value):
        """Events called when the "CANCEL" dialog box button is clicked."""
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def save_to_bd(self, *args):
        if '' in args:
            pass
        else:
            self.ids.tag_icon.icon = self.ids.comment.text = self.ids.price.text = self.ids.odometr.text = self.ids.mydate.text = self.ids.tag_label.text = ''
            sql.execute('INSERT INTO myTable VALUES(?, ?, ?, ?, ?, ?)', args)
            db.commit()
            self.current = 'main_screen'

    def update_list(self):
        self.ids.container.clear_widgets()
        db_record: list = sql.execute('SELECT rowid, * FROM myTable ORDER BY date DESC').fetchall()
        for i in range(len(db_record)):
            list_item = CustomThreeLineRightIconListItem(
                    text=f'{db_record[i][5]}',
                    secondary_text=f'{db_record[i][2]}',
                    tertiary_text=f'{db_record[i][4]}',
                    row_id=f'{db_record[i][0]}',
                    tag_icon=f'{db_record[i][1]}',
                    comment=f'{db_record[i][2]}',
                    price=f'{db_record[i][3]}',
                    odometr=f'{db_record[i][4]}',
                    date=f'{db_record[i][5]}',
                    tag=f'{db_record[i][6]}',
                    )
            list_item.add_widget(IconRightWidget(icon=db_record[i][1]))
            self.ids.container.add_widget(list_item)

    def change_or_delete_item(self, instance):
        self.ids.tag_icon.icon = instance.tag_icon
        self.ids.tag_label.text = instance.tag
        self.ids.comment.text = instance.comment
        self.ids.price.text = instance.price
        self.ids.odometr.text = instance.odometr
        self.ids.mydate.text = instance.date


class MyApp(MDApp, MyRoot):
    def build(self):
        self.title = 'myapp'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return MyRoot()

    def on_start(self):
        self.root.update_list()

    def on_stop(self):
        with open('settings.json', 'w') as f:
            json.dump(data, f)


if __name__ == "__main__":
    MyApp().run()
