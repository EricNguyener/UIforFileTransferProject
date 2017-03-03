from tkinter import *
from tkinter import ttk as ttk, messagebox, filedialog
from datetime import datetime, timedelta
import os, shutil, time


class FileCheck:

    def __init__(self, master):

        #Frame for header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        #Daily Folder
        self.dailyFolderName = StringVar()
        print (self.dailyFolderName)
        self.daily = (self.dailyFolderName.get())
        
        #Destination Folder
        self.destFolderName = StringVar()
        print (self.destFolderName)
        self.dest = (self.destFolderName.get())
        
        #Frame for labels and buttons
        self.frame_steps = ttk.Frame(master)
        self.frame_steps.pack()

        #tep labels
        dailyStepLabel = ttk.Label(self.frame_steps, text = 'Step 1.')
        dailyStepLabel.grid(row = 0, column = 0, columnspan = 2, pady = 5, sticky = 'w')
        destStepLabel = ttk.Label(self.frame_steps, text = 'Step 2.')
        destStepLabel.grid(row = 2, column = 0, columnspan = 2, pady = 5, sticky = 'w')
        initiateStepLabel = ttk.Label(self.frame_steps, text = 'Step 3. Execute File Check')
        initiateStepLabel.grid(row = 7, column = 0, columnspan = 2, pady = 5, sticky = 'w')
        
        #buttons   
        dailyButton = ttk.Button(self.frame_steps, text = 'Daily Folder...', command = self.selectDailyFolder)
        dailyButton.grid(row = 1, column = 1, pady = 5, sticky = 'w')
        destButton = ttk.Button(self.frame_steps, text = 'Destination Folder...', command = self.selectDestFolder)
        destButton.grid(row = 4, column = 1, pady = 5, sticky = 'w')
        initiateButton = ttk.Button(self.frame_steps, text = 'Initiate', command = lambda: self.timeCompare(self.dailyFileCheck,self.destFileCheck))
        initiateButton.grid(row = 8, column = 1, pady = 5, sticky = 'w')
        
        #path labels
        self.frame_path = ttk.Frame(master)
        self.frame_path.pack()
        dailyPathLabel = ttk.Label(self.frame_steps, text = self.dailyFolderName, textvariable = self.dailyFolderName)
        dailyPathLabel.grid(row = 1, column = 2, rowspan = 1, sticky = 'W')
        dailyPathLabel.config(foreground = 'blue')
        destPathLabel = ttk.Label(self.frame_steps, text = self.destFolderName, textvariable = self.destFolderName)
        destPathLabel.grid(row = 4, column = 2, rowspan = 1, sticky = 'W')
        destPathLabel.config(foreground = 'blue')
   

#Daily folder Browse Window        
    def selectDailyFolder(self):
        self.dailyFileCheck = filedialog.askdirectory(initialdir = "C:/Users/Thien Nguyen/Desktop/", title = "Daily Folder...") #Daily folder location
        self.dailyFolderName.set(self.dailyFileCheck)
        print (self.dailyFileCheck)
        print (self.dailyFolderName.get())
        
#Destination folder Browse Window        
    def selectDestFolder(self):
        self.destFileCheck = filedialog.askdirectory(initialdir = "C:/Users/Thien Nguyen/Desktop/", title = "Destination Folder...") #Destination folder location
        self.destFolderName.set(self.destFileCheck)
        print (self.destFileCheck)
        print (self.destFolderName.get())


#Gets file's modification time then time 24 hours ago
#Finds each file's path
#And if the file's extension = .txt and modified time is greater than 24hrs ago
#Copies file(s) to destination folder
    def timeCompare(self, dailyFileCheck, destFileCheck):
        print ('hello {}'.format(dailyFileCheck)) #checks to see if the daily folder name is passing to this function
        print ('hello {}'.format(destFileCheck)) #checks to see if the dest folder name is passing to this function
        print ()
        currentTime = datetime.now() #Current Time
        time24hoursAgo = currentTime - timedelta(hours = 24) #24hrs from current time
        for f in os.listdir(dailyFileCheck): #os.listdir - search through given directory
            files = os.path.realpath(os.path.join(dailyFileCheck,f)) #shows the file's path then joins the file's path and the directory's paths.  This provides the datetime with the entire file's path
            if files.endswith('.txt'):
                 fileSrcModifiedTime = datetime.fromtimestamp(os.path.getmtime(files)) #gives us each file's modified time
            if fileSrcModifiedTime > time24hoursAgo: #if file's modified time is greater than 24 hours old copy file to destination folder
                    print (files, "copied to: ", destFileCheck)
                    shutil.copy(files,destFileCheck) #copys file to destination
            else:
                    print (files, "not copied")
              


                    


def main():
    root = Tk() 
    root.wm_title("File Check")
    root.minsize(320, 300)
    filecheck = FileCheck(root) #Sets class to root level
    root.mainloop() 

if __name__ == '__main__' : main() #Runs the main function which runs the class and functions
















# Experiment with previous drill's code


### Modification time
##    file_m_time = datetime.datetime.fromtimestamp(path.getmtime(fname))
##
##    print datetime.datetime.now()
##    print file_m_time
##
### Different between today and file modification time
##
##    tdelta = datetime.datetime.now() - file_m_time
##
##    print tdelta
##    print 'days : %d' % tdelta.days
##
### File will be archived/logged if modded within the last 24hrs
##
##    if tdelta.days == 0:
##        global ready_to_archive
##        ready_to_archive = ready_to_archive + 1
##        return True
##    else: return False
