from luo_peli import luo_peli

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()        
        if vastaus.endswith("a") or vastaus.endswith("b") or vastaus.endswith("c"):
            peli = luo_peli(vastaus)
            if peli:
                peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
