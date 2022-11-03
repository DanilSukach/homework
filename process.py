from multiprocessing import Process
import click


def discriminant(a: int, b: int, c: int) -> int:
    D = b**2 - 4 * a * c
    return D


def x1(a: int, b: int, c: int, D: int) -> float:
    x = (-b + D**0.5) / (2 * a)
    print("X1 = ", x)


def x2(a: int, b: int, c: int, D: int) -> float:
    x = (-b - D**0.5) / (2 * a)
    print("X2 = ", x)


@click.command()
@click.argument("a", default=1)
@click.argument("b", default=1)
@click.argument("c", default=1)
def main(a, b, c):
    D = discriminant(a, b, c)
    process1 = Process(target=x1, args=(a, b, c, D))
    process2 = Process(target=x2, args=(a, b, c, D))

    process1.start()
    process2.start()

    process1.join()
    process2.join()


if __name__ == "__main__":
    main()
