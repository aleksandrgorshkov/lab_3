def find_product_index(products, target_product):

	try:
		return products.index(target_product)
	except ValueError:
		return None


# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Товары для поиска
for find_item in ['банан', 'груша', 'персик']:
	index_item = find_product_index(items_list, find_item)  # Вызов функции для получения индекса товара
	if index_item is not None:
		print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
	else:
		print(f"Товар '{find_item}' не найден в списке.")