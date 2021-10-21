from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,BooleanProperty


class MyGridLayout(GridLayout):
    count = StringProperty('0')
    z = 0
    count_enabled = BooleanProperty(False)
    #slider_value_txt = StringProperty('0')
    def increment(self):
        #print('Button clicked')
        if  self.count_enabled:
            self.z  += 1
            self.count = str(self.z)

    def state_button(self,widget):
        #print(widget.state)
        if widget.state == 'down':
            widget.text = 'ON'
            self.count_enabled = True
        else:
            widget.text = 'OFF'
            self.count_enabled = False

    def on_switch_active(self,widget):
        print(str(widget.active))

    def on_slider_value(self,widget):
        print(str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))

class MainApp(App):
    def build(self):
        return 

MainApp().run()