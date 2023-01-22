from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from connection_db import Connection


"""
CREATE TABLE Employee (
    ID INT PRIMARY KEY,
    article VARCHAR(255) NOT NULL,
    sales_date DATETIME NOT NULL,
    sales INT NOT NULL
);"""


class DataUploader(GridLayout):
    def __init__(self, **kwargs):
        super(DataUploader, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Article'))
        self.article = TextInput(multiline=False)
        self.add_widget(self.article)
        self.add_widget(Label(text='Sales date'))
        self.date = TextInput(multiline=False)
        self.add_widget(self.date)
        self.add_widget(Label(text='Sales'))
        self.sales = TextInput(multiline=False)
        self.add_widget(self.sales)
        self.submit = Button(text='Submit')
        self.submit.bind(on_press=self.upload_data)
        self.add_widget(self.submit)

    def upload_data(self, instance):
        connection = Connection

        article = self.article.text
        date = self.date.text
        sales = self.sales.text

        # insert data into table
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO Employee (article, date, salary) VALUES ('{article}', '{date}', '{sales}')")
        connection.commit()


class MyApp(App):
    def build(self):
        return DataUploader()


if __name__ == '__main__':
    MyApp().run()
