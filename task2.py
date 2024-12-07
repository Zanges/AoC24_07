from task1 import load, parse


def build_calculations(calculation):
    results = []
    for i, value in enumerate(calculation):
        if i == 0:
            results.append(int(value))
            continue
        calculation_results = []
        for result in results:
            calculation_results.append(result + int(value))
            calculation_results.append(result * int(value))
            if result == 0:
                calculation_results.append(int(value))
            else:
                calculation_results.append(int(str(result) + value))
        results = calculation_results
    return results


def main():
    file_content = load("input.txt")
    data = parse(file_content)
    correct_results = 0
    sum_correct_results = 0
    for wanted_result, calculation in data:
        results = build_calculations(calculation)
        for result in results:
            if result == int(wanted_result):
                print(f"Correct result: {wanted_result} = {calculation}")
                correct_results += 1
                sum_correct_results += int(wanted_result)
                break

    print(f"Correct results: {correct_results}")
    print(f"Sum of correct results: {sum_correct_results}")


if __name__ == "__main__":
    main()