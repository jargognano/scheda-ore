#!/usr/bin/env python3

import customtkinter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class App(customtkinter.CTk):
        def __init__(self):
                super().__init__()

                self.title("Scheda Ore - Studio di Registrazione")
                self.geometry("1050x500")
                self.grid_columnconfigure((0, 1), weight=1)
                
                # riga vuota
                self.etichetta = customtkinter.CTkLabel(self, text="Studio di registrazione", fg_color="orange", text_color="black")
                self.etichetta.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
                
                # riga legenda
                self.gruppo = customtkinter.CTkLabel(self, text="NOME GRUPPO")
                self.gruppo.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
                self.nome_gruppo = customtkinter.CTkEntry(self, placeholder_text="")
                self.nome_gruppo.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
                self.data_lab = customtkinter.CTkLabel(self, text="DATA")
                self.data_lab.grid(row=1, column=2, padx=20, pady=(0, 20), sticky="w")
                self.ore_lab = customtkinter.CTkLabel(self, text="ORE DI REGISTRAZIONE")
                self.ore_lab.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w")
                self.costo_ora_lab = customtkinter.CTkLabel(self, text="COSTO ORARIO")
                self.costo_ora_lab.grid(row=1, column=4, padx=20, pady=(0, 20), sticky="w")
                self.sub_strum_lab = customtkinter.CTkLabel(self, text="SUBTOTALE")
                self.sub_strum_lab.grid(row=1, column=5, padx=20, pady=(0, 20), sticky="w")

                # riga primo strumento
                self.strum1 = customtkinter.CTkLabel(self, text="STRUMENTO 1")
                self.strum1.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
                self.strum_choice1 = customtkinter.CTkOptionMenu(self, values=["Strumento...", "Batteria", "Chitarra", "Basso", "Voce", "Altro"])
                self.strum_choice1.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")
                self.data1 = customtkinter.CTkEntry(self, placeholder_text="Registrato il...")
                self.data1.grid(row=2, column=2, padx=20, pady=(0, 20), sticky="w")
                self.ore1 = customtkinter.CTkEntry(self, placeholder_text="Registrato per...")
                self.ore1.grid(row=2, column=3, padx=20, pady=(0, 20), sticky="w")
                self.costo1 = customtkinter.CTkEntry(self, placeholder_text="30 €")
                self.costo1.grid(row=2, column=4, padx=20, pady=(0, 20), sticky="w")
                self.sub_strum1 = customtkinter.CTkLabel(self, text="0 €")
                self.sub_strum1.grid(row=2, column=5, padx=20, pady=(0, 20), sticky="w")

                # riga secondo strumento
                self.strum2 = customtkinter.CTkLabel(self, text="STRUMENTO 2")
                self.strum2.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")
                self.strum_choice2 = customtkinter.CTkOptionMenu(self, values=["Strumento...", "Batteria", "Chitarra", "Basso", "Voce", "Altro"])
                self.strum_choice2.grid(row=3, column=1, padx=20, pady=(0, 20), sticky="w")
                self.data2 = customtkinter.CTkEntry(self, placeholder_text="Registrato il...")
                self.data2.grid(row=3, column=2, padx=20, pady=(0, 20), sticky="w")
                self.ore2 = customtkinter.CTkEntry(self, placeholder_text="Registrato per...")
                self.ore2.grid(row=3, column=3, padx=20, pady=(0, 20), sticky="w")
                self.costo2 = customtkinter.CTkEntry(self, placeholder_text="30 €")
                self.costo2.grid(row=3, column=4, padx=20, pady=(0, 20), sticky="w")
                self.sub_strum2 = customtkinter.CTkLabel(self, text="0 €")
                self.sub_strum2.grid(row=3, column=5, padx=20, pady=(0, 20), sticky="w")

                # riga terzo strumento
                self.strum3 = customtkinter.CTkLabel(self, text="STRUMENTO 3")
                self.strum3.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="w")
                self.strum_choice3 = customtkinter.CTkOptionMenu(self, values=["Strumento...", "Batteria", "Chitarra", "Basso", "Voce", "Altro"])
                self.strum_choice3.grid(row=4, column=1, padx=20, pady=(0, 20), sticky="w")
                self.data3 = customtkinter.CTkEntry(self, placeholder_text="Registrato il...")
                self.data3.grid(row=4, column=2, padx=20, pady=(0, 20), sticky="w")
                self.ore3 = customtkinter.CTkEntry(self, placeholder_text="Registrato per...")
                self.ore3.grid(row=4, column=3, padx=20, pady=(0, 20), sticky="w")
                self.costo3 = customtkinter.CTkEntry(self, placeholder_text="30 €")
                self.costo3.grid(row=4, column=4, padx=20, pady=(0, 20), sticky="w")
                self.sub_strum3 = customtkinter.CTkLabel(self, text="0 €")
                self.sub_strum3.grid(row=4, column=5, padx=20, pady=(0, 20), sticky="w")

                # riga quarto strumento
                self.strum4 = customtkinter.CTkLabel(self, text="STRUMENTO 4")
                self.strum4.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="w")
                self.strum_choice4 = customtkinter.CTkOptionMenu(self, values=["Strumento...", "Batteria", "Chitarra", "Basso", "Voce", "Altro"])
                self.strum_choice4.grid(row=5, column=1, padx=20, pady=(0, 20), sticky="w")
                self.data4 = customtkinter.CTkEntry(self, placeholder_text="Registrato il...")
                self.data4.grid(row=5, column=2, padx=20, pady=(0, 20), sticky="w")
                self.ore4 = customtkinter.CTkEntry(self, placeholder_text="Registrato per...")
                self.ore4.grid(row=5, column=3, padx=20, pady=(0, 20), sticky="w")
                self.costo4 = customtkinter.CTkEntry(self, placeholder_text="30 €")
                self.costo4.grid(row=5, column=4, padx=20, pady=(0, 20), sticky="w")
                self.sub_strum4 = customtkinter.CTkLabel(self, text="0 €")
                self.sub_strum4.grid(row=5, column=5, padx=20, pady=(0, 20), sticky="w")

                # riga quinto strumento
                self.strum5 = customtkinter.CTkLabel(self, text="STRUMENTO 5")
                self.strum5.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="w")
                self.strum_choice5 = customtkinter.CTkOptionMenu(self, values=["Strumento...", "Batteria", "Chitarra", "Basso", "Voce", "Altro"])
                self.strum_choice5.grid(row=6, column=1, padx=20, pady=(0, 20), sticky="w")
                self.data5 = customtkinter.CTkEntry(self, placeholder_text="Registrato il...")
                self.data5.grid(row=6, column=2, padx=20, pady=(0, 20), sticky="w")
                self.ore5 = customtkinter.CTkEntry(self, placeholder_text="Registrato per...")
                self.ore5.grid(row=6, column=3, padx=20, pady=(0, 20), sticky="w")
                self.costo5 = customtkinter.CTkEntry(self, placeholder_text="30 €")
                self.costo5.grid(row=6, column=4, padx=20, pady=(0, 20), sticky="w")
                self.sub_strum5 = customtkinter.CTkLabel(self, text="0 €")
                self.sub_strum5.grid(row=6, column=5, padx=20, pady=(0, 20), sticky="w")

                # riga sesto strumento
                self.strum6 = customtkinter.CTkLabel(self, text="STRUMENTO 6")
                self.strum6.grid(row=7, column=0, padx=20, pady=(0, 20), sticky="w")
                self.strum_choice6 = customtkinter.CTkOptionMenu(self, values=["Strumento...", "Batteria", "Chitarra", "Basso", "Voce", "Altro"])
                self.strum_choice6.grid(row=7, column=1, padx=20, pady=(0, 20), sticky="w")
                self.data6 = customtkinter.CTkEntry(self, placeholder_text="Registrato il...")
                self.data6.grid(row=7, column=2, padx=20, pady=(0, 20), sticky="w")
                self.ore6 = customtkinter.CTkEntry(self, placeholder_text="Registrato per...")
                self.ore6.grid(row=7, column=3, padx=20, pady=(0, 20), sticky="w")
                self.costo6 = customtkinter.CTkEntry(self, placeholder_text="30 €")
                self.costo6.grid(row=7, column=4, padx=20, pady=(0, 20), sticky="w")
                self.sub_strum6 = customtkinter.CTkLabel(self, text="0 €")
                self.sub_strum6.grid(row=7, column=5, padx=20, pady=(0, 20), sticky="w")
                
                # riga mix e master
                self.mix_label = customtkinter.CTkLabel(self, text="MIX")
                self.mix_label.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="w")
                self.mix_par = customtkinter.CTkEntry(self, placeholder_text="Costo mix")
                self.mix_par.grid(row=8, column=1, padx=20, pady=(0, 20), sticky="w")
                self.brani_label = customtkinter.CTkLabel(self, text="BRANI")
                self.brani_label.grid(row=8, column=2, padx=20, pady=(0, 20), sticky="w")
                self.brani_entry = customtkinter.CTkEntry(self, placeholder_text="N. Brani")
                self.brani_entry.grid(row=8, column=3, padx=20, pady=(0, 20), sticky="w")
                self.master_label = customtkinter.CTkLabel(self, text="MASTER")
                self.master_label.grid(row=8, column=4, padx=20, pady=(0, 20), sticky="w")
                self.master_entry = customtkinter.CTkEntry(self, placeholder_text="Costo Master")
                self.master_entry.grid(row=8, column=5, padx=20, pady=(0, 20), sticky="w")
                
                # Collegare la funzione di aggiornamento agli eventi di modifica per il campo mix
                self.mix_par.bind("<KeyRelease>", lambda event: self.calcola_totale())

                # Collegare la funzione di aggiornamento agli eventi di modifica per il campo brani
                self.brani_entry.bind("<KeyRelease>", lambda event: self.calcola_totale())

                # Collegare la funzione di aggiornamento agli eventi di modifica per il campo master
                self.master_entry.bind("<KeyRelease>", lambda event: self.calcola_totale())

                
                # Collegare la funzione di aggiornamento agli eventi di modifica dei campi di input per strumento 1
                self.ore1.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore1, self.costo1, self.sub_strum1))
                self.costo1.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore1, self.costo1, self.sub_strum1))
                self.sub_strum1.bind("<Configure>", lambda event: self.calcola_totale())

                # Collegare la funzione di aggiornamento agli eventi di modifica dei campi di input per strumento 2
                self.ore2.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore2, self.costo2, self.sub_strum2))
                self.costo2.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore2, self.costo2, self.sub_strum2))
                self.sub_strum2.bind("<Configure>", lambda event: self.calcola_totale())

                # Collegare la funzione di aggiornamento agli eventi di modifica dei campi di input per strumento 3
                self.ore3.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore3, self.costo3, self.sub_strum3))
                self.costo3.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore3, self.costo3, self.sub_strum3))
                self.sub_strum3.bind("<Configure>", lambda event: self.calcola_totale())

                # Collegare la funzione di aggiornamento agli eventi di modifica dei campi di input per strumento 4
                self.ore4.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore4, self.costo4, self.sub_strum4))
                self.costo4.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore4, self.costo4, self.sub_strum4))
                self.sub_strum4.bind("<Configure>", lambda event: self.calcola_totale())

                # Collegare la funzione di aggiornamento agli eventi di modifica dei campi di input per strumento 5
                self.ore5.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore5, self.costo5, self.sub_strum5))
                self.costo5.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore5, self.costo5, self.sub_strum5))
                self.sub_strum5.bind("<Configure>", lambda event: self.calcola_totale())

                # Collegare la funzione di aggiornamento agli eventi di modifica dei campi di input per strumento 6
                self.ore6.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore6, self.costo6, self.sub_strum6))
                self.costo6.bind("<KeyRelease>", lambda event: self.update_subtotal(self.ore6, self.costo6, self.sub_strum6))
                self.sub_strum6.bind("<Configure>", lambda event: self.calcola_totale())

                # riga totale
                self.tot_label = customtkinter.CTkLabel(self, text="TOTALE", fg_color="green")
                self.tot_label.grid(row=9, column=0, padx=20, pady=(0, 20), sticky="ew")
                self.tot_entry = customtkinter.CTkLabel(self, text="0 €")
                self.tot_entry.grid(row=9, column=1, padx=20, pady=(0, 20), sticky="ew")
                
                 # pulsante per esportare in PDF
                self.export_button = customtkinter.CTkButton(self, text="Esporta in PDF", fg_color="blue", command=self.esporta_pdf)
                self.export_button.grid(row=9, column=5, padx=20, pady=(0, 20), sticky="ew")

                # Funzione per aggiornare il subtotale
        def update_subtotal(self, ore_entry, costo_entry, sub_label):
            try:
                ore = float(ore_entry.get())
                costo = float(costo_entry.get().replace('€', '').strip())
                subtotal = ore * costo
                sub_label.configure(text=f"{subtotal:.2f} €")
            except ValueError:
                sub_label.configure(text="0 €")
            
        def calcola_totale(self):
            try:
                subtotal1 = float(self.sub_strum1.cget("text").replace('€', '').strip())
                subtotal2 = float(self.sub_strum2.cget("text").replace('€', '').strip())
                subtotal3 = float(self.sub_strum3.cget("text").replace('€', '').strip())
                subtotal4 = float(self.sub_strum4.cget("text").replace('€', '').strip())
                subtotal5 = float(self.sub_strum5.cget("text").replace('€', '').strip())
                subtotal6 = float(self.sub_strum6.cget("text").replace('€', '').strip())
                
                # Calcolo del costo mix moltiplicato per il numero di brani
                mix_cost = float(self.mix_par.get().replace('€', '').strip()) if self.mix_par.get() else 0
                num_brani = float(self.brani_entry.get().strip()) if self.brani_entry.get() else 0
                mix_total = mix_cost * num_brani

                # Calcolo del sub-totale per il master
                master_cost = float(self.master_entry.get().replace('€', '').strip()) if self.master_entry.get() else 0

                # Somma totale
                total = subtotal1 + subtotal2 + subtotal3 + subtotal4 + subtotal5 + subtotal6 + mix_total + master_cost
                self.tot_entry.configure(text=f"{total:.2f} €")
            except ValueError:
                self.tot_entry.configure(text="0 €")


        
        def esporta_pdf(self):
                dati = [
                {
                        "strumento": self.strum_choice1.get(),
                        "data": self.data1.get(),
                        "ore": self.ore1.get(),
                        "costo": self.costo1.get(),
                        "subtotale": self.sub_strum1.cget("text")
                },
                {
                        "strumento": self.strum_choice2.get(),
                        "data": self.data2.get(),
                        "ore": self.ore2.get(),
                        "costo": self.costo2.get(),
                        "subtotale": self.sub_strum2.cget("text")
                },
                {
                        "strumento": self.strum_choice3.get(),
                        "data": self.data3.get(),
                        "ore": self.ore3.get(),
                        "costo": self.costo3.get(),
                        "subtotale": self.sub_strum3.cget("text")
                },
                {
                        "strumento": self.strum_choice4.get(),
                        "data": self.data4.get(),
                        "ore": self.ore4.get(),
                        "costo": self.costo4.get(),
                        "subtotale": self.sub_strum4.cget("text")
                },
                {
                        "strumento": self.strum_choice5.get(),
                        "data": self.data5.get(),
                        "ore": self.ore5.get(),
                        "costo": self.costo5.get(),
                        "subtotale": self.sub_strum5.cget("text")
                },
                {
                        "strumento": self.strum_choice6.get(),
                        "data": self.data6.get(),
                        "ore": self.ore6.get(),
                        "costo": self.costo6.get(),
                        "subtotale": self.sub_strum6.cget("text")
                }
                ]
                
                # Calcola il totale delle ore e dei costi
                totale_ore = sum(int(record["ore"]) for record in dati if record["ore"].isdigit())
                totale_costo = sum(int(record["costo"].replace(" €", "")) * int(record["ore"]) for record in dati if record["ore"].isdigit())
                
                # Calcola il costo totale del mix e master
                mix_cost = float(self.mix_par.get().replace('€', '').strip()) if self.mix_par.get() else 0
                num_brani = float(self.brani_entry.get().strip()) if self.brani_entry.get() else 0
                mix_total = mix_cost * num_brani
                master_cost = float(self.master_entry.get().replace('€', '').strip()) if self.master_entry.get() else 0

                # Aggiungi il costo del mix e master al totale delle ore
                totale_costo += mix_total + master_cost

                nome_file = f"dati rec {self.nome_gruppo.get()}.pdf"
                self.genera_pdf(dati, nome_file, totale_ore, totale_costo)
        
        def genera_pdf(self, dati, nome_file, totale_ore, totale_costo):
                c = canvas.Canvas(nome_file, pagesize=letter)
                larghezza, altezza = letter

                y = altezza - 40  # Iniziamo dall'alto della pagina
                c.drawString(30, y, f"Nome Gruppo: {self.nome_gruppo.get()}")
                y -= 20
                c.drawString(30, y, "Dati registrazione:")
                y -= 20

                for record in dati:
                        c.drawString(30, y, f"Strumento: {record['strumento']}")
                        y -= 15
                        c.drawString(30, y, f"Data: {record['data']}")
                        y -= 15
                        c.drawString(30, y, f"Ore: {record['ore']}")
                        y -= 15
                        c.drawString(30, y, f"Costo: {record['costo']}")
                        y -= 15
                        c.drawString(30, y, f"Subtotale: {record['subtotale']}")
                        y -= 25

                        # Se arriviamo troppo in basso nella pagina, aggiungiamo una nuova pagina
                        if y < 40:
                                c.showPage()
                                y = altezza - 40
                
                # Aggiungi le voci per costo mix, numero brani e costo master
                c.drawString(30, y, f"Costo Mix: {self.mix_par.get() if self.mix_par.get() else 'N/A'}")
                y -= 15
                c.drawString(30, y, f"Numero Brani: {self.brani_entry.get() if self.brani_entry.get() else 'N/A'}")
                y -= 15
                c.drawString(30, y, f"Costo Master: {self.master_entry.get() if self.master_entry.get() else 'N/A'}")
                y -= 25
                
                # Aggiungi il totale delle ore e il totale del costo
                c.drawString(30, y, f"Totale Ore: {totale_ore}")
                y -= 20
                c.drawString(30, y, f"Totale Costo: {totale_costo} €")

                c.save()
        
app = App()
app.mainloop()