import madhu_power as power
import pranali_substract as sub
import renuka_mod as mod
import suraj_multiply as mul
import suyash_divide as div
import sindhu_add as add


def main():
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    print("Addition : ", add.add(a, b))
    print("subtraction : ", sub.substract(a, b))
    print(" Multiplication : ", mul.multiply(a, b))
    print("Division", div.divide(a, b))
    print("Mod:", mod.mod(a, b))
    print("Power : ", power.power(a, b))


if __name__ == "__main__":
    main()
