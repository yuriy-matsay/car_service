from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screenmanager import MDScreenManager


Window.size = 400, 700


class Tab(MDFloatLayout, MDTabsBase):
    pass

#class MyRoot(MDScreenManager):
#    def fu(self, instance):
#        print(instance.text)
#    pass

class MyApp(MDApp):
    def build(self):
        self.title = 'myapp'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

    def fu(self, instance):
        print(instance.text)
        instance.text = '2345'




if __name__ == "__main__":
    MyApp().run()
