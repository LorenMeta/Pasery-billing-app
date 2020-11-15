from tkinter import *
import math, random, os
from tkinter import messagebox


class Fatura:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Fatura Shitje")
        self.root.configure(bg="lightgray")
        welcome = Label(self.root, text='Mirësevini', bd=20, bg="#323176", fg='white', relief=GROOVE,
                        font=("times new roman", 40, "bold"), pady=2, padx=1366).place(relwidth=1, relheight=0.15)

        self.byrek = IntVar()
        self.pite = IntVar()
        self.pica = IntVar()

        self.torta500 = IntVar()
        self.torta1000 = IntVar()
        self.trilece = IntVar()
        self.pasta = IntVar()
        self.bakllava = IntVar()
        self.tollumba = IntVar()
        self.zupa = IntVar()

        self.biskota10 = IntVar()
        self.biskota80 = IntVar()
        self.pufka100 = IntVar()
        self.pufka = IntVar()
        self.gurabie = IntVar()
        self.hallve = IntVar()
        self.amareta = IntVar()

        self.uje = IntVar()
        self.ivi = IntVar()
        self.amita = IntVar()
        self.dhalle = IntVar()

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.fatura = StringVar()
        x = random.randint(0, 10000)
        self.fatura.set(str(x))

        self.tvsh_entry = StringVar()
        self.total_price = StringVar()

        # ========================TE DHENAT E KLIENTIT============================

        F1 = LabelFrame(self.root, text='Të dhënat e klientit', relief=GROOVE, bd=7,
                        font=("times new roman", 20, "bold"), fg='gold', bg="#323176")
        F1.place(x=0, y=120, relwidth=1)

        costumer_name_label = Label(F1, text='Emri Mbiemri:', font=("times new roman", 20, "bold"), fg='white',
                                    bg="#323176").grid(row=0, column=0, padx=20, pady=5)
        costumer_name_entry = Entry(F1, textvariable=self.c_name, width=15, font=("times new roman", 15), bd=7,
                                    relief=SUNKEN).grid(row=0, column=1)

        costumer_phone_label = Label(F1, text='Nr. Telefonit:', font=("times new roman", 20, "bold"), fg='white',
                                     bg="#323176").grid(row=0, column=2, padx=20, pady=5)
        costumer_phone_entry = Entry(F1, textvariable=self.c_phone, width=15, font=("times new roman", 15), bd=7,
                                     relief=SUNKEN).grid(row=0, column=3)

        costumer_bill_label = Label(F1, text='Nr. Fatures:', font=("times new roman", 20, "bold"), fg='white',
                                    bg="#323176").grid(row=0, column=4, padx=20, pady=5)
        costumer_bill_entry = Entry(F1, width=15, textvariable=self.fatura, font=("times new roman", 15), bd=7).grid(
            row=0, column=5)

        save_button = Button(F1, text='Ruaj', command = self.save_bill, font=("times new roman", 12, "bold"), width=10, bd=7, ).grid(row=0,
                                                                                                             column=6,
                                                                                                             pady=10,
                                                                                                             padx=60)

        # =========================PRODUKTET=======================================

        # =========================BRUMI==================================

        F2 = LabelFrame(self.root, text='Produkte brumi', relief=GROOVE, bd=7, font=("times new roman", 20, "bold"),
                        fg='gold', bg="#323176")
        F2.place(x=10, y=230, width=300, height=200)

        byrek_label = Label(F2, text='Byrek', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(
            row=0, column=0, padx=10)
        byrek_entry = Entry(F2, width=10, textvariable=self.byrek, font=("times new roman", 15), bd=7,
                            relief=SUNKEN).grid(row=0, column=1)

        pite_label = Label(F2, text='Pite', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(row=1,
                                                                                                                 column=0,
                                                                                                                 pady=10)
        pite_entry = Entry(F2, width=10, textvariable=self.pite, font=("times new roman", 15), bd=7,
                           relief=SUNKEN).grid(row=1, column=1)

        Pica_label = Label(F2, text='Pica', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 pady=10)
        Pica_entry = Entry(F2, width=10, textvariable=self.pica, font=("times new roman", 15), bd=7,
                           relief=SUNKEN).grid(row=2, column=1)
        # =============================EMBELSIRA======================================

        F3 = LabelFrame(self.root, text='Embëlsira', relief=GROOVE, bd=7, font=("times new roman", 20, "bold"),
                        fg='gold', bg="#323176")
        F3.place(x=340, y=230, width=300, height=500)

        torta500_label = Label(F3, text='Torta 500', font=("times new roman", 20, "bold"), fg='white',
                               bg="#323176").grid(row=0, column=0)
        torta500_entry = Entry(F3, width=10, textvariable=self.torta500, font=("times new roman", 15), bd=7,
                               relief=SUNKEN).grid(row=0, column=1)

        torta1000_label = Label(F3, text='Torta 1000', font=("times new roman", 20, "bold"), fg='white',
                                bg="#323176").grid(row=1, column=0, pady=10)
        torta1000_entry = Entry(F3, width=10, textvariable=self.torta1000, font=("times new roman", 15), bd=7,
                                relief=SUNKEN).grid(row=1, column=1)

        Trilece_label = Label(F3, text='Trilece', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(
            row=2, column=0, pady=10)
        Trilece_entry = Entry(F3, width=10, textvariable=self.trilece, font=("times new roman", 15), bd=7,
                              relief=SUNKEN).grid(row=2, column=1)

        Pasta_label = Label(F3, text='Pasta', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(
            row=3, column=0, pady=10)
        Pasta_entry = Entry(F3, width=10, textvariable=self.pasta, font=("times new roman", 15), bd=7,
                            relief=SUNKEN).grid(row=3, column=1)

        Bakllava_label = Label(F3, text='Bakllava', font=("times new roman", 20, "bold"), fg='white',
                               bg="#323176").grid(row=4, column=0, pady=10)
        Bakllava_entry = Entry(F3, width=10, textvariable=self.bakllava, font=("times new roman", 15), bd=7,
                               relief=SUNKEN).grid(row=4, column=1)

        Tollumba_label = Label(F3, text='Tollumba', font=("times new roman", 20, "bold"), fg='white',
                               bg="#323176").grid(row=5, column=0, pady=10)
        Tollumba_entry = Entry(F3, width=10, textvariable=self.tollumba, font=("times new roman", 15), bd=7,
                               relief=SUNKEN).grid(row=5, column=1)

        Zupa_label = Label(F3, text='Zupa', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(row=6,
                                                                                                                 column=0,
                                                                                                                 pady=10)
        Zupa_entry = Entry(F3, width=10, textvariable=self.zupa, font=("times new roman", 15), bd=7,
                           relief=SUNKEN).grid(row=6, column=1)

        # ==========================BISKOTA========================

        F4 = LabelFrame(self.root, text='Biskota', relief=GROOVE, bd=7, font=("times new roman", 20, "bold"), fg='gold',
                        bg="#323176")
        F4.place(x=670, y=230, width=300, height=500)

        biskota10_label = Label(F4, text='Biskota 10', font=("times new roman", 20, "bold"), fg='white',
                                bg="#323176").grid(row=0, column=0)
        biskota10_entry = Entry(F4, width=10, textvariable=self.biskota10, font=("times new roman", 15), bd=7,
                                relief=SUNKEN).grid(row=0, column=1)

        Biskota80_label = Label(F4, text='Biskota 80', font=("times new roman", 20, "bold"), fg='white',
                                bg="#323176").grid(row=1, column=0, pady=10)
        Biskota80_entry = Entry(F4, width=10, textvariable=self.biskota80, font=("times new roman", 15), bd=7,
                                relief=SUNKEN).grid(row=1, column=1)

        Pufka100_label = Label(F4, text='Pufka 100', font=("times new roman", 20, "bold"), fg='white',
                               bg="#323176").grid(row=2, column=0, pady=10)
        Pufka100_entry = Entry(F4, width=10, textvariable=self.pufka100, font=("times new roman", 15), bd=7,
                               relief=SUNKEN).grid(row=2, column=1)

        Pufka_label = Label(F4, text='Pufka', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(
            row=3, column=0, pady=10)
        Pufka_entry = Entry(F4, width=10, textvariable=self.pufka, font=("times new roman", 15), bd=7,
                            relief=SUNKEN).grid(row=3, column=1)

        Gurabie_label = Label(F4, text='Gurabie', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(
            row=4, column=0, pady=10)
        Gurabie_entry = Entry(F4, width=10, textvariable=self.gurabie, font=("times new roman", 15), bd=7,
                              relief=SUNKEN).grid(row=4, column=1)

        Hallve_label = Label(F4, text='Hallvë', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(
            row=5, column=0, pady=10)
        Hallve_entry = Entry(F4, width=10, textvariable=self.hallve, font=("times new roman", 15), bd=7,
                             relief=SUNKEN).grid(row=5, column=1)

        Amareta_label = Label(F4, text='Amareta', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(
            row=6, column=0, pady=10)
        Amareta_entry = Entry(F4, width=10, textvariable=self.amareta, font=("times new roman", 15), bd=7,
                              relief=SUNKEN).grid(row=6, column=1)

        # =======================PIJE=================================

        F5 = LabelFrame(self.root, text='Pije', relief=GROOVE, bd=7, font=("times new roman", 20, "bold"), fg='gold',
                        bg="#323176")
        F5.place(x=10, y=450, width=300, height=280)

        uje_label = Label(F5, text='Ujë', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=20)
        uje_entry = Entry(F5, width=10, textvariable=self.uje, font=("times new roman", 15), bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10)

        ivi_label = Label(F5, text='Ivi', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(row=1,
                                                                                                               column=0,
                                                                                                               padx=20,
                                                                                                               pady=20)
        ivi_entry = Entry(F5, width=10, textvariable=self.ivi, font=("times new roman", 15), bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10)

        amita_label = Label(F5, text='Amita', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(
            row=2, column=0, padx=20, pady=10)
        amita_entry = Entry(F5, width=10, textvariable=self.amita, font=("times new roman", 15), bd=7,
                            relief=SUNKEN).grid(row=2, column=1, padx=10)

        dhalle_label = Label(F5, text='Dhalle', font=("times new roman", 20, "bold"), fg='white', bg="#323176").grid(
            row=3, column=0, padx=20, pady=10)
        dhalle_entry = Entry(F5, width=10, textvariable=self.dhalle, font=("times new roman", 15), bd=7,
                             relief=SUNKEN).grid(row=3, column=1, padx=10)

        # =======================TOTAL TVSH/PA TVSH===================

        F6 = Frame(self.root, relief=GROOVE, bd=7)
        F6.place(x=1010, y=530, width=300, height=200)

        fshij_faturen = Button(F6, command=self.clear, text='FSHIJ', font=("times new roman", 15, "bold"), bg='#75ACFB',
                               fg='white', pady=15, width=10).grid(row=0, column=0, padx=5)
        totali_fatures = Button(F6, command=lambda: [self.total(), self.bill_area()], text='Totali',
                                font=("times new roman", 15, "bold"), bg='#75ACFB', fg='white', pady=15, width=10).grid(
            row=0, column=1, padx=5)

        tvsh_label = Label(F6, text='TVSH', font=("times new roman", 20, "bold"), fg='white', bg="#323176", pady=5,
                           padx=5).grid(row=2, column=0, pady=10)
        tvsh_entry = Entry(F6, width=10, textvariable=self.tvsh_entry, font=("times new roman", 15), bd=7,
                           relief=SUNKEN).grid(row=2, column=1)

        totali_label = Label(F6, text='Totali', font=("times new roman", 20, "bold"), fg='white', bg="#323176", pady=5,
                             padx=5).grid(row=3, column=0, pady=5)
        totali_entry = Entry(F6, width=10, textvariable=self.total_price, font=("times new roman", 15), bd=7,
                             relief=SUNKEN).grid(row=3, column=1)

        # ======================FATURA================================

        F7 = Frame(self.root, relief=GROOVE, bd=7)
        F7.place(x=990, y=230, width=350, height=280)
        titulli_fatura = Label(F7, text='Fatura', font=("times new roman", 15, "bold"), relief=GROOVE, bd=7).pack(
            fill=X)
        scroll_y = Scrollbar(F7, orient=VERTICAL)
        self.txtarea = Text(F7, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        self.welcome_bill()

    def total(self):
        self.brk = self.byrek.get() * 50
        self.pit = self.pite.get() * 50
        self.pic = self.pica.get() * 60
        self.t500 = self.torta500.get() * 500
        self.t1000 = self.torta1000.get() * 1000
        self.trile = self.trilece.get() * 70
        self.past = self.pasta.get() * 50
        self.baklla = self.bakllava.get() * 70
        self.toll = self.tollumba.get() * 20
        self.zup = self.zupa.get() * 50
        self.b10 = self.biskota10.get() * 10
        self.b80 = self.biskota80.get() * 80
        self.puf100 = self.pufka100.get() * 100
        self.puf = self.pufka.get() * 10
        self.gurab = self.gurabie.get() * 10
        self.hallv = self.hallve.get() * 10
        self.amaret = self.amareta.get() * 20
        self.uj = self.uje.get() * 50
        self.iv = self.ivi.get() * 60
        self.amit = self.amita.get() * 60
        self.dhall = self.dhalle.get() * 50

        self.total_total_price = (
                self.brk +
                self.pit +
                self.pic +
                self.t500 +
                self.t1000 +
                self.trile +
                self.past +
                self.baklla +
                self.toll +
                self.zup +
                self.b10 +
                self.b80 +
                self.puf100 +
                self.puf +
                self.gurab +
                self.hallv +
                self.amaret +
                self.uj +
                self.iv +
                self.amit +
                self.dhall
        )

        self.total_price.set("LEK " + str(self.total_total_price))
        self.tvsh_entry.set("LEK " + str(self.total_total_price * 0.2))

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t Miresevini Pasticeri Pellumbi\n")
        self.txtarea.insert(END, f"\n Nr. Fatures : {self.fatura.get()}")
        self.txtarea.insert(END, f"\n Emri : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Nr. Telefonit : {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=======================================")
        self.txtarea.insert(END, f"\nProduktet\t\tSasia\t\tCmimi")
        self.txtarea.insert(END, f"\n=======================================")

    def bill_area(self):
        if self.c_name.get() == "":
            messagebox.showerror("Error", "Ploteso te dhenat e klientit")
        elif self.total_price.get() == "LEK 0":
            messagebox.showerror("Error", "Nuk ka asnje produkt")
        else:
            self.welcome_bill()
            if self.byrek.get() != 0:
                self.txtarea.insert(END, f"\n Byrek\t\t{self.byrek.get()}\t\t{self.brk}")
            if self.pite.get() != 0:
                self.txtarea.insert(END, f"\n Pite\t\t{self.pite.get()}\t\t{self.pit}")
            if self.pica.get() != 0:
                self.txtarea.insert(END, f"\n Pica\t\t{self.pica.get()}\t\t{self.pic}")
            if self.torta500.get() != 0:
                self.txtarea.insert(END, f"\n Torta 500\t\t{self.torta500.get()}\t\t{self.t500}")
            if self.torta1000.get() != 0:
                self.txtarea.insert(END, f"\n Torta 1000\t\t{self.torta1000.get()}\t\t{self.t1000}")
            if self.trilece.get() != 0:
                self.txtarea.insert(END, f"\n Trilece\t\t{self.trilece.get()}\t\t{self.trile}")
            if self.pasta.get() != 0:
                self.txtarea.insert(END, f"\n Pasta\t\t{self.pasta.get()}\t\t{self.past}")
            if self.bakllava.get() != 0:
                self.txtarea.insert(END, f"\n Bakllava\t\t{self.bakllava.get()}\t\t{self.baklla}")
            if self.tollumba.get() != 0:
                self.txtarea.insert(END, f"\n Tollumba\t\t{self.tollumba.get()}\t\t{self.toll}")
            if self.zupa.get() != 0:
                self.txtarea.insert(END, f"\n Zupa\t\t{self.zupa.get()}\t\t{self.zup}")
            if self.biskota10.get() != 0:
                self.txtarea.insert(END, f"\n Biskota 10\t\t{self.biskota10.get()}\t\t{self.b10}")
            if self.biskota80.get() != 0:
                self.txtarea.insert(END, f"\n Biskota 80\t\t{self.biskota80.get()}\t\t{self.b80}")
            if self.pufka100.get() != 0:
                self.txtarea.insert(END, f"\n Pufka 100\t\t{self.pufka100.get()}\t\t{self.puf100}")
            if self.pufka.get() != 0:
                self.txtarea.insert(END, f"\n Pufta\t\t{self.pufka.get()}\t\t{self.puf}")
            if self.gurabie.get() != 0:
                self.txtarea.insert(END, f"\n Gurabie\t\t{self.gurabie.get()}\t\t{self.gurab}")
            if self.hallve.get() != 0:
                self.txtarea.insert(END, f"\n Hallve\t\t{self.hallve.get()}\t\t{self.hallv}")
            if self.amareta.get() != 0:
                self.txtarea.insert(END, f"\n Amareta\t\t{self.amareta.get()}\t\t{self.amaret}")
            if self.uje.get() != 0:
                self.txtarea.insert(END, f"\n Uje\t\t{self.uje.get()}\t\t{self.uj}")
            if self.ivi.get() != 0:
                self.txtarea.insert(END, f"\n Ivi\t\t{self.ivi.get()}\t\t{self.iv}")
            if self.amita.get() != 0:
                self.txtarea.insert(END, f"\n Amita\t\t{self.amita.get()}\t\t{self.amit}")
            if self.dhalle.get() != 0:
                self.txtarea.insert(END, f"\n Dhalle\t\t{self.dhalle.get()}\t\t{self.dhall}")

            self.txtarea.insert(END, f"\n---------------------------------------")
            self.txtarea.insert(END, f"\n TVSH : \t\t\t {self.tvsh_entry.get()}")
            self.txtarea.insert(END, f"\n Totali : \t\t\t {self.total_price.get()}")
            self.txtarea.insert(END, f"\n---------------------------------------")

            self.save_bill()

    def clear(self):
        self.byrek.set(0)
        self.pite.set(0)
        self.pica.set(0)

        self.torta500.set(0)
        self.torta1000.set(0)
        self.trilece.set(0)
        self.pasta.set(0)
        self.bakllava.set(0)
        self.tollumba.set(0)
        self.zupa.set(0)

        self.biskota10.set(0)
        self.biskota80.set(0)
        self.pufka100.set(0)
        self.pufka.set(0)
        self.gurabie.set(0)
        self.hallve.set(0)
        self.amareta.set(0)

        self.uje.set(0)
        self.ivi.set(0)
        self.amita.set(0)
        self.dhalle.set(0)

        self.c_name.set("")
        self.c_phone.set("")
        self.fatura.set("")
        x = random.randint(0, 10000)
        self.fatura.set(str(x))

        self.tvsh_entry.set("")
        self.total_price.set("")

        self.welcome_bill()


    def save_bill(self):
        op = messagebox.askyesnocancel("Ruaj faturen", "Deshironi te ruani faturen?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0',END)
            f1 = open(r"C:\Users\Loren\Desktop\billing_app\Faturat/" + str(self.c_name.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return


root = Tk()
obj = Fatura(root)
root.mainloop()



