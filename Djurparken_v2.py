from abc import ABC, abstractmethod
import random
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog


class PetOwner(): # klass som representerar djurägaren
    def __init__(self, name): #Konstruktor
        self.__name = name
        self.__djur = []
        self.__balls = [Ball("grön", 100), Ball("blå", 100), Ball("röd", 100)]
    '''
    större delen av PetOwner alla djurklasser är densamma som V1 av programmet, enstaka tillägg eller förändringar, 
    - metoder för att ge GUI klassen åtkomst
    - bytt ut vissa print metoder till return metoder för att kunna visa som info i GUi istället
    '''


    def get_animal_list(self):
        return self.__djur

    def get_balls(self):
        return self.__balls
    
    def ball_add(self, ball):
        self.__balls.append(ball)

    def remove_ball(self, ball):
        self.__balls.remove(ball) 

    def animal_add(self, animal):
        '''
        används endast för att snabbt kunna lägga till ett nytt djur
        t.ex 
        Jocke.animal_add(Dog(5, "Ludde"))
        '''
        self.__djur.append(animal)

    def animal_remove(self, animal):
        print(animal)
        self.__djur.remove(animal)


    def add_animal(self, Silent=False): # skapar och lägger till ett djur i listan beroende på val av användaren
        '''
        valde att låta användaren lägga till djur själv istället för att hårdkoda in djur.
        reflektioner:
        hade nog kunnat göra denna metod kortare, mycket onödig repetition
        särskilt if villkors delen.
        gör det den ska; låter vara tills vidare.
        '''    
        while True:
            print("Vilket djur vill du lägga till? (Katt, Hund, Valp, Kanin, Papegoja)")
            print("1. Katt")
            print("2. Hund")
            print("3. Hundvalp")
            print("4. Kanin")
            print("5. Papegoja")
            print("Ange '0' för att återgå till menyn")

            choice = self.get_int("val: ")
            
            if choice == 1:
                name = self.get_str("Ange ett namn: ")
                age = self.get_int("Ålder? ")
                animal = Cat(age, name)
            
            elif choice == 2:
                name = self.get_str("Ange ett namn: ")
                age = self.get_int("Ålder? ")
                animal = Dog(age, name )

            elif choice == 3:
                name = self.get_str("Ange ett namn: ")
                months = self.get_int("Ålder i månader? ")
                animal = Puppy(months, name)

            elif choice == 4:
                name = self.get_str("Ange ett namn: ")
                age = self.get_int("Ålder? ")
                animal = Rabbit(age, name)

            elif choice == 5:
                name = self.get_str("Ange ett namn: ")
                age = self.get_int("Ålder? ")
                animal = Parrot(age, name)

            elif choice == 0:
                return True
            
            else:
                print("Ogiltigt val")            
                continue

            self.__djur.append(animal)
            print(f"{name} är tillagd!")
            break


    def remove_animal(self): # låter användaren välja ett djur att ta bort.
        if not self.__djur:
            print("Du har inga djur!.")
            return
        while True:
            self.prt_animal_as_list()
            choice = self.get_int("Ange val: ") - 1
            if 0 <= choice < len(self.__djur): # jämför valet med längden av listan för djur
                print(f"Du släpper löst {self.__djur[choice]._name} i det fria")
                self.__djur.pop(choice)
                break
            else:
                print("Felaktig inmatning, försök igen.")

    def ball_add(self,ball):
        ball = ball
        self.__balls.append(ball)

    def add_ball(self): # låter användaren lägga till en boll i listan av bollar.
        print("Vilken typ av boll vill du köpa?")
        print("1. Blå  - Perfekt till lite större djur som t.ex hundar.")
        print("2. Röd  - Mellanstor boll till mellanstora djur. ")
        print("3. Grön - liten boll för små djur. ")
        while True:
            choice = self.get_int("Val: ")
            if choice == 1:
                self.__balls.append(Ball("blå", 100))
                print("Du köper en blå boll.")
                break
            elif choice == 2:
                self.__balls.append(Ball("röd", 100))
                print("Du köper en röd boll.")
                break
            elif choice == 3:
                self.__balls.append(Ball("grön", 100)) 
                print("Du köper en grön boll.")
                break           
            else:
                print("Ogiltigt val, försök igen. Ange siffra.")




    def play(self, silent=False): # metod för att leka med djur, inkl val av djur, val av boll
        '''
        Denna metod växte mer och mer under tidens gång, hade kanske kunnat undvika att trippel-nesta denna med
        andra metoder men väljer att låta det vara som det är för tillfället. 

        reflektioner:
        att använda fler metoder hade sparat lite huvudvärk i loop-hell... t.ex en för boll och en utan osv.
        '''
        if not self.__djur: # check om listan med djur är tom
            print("Inga djur att leka med.") 
            return
        
        while True: #huvudloop
            print("Vilket djur vill du leka med? Ange '0' för att återgå.")
            self.prt_animal_as_list()
            choice = self.get_int("Ange numret på djuret: ") - 1 #låter användaren välja ett djur , -1 för index
            
            if choice == -1: # återgår till menyn om använder matar in "0"
                return True # "True" sätter igång silent funktionen så att användaren slipper 2 inputs.

            elif 0 <= choice < len(self.__djur): # kollar så att inmatning är giltigt mot längden av listan
                animal_choice = self.__djur[choice] # anger valet av djur till en variabel.
                if animal_choice._type == "papegoja": # undviker att fråga användaren om den vill kasta en boll till en papegoja.
                    animal_choice.interact()
                    break
                else:
                    continue_loop = True # för att kunna avsluta loopen korrekt
                    while continue_loop:
                        choice = self.get_str("Vill du använda en boll? ja/nej: ").strip().lower()
                        if choice == "ja":
                            for idx, ball in enumerate(self.__balls): 
                                print(f"{idx + 1}. färg: {ball.color} kvalitet: {ball.quality}") # printar ut listan av bollar med info
                            while True:
                                ball_choice = self.get_int("Vilken boll vill du använda?: ") - 1 
                                if 0 <= ball_choice < len(self.__balls): # kollar så att inmatningen är giltig mot längden av listan med bollar
                                    if self.__balls[ball_choice].quality <= 0: # kollar så att bollen är hel.
                                        print("Bollen är för sliten för att leka med, du borde slänga den när ni lekt klart...")
                                        self.remove_ball(self.__balls[ball_choice]) # tar bort bollen ur listan
                                        break
                                    else:
                                        animal_choice.interact(self.__balls[ball_choice]) # kallar på valda djurets interact metod med vald boll som parameter
                                        break
                                else:
                                    print("Ogiltigt val")


                        elif choice == "nej":
                            animal_choice.interact() # kallar på interact() för valt djur utan en parameter för boll
                            break

                        else:
                            print("Ogiltigt svar, Ange 'ja' / 'nej' ")
                            continue
                        
                        continue_loop = False # avslutar boll-fråga-loop
                        
                    break
                
            else:
                print("Ogiltigt val") # ogiltigt val av djur, låter användaren försöka igen
              

    def feed(self, Silent=False):  # låter användaren välja ett djur samt mat att mata med
        if not self.__djur: # check för att kolla om det finns djur i listan
            print("Inga djur att mata.")
            return

        while True: # loop som hanterar val av djur
            print("Vilket djur vill du mata? '0' för att återgå till menyn")
            self.prt_animal_as_list
            choice = self.get_int("Ange numret på djuret: ") - 1 # tilldelar val till en variabel samt justerar index

            if choice == -1:
                return True # Skickar silent = true för att slippa behöva trycka 2 gånger efter "0" inmatats

            elif 0 <= choice < len(self.__djur): # jämför val mot längden av listan för check av giltig inmatning
                animal_type = self.__djur[choice]._type
                if self.__djur[choice]._hungrymeter >= 100: # kollar ifall valt djur är 'hungrigt'
                    print(f"{self.__djur[choice]._name} verkar inte vara hungrig just nu.")
                else:
                    food = self.get_food_type(animal_type)
                    self.__djur[choice].eat(food) # kallar på eat() för valt djur
                break
            else:
                print("Ogiltigt val, försök igen.\n: ")


    def get_food_type(self, animal_type): # presenterar val av mat i form av meny beroende på typ av djur som valts
        '''
        i eftertanke hade varje typ av djur kanske kunnat få varsin metod för bättre struktur.. 
        låt vara tills vidare och fixa om det finns tid över - gör det den ska utan problem.
        '''
        if animal_type == "katt":
            print("Välj mat för katten:")
            print("1. torrfoder")
            print("2. blötmat")
            print("3. fisk")
            choice = self.get_int("Ange val: ")
            if choice == 1:
                return "torrfoder"
            elif choice == 2:
                return "blötmat"
            elif choice == 3:
                return "fisk"
            else:
                print("Ogiltigt val, standardmat 'torrfoder' används.")
                return "torrfoder"

        elif animal_type == "hund":
            print("Välj mat för hunden:")
            print("1. Torrfoder")
            print("2. Ben")
            print("3. köttbullar")
            choice = self.get_int("Ange val: ")
            if choice == 1:
                return "torrfoder"
            elif choice == 2:
                return "ben"
            elif choice == 3:
                return "köttbullar"
            else:
                print("Ogiltigt val, standardmat 'torrfoder' används.")
                return "torrfoder"

        elif animal_type == "valp":
            print("Välj mat för valpen:")
            print("1. Valpfoder")
            print("2. Mjölk")
            print("3. Gurka")
            choice = self.get_int("Ange val: ")
            if choice == 1:
                return "valpfoder"
            elif choice == 2:
                return "mjölk"
            elif choice == 3:
                return "gurka"
            else:
                print("Ogiltigt val, standardmat 'valpfoder' används.")
                return "valpfoder"

        elif animal_type == "kanin":
            print("Välj mat för kaninen:")
            print("1. Grönsaker")
            print("2. Hö")
            print("3. Morot")
            choice = self.get_int("Ange val: ")
            if choice == 1:
                return "grönsaker"
            elif choice == 2:
                return "hö"
            elif choice == 3:
                return "morot"
            else:
                print("Ogiltigt val, standardmat 'grönsaker' används.")
                return "grönsaker"

        elif animal_type == "papegoja":
            print("Välj mat för papegojan:")
            print("1. Frukt")
            print("2. Nötter")
            print("3. Fröblandning")
            choice = self.get_int("Ange val: ")
            if choice == 1:
                return "frukt"
            elif choice == 2:
                return "nötter"
            elif choice == 3:
                return "fröblandning"
            else:
                print("Ogiltigt val, standardmat 'frukt' används.")
                return "frukt"


    def print_animals(self): # skriver ut alla djur
        for djur in self.__djur:
            print(djur)
        return self.__djur # skickar tillbaka djur listan till GUI klassen medans funktionen för terminalen återstår


    def prt_animal_as_list(self): # skriver ut alla djur samt index, för menyanvändning
        for idx, djur in enumerate(self.__djur): # enumerate ger tillgång till index och objektet
            print(f"{idx + 1}. {djur._name} ({djur._type}) {djur._hungrymeter}") # skriver ut info för varje position i listan, numrerat.


    def get_int(self, choice): # hanterar felinmatning av heltal som en metod
        while True:
            try:
                return int(input(choice))
            except ValueError:
                print("felaktig inmatning, ange siffror.")


    def get_str(self, choice): # hanterar felinmatning för sträng samt formaterar.
        while True:
            user_input = input(choice).strip().lower()
            if user_input: # om inte tomt, returnera
                return user_input
            else:
                print("felaktig inmatning, försök igen.")


    def menu(self,): # method som skriver ut huvudmenyn.
        print("\nVad vill du göra?")  
        print("1. Lägg till Djur")
        print("2. Lek med djur")
        print("3. Mata djur")
        print("4. Skriv ut djur.")
        print("5. Köp en ny boll")
        print("6. Släpp löst ett djur")
        print("0. Stäng programmet")   
        
           
    def Run(self,): # kör menyn
        return_menu = "Återgå till menyn med enter" # minska clutter i koden med en variabel
        while True:
            self.menu() # skriver ut menyn via metod.
            choice = self.get_str("Ange ditt val: ").strip()

            if choice == '0': # avslutar programmet
                # self.exit_program()
                break

            elif choice == '1': # skapa och lägga till djur
                silent = self.add_animal()
                if not silent:
                    input(f"\n{return_menu}")
                
            elif choice == '2': # skriver ut djur och låter användaren välja ett djur att leka med genom interact()
                silent = self.play()
                if not silent:
                    input(f"\n{return_menu}")
                           
            elif choice == '3': # skriver ut djur och låter användaren välja ett djur att mata genom feed()
                silent = self.feed() # tar en bool från feed(), för att låta återgå funktionen fungera som en input istället för 2
                if not silent:
                    input(f"\n{return_menu}")
                        
            elif choice == '4': # skriver ut djur
                self.print_animals()
                input(f"\n{return_menu}")
                                       
            elif choice == '5': # lägger till boll
                self.add_ball()
                input(f"\n{return_menu}")      
                
            elif choice == '6': # tar bort ett djur
                self.remove_animal()
                input(f"\n{return_menu}")           

            else:
                print("ogiltigt val, ange ett val mellan 1-6")


class Ball: # klass som representerar bollar
    def __init__(self, color, quality):
        self.color = color
        self.quality = int(quality)

    
    def lower_quality(self, amount): # sänker kvaliten på bollen (om t.ex en hund tuggar på den)
        self.quality -= amount 
        if self.quality < 0: # safeguard för att kvalitén inte ska bli negativ
            self.quality = 0

    def is_broken(self):
        return self.quality <= 0

    def __str__(self):
        return f"{self.color} boll, kvalitet: {self.quality}%"


class Animal(ABC): # parent class för alla djur  
    def __init__(self, _Age, _Name):
        self._age = _Age
        self._name = _Name
        self._favourite_food = ""
        self._hungrymeter = 80 # används som ett threshold för true/false på hungry
        self._hungry = False
        self.update_hunger() # uppdaterar ^ 

    def remove_ball():
        pass


    @abstractmethod #För att klassen ska bli abstrakt
    def eat(self, food):
        pass


    def getname(self):
        return (f"{self._name}")
        #Kod för att returnera namn


    @abstractmethod
    def interact(self):
        pass


    def update_hunger(self): # sätter true eller false på hungry beroende på värdet av hungrymeter
        self._hungry = self._hungrymeter < 30


    def set_hungrymeter(self, value):  # tar emot ett värde och tilldelar det till hungrymeter samt uppdaterar hungry
        self._hungrymeter = max(0, min(100, value))
        self.update_hunger()


        # 2 metoder för att öka eller minska hungrymeter, detta för att hålla intervallet för variabeln mellan 0-100
    def decrease_hungrymeter(self, value):
        self.set_hungrymeter(self._hungrymeter - value)

    def increase_hungrymeter(self, value):
        self.set_hungrymeter(self._hungrymeter + value)
    
    
    def __str__(self): # returnerar ut info i form av en sträng
        return f"{self._type}, {self._name}, ålder: {self._age}, hungrig: {self._hungry} ({self._hungrymeter}%)"


class Dog(Animal,): # klass som representerar hund
    def __init__(self, _Age, _Name):
        super().__init__(_Age, _Name)
        self._favourite_food = "köttbullar"
        self._type = "hund"
        self._favourite_color = "blå"

    
    def eat(self, food):
        if food == self._favourite_food:
            self.increase_hungrymeter(60)
            return f"{self._name} glufsar i sig massor av {food} och är nu mätt!"
        
        elif food == "ben" and self._age >= 15:
            self.increase_hungrymeter(20)
            return (f"{self._name} är gammal och tänderna är inte i det bästa skicket.\n"
                    f"{self._name} får tugga endast i en liten stund.")
        
        else:
            self.increase_hungrymeter(40)
            return (f"{self._name} äter likgiltigt lite {food}, du säger att man inte alltid kan äta {self._favourite_food}.")


    def interact(self, ball=None):  # metod för att leka
        if self._hungry:
            return f"{self._name} verkar vara för hungrig för att leka!"

        if ball is not None:
            if ball.color == self._favourite_color:  # om favoritfärg
                if ball.quality > 0:  # check för trasig boll
                    ball.lower_quality(20)  # sänker kvalitet på boll
                    self.decrease_hungrymeter(20)  # gör djuret lite hungrigare efter lek.
                    return (f"Du kastar iväg den {ball.color}a bollen och {self._name} jagar efter som en galning!\n"
                            f"Efter mycket lek och tuggande har bollens kvalitet minskat till {ball.quality}%.")
                else:
                    return "Bollen är för sliten för att leka med."
            else:
                return f"{self._name} verkar inte så intresserad av den bollen."
        
        # Om ingen boll används
        self.decrease_hungrymeter(20)
        leksak = random.choice(["Dragkampsrepet", "pipleksaken", "frisbeen"])
        return (f"Du och hunden {self._name} leker med {leksak} en stund.\n"
                f"{self._name} är nu lite hungrigare.")



class Puppy(Dog): # klass som representerar valp
    def __init__(self, _months, _Name):
        super().__init__(0, _Name)
        self._months = _months
        self._type = "valp"
        self._favourite_food = "valpfoder"
        self._favourite_color = "röd"        
        
    
    def eat(self, food):  # matar valp, med åldersvillkor på viss mat
        if self._months < 6:
            if food == "mjölk":
                self.increase_hungrymeter(80)
                return f"{self._name} dricker {food} och är nu mätt!"
            else:
                return (f"{self._name} är för ung för att äta {food}. "
                        "(valpar under 6 månader äter endast mjölk)")
        else:
            if food == self._favourite_food:
                self.increase_hungrymeter(80)
                return f"{self._name} verkar tycka om {food} och är nu mätt!"
            else:
                self.increase_hungrymeter(40)
                return (f"{self._name} tuggar glatt {food}, men det är inte så mättande.")
                

    def __str__(self):
        return f"{self._type}, {self._name}, ålder: {self._months} månader, hungrig: {self._hungry} ({self._hungrymeter}%)"


class Cat(Animal): # klass som representerar katt
    def __init__(self, _Age, _Name):
        super().__init__(_Age, _Name)
        self._type = "katt"
        self._favourite_food = "fisk"
        self._favourite_color = "röd"

    def interact(self, ball=None):
        if self._hungry:
            return f"{self._name} verkar vara för hungrig för att leka!"

        if ball is not None and ball.color == self._favourite_color:  # om favoritfärg
            if ball.quality > 0:  # extra check för trasig boll 
                ball.lower_quality(20)  # sänker kvalitet på boll
                self.decrease_hungrymeter(20)  # gör djuret lite hungrigare efter lek
                return (f"{self._name} leker glatt med den {ball.color}a bollen!\n"
                        f"Bollens kvalitet har minskat till {ball.quality}% efter en lång lekstund.")
            else:
                return "Bollen är för sliten för att leka med, du slänger den."

        elif ball is not None and ball.color != self._favourite_color:  # om inte favoritfärg
            return f"{self._name} verkar inte så intresserad av den bollen."

        else:  # om inte en boll används
            self.decrease_hungrymeter(20)
            leksak = random.choice(["laserpekaren", "katt-trädet", "katt-tunneln"])
            return (f"Du och katten {self._name} leker med {leksak} en stund.\n"
                    f"{self._name} är nu lite hungrigare.")

    def eat(self, food):
        if food == self._favourite_food:
            self.increase_hungrymeter(100)
            return (f"{self._name} jamade som en galning när du tog fram {food} och är nu mätt och glad!")
        else:
            self.increase_hungrymeter(30)
            returninfo = self.hunt(food)
            return returninfo

    def hunt(self,food):  # simulerar jakt, 50/50 att katt lyckas fånga mat och bli mätt
        success_message = (
        f"{self._name} äter lite {food} men verkar inte helt nöjd.\n"
        f"{self._name} tar sig ut på jakt efter mat...\n"
        f"{self._name} verkar få syn på något i buskarna...\n"
        f"{self._name} tar sats och dyker in...\n"
        f"{self._name} lyckades fånga mat och är nu mätt!"
        )

        failure_message = (
        f"{self._name} äter lite {food} men verkar inte helt nöjd.\n"
        f"{self._name} tar sig ut på jakt efter mat...\n"
        f"{self._name} verkar få syn på något i buskarna...\n"
        f"{self._name} tar sats och dyker in...\n"
        f"{self._name} misslyckades med sin jakt och är nu lika hungrig som innan."
        )

        return success_message if random.random() < 0.5 else failure_message



class Rabbit(Animal): # klass som representerar en kanin
    def __init__(self, _Age, _Name):
        super().__init__(_Age, _Name)
        self._type = "kanin"
        self._favourite_food = "morot" 
        self._favourite_color = "grön" # bollfärg

    
    def eat(self, food):
        if food == self._favourite_food:
            self.increase_hungrymeter(100)
            return f"du lockar fram {self._name} med en {food} som försvinner ner i magen snabbt"

        else:
            self.increase_hungrymeter(50)
            return f"du ställer in {food} i buren, {self._name} hoppar fram och äter lite grann."

    
    def interact(self, ball=None):
        if self._hungry:
            return f"{self._name} verkar vara för hungrig för att leka!"

        elif ball is not None and ball.color == self._favourite_color: # om favoritfärg
            if ball.quality > 0: # check för trasig boll 
                ball.lower_quality(20) # sänker kvalitet på boll
                self.decrease_hungrymeter(20) # gör djuret lite hungrigare efter lek.
                return f"Du kastar fram den {ball.color}a bollen, {self._name} tuggar lite på den men verkar inte så intresserad efter den insett att det inte är mat. \nEfter en stunds gnagande har bollens kvalitet har minskat till {ball.quality}%."
                
            else:
                return "Bollen är för sliten för att leka med"

        elif ball is not None and ball.color != self._favourite_color: # om inte favoritfärg
            return f"{self._name} verkar inte så intresserad av den bollen."

        else: # om inte en boll används
            self.decrease_hungrymeter(20)
            leksak = random.choice(["hinderbanan", "att göra tricks", "kurragömma med godis"])
            return f"Du och {self._name} leker med {leksak} en stund. \n{self._name} är nu lite hungrigare."





class Parrot(Animal): # klass som representerar en papegoja
    def __init__(self, _Age, _Name):
        super().__init__(_Age, _Name)
        self._type = "papegoja"
        self._favourite_food = "nötter"
        

    def eat(self, food):
        if food == self._favourite_food:
            self.increase_hungrymeter(100)
            return f"du ställer in lite {food} i buren, {self._name} verkar helnöjd!"
            
        else:
            self.increase_hungrymeter(50)
            return f"du ställer in {food} i buren, {self._name} äter lite av det men petar mest i maten."

    

    def interact(self,ball=None): # interact, denna utan boll eftersom det är en fågel.
        if self._hungry:
            return f"{self._name} verkar vara för hungrig för att leka!"
        elif ball:
            return f"{self._name} är inte alls intresserad av bollar."
        else:
            self.decrease_hungrymeter(30)
            leksak = random.choice(["gungan", "träklubban", "pusslet"]) 
            return f"Du och {self._name} leker med {leksak} en stund \n{self._name} är nu lite hungrigare."



# Jocke = PetOwner("Jocke") # lägger till en rad djur samt välkomstmeddelande.
# Jocke.animal_add(Dog(15, "Ludde"))

# time.sleep(6) # ta bort om du vill starta om programmet snabbare


# Jocke.Run() # kör programmet


#v2 börjar här..
class PetOwnerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jockes Djurpark")
        self.buttons = [] # lista att ha knapparna i, detta låter menyn vara dynamisk

        self.geometry("800x600") 
        self.configure(bg="darkgray") # liten kant mellan ramarna..
        
        # skapar ramar för menyn(knappar) och inforuta(för text som programmet är baserat på)
        self.menu_frame = ttk.Frame(self)
        self.info_frame = ttk.Frame(self)

        self.menu_frame.pack(side="left", fill="y", expand=True) # meny till vänster, fyller på höjden(antagligen efter knappstorlek med?)
        self.info_frame.pack(side="right", fill="both", expand=True) # inforuta till höger, fyller resten av rutan

        self.info_text = tk.Text(self.info_frame, bg="lightgray", foreground="black", font=("arial", 11, "bold")) # skapar en textruta i informations-ramen
        self.info_text.pack(expand=True, fill="both") # packar den så att den fyller hela ytan i ramen

        style = ttk.Style()
        style.configure('TButton', background='gray') # ändrar färg för runt knappar och menysidan grå
        style.configure('TFrame', background='gray') # -''-
        self.menu_frame.grid_columnconfigure(0, weight=0, minsize=150)# statisk minsta storlek på knappgrid
 


        self.jocke = PetOwner("Jocke") # skapar en djurägare och lägger till djur
        self.jocke.animal_add(Dog(25, "Ludde"))
        self.jocke.animal_add(Cat(2, "Iris"))
        self.jocke.animal_add(Puppy(5, "Isaac"))
        self.jocke.animal_add(Rabbit(3, "Hoppis"))
        self.jocke.animal_add(Parrot(50, "Charlie"))
        
        

        self.main_menu() # kör huvudmeny
        
        '''Här kommer en lång lista metoder, som för det mesta ligger i ordning, många av dessa är mest
        1, välj objekt, 
        2 skicka objektet till respektive metod i respektive klass, ibland med en parameter för mat eller boll, eller lägg till/ta bort ur x lista osv.
        3. vissa metoder för att uppdatera ui't, som clear infobox eller clear buttons'''
        
        
    def main_menu(self): # huvudmeny
        self.remove_buttons() # tömmer knapplistan(menyn)
        self.clear_infobox() # tömmer inforutan

        self.info_text.insert(tk.END, "Jockes Djurpark \n\n")
        self.info_text.insert(tk.END, "Vad vill du göra?\n")

        self.add_button("Lägg till ett djur", self.add_animal_menu)
        self.add_button("Leka med djur", self.play_menu)
        self.add_button("Mata djur", self.feed_menu)
        self.add_button("Visa djur i parken", self.print_animals)
        self.add_button("Köp en ny lek-boll", self.buy_ball_menu)
        self.add_button("Släpp löst ett djur", self.release_animal_menu)

        self.layout_buttons()

    def add_animal_menu(self): # meny för att välja djur att lägga till
        self.remove_buttons()
        self.clear_infobox()
        self.info_text.insert(tk.END, "Vilket djur vill du lägga till?")
        self.add_button("Katt", lambda:self.add_animal("Katt"))
        self.add_button("hund", lambda:self.add_animal("Hund"))
        self.add_button("hundvalp", lambda:self.add_animal("Hundvalp"))
        self.add_button("kanin", lambda:self.add_animal("Kanin"))
        self.add_button("papegoja", lambda:self.add_animal("Papegoja"))
        self.add_button("tillbaka till huvudmenyn", lambda:self.main_menu())
        
        self.layout_buttons()



    def add_animal(self, animal_type):  # frågar om namn + ålder och lägger till ett djur i parken

        name = simpledialog.askstring("", f"Ange namnet på din {animal_type}:") # popup fönster för att fråga om namnet
        if name is None or not name.strip():  # om inmatningen är tom/space eller tryckte på avbryt
            self.info_text.insert(tk.END, "\nInmatningen avbröts, inget djur har lagts till.\n")
            return  # avbryter metod
        
        
        age = simpledialog.askinteger("", f"Ange åldern på din {name}:") # fråga om ålder nytt fönster
        if age is None:  #om användaren avbryter inmatningen
            self.info_text.insert(tk.END, "\nInmatningen avbröts, inget djur har lagts till.\n")
            return
        if age < 0 or age > 100:  # avbruter om åldern är negativ eller orimligt stort
            self.info_text.insert(tk.END, "\nAnge ett rimligt åldersintervall! försök igen.\n")
            return

        # skapar ett djur beroende på animal_typew
        if animal_type == "Katt":
            animal = Cat(age, name)
        elif animal_type == "Hund":
            animal = Dog(age, name)
        elif animal_type == "Hundvalp":
            animal = Puppy(age, name)
        elif animal_type == "Kanin":
            animal = Rabbit(age, name)
        elif animal_type == "Papegoja":
            animal = Parrot(age, name)


        # lägger till djuret i parken
        self.jocke.animal_add(animal)
        self.info_text.insert(tk.END, f"\n{name} har lagts till i parken!\n")

    def play_menu(self): # låter användaren välja ett djur att leka med
        self.remove_buttons()
        self.clear_infobox()
        self.info_text.insert(tk.END, "Vilket djur vill du leka med?")
        self.print_animals()
        
        animals = self.jocke.get_animal_list()
        
        for animal in animals:
            self.add_button(animal._name,  lambda a=animal: self.ask_ball_menu(a))

        self.add_button("tillbaka till huvudmenyn", lambda:self.main_menu())
        self.layout_buttons()


    def ask_ball_menu(self, animal,): # frågar användaren om den vill leka med eller utan boll
        self.remove_buttons()
        self.clear_infobox()
        self.info_text.insert(tk.END, f"Vill leka med en boll med {animal._name}?")
        self.add_button("Lek utan boll", lambda: self.play_no_ball(animal))
        self.add_button("lek med boll", lambda: self.play_with_ball_menu(animal))
        self.add_button("tillbaka", lambda:self.play_menu())
        self.add_button("tillbaka till huvudmenyn", lambda:self.main_menu())
        self.layout_buttons()


    def play_with_ball_menu(self, animal): # om användaren väljer att leka med boll
        self.remove_buttons()
        self.clear_infobox()
        self.info_text.insert(tk.END, "Välj en färg!")
        
        balls = self.jocke.get_balls()
        for ball in balls:
            self.add_button(ball.color, lambda b=ball: self.play_with_ball(animal, b))
            
        self.add_button("tillbaka", lambda:self.ask_ball_menu(animal))
        self.add_button("tillbaka till huvudmenyn", lambda:self.main_menu())
        self.layout_buttons()


    def play_no_ball(self,animal): # om användaren väljer att leka utan boll
        self.clear_infobox()
        result = animal.interact()
        self.info_text.insert(tk.END, result + "\n")

    def play_with_ball(self,animal, ball): # skickar vidare parametrar till valt djur med vald boll.
        self.clear_infobox()
        result = animal.interact(ball)

        self.info_text.insert(tk.END, result + "\n")
        if ball.is_broken():
            self.jocke.remove_ball(ball)
            self.info_text.insert(tk.END, "Dags att köpa ny!\n")


    def layout_buttons(self): # ordnar row för knapparna för jämnt mellanrum med hjälp av weight, utan denna i början hamnade dem lite hejvilt!
        for index in range(len(self.buttons)):
            self.menu_frame.rowconfigure(index, weight=1)


    def add_button(self, text, command): # lägger till en knapp, med label och kommando
        button = ttk.Button(self.menu_frame, text=text, command=command) # skapar knapp
        button.grid(row=len(self.buttons), column=0, sticky="we") # placerar den i nästa rad i ramen
        self.buttons.append(button) # lägger till den i listan.


    def remove_buttons(self): # tar bort knapparna i guit så att man kan dynamiskt byta ut dem till en sub-meny
        for button in self.buttons:
            button.grid_forget()
        self.buttons = [] # utan denna finns det "osynliga" knappar



    
    def feed_menu(self): # meny för val av djur att mata
        self.remove_buttons()
        self.clear_infobox()
        
        self.info_text.insert(tk.END, "Vilket djur vill du mata?")
        self.print_animals()
        animals = self.jocke.get_animal_list()
        for animal in animals: # skapar knappar för varje djur, lambda "fryser" värdet av animal i knappen.
            self.add_button(animal._name,  lambda a=animal: self.feed_animal(a))
            
        self.add_button("tillbaka till huvudmenyn", lambda:self.main_menu())
        self.layout_buttons()


    def feed_animal(self, animal): # meny för val av mat för valt djur
        self.remove_buttons()
        self.clear_infobox()
        self.info_text.insert(tk.END, f"Vilken typ av mat vill du ge {animal._name}?")

        food_options = { # matalternativ för varje djurtyp
            "katt": ["torrfoder", "blötmat", "fisk"], # key->lista, animal_type = key
            "hund": ["torrfoder", "ben", "köttbullar"],
            "valp": ["valpfoder", "mjölk", "gurka"],
            "kanin": ["grönsaker", "hö", "morot"],
            "papegoja": ["frukt", "nötter", "fröblandning"]
        }

        animal_type = animal._type.lower() # hämtar matalternativ för valt djur
        options = food_options[animal_type]
        for food in options: # skapar knappar för varje alternativ
            self.add_button(food, lambda f=food: self.feed_selected_food(animal, f))

        self.add_button("Tillbaka", lambda: self.feed_menu())
        self.add_button("Tillbaka till huvudmenyn", lambda: self.main_menu())
        self.layout_buttons()


    def feed_selected_food(self, animal, food): # skickar maten till valt djur
        result = animal.eat(food) # result tar tillbaka en string som visar vad djuret "tyckte" om maten.
        self.clear_infobox()
        self.info_text.insert(tk.END, result )



    def print_animals(self): # skriver ut alla djur
        animal_info = self.jocke.print_animals()
        self.info_text.insert(tk.END, "\nHär är alla djur i parken just nu\n")
        for animal in animal_info:
            self.info_text.insert(tk.END, f"\n{animal}")



        
    def buy_ball_menu(self): # köp boll meny
        self.remove_buttons()
        self.clear_infobox()
        
        
        self.info_text.insert(tk.END, "Vilken typ av boll vill du köpa?\n\nBlå - perfekt till lite större djur som t.ex hundar.\nRöd - mellanstor boll till mellanstora djur\nGrön - liten boll för små djur.")

        ball_options = {
            "blå",
            "röd",
            "grön"
        }

        for color in ball_options: # skapar knappar för varje boll
            self.add_button(color, lambda c=color: self.buy_ball(c))

        self.add_button("Tillbaka", lambda: self.main_menu())
        self.add_button("Tillbaka till huvudmenyn", lambda: self.main_menu())
        self.layout_buttons()

    def buy_ball(self, color): # köper boll av vald färg, om det inte redan finns en
        ball = Ball(color,100)
        ball_list = self.jocke.get_balls()
        for balls in ball_list: # kollar om det redan finns en boll av den valda färgen
            if balls.color == ball.color:
                self.clear_infobox() # rensar rutan så att texten inte spammas
                self.info_text.insert(tk.END, f"du har redan en {color} boll!")
                return 
    
        self.jocke.ball_add(ball)
        self.clear_infobox()
        self.info_text.insert(tk.END, f"\ndu köper en {ball.color} boll.")



    def release_animal_menu(self): # val av djur att ta bort från djurparken(listan)
        self.remove_buttons()
        self.clear_infobox()

        self.info_text.insert(tk.END, "Här kan du släppa löst ett djur i det vilda, du kommer inte kunna få tillbaka det!\n")
        self.print_animals()
        self.info_text.insert(tk.END, "\n\nVälj ett djur.")
        animal_list = self.jocke.get_animal_list()
        for animal in animal_list:
            self.add_button(animal._name,  lambda a=animal: self.release_animal(a))

        self.add_button("Tillbaka till huvudmenyn", lambda: self.main_menu())
        self.layout_buttons()


    def release_animal(self, animal): # tar bort det valja djuret
        self.jocke.animal_remove(animal)
        self.info_text.insert(tk.END, f"\n Släppte löst {animal}!")
        self.release_animal_menu()


    def remove_ball(self, ball): # tar bort en boll, används när en boll når 0 i quality.
        self.jocke.remove_ball(ball)

    def close_program(self):
        pass

    def clear_infobox(self): #tömmer inforutan
        self.info_text.delete(1.0, tk.END)



gui = PetOwnerGUI()
gui.mainloop() # kör programmet