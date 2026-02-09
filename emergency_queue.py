class Patient:
    def __init__(self, name: str, urgency: int):
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    def _parent_index(self, i):
        return (i - 1) // 2

    def _left_index(self, i):
        return 2 * i + 1

    def _right_index(self, i):
        return 2 * i + 2

    def heapify_up(self, index) -> None:
        while index > 0:
            parent = self._parent_index(index)
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index) -> None:
        n = len(self.data)
        while True:
            left = self._left_index(index)
            right = self._right_index(index)
            smallest = index

            if left < n and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < n and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def insert(self, patient: Patient) -> None:
        # (optional) basic validation
        if not isinstance(patient, Patient):
            raise TypeError("insert() expects a Patient object")
        if not isinstance(patient.urgency, int) or not (1 <= patient.urgency <= 10):
            raise ValueError("urgency must be an int from 1 to 10")

        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root

    def print_heap(self) -> None:
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")


# -------------------- Tests --------------------
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    next_up = heap.peek()
    print("Peek:", next_up.name, next_up.urgency)  # Taylor 1

    served = heap.remove_min()
    print("Served:", served.name)  # Taylor
    heap.print_heap()

    # Edge cases
    empty = MinHeap()
    assert empty.peek() is None
    assert empty.remove_min() is None

    one = MinHeap()
    one.insert(Patient("Solo", 2))
    assert one.peek().name == "Solo"
    assert one.remove_min().name == "Solo"
    assert one.remove_min() is None

    # Validation tests (uncomment to see errors)
    # heap.insert("not a patient")
    # heap.insert(Patient("BadUrgency", 99))

