#DAY 83 |  Exercise

import win32com.client as wincom

speaker_number = 0  #or 1
spk = wincom.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)


names = ['Google''Samsung''Facebook''Amazon''Netflix']

# while(True):
for name in names:
    spk.Speak(f"Shoutout to {name}")
    print(names)
    


