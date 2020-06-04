from bs4 import BeautifulSoup
import requests


def word():
    while True:
        try :
            a = input()
            a = int(a)
            raise AssertionError
        except ValueError:
            break
        except AssertionError:
            print("C'est impossible de chercher ce mot ! \n                                    Veuillez réssayer avec un autre mot !")
            continue
    return a
t = word()

def main():
    global t
    try:
        class_ = 'dictLink featured'
        url = "https://www.linguee.fr/francais-anglais/search?source=auto&query=" + t
        source = requests.get(url).text
        soup = BeautifulSoup(source, "html5lib")
        a = soup.find('a', class_= class_)
        print(a.text)
    except:
        print("C'est impossibe !!!!")
        raise Exception
if __name__=='__main__':
    main()
