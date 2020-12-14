class Sorting:
    def bubble_sort_asc(l):
        for i in range(len(l) - 1, 0, -1):
            for j in range(i):
                if l[j] > l[j + 1]:
                    temp = l[j]
                    l[j] = l[j + 1]
                    l[j + 1] = temp
        return l

    def bubble_sort_dsc(l):
        for i in range(len(l) - 1, 0, -1):
            for j in range(i):
                if l[j] < l[j + 1]:
                    temp = l[j]
                    l[j] = l[j + 1]
                    l[j + 1] = temp
        return l

    def selection_sort_asc(l):
        for i in range(len(l)):
            min_index = i
            for j in range(i+1, len(l)):
                if l[min_index] > l[j]:
                    min_index = j
                l[i], l[min_index] = l[min_index], l[i]
        return l

    def selection_sort_dsc(l):
        for i in range(len(l)):
            min_index = i
            for j in range(i+1, len(l)):
                if l[min_index] < l[j]:
                    min_index = j
                l[i], l[min_index] = l[min_index], l[i]
        return l

    def insertion_sort_asc(l):
        n = len(l)
        for i in range(1, n):
            key = l[i]
            j = i-1
            while j >= 0 and l[j] > key:
                l[j+1] = l[j]
                j = j-1
                l[j + 1] = key
        return l

    def insertion_sort_dsc(l):
        n = len(l)
        for i in range(1, n):
            key = l[i]
            j = i-1
            while j >= 0 and l[j] < key:
                l[j+1] = l[j]
                j = j-1
                l[j + 1] = key
        return l

l = [4,4,3,2,5,1,5,1,0]
print("Sortowanie bąbelkowe rosnąco: ")
print(Sorting.bubble_sort_asc(l))
print("Sortowanie bąbelkowe malejąco: ")
print(Sorting.bubble_sort_dsc(l))
print("---")
print("Sortowanie przez wybieranie rosnąco: ")
print(Sorting.selection_sort_asc(l))
print("Sortowanie przez wybieranie malejąco: ")
print(Sorting.selection_sort_dsc(l))
print("---")
print("Sortowanie przez wstawianie rosnąco: ")
print(Sorting.insertion_sort_asc(l))
print("Sortowanie przez wybieranie malejąco: ")
print(Sorting.insertion_sort_dsc(l))

