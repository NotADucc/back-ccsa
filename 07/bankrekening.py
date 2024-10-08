class BankRekening:
    def __init__(self, naam, nummer, bedrag = 0) :
        self.naam = naam
        self.nummer = nummer
        self.bedrag = bedrag
    def __str__(self) :
        return f'{self.naam}, {self.nummer}, bedrag: {self.bedrag}'
        
    def __repr__(self) :
        return f"BankRekening('{self.naam}', '{self.nummer}', {self.bedrag})"
        
    def storten(self, num) :
        self.bedrag += num
        
    def afhalen(self, num) :
        self.bedrag -= num