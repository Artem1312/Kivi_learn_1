from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class BoxApp(App):
    def build(self):
        #bl = BoxLayout()
        #gl = GridLayout(cols=10, padding=[10], spacing=3)
        gl = GridLayout(rows=10, padding=[10], spacing=3)
        ''' 
        gl.add_widget(Button(text='Button 1'))
        gl.add_widget(Button(text='Button 2'))
        gl.add_widget(Button(text='Button 3'))
        gl.add_widget(Button(text='Button 4'))
        '''

        for x in range(50):
            gl.add_widget(Button(text='X'))
        return gl


if __name__ == "__main__":
    BoxApp().run();
