from models.Books import Books
from models.Magazine import Magazine
from models.Monograph import Monograph

if __name__ == '__main__':
    the_economist = Magazine("The Economist", 40, "Finance")

    Dune = Books("Frank Herbert", "Dune", 199, 554, "Sci-Fi")

    Rains_in_Lviv = Monograph("Causes of rains in Lviv", 67, "Meteorology")

    print(f"{the_economist}")
    print(f"{Dune}")
    print(f"{Rains_in_Lviv}")

