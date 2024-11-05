def find_common_participants(group1, group2, n=','):
	first = set(group1.split(n))
	second = set(group2.split(n))
	common_participants = first.intersection(second)
	return sorted(common_participants)

# Пример использования с разделителем '|'
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызов функции без указания третьего аргумента, будет использован разделитель '|'
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)

# Пример использования с другим разделителем (например, запятая)
participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

# Вызов функции с указанием третьего аргумента, разделитель будет ','
print (find_common_participants(participants_first_group_comma, participants_second_group_comma, n=','))