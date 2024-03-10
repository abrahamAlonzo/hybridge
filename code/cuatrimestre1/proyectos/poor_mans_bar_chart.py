
def intro():
    print("Introduce una palabra: ")
    palabra = input()
    return palabra

def count_frecuency(palabra):
    frecuency = {}
    for letter in palabra:
        if letter in frecuency:
            frecuency[letter] += 1
        else:
            frecuency[letter] = 1

    sorted_frecuency = sort_frecuency_by_letter(frecuency)
    return sorted_frecuency

def print_bars_using_chart_data(chart_data):
    for letter, count in chart_data:
        print(letter + " " + "|" + count * "*")
    
    

def sort_frecuency_by_letter(frecuency):
    return sorted(frecuency.items(), key=lambda x: x[0])

def main():
    palabra = intro()
    chart_data = count_frecuency(palabra)
    print_bars_using_chart_data(chart_data)
if __name__ == "__main__":
    main()