from textsize import * 
import shutil
import face_recognition
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import time
import pickle
from tkinter import filedialog

import tkinter as tk
from tkinter import * 
from tkinter import Message ,Text
import cv2
import os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
button_width=300
button_height=45

fontsize = 20
font = ImageFont.truetype("arial.ttf", fontsize)


window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("UiTM Attendance system")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)

window.geometry('1920x1080')
window.state('zoomed')
window.configure(background="#515151")



#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

#path = "profile.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(window, image = img)


#panel.pack(side = "left", fill = "y", expand = "no")

#cv_img = cv2.imread("img541.jpg")
#x, y, no_channels = cv_img.shape
#canvas = tk.Canvas(window, width = x, height =y)
#canvas.pack(side="left")
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img)) 
# Add a PhotoImage to the Canvas
#canvas.create_image(0, 0, image=photo, anchor=tk.NW)

#msg = Message(window, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)

known_face_encodings =[]
known_face_names = []
names = []
Ids = []

def Resize_Image(image, maxsize):
    r1 = image.size[0]/maxsize[0] # width ratio
    r2 = image.size[1]/maxsize[1] # height ratio
    ratio = max(r1, r2)
    newsize = (int(image.size[0]/ratio), int(image.size[1]/ratio))
    image = image.resize(newsize, Image.ANTIALIAS)
    return image


student_id =Image.open("icons/student_id.png")
student_id = Resize_Image(student_id,[button_width,100])
student_id =ImageTk.PhotoImage(student_id)

student_name =Image.open("icons/student_name.png")
student_name = Resize_Image(student_name,[button_width,100])
student_name =ImageTk.PhotoImage(student_name)

attendance =Image.open("icons/attendance.png")
attendance = Resize_Image(attendance,[button_width,100])
attendance =ImageTk.PhotoImage(attendance)

msg =Image.open("icons/msg.png")
msg = Resize_Image(msg,[button_width,100])
msg =ImageTk.PhotoImage(msg)

xlabels=300

title =Image.open("icons/title.png")
 #title = Resize_Image(title,[button_width,100])
title =ImageTk.PhotoImage(title)

logo1 =Image.open("icons/um6p_emines_logo.png")
logo1 = Resize_Image(logo1,[button_width,50])
logo1 =ImageTk.PhotoImage(logo1)



title_img = tk.Label(window, border=0,image = title  ,bg="#515151"  , activebackground = "#515151") 
title_img.place(x=-160, y=40)

#logos
logo1_img = tk.Label(window, border=0,image = logo1  ,bg="#515151"  , activebackground = "#515151") 
logo1_img.place(x=65, y=10)


####
lbl = tk.Label(window,border=0 ,image = student_id  ,bg="#515151"  , activebackground = "#515151" ) 
lbl.place(x=xlabels, y=200)

txt = tk.Entry(window,width=15 ,bg="#F1F0F0" ,fg="#5B5B5B",font=('Cambria', 20, ' bold '),justify = CENTER)
txt.place(x=700, y=205)

lbl2 = tk.Label(window, border=0 ,image = student_name  ,bg="#515151"  , activebackground = "#515151" ) 
lbl2.place(x=xlabels, y=300)

txt2 = tk.Entry(window,width=15  ,bg="#F1F0F0"  ,fg="#5B5B5B",font=('Cambria', 20, ' bold ') ,justify = CENTER )
txt2.place(x=700, y=305)

lbl3 = tk.Label(window, border=0 ,image = msg  ,bg="#515151"  , activebackground = "#515151") 
lbl3.place(x=400, y=400)

lbl4 = tk.Label(window, border=0 ,image = attendance  ,bg="#515151"  , activebackground = "#515151") 
lbl4.place(x=400, y=650)
#notif

message = tk.Label(window, text="" ,bg="#F1F0F0"  ,fg="#BC2226"  ,width=30  ,height=2, activebackground = "#515151" ,font=('times', 15, ' bold ')) 
message.place(x=750, y=400)


#scrolable text
frame1 = tk.Frame(window,width=300, height=20,bg = '#ffffff',
                  borderwidth=1, relief="sunken")

s = tk.Scrollbar(frame1)
s.pack(side=RIGHT, fill=Y)
T = tk.Text(frame1, width=45, height=5, wrap="word",
                   yscrollcommand=s.set,
                   borderwidth=0, highlightthickness=0)

s.config(command=T.yview)
s.pack(side="right", fill="y")
T.pack(side="left", fill="both", expand=True)
frame1.place(x=750,y=632)
# for i in range(40): 
#    T.insert(tk.END, "This is line %d\n" % i)



#sig
sigg =Image.open("icons/sig.png")
sigg = Resize_Image(sigg,[200,50])
sigg =ImageTk.PhotoImage(sigg)
lbl_sig = tk.Label(window, border=0 ,image = sigg  ,bg="#515151"  , activebackground = "#515151") 
lbl_sig.place(x=1250, y=730)

#logos 
# sigg =Image.open("icons/sig.png")
# sigg = Resize_Image(sigg,[150,100])
# sigg =ImageTk.PhotoImage(sigg)
# lbl_sig = tk.Label(window, border=0 ,image = sigg  ,bg="#515151"  , activebackground = "#515151") 
# lbl_sig.place(x=1300, y=1080-130)



 
def clear1():
    print("clear1")
    txt.delete(0, 'end')    
    res = ""
    
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    print("clear2")
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():  
    print("status: %d" % (var1.get()))  
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        sampleNum=0
        student_dir=""
        face_file_name=""
        while(True):
            ret, img = cam.read()
            #display the frame
            cv2.imshow('frame', img)
            key=cv2.waitKey(1)
            if  key & 0xFF == ord('s'):
                dirname = 'TrainingImage_lecturer'
                student_dir=dirname+"/"+Id+'.'+name
                print(student_dir)
                os.makedirs(student_dir, exist_ok=True)

                #os.mkdir(dirname)
                sampleNum=sampleNum+1
                face_file_name=name +"."+Id +'.'+ str(sampleNum) + ".jpg"
                cv2.imwrite(os.path.join(student_dir, face_file_name ), img)
                print("take img")
            #wait for 100 miliseconds 
            elif key & 0xFF == ord('q'):
                #print("qqqq")
                break
 
        #print("khrejt")
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

        #train last img
        if (var1.get()==1):
            TrainLastImage(student_dir,face_file_name)

        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)

#check button
var1 = IntVar()
Checkbutton(window, text="train student that will be added", variable=var1,bg="#515151",activebackground = "#515151").place(x=265,y=620) #,bg="#515151",  activebackground = "#515151",fg="#ffffff"

#######added


def TakeImages_folder():  #choose file and the program will create the folder with id and name
    print("take img file")      
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):

        loaded_dir = file_path = filedialog.askopenfilename()
        print(loaded_dir)
        dirname = 'TrainingImage_lecturer'
        student_dir=dirname+"/"+str(Id)+'.'+name
        #print(student_dir)
        os.makedirs(student_dir, exist_ok=True)
                
        face_file_name=name +"."+str(Id) +'.'+ str(1) + ".jpg"
        shutil.copy(loaded_dir,os.path.join(student_dir, face_file_name ))
        img = Image.open(loaded_dir)
        img.show() 
        #train last img
        if (var1.get()==1):
            TrainLastImage(student_dir,face_file_name)

        res = "Images Saved for ID : " + Id +" Name : "+ name
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)


def process_and_encode(images):
    # initialize the list of known encodings and known names
    known_encodings = {}
    ppl_with_bad_imgs = []
    #known_names = []
    print("[LOG] Encoding faces ...")

    with open('StudentDetails\StudentDetails.csv','w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['Id', 'Name'])
    csvFile.close()

    for image_path in tqdm(images):
        # Load image
        image = face_recognition.load_image_file(image_path)

        # the person's name is the name of the folder where the image comes from
        name = image_path.split(os.path.sep)[-2]

        #check if there are any faces first
        number_of_faces = len(face_recognition.face_locations(image))
        #print(number_of_faces)
        if (number_of_faces==1):
            # Encode the face into a 128-d embeddings vector
            known_encodings[name] = face_recognition.face_encodings(image)[0]
            print(name)
            Id=name.split('.')[0]
            only_name=name.split('.')[1]
            row = [Id , only_name]
            #print(row)
            with open('StudentDetails\StudentDetails.csv','a', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
        elif(number_of_faces==0):
            ppl_with_bad_imgs.append(name)
            #print("image to change for " + name)
            #print(ppl_with_bad_imgs)
            
    if (len(ppl_with_bad_imgs)):
        # Converting integer list to string list 
        s = [i for i in ppl_with_bad_imgs] 
      
        # Join list items using join() 
        res = " ".join(s)
      
        res = "invalid pics for: " + res
    else:
        res = "Traning finished"
    message.configure(text = res)

    
    return  known_encodings

#######


def TrainImages():
    global known_face_encodings
    global known_face_names
    res = "Trainning start"  
    message.configure(text = res)
    
    dataset_dir="TrainingImage_lecturer"
    #names,Ids = getNamesAndIds(dataset_dir)
    
    images = []
    for direc, _, files in tqdm(os.walk(dataset_dir)):
        for file in files:
            if file.endswith("jpg"):
                images.append(os.path.join(direc,file))

    #print(images)
    
    known_face_encodings = process_and_encode(images)

    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(known_face_encodings, f)

def TrainLastImage(imgpath,_face_file_name):

    # Load face encodings
    with open('dataset_faces.dat', 'rb') as f:
        all_face_encodings = pickle.load(f)

    # Grab the list of names and the list of encodings
    known_face_names = list(all_face_encodings.keys())
    known_face_encodings = np.array(list(all_face_encodings.values()))
    print(os.path.join(imgpath,_face_file_name))
    image = face_recognition.load_image_file(os.path.join(imgpath,_face_file_name))
    temp=os.path.join(imgpath,_face_file_name)
    _name = os.path.basename(temp.split(os.path.sep)[-2])
    print("name %s : ",_name)
    print(known_face_encodings.shape)
    known_face_encodings2=dict(zip(known_face_names, known_face_encodings))
    print(known_face_encodings2.keys())
    print("lenght1 %d : ",len(known_face_encodings2))
    known_face_encodings2[_name]=face_recognition.face_encodings(image)[0]
    print(known_face_encodings2.keys())
    #known_face_encodings.append(face_recognition.face_encodings(image)[0])
    #known_face_names.append(_name)
    #known_face_encodings=np.concatenate(known_face_encodings,face_recognition.face_encodings(image)[0])


    print("lenght2 %d : ",len(known_face_encodings2))
    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(known_face_encodings2, f)



def getNamesAndIds(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    print(imagePaths)

    #create empth namelist
    names=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #getting the Id from the image
         # print(os.path.basename(os.path.normpath(imagePath)))
        imagePath_lastFolder=os.path.basename(os.path.normpath(imagePath))
        Id=int(imagePath_lastFolder.split('.')[0])
         # print(imagePath_lastFolder.split('.')[0])

        # extract the face name 
        name=imagePath_lastFolder.split('.')[1]
        names.append(name)
        Ids.append(Id)        
    return names,Ids


def TrackImages():

    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)  
    
    # Load face encodings
    with open('dataset_faces.dat', 'rb') as f:
        all_face_encodings = pickle.load(f)

    # Grab the list of names and the list of encodings
    known_face_names = list(all_face_encodings.keys())
    known_face_encodings = np.array(list(all_face_encodings.values()))

    #unknown_image = face_recognition.load_image_file("lecturer_test.jpg")
    loaded_dir_un = filedialog.askopenfilename()
    unknown_image = face_recognition.load_image_file(loaded_dir_un)

    face_locations = face_recognition.face_locations(unknown_image)
    unknown_face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
    pil_image = Image.fromarray(unknown_image)
    draw = ImageDraw.Draw(pil_image)

    count_unknown=0
    for (top, right, bottom, left), unknown_face_encoding in zip(face_locations, unknown_face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding,tolerance=0.45)

        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, unknown_face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        font = getFontSize(name,top, right, bottom, left)
        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name,font=font)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 3, bottom - text_height - 5), name,font=font, fill=(255, 255, 255, 255))

        #save in file
        if(name!="Unknown"):
            ts = time.time()      
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            Id=name.split('.')[0]
            only_name=name.split('.')[1]
            attendance.loc[len(attendance)] = [Id,only_name,date,timeStamp]
        else :
            print("unknown person(s)")
            count_unknown += 1
            res_mes="number of unknown faces detected : " + str(count_unknown)
            message.configure(text= res_mes)
    
    
    # create attendance file
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    img_fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".png"
    pil_image.save(img_fileName)
    attendance.to_csv(fileName,index=False)
    res=attendance
    T.delete('1.0', END)
    T.insert(tk.END, res)

    # Remove the drawing library from memory as per the Pillow docs
    del draw

    # Display the resulting image
    pil_image.show()





take_pics =Image.open("icons/take_pics.png")
take_pics = Resize_Image(take_pics,[button_width,button_height])
take_pics =ImageTk.PhotoImage(take_pics)

load_folder =Image.open("icons/load_folder.png")
load_folder = Resize_Image(load_folder,[button_width,button_height])
load_folder =ImageTk.PhotoImage(load_folder)

record_attendance =Image.open("icons/record_attendance.png")
record_attendance = Resize_Image(record_attendance,[button_width,button_height])
record_attendance =ImageTk.PhotoImage(record_attendance)

train_model =Image.open("icons/train_model.png")
train_model = Resize_Image(train_model,[button_width,button_height])
train_model =ImageTk.PhotoImage(train_model)

  
clear =Image.open("icons/clear.png")
clear = Resize_Image(clear,[button_width,button_height])
clear =ImageTk.PhotoImage(clear)



xclear=1100
clearButton = tk.Button(window, command=clear1  ,border=0 ,image =clear  ,bg="#515151"  , activebackground = "#515151")
clearButton.place(x=xclear, y=200)
clearButton2 = tk.Button(window, command=clear2 ,border=0 ,image =clear  ,bg="#515151"  , activebackground = "#515151")
clearButton2.place(x=xclear, y=300)    




center_x=(window.winfo_screenwidth()-button_width)/2
takeImg = tk.Button(window, command=TakeImages ,border=0 ,image =take_pics  ,bg="#515151"  , activebackground = "#515151" )
takeImg.place(x=center_x-400, y=500)

loadFolder = tk.Button(window, command=TakeImages_folder ,border=0 ,image =load_folder  ,bg="#515151"  , activebackground = "#515151" )
loadFolder.place(x=center_x-400, y=560)

trainImg = tk.Button(window, command=TrainImages  ,border=0,image= train_model ,bg="#515151"  , activebackground = "#515151" )
trainImg.place(x=center_x, y=525)
#print(window.winfo_screenwidth())
trackImg = tk.Button(window, command =TrackImages ,border=0,image= record_attendance ,bg="#515151"  , activebackground = "#515151")
trackImg.place(x=center_x+400, y=525)
# quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
# quitWindow.place(x=500, y=600)
# copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('Cambria', 30, 'italic bold underline'))
# copyWrite.tag_configure("superscript", offset=10)
# copyWrite.insert("insert", "UiTM Attendance System","", "TEAM", "superscript")
# copyWrite.configure(state="disabled",fg="red"  )
# copyWrite.pack(side="left")
# copyWrite.place(x=800, y=750)
 
window.mainloop()
