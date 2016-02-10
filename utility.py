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
                print("Voici le titre des livres en 2012 : {0}".format(row['Title']))


def isBookAvailable(bookname):  # Fonction qui dit si le livre est disponible.
    dateInput = input("Entrez la date d'aujourd'hui (YYYY-MM-DD): \n")
    dateInputConvertie = datetime.strptime(dateInput, "%Y-%M-%d")
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
                            #print(bookCopyNo)
                            with open(bookLoadStr, newline='', mode='r') as csvBookLoad:
                                readerBookLoad = csv.DictReader(csvBookLoad)
                                for row in readerBookLoad:
                                    if (row["CopyNo"] == bookCopyNo):  # À partir d'ici
                                        dateLivre= row["DateDue"]
                                        dateLivreConvertie = datetime.strptime(dateLivre, "%Y-%M-%d")
                                        # print(dateLivreConvertie)
                                        # print(dateInputConvertie)
                                        if dateLivreConvertie > dateInputConvertie:
                                            print("La copie du livre: %s"%bookname, bookCopyNo, "est disponible.")

                                            # Comment simplement printer une copie?


def memberNameWithBookName(bookname):
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
                            print(bookCopyNo)
                            with open(bookLoadStr, newline='', mode='r') as csvBookLoad:
                                readerBookLoad = csv.DictReader(csvBookLoad)
                                for row in readerBookLoad:
                                    if (row["CopyNo"] == bookCopyNo):  # À partir d'ici
                                        borrower = row["BorrowerNo"]
                                        with open(borrowerStr, newline='', mode='r') as csvBorrower:
                                            readerBorrower = csv.DictReader(csvBorrower)
                                            for row in readerBorrower:
                                                if (row["BorrowerNo"] == borrower):
                                                    print(row["BorrowerName"])


def listeMembreAvecLivre():
    dateInput = input("Entrez la date d'aujourd'hui (YYYY-MM-DD): \n")
    dateInputConvertie = datetime.strptime(dateInput, "%Y-%M-%d")
    with open(bookLoadStr, newline='', mode='r') as csvBookLoad:
        readerBookLoad = csv.DictReader(csvBookLoad)
        for row in readerBookLoad:
             date= row["DateDue"]
             dateConvertie = datetime.strptime(date, "%Y-%M-%d")
             #print(dateConvertie)
             if dateConvertie > dateInputConvertie:
                 borrower = row["BorrowerNo"]
                 with open(borrowerStr, newline='', mode='r') as csvBorrower:
                    readerBorrower = csv.DictReader(csvBorrower)
                    for row in readerBorrower:
                        if (row["BorrowerNo"] == borrower):
                            print(row["BorrowerName"])











