#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    print('Hashtable', ht)

    for i in range(length):
        weight_in = weights[i]
        checked = hash_table_retrieve(ht, limit - weight_in)
        if checked is not None:
            results = (i, checked)
            return results
        else:
            hash_table_insert(ht, weight_in, i)
    print({"Weights": weights, "Length": length, 'Limit': limit})

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
