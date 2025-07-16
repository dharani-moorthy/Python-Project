#DOF = 3 × (n - 1) - 2 × l - h
#Grübler Equation for calculating That’s the **Grübler’s equation** for calculating the *Degrees of Freedom (DOF)* in planar mechanisms! It helps determine how many independent movement in a mechanism
from tkinter import *
root=Tk()
root.geometry("700x700")
root.title("DOF")
root.configure(background="#ADD8E6")
name_app=Label(root,text="formula",font=("Allegro",50),background="#ADD8E6")
name_app.pack()
n_label=Label(root,text="n",bg="#ADD8E6")#n = number of links (including the fixed Frame)
n_label.pack()
n_entry=Entry(root,font=("CG Times",15))
n_entry.pack(pady=5)
l_label=Label(root,text="l",bg="#ADD8E6")#l = number of lower pairs (like revolute or prismatic joints)
l_label.pack()
l_entry=Entry(root,font=("CG Times",15))
l_entry.pack(pady=5)
h_label=Label(root,text="h",background="#ADD8E6")#h = number of higher pairs (like cam or gear contacts)
h_label.pack()
h_entry=Entry(root,font=("CG Times",15))
h_entry.pack(pady=5)
def fr():
    n=int(n_entry.get())
    l=int(l_entry.get())
    h=int(h_entry.get())
    g=(3 * (n - 1) - 2 * l - h)#formula
    if g <= 0:
        result.config(text=f"The value of DOF = {g}\nConsider rewriting the numbers to refine the system.")
    else:
        result.config(text=f"The value of DOF = {g}\n Done........")
z=Button(root,text="calculate",command=fr)
z.pack()
result=Label(root,bg="pink")
result.pack()
root.mainloop()
