class Volume:
    def volume_up(self):
        print("Volume Up!")
    def volume_down(self):
        print("Volume Down!")
    

class Channel:
    def channel_up(self):
        print("Channel Up!")
    def channel_down(self):
        print("Channel Down!")
class RemoteControl(Volume,Channel):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def __str__(self):
        return f"Name : {self.name}"
    
    
volume = Volume()
volume.volume_up()
volume.volume_down()
channel = Channel()
channel.channel_down()
channel.channel_up()

control = RemoteControl("Sony")
control.volume_down()
control.volume_up()
control.channel_down()
control.channel_up()