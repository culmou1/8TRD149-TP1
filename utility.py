import csv
from datetime import datetime

bookStr = 'books.csv'
bookCopyStr = 'bookcopy.csv'
bookLoadStr = 'bookload.csv'
borrowerStr = 'borrower.csv'


def getYear2012():  # Fonction qui retourne les livres sortis en 2012.
    with open(bookStr, newline='', mode='r') as csvBook:  # csvBook <- bookStr
        readerbook = csv.DictReader(csvBook)  # DictReader permet de lire un fichier.
        for row in readerbook:  # Pour chaque rangée dans readerBook.
            if int(row["Year"]) == 2012:
                print("Voici les livres publies en 2012 : {0}".format(row['Title']))


def isBookAvailable():  # Fonction qui dit si le livre est disponible.
    bookname = input("Entrez le titre du livre : \n")
    dateInput = input("Entrez la date d'aujourd'hui (YYYY-MM-DD): \n")
    dateInputConvertie = datetime.strptime(dateInput, "%Y-%m-%d")
    with open(bookStr, newline='', mode='r') as csvBook:  # csvBook <- bookStr
        readerbook = csv.DictReader(csvBook)
        for row in readerbook:
            if (row["Title"]) == bookname:  # Si le livre entré en paramètre = un titre dans la liste.
                bookISBN = row["ISBN"]  # Récupère le ISBN du livre.
                with open(bookCopyStr, newline='', mode='r') as csvBookCopy:  # csvBookCopy <- bookCopyStr
                    readerBookCopy = csv.DictReader(csvBookCopy)
                    for row in readerBookCopy:
                        if (row["ISBN"] == bookISBN):
                            bookCopyNo = row["CopyNo"]  # Récupère le numéro de la copie de livre à vérifier.
                            with open(bookLoadStr, newline='', mode='r') as csvBookLoad:
                                readerBookLoad = csv.DictReader(csvBookLoad)
                                for row in readerBookLoad:
                                    if (row["CopyNo"] == bookCopyNo):
                                        dateDue= row["DateDue"]
                                        dateDueConvertie = datetime.strptime(dateDue, "%Y-%m-%d")
                                        # Si la date entré est plus recente que la date de remise
                                        if dateDueConvertie < dateInputConvertie:
                                            print("La copie du livre: %s"%bookname, bookCopyNo, "est disponible. \n")



def memberNameWithBookName():
    bookname = input ("Entrez le titre du livre : \n")
    dateInput = input("Entrez la date d'aujourd'hui (YYYY-MM-DD): \n")
    dateInputConvertie = datetime.strptime(dateInput, "%Y-%m-%d")
    with open(bookStr, newline='', mode='r') as csvBook:  # csvBook <- bookStr
        readerbook = csv.DictReader(csvBook)
        for row in readerbook:
            if (row["Title"]) == bookname:  # Si le livre entré en paramètre = un titre dans la liste.
                bookISBN = row["ISBN"]  # Récupère le ISBN du livre.
                with open(bookCopyStr, newline='', mode='r') as csvBookCopy:  # csvBookCopy <- bookCopyStr
                    readerBookCopy = csv.DictReader(csvBookCopy)
                    for row in readerBookCopy:
                        if (row["ISBN"] == bookISBN):
                            bookCopyNo = row["CopyNo"]  # Récupère le numéro de la copie de livre à vérifier.
                            with open(bookLoadStr, newline='', mode='r') as csvBookLoad:
                                readerBookLoad = csv.DictReader(csvBookLoad)
                                for row in readerBookLoad:
                                    dateDue = row["DateDue"]
                                    dateOut = row["DateOut"]
                                    dateDueConvertie = datetime.strptime(dateDue, "%Y-%m-%d")
                                    dateOutConvertie = datetime.strptime(dateOut, "%Y-%m-%d")
                                    # Si la date entré est entre la dete de sortie et celle de remise du livre.
                                    if (row["CopyNo"] == bookCopyNo and (dateOutConvertie < dateInputConvertie and dateDueConvertie > dateInputConvertie)):
                                        borrower = row["BorrowerNo"]    # Récupère le numéro de l'emprunteur.
                                        with open(borrowerStr, newline='', mode='r') as csvBorrower:
                                            readerBorrower = csv.DictReader(csvBorrower)
                                            for row in readerBorrower:
                                                if (row["BorrowerNo"] == borrower):
                                                    print(row["BorrowerName"])



def listeMembreAvecLivre():
    dateInput = input("Entrez la date d'aujourd'hui (YYYY-MM-DD): \n")
    dateInputConvertie = datetime.strptime(dateInput, "%Y-%m-%d")
    with open(bookLoadStr, newline='', mode='r') as csvBookLoad:
        readerBookLoad = csv.DictReader(csvBookLoad)
        for row in readerBookLoad:
             dateDue = row["DateDue"]
             dateOut = row["DateOut"]
             dateDueConvertie = datetime.strptime(dateDue, "%Y-%m-%d")
             dateOutConvertie = datetime.strptime(dateOut, "%Y-%m-%d")
             # Si la date entré est entre la dete de sortie et celle de remise du livre.
             if (dateOutConvertie < dateInputConvertie and dateDueConvertie > dateInputConvertie):
                 borrower = row["BorrowerNo"]
                 with open(borrowerStr, newline='', mode='r') as csvBorrower:
                    readerBorrower = csv.DictReader(csvBorrower)
                    for row in readerBorrower:
                        if (row["BorrowerNo"] == borrower):
                            print(row["BorrowerName"])











