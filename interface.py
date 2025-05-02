from tkinter import *
from tkinter import ttk

# База калорій
calories = {
    "яблуко": 52,
    "банан": 89,
    "курка": 165,
    "рис": 130,
    "хліб": 250
}

total_cal = 0

def add_product():
    global total_cal
    name = comb.get().lower()
    try:
        grams = float(ent2.get())
    except ValueError:
        res_list.insert(END, "Невірна кількість грамів")
        return

    if name in calories:
        cal = calories[name] * grams / 100
        total_cal += cal
        res_list.insert(END, f"{name.capitalize()} – {grams} г = {cal:.1f} ккал")
        label_total.config(text=f"Загалом: {total_cal:.1f} ккал")
    else:
        res_list.insert(END, f"Немає в базі: {name}")

# Вікно
win = Tk()
win.title("Калькулятор калорій")
win.geometry('500x600')
win.configure(bg="#e0f7fa")  # Блакитний фон

# Напис 1
nap1 = Label(win, text="Назва продукту:", font=('Comic Sans MS', 16), fg="black")
nap1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Випадаючий список
comb = ttk.Combobox(win, font=('Comic Sans MS', 15), width=10, values=['Яблуко', 'Банан', 'Курка', 'Рис', 'Хліб'])
comb.grid(row=0, column=1, padx=10, pady=10)

# Напис 2
nap2 = Label(win, text="Кількість грамів:", font=('Comic Sans MS', 16),  fg="black")
nap2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Поле 2
ent2 = Entry(win, font=('Comic Sans MS', 16), width=20)
ent2.grid(row=1, column=1, padx=10, pady=10)

# Кнопка
but = Button(win, text='Додати', font=('Comic Sans MS', 16), width=10, height=2, bg="green", fg='black', command=add_product)
but.grid(row=2, column=0, columnspan=2, pady=10)

# Результати
res_list = Listbox(win, font=('Courier', 12), width=45, height=10)
res_list.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Загальна сума калорій
label_total = Label(win, text="Загалом: 0 ккал", font=('Comic Sans MS', 14), bg="#e0f7fa", fg="black")
label_total.grid(row=4, column=0, columnspan=2, pady=10)

win.mainloop()
