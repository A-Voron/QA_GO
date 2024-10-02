input_string = "3913:10239,5417:14257,8237:21509,8687:22621,9487:24609,9650:25066,9991:25921,10078:26135,10080:26136,10124:24336,10340:26754,10369:24020,10409:26922,10516:27142,10535:27192,10545:27223,10622:27393,10665:27503,10721:27627,10744:27689,10746:27693,10864:27952,10865:27954,11118:28550,11124:28562,11195:27414,11211:28872,11244:28944,11247:28952,11302:29097,11381:27678,11404:29359,11405:29361,11499:29713,11567:29882,11631:30033,11640:30055,11667:30118,11682:30146,11734:30282,11807:30580,11891:30924,11924:30931,11944:31027,11974:31135,12048:31449,12050:31452,12139:28940,12142:31661,12432:32274,12520:32415,12639:32727,12647:32750,12677:32839,12686:32862,12784:33124,12862:33261,12875:33288,12881:33305,12893:33334,12895:33338"

# Разделяем строку на части по двоеточию
parts = input_string.split(',')

# Создаем списки чисел
numbers_before = []
numbers_after = []

for part in parts:
    if ':' in part:
        num_before, num_after = part.split(':')
        numbers_before.append(num_before.strip())
        numbers_after.append(num_after.strip())
    else:
        print(f"Необработанное значение: {part}")

# Удаляем пустые элементы
numbers_before = [num for num in numbers_before if num]
numbers_after = [num for num in numbers_after if num]

# Сортируем числа
numbers_before.sort(key=int)
numbers_after.sort(key=int)

# Формируем итоговые строки
before_str = '|'.join(numbers_before)
count_before_str = len(before_str.split('|'))
after_str = '|'.join(numbers_after)
count_after_str = len(after_str.split('|'))

print(f"Экспов-{count_before_str}: {before_str}")
print("-----")
print(f"Варианты-{count_after_str}: {after_str}")

