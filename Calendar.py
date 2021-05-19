class Year:
    
    def __init__(self, year):
        self.year = int(year)
        self.initial_day = int
        self.is_leap_year = bool
        self.months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        self.days_in_a_month = {"janeiro":31,"fevereiro": 28, "março": 31, "abril": 30,"maio": 31, "junho": 30, "julho": 31, "agosto": 31, "setembro": 30,
        "outubro": 31,"novembro": 30,"dezembro": 31}
        self.name_days_week = ["dom","seg","ter","quar","quin", "sex", "sab"]
        self.calculate_if_is_leap_year()
        self.calculate_initial_day()
        

    def calculate_if_is_leap_year(self):

        if (self.year < 1583 and self.year % 4 == 0):
            self.is_leap_year = True
            self.change_feb_to_29_days()
        elif(self.year%400 == 0 or self.year%4 == 0 and self.year%100 != 0):
            self.is_leap_year = True
            self.change_feb_to_29_days()
        else:
            self.is_leap_year = False
        return print(self.is_leap_year)

    def change_feb_to_29_days(self):
        if(self.is_leap_year == True):
            self.days_in_a_month[1] = 29

    def calculate_initial_day(self):
        if(self.year < 1583):
            self.initial_day = int(((self.year*365) + (self.year-1)/4)%7)
            #The results means: sab = 1 dom = 2 seg = 3 ter = 4 quar = 5 quin = 6 sex = 0
            self.converts_initial_day_to_an_unique_table_of_values(self.initial_day)
        
        else:
            self.initial_day = ((self.year-1)*365 + int((self.year-1)/4) - int((self.year-1)/100) + int(((self.year-1)/400)) + 1)%7
            print(self.initial_day)   
        #The results means: dom = 0 seg = 1 ter = 2 quar = 3 quin = 4 sex = 5 sab = 6

    #Esse metodo é util apenas pra printar no console
    def converts_initial_day_to_an_unique_table_of_values(self, value_of_day):
        self.value_of_day = str(value_of_day)
        #converts to dom = 0 seg = 1 ter = 2 quar = 3 quin = 4 sex = 5 sab = 6
        table_of_conversion = {"2":0, "3":1, "4":2, "5":3, "6":4, "0":5, "1":6}
        self.initial_day = table_of_conversion.get(self.value_of_day)
        return print(self.initial_day)




class Calendar(Year):
    
    def __init__(self,year):
        Year.__init__(self,year)
        self.print_the_months()
        
        
    def print_the_months(self):
        for self.month in self.months:
            print(f"\t{self.month}")
            self.print_the_name_of_days()
    

    def print_the_name_of_days(self):
        for day in self.name_days_week:
            print(f"\t{day}", end =" ")
        print("\n")
        self.verify_initial_day_in_month_to_put_blank_spaces()
        print("\n")

    def verify_initial_day_in_month_to_put_blank_spaces(self):
        self.blank_spaces = 0
        while(self.blank_spaces < self.initial_day):
            print(f"\t", end =" ")
            self.blank_spaces += 1
        self.blank_spaces = 0
        self.print_the_days()    

    def print_the_days(self):
        day = 1
        while(day <= self.days_in_a_month[self.month]):
            print(f"\t{day}", end =" ")
            #O initial day tbm serve como contador do dia da semana
            self.initial_day += 1
            if(self.initial_day > 6): 
                print("\n")
                self.initial_day = 0
            day+=1  

            

        


var_teste = Calendar(2021)