from tkinter import *
from tkinter import ttk, StringVar
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime



class LibraryManagementSystem:

    def __init__(self, root):
        self.root=root
        self.root.geometry("1366x750+0+0")
        self.root.title("Library managemnt system")

        #================================Variable==============================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrow_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturn_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()




        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="Powder Blue",fg="red",bd=20, relief =RIDGE,font=("times new roman", 40, "bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=10,relief=RIDGE,padx=20,bg="Powder Blue")
        frame.place(x=0,y=108,width=1363,height=384)
        #===============================Data Frame Left==============================
        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBERSHIP INFORMATION",bg="Powder Blue",fg="red",bd=10, relief =RIDGE,font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0,y=5,width=825,height=340)

        lblMember=Label(DataFrameLeft,text="Member Type",bg="Powder Blue",font=("arial", 12, "bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial", 10, "bold"),width=29,state="readonly")
        comMember["value"]=("Admin Staf", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_No=Label(DataFrameLeft, text="PRN No:", bg="Powder Blue", font=("arial", 12, "bold"), padx=2)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial", 13, "bold"), textvariable=self.prn_var, width=29)
        txtPRN_No.grid(row=1, column=1,)

        lblTitle=Label(DataFrameLeft,font=("arial",12, "bold"),text="ID No:", padx=2, pady=6, bg="Powder Blue")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.id_var, width=29)
        txtTitle.grid(row=2, column=1, )

        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Firstname:", padx=2,pady=6,bg="Powder Blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1, )

        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lastname:", padx=2,pady=6,bg="Powder Blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lastname_var ,width=29)
        txtLastName.grid(row=4, column=1, )

        lblAdd1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address1:", padx=2,pady=6,bg="Powder Blue")
        lblAdd1.grid(row=5, column=0, sticky=W)
        txtAdd1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address1_var , width=29)
        txtAdd1.grid(row=5, column=1,)

        lblAdd2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address2:", padx=2,pady=6,bg="Powder Blue")
        lblAdd2.grid(row=6, column=0, sticky=W)
        txtAdd2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address2_var, width=29)
        txtAdd2.grid(row=6, column=1, )

        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PostCode:", padx=2, pady=6, bg="Powder Blue")
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7, column=1, )

        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=6, bg="Powder Blue")
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1, )

        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="BookId:", padx=2, pady=6, bg="Powder Blue")
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.bookid_var, width=29)
        txtBookId.grid(row=0, column=3, )

        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="BookTitle:", padx=2, pady=6, bg="Powder Blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1, column=3, )

        lblAuther = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Auther Name:", padx=2, pady=6, bg="Powder Blue")
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.author_var, width=29)
        txtAuther.grid(row=2, column=3, )

        lblDateBorrowed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=6, bg="Powder Blue")
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dateborrow_var, width=29)
        txtDateBorrowed.grid(row=3, column=3, )

        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=6, bg="Powder Blue")
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.datedue_var , width=29)
        txtDateDue.grid(row=4, column=3, )

        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days On Book:", padx=2, pady=6, bg="Powder Blue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.daysonbook_var, width=29)
        txtDaysOnBook.grid(row=5, column=3, )

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=6, bg="Powder Blue")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.latereturn_var, width=29)
        txtLateReturnFine.grid(row=6, column=3, )

        lblDateOverdate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=6, bg="Powder Blue")
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateoverdue_var, width=29)
        txtDateOverdate.grid(row=7, column=3, )

        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=6, bg="Powder Blue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.finalprice_var, width=29)
        txtActualPrice.grid(row=8, column=3, )

        # ===============================Data Frame Right==============================
        DataFrameRight=LabelFrame(frame, text="BOOK DETAILS", bg="Powder Blue", fg="red", bd=10, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=830,y=5,width=470,height=340)
        
        self.txtBox = Text(DataFrameRight, font=("open sans", 11, "bold"), width=29, height=16, padx=4, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks = ['Head Firt Book', 'Learn Python The Hard', 'Python Programming', "Eloquent JavaScript",
                    'Python CookBook', 'Machine learning ', 'Machine tecnology', 'My Python', 'Joss Ellif guru', 'Grokking Algorithms',
                    'Fluent Python', 'Machine python', 'Advance Python', 'Inton Python', 'RedChilli Python',
                    'Ishq Python','Introduction to DSA','The C++ Programme', 'Java Good Code'
                                    ]
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head Firt Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("python manual")
                self.author_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")

            elif(x == "Learn Python The Hard"):
                self.bookid_var.set("BKID5563")
                self.booktitle_var.set("Clean Cood")
                self.author_var.set("Robert C.Martin")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 =d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.650")

            elif(x == "Python Programming"):
                self.bookid_var.set("BKID5443")
                self.booktitle_var.set("The Pragmatic Programmer")
                self.author_var.set("Steve McConnell")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.700")

            elif(x =="Eloquent JavaScript"):
                self.bookid_var.set("BKID4343")
                self.booktitle_var.set("Eloquent JavaScript")
                self.author_var.set("Kyle Simpson")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.750")

            elif(x == "Python CookBook"):
                self.bookid_var.set("BKID6743")
                self.booktitle_var.set("Python CookBook")
                self.author_var.set("Joshua Bloch")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.540")

            elif(x =="Machine learning"):
                self.bookid_var.set("BKID7543")
                self.booktitle_var.set("Into to Machine learning")
                self.author_var.set("Eric Matthes")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.799")

            elif(x == "Machine tecnologyg"):
                self.bookid_var.set("BKID7563")
                self.booktitle_var.set("Machine tecnology")
                self.author_var.set("Douglas Crockford")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.989")

            elif(x == "My Python"):
                self.bookid_var.set("BKID5563")
                self.booktitle_var.set("My Python")
                self.author_var.set("Zed A. Shaw")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.479")

            elif(x == "Joss Ellif guru"):
                self.bookid_var.set("BKID5363")
                self.booktitle_var.set("Joss Ellif guru")
                self.author_var.set("Martin Fowler")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.479")

            elif(x == "Grokking Algorithms"):
                self.bookid_var.set("BKID1273")
                self.booktitle_var.set("Grokking Algorithms")
                self.author_var.set("Aditya Bhargava")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.555")

            elif(x == "Fluent Python"):
                self.bookid_var.set("BKID9843")
                self.booktitle_var.set("Fluent Python")
                self.author_var.set("Luciano Ramalho")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.699")

            elif(x == "Machine python"):
                self.bookid_var.set("BKID9854")
                self.booktitle_var.set("Machine python")
                self.author_var.set("Luciano Ramalho")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.699")
                
            elif(x == "Advance Python"):
                self.bookid_var.set("BKID9354")
                self.booktitle_var.set("Advance Python")
                self.author_var.set("Eric Matthes")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.729")
                
            elif(x == "Inton Python"):
                self.bookid_var.set("BKID2135")
                self.booktitle_var.set("Inton Python")
                self.author_var.set("Wes McKinney")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.567")
                
            elif(x == "RedChilli Python"):
                self.bookid_var.set("BKID9845")
                self.booktitle_var.set("RedChilli Python")
                self.author_var.set("Frederick P. Brooks Jr")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.955")
                
            elif(x == "Ishq Python"):
                self.bookid_var.set("BKID7455")
                self.booktitle_var.set("Ishq Python")
                self.author_var.set("Al Sweigart")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.542")
                
            elif(x == "Introduction to DSA"):
                self.bookid_var.set("BKID7239")
                self.booktitle_var.set("Introduction to DSA")
                self.author_var.set("Kyle Simpsont")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.239")
                
            elif (x == "The C++ Programme"):
                self.bookid_var.set("BKID2139")
                self.booktitle_var.set("The C++ Programme")
                self.author_var.set("Kathy Sierra")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.355")
                
            elif (x == "Java Good Code"):
                self.bookid_var.set("BKID6451")
                self.booktitle_var.set("Java Good Code")
                self.author_var.set("Bert Bates")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturn_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.677")


        listBox =Listbox(DataFrameRight, font=("arial", 11, "bold"), width=22, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        #=======================================Button Frame=====================================
        framebutton = Frame(self.root, bd=10, relief=RIDGE, padx=2, bg="Powder Blue")
        framebutton.place(x=0, y=490, width=1363, height=60)

        btnAddData=Button(framebutton,command=self.adda_data, text="Add Data", font=("arial", 12, "bold"), width=21, bg="Blue",fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(framebutton, command=self.showData, text="Show Data", font=("arial", 12, "bold"), width=21, bg="Blue", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(framebutton, command=self.update, text="Update", font=("arial", 12, "bold"), width=21, bg="Blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(framebutton, command=self.delete, text="Delete", font=("arial", 12, "bold"), width=22, bg="Blue", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(framebutton, command=self.reset, text="Reset", font=("arial", 12, "bold"), width=21, bg="Blue", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(framebutton, command=self.iExit, text="Exit", font=("arial", 12, "bold"), width=21, bg="Blue", fg="white")
        btnAddData.grid(row=0, column=5)

        #=======================================Infromation Frame=====================================
        FrameDetails=Frame(self.root, bd=10, relief=RIDGE, padx=20, bg="powder Blue")
        FrameDetails.place(x=0, y=550, width=1363, height=145)

        Table_frame=Frame(FrameDetails, bd=7, relief=RIDGE, padx=20, bg="powder Blue")
        Table_frame.place(x=0, y=3, width=1300, height=120)

        xscrollbar = Scrollbar(Table_frame, orient=HORIZONTAL)
        yscrollbar = Scrollbar(Table_frame, orient=VERTICAL)

        self.libray_table=ttk.Treeview(Table_frame,columns=("memebertype","prnno", "title", "firtname", "lastname", "adress1", "adress2", "postid", "mobileno", "bookid", "booktitle", "auther", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "Finalprice"),xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)

        xscrollbar.pack(side=BOTTOM, fill=X)
        yscrollbar.pack(side=RIGHT, fill=Y)

        xscrollbar.config(command=self.libray_table.xview)
        yscrollbar.config(command=self.libray_table.yview)


        self.libray_table.heading("memebertype", text="Memeber Type")
        self.libray_table.heading("prnno", text="PRN No")
        self.libray_table.heading("title", text="Title")
        self.libray_table.heading("firtname", text="First Name")
        self.libray_table.heading("lastname", text="Last Name")
        self.libray_table.heading("adress1", text="Adress1")
        self.libray_table.heading("adress2", text="Adress2")
        self.libray_table.heading("postid", text="Post ID")
        self.libray_table.heading("mobileno", text="Mobile Number")
        self.libray_table.heading("bookid", text="Book ID")
        self.libray_table.heading("booktitle", text="Book Title")
        self.libray_table.heading("auther", text="Author")
        self.libray_table.heading("dateborrowed", text="Date Of Borrowed")
        self.libray_table.heading("datedue", text="Date Due")
        self.libray_table.heading("days", text="DaysOnBook")
        self.libray_table.heading("latereturnfine", text="LateReturnFine")
        self.libray_table.heading("dateoverdue", text="DateOverDue")
        self.libray_table.heading("Finalprice", text="Final Price")

        self.libray_table["show"]="headings"
        self.libray_table.pack(fill=BOTH, expand=1)

        self.libray_table.column("memebertype", width=100)
        self.libray_table.column("prnno", width=100)
        self.libray_table.column("title", width=100)
        self.libray_table.column("firtname", width=100)
        self.libray_table.column("lastname", width=100)
        self.libray_table.column("adress1", width=100)
        self.libray_table.column("adress2", width=100)
        self.libray_table.column("postid", width=100)
        self.libray_table.column("mobileno", width=100)
        self.libray_table.column("bookid", width=100)
        self.libray_table.column("booktitle", width=100)
        self.libray_table.column("auther", width=100)
        self.libray_table.column("dateborrowed", width=100)
        self.libray_table.column("datedue", width=100)
        self.libray_table.column("days", width=100)
        self.libray_table.column("latereturnfine", width=100)
        self.libray_table.column("dateoverdue",width=100)
        self.libray_table.column("Finalprice",width=100)
        
        self.fetch_data()
        self.libray_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adda_data (self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Happy@123", database="library_db")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrow_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturn_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()
            ))
        conn.commit()
        self.fetch_data()
        conn.close()


        messagebox.showinfo("success", "Member Has been inserted successfully")
        
    def update(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Happy@123", database="library_db")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PosdId=%s, Mobile=%s, BookId=%s, Booktitle=%s, Auther=%s, dateborrow=%s, datedue=%s, daysonbook=%s, latereturn=%s, dateoverdue=%s, finalprice=%s where PRN_NO=%s",(
            self.member_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrow_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturn_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            self.prn_var.get()
            
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success", "Member has been Update")
        
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Happy@123", database="library_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.libray_table.delete(*self.libray_table.get_children())
            for i in rows:
                self.libray_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    def get_cursor(self,event=""):
        cursor_row=self.libray_table.focus()
        content=self.libray_table.item(cursor_row)
        row=content['values']
        
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrow_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturn_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
        
    def showData(self):
        self.txtBox.insert(END, "Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END, "PRN No:\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END, "ID No:\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END, "FirstName:\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END, "LastName:\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END, "Address1:\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END, "Address2:\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END, "Post Code:\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END, "Mobile No:\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END, "Book ID:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END, "Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END, "Author:\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END, "DateBorrowed:\t\t"+self.dateborrow_var.get()+"\n")
        self.txtBox.insert(END, "Datedue:\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END, "DaysOnBook:\t\t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END, "LateRateFine:\t\t"+self.latereturn_var.get()+"\n")
        self.txtBox.insert(END, "DateOverDue:\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END, "FinalPrice:\t\t"+self.finalprice_var.get()+"\n")
        
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrow_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturn_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System", "Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the Member")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Happy@123", database="library_db")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            Value=(self.prn_var.get(),)
            my_cursor.execute(query,Value)
            
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success", "Member has been Delete")





if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()