from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        # 메인 레이아웃
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 카운터 표시 레이블
        self.counter_label = Label(
            text='0',
            font_size=50
        )
        
        # +1 버튼
        increment_button = Button(
            text='+1',
            font_size=30,
            size_hint=(1, 0.5)
        )
        increment_button.bind(on_press=self.increment_counter)
        
        # 위젯 추가
        layout.add_widget(self.counter_label)
        layout.add_widget(increment_button)
        
        return layout
    
    def increment_counter(self, instance):
        # 현재 값을 가져와서 1 증가
        current = int(self.counter_label.text)
        self.counter_label.text = str(current + 1)

if __name__ == '__main__':
    CounterApp().run()