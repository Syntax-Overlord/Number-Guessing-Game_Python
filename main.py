from random import randint

guesses = 7

random_number = randint(1, 100)


class NumberGuessingGame:
    def __init__(self) -> None:
        self.guesses: int = 7
        self.random_number: int = randint(1, 100)
        self.attempt: int = 0
        return

    def get_input(self) -> int:
        while not (
            (
                input_ := input(f"Attempt {self.attempt}/7 - Enter your guess: ")
                .strip()
                .isdigit()
            )
            and 1 <= input_ <= 100
        ):
            print("Invalid input!")

        out: int = int(input_)
        return out

    def check(self, user_input: int) -> int:
        # 0 -> Correct Guess
        # -1-> Too Low
        # 1 -> Too High
        if user_input == self.random_number:
            return 0

        if user_input < self.random_number:
            return -1
        else:
            return 1

    def guess_used(self) -> None:
        self.guesses -= 1

    def attempt_used(self) -> None:
        self.attempt += 1
        self.guess_used()

    def start(self) -> None:
        print(self.random_number)
        while self.guesses:
            self.attempt_used()

            user_guess: int = self.get_input()

            result: int = self.check(user_guess)

            if result:
                if result < 0:
                    print("Too Low!")
                else:
                    print("Too High!")
            else:
                print("Congratulations! You guessed the correct number!")
                print(f"You guessed it in {self.attempt} attempt(s).")


def main():
    game = NumberGuessingGame()
    game.start()
    return


if __name__ == "__main__":
    main()
