from classes import Weather
import tkinter
import customtkinter as ctk

def get_weather():
    city_text = entry_city.get()
    weather = Weather(city_text)
    if weather.print_weather() == '>>> City not found':
        info_label.configure(text=f'{weather.print_weather()}', text_color='red')
    else:
        info_label.configure(text=f'{weather.print_weather()}', text_color='#153626')

if __name__ == '__main__':
    window = ctk.CTk()
    window.geometry('500x250')
    window.title('Weather')
    window.resizable(False, False)
    window.config(bg='#adcbb5')

    enter_city = ctk.CTkLabel(master=window, text='Enter city:', width=100, height=25, font=('Microsoft YaHei Light', 18), bg_color='#adcbb5', text_color='#153626')
    entry_city = ctk.CTkEntry(master=window, width=175, height=30, corner_radius=10, font=('Microsoft YaHei Light', 18), bg_color='#adcbb5', fg_color='#7cc398', border_color='#62a77c', text_color='#153626')
    btn = ctk.CTkButton(master=window, text='Get weather', command=get_weather, width=120, height=32, border_width=0, corner_radius=10, font=('Microsoft YaHei UI Light', 16), bg_color='#adcbb5', fg_color='#7cc398', hover_color='#62a77c', text_color='#153626')
    info_label = ctk.CTkLabel(master=window, text='', width=100, height=25, font=('Cascadia Mono Light', 18), bg_color='#adcbb5', text_color='#153626')

    info_label.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    btn.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    entry_city.place(relx=0.65, rely=0.2, anchor=tkinter.CENTER)
    enter_city.place(relx=0.35, rely=0.2, anchor=tkinter.CENTER)
    window.mainloop()