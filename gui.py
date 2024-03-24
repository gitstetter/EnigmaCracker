import logging
import tkinter as tk
from tkinter import ttk

from enigmator import ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from enigmator import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from enigmator import Enigma
from enigmator import Plugboard

logging.basicConfig(filename='gui.log',
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    # datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


ROTORS = [ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V]
REFLECTORS = [REFLECTOR_A, REFLECTOR_B, REFLECTOR_C]

ROTOR_MAP ={str(rotor):rotor for rotor in ROTORS}
REFLECTOR_MAP ={str(reflector):reflector for reflector in REFLECTORS}

EnigmaMachine=Enigma(reflector=REFLECTOR_B, 
                left_rotor=ROTOR_III, 
                middle_rotor=ROTOR_II, 
                right_rotor=ROTOR_I, 
                rotor_positions="1 1 1",
                ring_positions="1 1 1",
                plugboard=Plugboard()
                )

def set_lbl_encrypt_out():
    plain_text = txt_plain.get("1.0", tk.END).replace("\n", "")
    encrypted_text=EnigmaMachine.encipher(plain_text=plain_text)
    lbl_encrypt_out["text"]=encrypted_text

def set_enigma_params():
    reflector=cbox_reflector.get()
    left_rotor=cbox_left_rotor.get()
    middle_rotor=cbox_middle_rotor.get()
    right_rotor=cbox_right_rotor.get()

    left_rotor_pos=cbox_left_rotor_pos.get()
    middle_rotor_pos=cbox_middle_rotor_pos.get()
    right_rotor_pos=cbox_right_rotor_pos.get()

    left_rotor_ring=cbox_left_rotor_ring.get()
    middle_rotor_ring=cbox_middle_rotor_ring.get()
    right_rotor_ring=cbox_right_rotor_ring.get()

    logging.info(f"Settings of EnigmaMachine were changed")
    logging.info("Before: "+str(EnigmaMachine))
    
    EnigmaMachine.reflector = REFLECTOR_MAP[reflector]
    EnigmaMachine.left_rotor = ROTOR_MAP[left_rotor]
    EnigmaMachine.left_rotor.rotor_position = int(left_rotor_pos)
    EnigmaMachine.left_rotor.ring_position = int(left_rotor_ring)
    EnigmaMachine.middle_rotor = ROTOR_MAP[middle_rotor]
    EnigmaMachine.middle_rotor.rotor_position = int(middle_rotor_pos)
    EnigmaMachine.middle_rotor.ring_position = int(middle_rotor_ring)
    EnigmaMachine.right_rotor = ROTOR_MAP[right_rotor]
    EnigmaMachine.right_rotor.rotor_position = int(right_rotor_pos)
    EnigmaMachine.right_rotor.ring_position = int(right_rotor_ring)
    plugsettings=txt_plugs.get("1.0", tk.END).replace("\n", "").strip()
    EnigmaMachine.plugboard = Plugboard(plugsettings)
    
    logging.info("After: "+str(EnigmaMachine))


window = tk.Tk()
window.title("Enigma Cracker!")

window.rowconfigure(0, minsize=50, weight=1)
window.rowconfigure(1, minsize=50, weight=1)
# window.columnconfigure(1, minsize=800, weight=1) #set the width the second column to 800 pix

frm_menu = tk.Frame(window, relief=tk.RAISED, bd=1)
frm_text = tk.Frame(window)
frm_encrypt_out = tk.Frame(window)

frm_enigma_setup = tk.Frame(frm_menu, relief=tk.RAISED, bd=1)
btn_encipher=tk.Button(frm_menu, text="encrypt!", command=set_lbl_encrypt_out)
btn_save=tk.Button(frm_menu, text="save!", command=set_enigma_params)

cbox_reflector = ttk.Combobox(frm_menu, values=REFLECTORS,state="readonly", width=len(max(REFLECTORS, key = len)))
cbox_reflector.current(1)
cbox_left_rotor = ttk.Combobox(frm_menu, values=ROTORS,state="readonly", width=len(max(ROTORS, key = len)))
cbox_left_rotor.current(2)
cbox_middle_rotor = ttk.Combobox(frm_menu, values=ROTORS, state="readonly", width=len(max(ROTORS, key = len)))
cbox_middle_rotor.current(1)
cbox_right_rotor = ttk.Combobox(frm_menu, values=ROTORS, state="readonly", width=len(max(ROTORS, key = len)))
cbox_right_rotor.current(0)

cbox_left_rotor_pos = ttk.Combobox(frm_menu, values=[x for x in range(1, 27)],state="readonly", width=3)
cbox_left_rotor_pos.current(0)
cbox_middle_rotor_pos = ttk.Combobox(frm_menu, values=[x for x in range(1, 27)],state="readonly", width=3)
cbox_middle_rotor_pos.current(0)
cbox_right_rotor_pos = ttk.Combobox(frm_menu, values=[x for x in range(1, 27)],state="readonly", width=3)
cbox_right_rotor_pos.current(0)

cbox_left_rotor_ring = ttk.Combobox(frm_menu, values=[x for x in range(1, 27)],state="readonly", width=3)
cbox_left_rotor_ring.current(0)
cbox_middle_rotor_ring = ttk.Combobox(frm_menu, values=[x for x in range(1, 27)],state="readonly", width=3)
cbox_middle_rotor_ring.current(0)
cbox_right_rotor_ring = ttk.Combobox(frm_menu, values=[x for x in range(1, 27)],state="readonly", width=3)
cbox_right_rotor_ring.current(0)

txt_plugs = tk.Text(frm_menu, width=29, height=1)
txt_plugs.insert(1.0, "AA BB CC")


lbl_pos = tk.Label(frm_menu, text="Rotor Position:", justify="left")
lbl_ring = tk.Label(frm_menu, text="Ring Position: ", justify="left")
lbl_plugs = tk.Label(frm_menu, text="Plug Settings:", justify="left")

txt_plain = tk.Text(frm_text, height=10)

lbl_encrypt_out = tk.Label(frm_encrypt_out, text="Encrypt your message above", justify="center")

frm_enigma_setup.grid(row=0, column=0)

cbox_reflector.grid(row=0, column=0)
cbox_left_rotor.grid(row=0, column=1)
cbox_middle_rotor.grid(row=0, column=2)
cbox_right_rotor.grid(row=0, column=3)

cbox_left_rotor_pos.grid(row=1, column=1)
cbox_middle_rotor_pos.grid(row=1, column=2)
cbox_right_rotor_pos.grid(row=1, column=3)

cbox_left_rotor_ring.grid(row=2, column=1)
cbox_middle_rotor_ring.grid(row=2, column=2)
cbox_right_rotor_ring.grid(row=2, column=3)

txt_plugs.grid(row=3, columnspan=3, column=1)

lbl_pos.grid(row=1, column=0)
lbl_ring.grid(row=2, column=0)
lbl_plugs.grid(row=3, column=0)

btn_save.grid(row=4, column=3, padx=5, pady=5) #expand horizontally in both directions and fill the entire frame
btn_encipher.grid(row=4, column=4, padx=5, pady=5) #expand horizontally in both directions and fill the entire frame
txt_plain.grid(row=1, column=0) #force the frame to expand in every direction.
lbl_encrypt_out.grid(row=1, column=1)

frm_menu.grid(row=0, column=1, sticky="nsew") #force the frame to expand vertically
frm_text.grid(row=0, column=2, sticky="nsew")
frm_encrypt_out.grid(row=1, column=2, sticky="nsew")#, sticky="ns")

window.mainloop()
