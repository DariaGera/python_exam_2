from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUserProduct( doc_name, data_name, product_name, dataset):
    if doc_name in dataset:
        if data_name in dataset[doc_name]:
            dataset[doc_name][data_name]=product_name


    else:
        dataset[doc_name]= dict()
        dataset[doc_name][data_name] = product_name



print("Task 1")

#додавання продукту
addUserProduct('AA #12345678','11.11.2018','apple', dataset)

#додавання дати
addUserProduct('AA #12345678','10','product_name',dataset)

#додавання продукта
addUserProduct('doc_name', 'data_name', 'product_name',dataset)

print(dataset)


print("\n\n")