def print_step(step, arr):
    print(f"Iterasi {step}: {arr}")

def bubble_sort(data):
    arr = data.copy()
    n = len(arr)
    print("\n--- Bubble Sort ---")
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print_step(i + 1, arr)
    return arr

def selection_sort(data):
    arr = data.copy()
    n = len(arr)
    print("\n--- Selection Sort ---")
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print_step(i + 1, arr)
    return arr

def insertion_sort(data):
    arr = data.copy()
    print("\n--- Insertion Sort ---")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print_step(i, arr)
    return arr

# Quick Sort dengan logger iterasi
def quick_sort(arr):
    print("\n--- Quick Sort ---")
    steps = [0]
    def sort(array):
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        res = sort(left) + middle + sort(right)
        steps[0] += 1
        print(f"Step {steps[0]}: {res}")
        return res
    return sort(arr)

def merge_sort(arr):
    print("\n--- Merge Sort ---")
    steps = [0]
    def sort(m_arr):
        if len(m_arr) <= 1:
            return m_arr
        mid = len(m_arr) // 2
        left = sort(m_arr[:mid])
        right = sort(m_arr[mid:])
        
        merged = sorted(left + right) # Simplified for display
        steps[0] += 1
        print(f"Merge {steps[0]}: {merged}")
        return merged
    return sort(arr)

# Main Program
def main():
    n = int(input("Masukkan jumlah data: "))
    data = []
    for i in range(n):
        val = int(input(f"Data ke-{i+1}: "))
        data.append(val)

    bubble_sort(data)
    selection_sort(data)
    insertion_sort(data)
    quick_sort(data)
    merge_sort(data)

if __name__ == "__main__":
    main()
