### Exercise 3 - Run Timing ###

def run_timing():
    runs = 0
    total_time = 0.0

    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:
            break

        runs = runs + 1
        total_time = total_time + float(one_run)

    print(f'Average of {total_time / runs}, over {runs} runs')

if __name__ == "__main__":
    run_timing()