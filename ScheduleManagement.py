from tkinter import messagebox
import tkinter as tk
from tkinter import *
import pymysql as mariadb
# import datetime
from datetime import *


# Connection to Database
mariadb_connection = mariadb.connect(host = 'localhost', user='root', password='', database='ScheduleManagement')
#mariadb_connection = mariadb.connect(host = 'localhost', user='spaceman', password='', database='test')
myCursor = mariadb_connection.cursor()
print("Connection Established")

global scheduleMessage
scheduleMessage = "Clave | Secc | DiaSem | Hora | Minuto | Duracion | Periodo | Semestre | IDSalon |"
global labelHeaderMessage
labelHeaderMessage = " IDSalon | Capacidad | Tipo "
global reservationMessage
reservationMessage = "| IDSalon | Nombre | FechaHora | Duracion |"
global format
format = '%Y-%m-%d %H:%M:%S'

# Show all rooms Info

def allRoomsInfo(myCursor):
    query = "SELECT * FROM Salones"
    myCursor.execute(query)
    myResult = myCursor.fetchall() # Get all rows of the statement

    print(labelHeaderMessage)
    labelHeader = Label(frame, justify=CENTER, text=labelHeaderMessage, bg="#020202", foreground="green").pack(side=TOP)

    for rows in myResult:
        print(rows)
        allRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)

def showComputerRoom(myCursor):
    query = "SELECT * FROM Salones WHERE Tipo = 'SC'"
    myCursor.execute(query)
    myResult = myCursor.fetchall() # Get all rows of the statement

    print(labelHeaderMessage)
    allRoomsLabelHeader = Label(frame, justify=CENTER, text=labelHeaderMessage, bg="#020202", foreground="green").pack(side=TOP)

    for rows in myResult:
        print(rows)
        computersRoomLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)

def showAuditorium(myCursor):
    query = "SELECT * FROM Salones WHERE Tipo = 'A'"
    myCursor.execute(query)
    myResult = myCursor.fetchall() # Get all rows of the statement

    print(labelHeaderMessage)
    auditoriumLabelHeader = Label(frame, justify=CENTER, text=labelHeaderMessage, bg="#020202", foreground="green").pack(side=TOP)

    for rows in myResult:
        print(rows)
        auditoriumLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)


def roomID(myCursor):
    window = tk.Tk()
    window.title('Room ID')
    window.geometry('350x50')
    window.resizable(0, 0)
    myEntry = Entry(window, show=None, font=('Arial', 14),  justify=tk.CENTER)
    myEntry.focus()
    myEntry.pack()

    def getEntry():
        entry = myEntry.get()
        query = f"SELECT * FROM Salones WHERE IDSalon = '{entry}'"
        myCursor.execute(query)
        myResult = myCursor.fetchone()
        print(labelHeaderMessage)
        roomIDHeader = Label(frame, justify=CENTER, text=labelHeaderMessage, bg="#020202", foreground="green").pack(side=TOP)
        print(myResult)
        roomIDLabel = Label(frame, justify=CENTER, text=myResult, bg="#020202", foreground="green").pack(side=TOP)
        window.destroy()

    # Buttons
    giveRoomID = tk.Button(
        window, text="Ok", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
    giveRoomID.pack()


def smallRooms(myCursor):
        query = "SELECT * FROM Salones WHERE Capacidad BETWEEN 0 AND 20"
        myCursor.execute(query)
        myResult = myCursor.fetchall() # Get all rows of the statement

        print(labelHeaderMessage)
        smallRoomsLabelHeader = Label(frame, justify=CENTER, text=labelHeaderMessage, bg="#020202", foreground="green").pack(side=TOP)

        for rows in myResult:
            print(rows)
            smallRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)

def mediumRooms(myCursor):
        query = "SELECT * FROM Salones WHERE Capacidad BETWEEN 21 AND 35"
        myCursor.execute(query)
        myResult = myCursor.fetchall() # Get all rows of the statement

        print(labelHeaderMessage)
        mediumRoomsLabelHeader = Label(frame, justify=CENTER, text=labelHeaderMessage, bg="#020202", foreground="green").pack(side=TOP)

        for rows in myResult:
            print(rows)
            mediumRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)

def largeRooms(myCursor):
        query = "SELECT * FROM Salones WHERE Capacidad BETWEEN 36 AND 50"
        myCursor.execute(query)
        myResult = myCursor.fetchall() # Get all rows of the statement

        print(labelHeaderMessage)
        largeRoomsLabelHeader = Label(frame, justify=CENTER, text=labelHeaderMessage, bg="#020202", foreground="green").pack(side=TOP)

        for rows in myResult:
            print(rows)
            largeRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)


def showCompleteSchedule(myCursor):
    query = "SELECT * FROM Horario"
    myCursor.execute(query)
    myResult = myCursor.fetchall() # Get all rows of the statement

    print(scheduleMessage)
    scheduleLabelHeader = Label(frame, justify=CENTER, text=scheduleMessage, bg="#020202", foreground="green").pack(side=TOP)

    for rows in myResult:
        print(rows)
        largeRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)

def showScheduleByPeriodSpring(myCursor):
    query = "SELECT * FROM Horario WHERE Periodo = 'Primavera 2020'"
    myCursor.execute(query)
    myResult = myCursor.fetchall() # Get all rows of the statement

    print(scheduleMessage)
    scheduleLabelHeader = Label(frame, justify=CENTER, text=scheduleMessage, bg="#020202", foreground="green").pack(side=TOP)

    for rows in myResult:
        print(rows)
        largeRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)

def showScheduleByPeriodAutumn(myCursor):
    query = "SELECT * FROM Horario WHERE Periodo = 'Otoño 2020'"
    myCursor.execute(query)
    myResult = myCursor.fetchall() # Get all rows of the statement

    print(scheduleMessage)
    scheduleLabelHeader = Label(frame, justify=CENTER, text=scheduleMessage, bg="#020202", foreground="green").pack(side=TOP)

    for rows in myResult:
        print(rows)
        largeRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)

# Input Validation
def onlyNumbers(input):
    return input.isdigit()

def specifiPartialScheduleDay(myCursor):
        window = tk.Tk()
        window.title('Give me a Day')
        window.geometry('350x50')
        window.resizable(0, 0)
        messagebox.showinfo("Information", "Please enter from 1 to 7, Being 1 on Monday")
        validation = window.register(onlyNumbers)
        myEntry = Entry(window, show=None, font=('Arial', 14),  justify=tk.CENTER)
        myEntry.config(validate="key", validatecommand=(validation, '%P'))
        myEntry.pack()
        myEntry.focus()


        def getEntry():
            entry = int(myEntry.get())
            # intEntry = int(entry)
            query = f"SELECT * FROM Horario WHERE DIASEM = '{entry}'"
            myCursor.execute(query)
            myResult = myCursor.fetchall()
            print(scheduleMessage)
            specifiPartialScheduleDayHeader = Label(frame, justify=CENTER, text=scheduleMessage, bg="#020202", foreground="green").pack(side=TOP)
            for rows in myResult:
                print(rows)
                specifiPartialScheduleDayLabel = Label(frame, justify=CENTER, text=myResult, bg="#020202", foreground="green").pack(side=TOP)
            window.destroy()

        # Buttons
        actionButton = tk.Button(
            window, text="Ok", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
        actionButton.pack()

def specifiPartialScheduleHour(myCursor):
        window = tk.Tk()
        window.title('Give me an Hour')
        window.geometry('350x50')
        window.resizable(0, 0)
        messagebox.showinfo("Information", "Please enter from 0 to 23")
        validation = window.register(onlyNumbers)
        myEntry = Entry(window, show=None, font=('Arial', 14),  justify=tk.CENTER)
        myEntry.config(validate="key", validatecommand=(validation, '%P'))
        myEntry.pack()
        myEntry.focus()


        def getEntry():
            entry = int(myEntry.get())
            # intEntry = int(entry)
            query = f"SELECT * FROM Horario WHERE Hora = '{entry}'"
            myCursor.execute(query)
            myResult = myCursor.fetchall()
            print(scheduleMessage)
            specifiPartialScheduleHourHeader = Label(frame, justify=CENTER, text=scheduleMessage, bg="#020202", foreground="green").pack(side=TOP)
            for rows in myResult:
                print(rows)
                specifiPartialScheduleHourLabel = Label(frame, justify=CENTER, text=myResult, bg="#020202", foreground="green").pack(side=TOP)
            window.destroy()

        # Buttons
        actionButton = tk.Button(
            window, text="Ok", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
        actionButton.pack()

def specifiPartialScheduleRoomID(myCursor):
        window = tk.Tk()
        window.title('Room ID')
        window.geometry('350x50')
        window.resizable(0, 0)
        myEntry = Entry(window, show=None, font=('Arial', 14),  justify=tk.CENTER)
        myEntry.focus()
        myEntry.pack()

        def getEntry():
            entry = myEntry.get()
            query = f"SELECT * FROM Horario WHERE IDSalon = '{entry}'"
            myCursor.execute(query)
            myResult = myCursor.fetchall()
            print(scheduleMessage)
            specifiPartialScheduleRoomIDHeader = Label(frame, justify=CENTER, text=scheduleMessage, bg="#020202", foreground="green").pack(side=TOP)
            for rows in myResult:
                print(rows)
                specifiPartialScheduleRoomIDLabel = Label(frame, justify=CENTER, text=myResult, bg="#020202", foreground="green").pack(side=TOP)
            window.destroy()

        # Buttons
        actionButton = tk.Button(
            window, text="Ok", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
        actionButton.pack()

def specifiPartialScheduleKey(myCursor):
        window = tk.Tk()
        window.title('Schedule Key')
        window.geometry('350x50')
        window.resizable(0, 0)
        myEntry = Entry(window, show=None, font=('Arial', 14),  justify=tk.CENTER)
        myEntry.focus()
        myEntry.pack()

        def getEntry():
            entry = myEntry.get()
            query = f"SELECT * FROM Horario WHERE Clave = '{entry}'"
            myCursor.execute(query)
            myResult = myCursor.fetchall()
            print(scheduleMessage)
            specifiPartialScheduleKeyHeader = Label(frame, justify=CENTER, text=scheduleMessage, bg="#020202", foreground="green").pack(side=TOP)
            for rows in myResult:
                print(rows)
                specifiPartialScheduleKeyLabel = Label(frame, justify=CENTER, text=myResult, bg="#020202", foreground="green").pack(side=TOP)
            window.destroy()

        # Buttons
        actionButton = tk.Button(
            window, text="Ok", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
        actionButton.pack()

def addSchedule(myCursor):
    window = tk.Tk()
    window.title('Add Schedule')
    window.resizable(0, 0)
    tk.Label(window, text="Clave").grid(row=0)
    tk.Label(window, text="Secc").grid(row=1)
    tk.Label(window, text="DIASEM").grid(row=2)
    tk.Label(window, text="Hora").grid(row=3)
    tk.Label(window, text="Minuto").grid(row=4)
    tk.Label(window, text="Duración").grid(row=5)
    tk.Label(window, text="Periodo").grid(row=6)
    tk.Label(window, text="Semestre").grid(row=7)
    tk.Label(window, text="IDSalon").grid(row=8)

    # For Key Course
    keysVar = StringVar(window)

    keysQuery = "SELECT DISTINCT Clave FROM Cursos"
    myCursor.execute(keysQuery)
    myResult = myCursor.fetchall()

    keys = []

    for row in myResult:
        print(row)
        keys.append(row)

    keysVar.set(row[0]) # set the default option

    keySelection = OptionMenu(window, keysVar, *keys)

    # For Secction
    seccVar = StringVar(window)

    seccQuery = "SELECT DISTINCT Secc FROM Cursos"
    myCursor.execute(seccQuery)
    myResult = myCursor.fetchall()

    secctions = []

    for row in myResult:
        print(row)
        secctions.append(row)

    seccVar.set(row[0]) # set the default option

    seccSelection = OptionMenu(window, seccVar, *secctions)

    # For Period
    periodVar = StringVar(window)

    periodQuery = "SELECT Titulo FROM Periodos"
    myCursor.execute(periodQuery)
    myResult = myCursor.fetchall()

    periods = []

    for row in myResult:
        print(row)
        periods.append(row)

    periodVar.set(row[0]) # set the default option

    periodSelection = OptionMenu(window, periodVar, *periods)

    entry3 = tk.Entry(window)
    entry4 = tk.Entry(window)
    entry5 = tk.Entry(window)
    entry6 = tk.Entry(window)
    entry8 = tk.Entry(window)
    entry9 = tk.Entry(window)

    keySelection.grid(row = 0, column = 1)
    seccSelection.grid(row = 1, column = 1)
    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)
    entry5.grid(row=4, column=1)
    entry6.grid(row=5, column=1)
    periodSelection.grid(row = 6, column = 1)
    entry8.grid(row=7, column=1)
    entry9.grid(row=8, column=1)

    def getEntry():

        savedFullEntries = []

        savedFullEntries.append(str(keysVar.get()).strip("(),'"))
        savedFullEntries.append(int(str(seccVar.get().strip("(),'"))))
        savedFullEntries.append(int(str(entry3.get()).strip("(),'")))
        savedFullEntries.append(int(str(entry4.get()).strip("(),'")))
        savedFullEntries.append(int(str(entry5.get()).strip("(),'")))
        savedFullEntries.append(int(str(entry6.get()).strip("(),'")))
        savedFullEntries.append(str(periodVar.get().strip("(),'")))
        savedFullEntries.append(int(str(entry8.get()).strip("(),'")))
        savedFullEntries.append(str(entry9.get()).strip("(),'"))

        print(savedFullEntries)

        # There was an f here

        query = "INSERT INTO Horario (Clave, Secc, DIASEM, Hora, Minuto, Duracion, Periodo, Semestre, IDSalon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        myCursor.execute(query, tuple(savedFullEntries))
        print(scheduleMessage)
        messageBoxConfirmation = messagebox.askyesno("Title","Do you want to save?")
        if messageBoxConfirmation == True:
            mariadb_connection.commit()
            showCompleteSchedule(myCursor)
        else:
            pass

        window.destroy()

    # Buttons
    actionButton = tk.Button(
        window, text="Send", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
    actionButton.grid(column=15)


def deleteSchedule(myCursor):
    window = tk.Tk()
    window.title('Delete Schedule')
    window.resizable(0, 0)
    tk.Label(window, text="Clave").grid(row=0)

    # For Key Course
    keysVar = StringVar(window)

    keysQuery = "SELECT DISTINCT Clave FROM Cursos"
    myCursor.execute(keysQuery)
    myResult = myCursor.fetchall()

    keys = []

    for row in myResult:
        print(row)
        keys.append(row)

    keysVar.set(row[0]) # set the default option

    keySelection = OptionMenu(window, keysVar, *keys)


    keySelection.grid(row = 0, column =1)


    def getEntry():

        keyToDelete = str(keysVar.get().strip("(),'"))

        print(keyToDelete)
        query = f"DELETE FROM Horario WHERE Clave = '{keyToDelete}'"
        myCursor.execute(query)
        messageBoxConfirmation = messagebox.askyesno("Title","Do you want to delete this record?")
        if messageBoxConfirmation == True:
            mariadb_connection.commit()
            showCompleteSchedule(myCursor)
        else:
            pass

        window.destroy()

    # Buttons
    actionButton = tk.Button(
        window, text="Send", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
    actionButton.grid(column=15)


def modSchedule(myCursor):
    window = tk.Tk()
    window.title('Modify Schedule')
    window.resizable(0, 0)
    tk.Label(window, text="Clave").grid(row=0)
    tk.Label(window, text="Secc").grid(row=1)
    tk.Label(window, text="DIASEM").grid(row=2)
    tk.Label(window, text="Hora").grid(row=3)
    tk.Label(window, text="Minuto").grid(row=4)
    tk.Label(window, text="Duración").grid(row=5)
    tk.Label(window, text="Periodo").grid(row=6)
    tk.Label(window, text="Semestre").grid(row=7)
    tk.Label(window, text="IDSalon").grid(row=8)

    # For Key Course
    keysVar = StringVar(window)

    keysQuery = "SELECT DISTINCT Clave FROM Cursos"
    myCursor.execute(keysQuery)
    myResult = myCursor.fetchall()

    keys = []

    for row in myResult:
        print(row)
        keys.append(row)

    keysVar.set(row[0]) # set the default option

    keySelection = OptionMenu(window, keysVar, *keys)

    # For Secction
    seccVar = StringVar(window)

    seccQuery = "SELECT DISTINCT Secc FROM Cursos"
    myCursor.execute(seccQuery)
    myResult = myCursor.fetchall()

    secctions = []

    for row in myResult:
        print(row)
        secctions.append(row)

    seccVar.set(row[0]) # set the default option

    seccSelection = OptionMenu(window, seccVar, *secctions)

    # For Period
    periodVar = StringVar(window)

    periodQuery = "SELECT Titulo FROM Periodos"
    myCursor.execute(periodQuery)
    myResult = myCursor.fetchall()

    periods = []

    for row in myResult:
        print(row)
        periods.append(row)

    periodVar.set(row[0]) # set the default option

    periodSelection = OptionMenu(window, periodVar, *periods)


    entry3 = tk.Entry(window)
    entry4 = tk.Entry(window)
    entry5 = tk.Entry(window)
    entry6 = tk.Entry(window)
    entry8 = tk.Entry(window)
    entry9 = tk.Entry(window)

    keySelection.grid(row = 0, column = 1)
    seccSelection.grid(row = 1, column = 1)
    periodSelection.grid(row = 6, column = 1)
    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)
    entry5.grid(row=4, column=1)
    entry6.grid(row=5, column=1)
    entry8.grid(row=7, column=1)
    entry9.grid(row=8, column=1)

    def getEntry():

        savedFullEntries = []

        savedFullEntries.append(int(str(entry3.get()).strip("(),'")))
        savedFullEntries.append(int(str(entry4.get()).strip("(),'")))
        savedFullEntries.append(int(str(entry5.get()).strip("(),'")))
        savedFullEntries.append(int(str(entry6.get()).strip("(),'")))
        savedFullEntries.append(str(periodVar.get().strip("(),'")))
        savedFullEntries.append(int(str(entry8.get()).strip("(),'")))
        savedFullEntries.append(str(entry9.get()).strip("(),'"))
        savedFullEntries.append(str(keysVar.get()).strip("(),'"))
        savedFullEntries.append(int(str(seccVar.get().strip("(),'"))))

        print(savedFullEntries)

        query = "UPDATE Horario SET DIASEM =%s, Hora=%s, Minuto =%s, Duracion =%s, Periodo =%s, Semestre =%s, IDSalon =%s WHERE Clave =%s AND Secc =%s"
        myCursor.execute(query, tuple(savedFullEntries))
        print(scheduleMessage)
        messageBoxConfirmation = messagebox.askyesno("Title","Do you want to save the changes?")
        if messageBoxConfirmation == True:
            mariadb_connection.commit()
            showCompleteSchedule(myCursor)
        else:
            pass

        window.destroy()

    # Buttons
    actionButton = tk.Button(
        window, text="Send", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
    actionButton.grid(column=15)


def makeReservation(myCursor):
    window = tk.Tk()
    window.title('Make a Reservation')
    window.resizable(0, 0)
    tk.Label(window, text="IDSalon").grid(row=0)
    tk.Label(window, text="Nombre").grid(row=1)
    tk.Label(window, text="Dia").grid(row=2)
    tk.Label(window, text="Mes").grid(row=3)
    tk.Label(window, text="Hora").grid(row=4)
    tk.Label(window, text="Minuto").grid(row=5)
    tk.Label(window, text="Duración").grid(row=6)

    entryNombre = tk.Entry(window)
    entryDuracion = tk.Entry(window)

    # Get Date Range
    def daterange(firstDate, endDate):
        for n in range(int ((endDate - firstDate).days)):
            yield firstDate + timedelta(n)

    # For IDRoom
    idRoomVar = StringVar(window)

    roomsQuery = "SELECT DISTINCT IDSalon FROM Salones"
    myCursor.execute(roomsQuery)
    myResult = myCursor.fetchall()

    rooms = []

    for row in myResult:
        print(row)
        rooms.append(row)
    idRoomVar.set(row[0]) # set the default option

    idRoomSelection = OptionMenu(window, idRoomVar, *rooms)

    # For Day
    dayVar = StringVar(window)
    days = []

    for i in range(1, 31):
        days.append(i)

    dayVar.set(days[0]) # set the default option
    daySelection = OptionMenu(window, dayVar, *days)

    # For Month
    monthVar = StringVar(window)
    months = [1,2,3,4,5,8,9,10,11,12]

    monthVar.set(months[0]) # set the default option
    monthsSelection = OptionMenu(window, monthVar, *months)

    # For Hours
    hourVar = StringVar(window)
    hours = []

    for i in range(0, 24):
        hours.append(i)

    hourVar.set(hours[0]) # set the default option
    hoursSelection = OptionMenu(window, hourVar, *hours)

    # For Minutes
    minutesVar = StringVar(window)
    minutes = [0, 10, 15, 30, 45]

    minutesVar.set(minutes[0]) # set the default option
    minutesSelection = OptionMenu(window, minutesVar, *minutes)

    allDates = []

    # Get First Date
    firstDateQuery = "SELECT Fechaini FROM Periodos WHERE Titulo = 'Primavera 2020'"
    myCursor.execute(firstDateQuery)
    firstDate = myCursor.fetchone()
    dateString = ''.join(str(e) for e in firstDate)
    print(dateString)
    newdateString = datetime.strptime(dateString, format)
    print(newdateString)


    # Get End Date
    endDateQuery = "SELECT Fechafin FROM Periodos WHERE Titulo = 'Primavera 2020'"
    myCursor.execute(endDateQuery)
    endDate = myCursor.fetchone()
    dateString = ''.join(str(e) for e in endDate)
    newEndDatetring = datetime.strptime(dateString, format)
    print(newEndDatetring)

    for single_date in daterange(newdateString, newEndDatetring):
        allDates.append(single_date.strftime("%Y-%m-%d %H:%M:%S"))

    print(len(allDates))


    idRoomSelection.grid(row = 0, column =1)
    entryNombre.grid(row=1, column=1)
    daySelection.grid(row = 2, column = 1)
    monthsSelection.grid(row = 3, column = 1)
    hoursSelection.grid(row = 4, column = 1)
    minutesSelection.grid(row = 5, column = 1)
    entryDuracion.grid(row=6, column=1)

    def getEntry():

        savedFullEntries = []
        dateTime = [2020]
        dateTimeSpecific = []

        # First Data

        savedFullEntries.append(str(idRoomVar.get()).strip("(),'"))
        savedFullEntries.append(str(entryNombre.get()).strip("(),'"))

        # Date

        dateTime.append(int(str(monthVar.get().strip("(),'"))))
        dateTime.append(int(str(dayVar.get().strip("(),'"))))

        # Time

        dateTimeSpecific.append(int(str(hourVar.get().strip("(),'"))))
        dateTimeSpecific.append(int(str(minutesVar.get().strip("(),'"))))
        dateTimeSpecific.append(00)

        # Join Date + Time

        dateTimeString = '-'.join(str(e) for e in dateTime)
        dateTimeSpecificString = ':'.join(str(e) for e in dateTimeSpecific)
        finalDateTimeString = dateTimeString + " " + dateTimeSpecificString

        print(finalDateTimeString)

        actualDate = datetime.strptime(finalDateTimeString, format)
        print(actualDate)

        savedFullEntries.append(actualDate)
        savedFullEntries.append(int(str(entryDuracion.get()).strip("(),'")))

        print(savedFullEntries)


        daysAdded = timedelta(7)
        finalDate = actualDate + daysAdded

        for i in range(len(allDates)):
            savedFullEntries[2] = finalDate
            finalDate += daysAdded
            print(savedFullEntries)
            query = "INSERT INTO Reservaciones (IDSalon, Nombre, FechaHora, Duracion) VALUES (%s, %s, %s, %s)"
            myCursor.execute(query, tuple(savedFullEntries))
            print(scheduleMessage)

        messageBoxConfirmation = messagebox.askyesno("Title","Do you want add this record?")
        if messageBoxConfirmation == True:
            mariadb_connection.commit()
            query = "SELECT * From Reservaciones"
            myCursor.execute(query)
            myResult = myCursor.fetchall() # Get all rows of the statement

            print(reservationMessage)
            labelHeader = Label(frame, justify=CENTER, text=reservationMessage, bg="#020202", foreground="green").pack(side=TOP)

            for rows in myResult:
                print(rows)
                allRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)
        else:
            pass

        window.destroy()

    # Buttons
    actionButton = tk.Button(
        window, text="Send", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
    actionButton.grid(column=15)


def deleteReservation(myCursor):
        window = tk.Tk()
        window.title('Delete a Reservation')
        window.resizable(0, 0)
        tk.Label(window, text="IDSalon").grid(row=0)
        tk.Label(window, text="Dia").grid(row=1)
        tk.Label(window, text="Mes").grid(row=2)
        tk.Label(window, text="Hora").grid(row=3)
        tk.Label(window, text="Minuto").grid(row=4)

        # For IDRoom
        idRoomVar = StringVar(window)

        roomsQuery = "SELECT DISTINCT IDSalon FROM Salones"
        myCursor.execute(roomsQuery)
        myResult = myCursor.fetchall()

        rooms = []

        for row in myResult:
            print(row)
            rooms.append(row)
        idRoomVar.set(row[0]) # set the default option

        idRoomSelection = OptionMenu(window, idRoomVar, *rooms)

        # For Day
        dayVar = StringVar(window)
        days = []

        for i in range(1, 31):
            days.append(i)

        dayVar.set(days[0]) # set the default option
        daySelection = OptionMenu(window, dayVar, *days)

        # For Month
        monthVar = StringVar(window)
        months = [1,2,3,4,5,8,9,10,11,12]

        monthVar.set(months[0]) # set the default option
        monthsSelection = OptionMenu(window, monthVar, *months)

        # For Hours
        hourVar = StringVar(window)
        hours = []

        for i in range(0, 24):
            hours.append(i)

        hourVar.set(hours[0]) # set the default option
        hoursSelection = OptionMenu(window, hourVar, *hours)

        # For Minutes
        minutesVar = StringVar(window)
        minutes = [0, 10, 15, 30, 45]

        minutesVar.set(minutes[0]) # set the default option
        minutesSelection = OptionMenu(window, minutesVar, *minutes)

        idRoomSelection.grid(row = 0, column =1)
        daySelection.grid(row = 1, column = 1)
        monthsSelection.grid(row = 2, column = 1)
        hoursSelection.grid(row = 3, column = 1)
        minutesSelection.grid(row = 4, column = 1)

        def getEntry():

            dateTime = [2020]
            dateTimeSpecific = []

            # First Data

            idRoomObtained = str(idRoomVar.get()).strip("(),'")

            # Date

            dateTime.append(int(str(monthVar.get().strip("(),'"))))
            dateTime.append(int(str(dayVar.get().strip("(),'"))))

            # Time

            dateTimeSpecific.append(int(str(hourVar.get().strip("(),'"))))
            dateTimeSpecific.append(int(str(minutesVar.get().strip("(),'"))))
            dateTimeSpecific.append(00)

            # Join Date + Time

            dateTimeString = '-'.join(str(e) for e in dateTime)
            dateTimeSpecificString = ':'.join(str(e) for e in dateTimeSpecific)
            finalDateTimeString = dateTimeString + " " + dateTimeSpecificString

            print(finalDateTimeString)

            actualDate = datetime.strptime(finalDateTimeString, format)
            print(actualDate)

            query = f"DELETE FROM Reservaciones WHERE FechaHora = '{actualDate}' AND IDSalon = '{idRoomObtained}'"
            myCursor.execute(query)
            print(scheduleMessage)

            messageBoxConfirmation = messagebox.askyesno("Title","Do you want to delete this record?")
            if messageBoxConfirmation == True:
                mariadb_connection.commit()

                # Actual Reservations

                query = "SELECT * From Reservaciones"
                myCursor.execute(query)
                myResult = myCursor.fetchall() # Get all rows of the statement

                print(reservationMessage)
                labelHeader = Label(frame, justify=CENTER, text=reservationMessage, bg="#020202", foreground="green").pack(side=TOP)

                for rows in myResult:
                    print(rows)
                    allRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)
            else:
                pass

            window.destroy()

        # Buttons
        actionButton = tk.Button(
            window, text="Send", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
        actionButton.grid(column=15)

def deleteReservationByRange(myCursor):
            window = tk.Tk()
            window.title('Delete a Reservation')
            window.resizable(0, 0)
            tk.Label(window, text="IDSalon").grid(row=0)
            tk.Label(window, text="Fecha Inicial").grid(row=1)
            tk.Label(window, text="Dia").grid(row=2)
            tk.Label(window, text="Mes").grid(row=3)
            tk.Label(window, text="Hora").grid(row=4)
            tk.Label(window, text="Minuto").grid(row=5)

            # For IDRoom
            idRoomVar = StringVar(window)

            roomsQuery = "SELECT DISTINCT IDSalon FROM Salones"
            myCursor.execute(roomsQuery)
            myResult = myCursor.fetchall()

            rooms = []

            for row in myResult:
                print(row)
                rooms.append(row)
            idRoomVar.set(row[0]) # set the default option

            idRoomSelection = OptionMenu(window, idRoomVar, *rooms)

            # For Day
            dayVar = StringVar(window)
            days = []

            for i in range(1, 31):
                days.append(i)

            dayVar.set(days[0]) # set the default option
            daySelection = OptionMenu(window, dayVar, *days)

            # For Month
            monthVar = StringVar(window)
            months = [1,2,3,4,5,8,9,10,11,12]

            monthVar.set(months[0]) # set the default option
            monthsSelection = OptionMenu(window, monthVar, *months)

            # For Hours
            hourVar = StringVar(window)
            hours = []

            for i in range(0, 24):
                hours.append(i)

            hourVar.set(hours[0]) # set the default option
            hoursSelection = OptionMenu(window, hourVar, *hours)

            # For Minutes
            minutesVar = StringVar(window)
            minutes = [0, 10, 15, 30, 45]

            minutesVar.set(minutes[0]) # set the default option
            minutesSelection = OptionMenu(window, minutesVar, *minutes)

            # For Day 2
            day2Var = StringVar(window)
            days2 = []

            for i in range(1, 31):
                days2.append(i)

            day2Var.set(days2[0]) # set the default option
            day2Selection = OptionMenu(window, day2Var, *days2)

            # For Month 2
            month2Var = StringVar(window)
            months2 = [1,2,3,4,5,8,9,10,11,12]

            month2Var.set(months2[0]) # set the default option
            months2Selection = OptionMenu(window, month2Var, *months2)

            # For Hours 2
            hour2Var = StringVar(window)
            hours2 = []

            for i in range(0, 24):
                hours2.append(i)

            hour2Var.set(hours2[0]) # set the default option
            hours2Selection = OptionMenu(window, hour2Var, *hours2)

            # For Minutes 2
            minutes2Var = StringVar(window)
            minutes2 = [0, 10, 15, 30, 45]

            minutes2Var.set(minutes2[0]) # set the default option
            minutes2Selection = OptionMenu(window, minutes2Var, *minutes2)



            idRoomSelection.grid(row = 0, column =1)

            # First Date

            daySelection.grid(row = 2, column = 1)
            monthsSelection.grid(row = 3, column = 1)
            hoursSelection.grid(row = 4, column = 1)
            minutesSelection.grid(row = 5, column = 1)

            # End Date

            day2Selection.grid(row = 2, column = 8)
            months2Selection.grid(row = 3, column = 8)
            hours2Selection.grid(row = 4, column = 8)
            minutes2Selection.grid(row = 5, column = 8)



            def getEntry():

                dateTime = [2020]
                dateTimeSpecific = []

                # First Data

                idRoomObtained = str(idRoomVar.get()).strip("(),'")

                # Date

                dateTime.append(int(str(monthVar.get().strip("(),'"))))
                dateTime.append(int(str(dayVar.get().strip("(),'"))))

                # Time

                dateTimeSpecific.append(int(str(hourVar.get().strip("(),'"))))
                dateTimeSpecific.append(int(str(minutesVar.get().strip("(),'"))))
                dateTimeSpecific.append(00)

                # Join Date + Time

                dateTimeString = '-'.join(str(e) for e in dateTime)
                dateTimeSpecificString = ':'.join(str(e) for e in dateTimeSpecific)
                finalDateTimeString = dateTimeString + " " + dateTimeSpecificString

                print(finalDateTimeString)

                actualDate = datetime.strptime(finalDateTimeString, format)
                print(actualDate)

                dateTime2 = [2020]
                dateTimeSpecific2 = []

                # Date 2

                dateTime2.append(int(str(month2Var.get().strip("(),'"))))
                dateTime2.append(int(str(day2Var.get().strip("(),'"))))

                # Time 2

                dateTimeSpecific2.append(int(str(hour2Var.get().strip("(),'"))))
                dateTimeSpecific2.append(int(str(minutes2Var.get().strip("(),'"))))
                dateTimeSpecific2.append(00)

                # Join Date + Time 2

                dateTimeString2 = '-'.join(str(e) for e in dateTime2)
                dateTimeSpecificString2 = ':'.join(str(e) for e in dateTimeSpecific2)
                finalDateTimeString2 = dateTimeString2 + " " + dateTimeSpecificString2

                print(finalDateTimeString2)

                actualDate2 = datetime.strptime(finalDateTimeString2, format)
                print(actualDate2)

                query = f"DELETE FROM Reservaciones WHERE FechaHora BETWEEN '{actualDate}' AND '{actualDate2}'  AND IDSalon = '{idRoomObtained}'"
                myCursor.execute(query)
                print(scheduleMessage)

                messageBoxConfirmation = messagebox.askyesno("Title","Do you want to delete this record?")
                if messageBoxConfirmation == True:
                    mariadb_connection.commit()

                    # Actual Reservations

                    query = "SELECT * From Reservaciones"
                    myCursor.execute(query)
                    myResult = myCursor.fetchall() # Get all rows of the statement

                    print(reservationMessage)
                    labelHeader = Label(frame, justify=CENTER, text=reservationMessage, bg="#020202", foreground="green").pack(side=TOP)

                    for rows in myResult:
                        print(rows)
                        allRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)
                else:
                    pass

                window.destroy()

            # Buttons
            actionButton = tk.Button(
                window, text="Send", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
            actionButton.grid(column=15)



def seeRoomReservation(myCursor):
        window = tk.Tk()
        window.title('Look Reservation')
        window.resizable(0, 0)
        tk.Label(window, text="IDSalon").grid(row=0)

        # For IDRoom
        idRoomVar = StringVar(window)

        roomsQuery = "SELECT DISTINCT IDSalon FROM Salones"
        myCursor.execute(roomsQuery)
        myResult = myCursor.fetchall()

        rooms = []

        for row in myResult:
            print(row)
            rooms.append(row)
        idRoomVar.set(row[0]) # set the default option

        idRoomSelection = OptionMenu(window, idRoomVar, *rooms)
        idRoomSelection.grid(row = 0, column =1)

        def getEntry():

            # First Data
            entry = str(idRoomVar.get()).strip("(),'")
            query = f"SELECT * FROM Reservaciones WHERE IDSalon = '{entry}' "
            myCursor.execute(query)
            myResult = myCursor.fetchall()
            print(myResult)
            labelHeader = Label(frame, justify=CENTER, text=reservationMessage, bg="#020202", foreground="green").pack(side=TOP)

            for rows in myResult:
                print(rows)
                allRoomsLabel = Label(frame, justify=CENTER, text=rows, bg="#020202", foreground="green").pack(side=TOP)

            window.destroy()

        # Buttons
        actionButton = tk.Button(
            window, text="Send", padx=10, pady=5, fg="white", bg="#263D42", command=getEntry)
        actionButton.grid(column=15)


root = tk.Tk()

# Custom Size
canvas = tk.Canvas(root, height=1000, width=1000, bg="#000000")
canvas.pack()

# Frame inside root
frame = LabelFrame(root, text="Main", bg="#020202", foreground="green")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

root.title('Schedule Manager')
root.geometry("1000x1000")
root.resizable(0, 0)

# Main Menu
menubar = Menu(root)
showRooms = Menu(menubar, tearoff=0)
showRooms.add_command(label="Show all Rooms", command=lambda: allRoomsInfo(myCursor))
menubar.add_cascade(label="Rooms", menu=showRooms)

subRoomsMenu = Menu(showRooms)
showRooms.add_cascade(label="Search for a Room/Rooms", menu=subRoomsMenu)

subRoomsCapacity = Menu(subRoomsMenu)
subRoomsCapacity.add_command(label="Small", command=lambda: smallRooms(myCursor))
subRoomsCapacity.add_command(label="Medium", command=lambda: mediumRooms(myCursor))
subRoomsCapacity.add_command(label="Large", command=lambda: largeRooms(myCursor))
subRoomsMenu.add_cascade(label="Room Capacity", menu=subRoomsCapacity)

subRoomsMenuType = Menu(subRoomsMenu)
subRoomsMenuType.add_command(label="Auditoriums", command=lambda: showAuditorium(myCursor))
subRoomsMenuType.add_command(label="Computer Rooms", command=lambda: showComputerRoom(myCursor))
subRoomsMenuType.add_command(label="Room ID", command=lambda: roomID(myCursor))
subRoomsMenu.add_cascade(label="Room Type/Room ID", menu=subRoomsMenuType)

reservation = Menu(menubar, tearoff=0)
reservation.add_command(label="Search Reservation By Room", command=lambda: seeRoomReservation(myCursor))
reservation.add_command(label="Make a reservation", command=lambda: makeReservation(myCursor))

# Delete Reservation
delReservation = Menu(reservation)
delReservation.add_command(label="By Range", command=lambda: deleteReservationByRange(myCursor))
delReservation.add_command(label="By Specific Date", command=lambda: deleteReservation(myCursor))
reservation.add_cascade(label="Remove Reservation", menu=delReservation )
menubar.add_cascade(label="Room Reservation", menu=reservation)

schedule = Menu(menubar, tearoff=0)
schedule.add_command(label="Show Complete Schedule", command=lambda: showCompleteSchedule(myCursor))

# Partial Schedule
partialSchedule = Menu(schedule)
partialSchedule.add_command(label="Spring", command=lambda: showScheduleByPeriodSpring(myCursor))
partialSchedule.add_command(label="Autumn", command=lambda: showScheduleByPeriodAutumn(myCursor))
schedule.add_cascade(label="Show Schedule By Period", menu=partialSchedule )

specifiPartialSchedule = Menu(schedule)
specifiPartialSchedule.add_command(label="By Day", command=lambda: specifiPartialScheduleDay(myCursor))
specifiPartialSchedule.add_command(label="By Hour", command=lambda: specifiPartialScheduleHour(myCursor))
specifiPartialSchedule.add_command(label="By Room ID", command=lambda: specifiPartialScheduleRoomID(myCursor))
specifiPartialSchedule.add_command(label="By Key", command=lambda: specifiPartialScheduleKey(myCursor))
schedule.add_cascade(label="Show Schedule By Specific Characteristic", menu=specifiPartialSchedule )

schedule.add_command(label="Add Schedule", command=lambda: addSchedule(myCursor))
schedule.add_command(label="Modify Schedule", command=lambda: modSchedule(myCursor))
schedule.add_command(label="Remove Schedule", command=lambda: deleteSchedule(myCursor))
menubar.add_cascade(label="Schedule", menu=schedule)

systemOptions = Menu(menubar, tearoff=0)
systemOptions.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="System Options", menu=systemOptions)

root.config(menu=menubar)
root.mainloop()
