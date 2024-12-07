def load(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def parse(file_content):
    lines = file_content.split("\n")
    data = []
    for line in lines:
        data.append(parse_line(line))
    return data


def parse_line(line):
    result, calculation = line.split(": ")
    calculation = calculation.split(" ")
    return result, calculation


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