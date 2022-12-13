from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
from pydub import AudioSegment
from pydub.generators import Sine, Square, Triangle, Sawtooth, Pulse
from pydub.playback import play
import threading
 
class app():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("274x285")
        self.window.title("SBT")
        backgr = "light blue"
        self.window.configure(background=backgr)
        self.WaveForms = ["Sine","Square","Triangle","Sawtooth","Pulse"]
 
        self.freq = IntVar()
        self.duration = IntVar()
        validatecommand = self.window.register(self.valid_durentry)
        validatecommand2 = self.window.register(self.valid_frentry)
        self.tone = None
 
        self.drlabel = Label(self.window,text="DURATION:",bg=backgr)
        self.drlabel.place(x=40,y=20)
        self.drentry = Entry(self.window,width=20,textvariable=self.duration,validate="key",validatecommand=(validatecommand, "%S"))
        self.drentry.place(x=110,y=20)
        self.frlabel = Label(self.window,text="FREQUENCY:",bg=backgr)
        self.frlabel.place(x=32,y=70)
        self.frentry = Entry(self.window,width=20,textvariable=self.freq,validate="key",validatecommand=(validatecommand2, "%S"))
        self.frentry.place(x=110,y=70)
        self.wfentry = ttk.Combobox(self.window,width=17)
        self.wfentry.place(x=110,y=120)
        self.wflabel = Label(self.window,text="WAVEFORM:",bg=backgr)
        self.wflabel.place(x=33,y=120)
        self.wfentry["values"] = self.WaveForms
        self.wfentry.current(0)
        self.lbl = Label(self.window,text="",width=38,bg=backgr)
        self.lbl.place(x=1,y=155)
        self.btnplay = Button(self.window,text="PLAY",bg="light green",width=28,command=self.init_task)
        self.btnplay.place(x=33,y=190)
        self.btnsave = Button(self.window,text="SAVE",bg="gold3",width=28,command=self.save_tone)
        self.btnsave.place(x=33,y=230)
 
        self.window.mainloop()
 
    def valid_frentry(self,char):
        return char in "0123456789."
 
    def valid_durentry(self,char):
        return char in "0123456789"
 
    def make_tone(self):
        if self.wfentry.get() == "Sine":
            self.tone = Sine(self.freq.get()).to_audio_segment(duration=self.duration.get())
        elif self.wfentry.get() == "Square":
            self.tone = Square(self.freq.get()).to_audio_segment(duration=self.duration.get())
        elif self.wfentry.get() == "Triangle":
            self.tone = Triangle(self.freq.get()).to_audio_segment(duration=self.duration.get())
        elif self.wfentry.get() == "Sawtooth":
            self.tone = Sawtooth(self.freq.get()).to_audio_segment(duration=self.duration.get())
        elif self.wfentry.get() == "Pulse":
            self.tone = Pulse(self.freq.get()).to_audio_segment(duration=self.duration.get())
        self.lbl.configure(text="PLAYING")
        play(self.tone)
        self.lbl.configure(text="")
 
    def save_tone(self):
        if self.tone:
            audio = filedialog.asksaveasfilename(initialdir="/",
                    title="SAVE",defaultextension=".wav")
            if audio != "":
                self.tone.export(audio,format="wav")
                messagebox.showinfo("SAVED","Saved audio tone.")
 
    def init_task(self):
        if self.freq.get() > 0 and self.duration.get() > 0:
            t = threading.Thread(target=self.make_tone)
            t.start()
 
if __name__=="__main__":
    app()