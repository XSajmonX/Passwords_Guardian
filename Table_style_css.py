def tab_style(table):
    table.setAlternatingRowColors(True)
    table.setStyleSheet("""
    QTableWidget {
        background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(132, 0, 193, 255), stop:1 rgba(0, 204, 97, 255));
        border: none;
    }
    QTableCornerButton::section {
        background-color: #0078D7; /* Górny lewy narożnik */
    }
    QHeaderView::section {
        background-color: #4A90E2;  /* Niebieskie tło */
        color: white;               /* Biały tekst */
        font-weight: bold;          /* Pogrubienie */
        font-size: 12pt;            /* Rozmiar czcionki */
        border: 1px solid black;    /* Obramowanie */
    }
    QHeaderView::section:vertical {
        background-color: #4A90E2;  /* Ten sam kolor co nagłówki kolumn */
        color: white;
        font-weight: bold;
        font-size: 12pt;
        border: 1px solid black;
    }
    QTableWidget {
        gridline-color: black; /* Siatka czarna */
        font-size: 12pt;       /* Większa czcionka */
    }

    QTableWidget::item:alternate {
        background-color: gray;  /* szary */
    }
    QTableWidget::item {
        background-color: #F2F2F2;  /* Jasnoszary */
    }
    QTableWidget::item:selected {
        background-color: #FF9800; /* Pomarańczowy */
        color: white;
    }
    """)


def button_style1(btn_show):
    btn_show.setStyleSheet("""
    QPushButton:hover{

        background-color: rgb(206, 34, 34);
    }
    QPushButton:pressed{
        background-color: rgb(1, 35, 255);
    }
    QPushButton{
        background-color: blue;
        font-size: 12pt;
        font-weight: bold;
        height:50px;
        border: 2px solid black;
    }
    """)


def button_style2(btn_copy):
    btn_copy.setStyleSheet("""
    QPushButton:hover{
        background-color: rgb(206, 34, 34);
    }
    QPushButton:pressed{
        background-color: rgb(1, 35, 255);
    }
    QPushButton{
        background-color: red;
        font-size: 12pt;
        font-weight: bold;
        height:50px;
        border: 2px solid black;
    }
    """)