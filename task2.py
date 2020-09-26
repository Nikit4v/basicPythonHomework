# print(f"{(hours:=int(int(time:=input())/3600))}:{(minutes:=int((int(time)-hours*3600)/60))}:{(seconds:=int(time)-minutes*60-hours*3600)}")
time = input()
hours = int(int(time)/3600)
minutes = int((int(time) - hours*3600)/60)
seconds = int(time) - minutes*60 - hours*3600
print(f"{hours}:{minutes}:{seconds}")
