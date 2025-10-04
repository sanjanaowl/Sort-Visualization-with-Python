import pygame
import random
import time


def main():
    unordered_list = [random.randint(10, 100) for i in range(1, 60)]
    # initializing pygame
    pygame.init()
    global screen
    global clock
    screen = pygame.display.set_mode((1000, 700))
    clock = pygame.time.Clock()

    drawing_merge_sort(unordered_list)
    pygame.quit()


def drawing_list(number_list, isDone):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((198, 166, 252))
        count = 0
        for i in number_list:
            pygame.draw.rect(screen, (13, 0, 47), (150 + count * 12, 300 - i, 10, i))
            count += 1
        pygame.display.flip()
        clock.tick(60)
        time.sleep(0.01)
        if isDone == False:
            running = False


def drawing_bubble_sort(number_list):
    while True:
        counter = 0
        for i in range(len(number_list)):
            if i != len(number_list) - 1:
                if number_list[i] > number_list[i + 1]:
                    number_list[i], number_list[i + 1] = (
                        number_list[i + 1],
                        number_list[i],
                    )
                    drawing_list(number_list, False)
                    counter += 1

        if counter < 1:
            drawing_list(number_list, True)
            return number_list


def drawing_selection_sort(number_list):
    for i in range(len(number_list)):
        min_number = i
        for j in range(i, len(number_list)):
            if number_list[j] < number_list[min_number]:
                min_number = j
            drawing_list(number_list, False)
        number_list[i], number_list[min_number] = (
            number_list[min_number],
            number_list[i],
        )
        drawing_list(number_list, False)
    drawing_list(number_list, True)


def drawing_insertion_sort(number_list):
    for i in range(len(number_list)):
        position = i
        while number_list[position] < number_list[position - 1] and position - 1 >= 0:
            number_list[position], number_list[position - 1] = (
                number_list[position - 1],
                number_list[position],
            )
            position = position - 1
            drawing_list(number_list, False)

    drawing_list(number_list, True)


def drawing_quick_sort(number_list):
    def get_pivot(pivot_list, low_p, high_p):
        i = low_p + 1
        j = high_p
        p = low_p
        while j > i:
            while i < high_p and pivot_list[i] <= pivot_list[p]:
                i = i + 1
            while j > low_p and pivot_list[j] > pivot_list[p]:
                j = j - 1
            if j > i:
                pivot_list[j], pivot_list[i] = pivot_list[i], pivot_list[j]
                drawing_list(pivot_list, False)
        if pivot_list[j] < pivot_list[p]:
            pivot_list[p], pivot_list[j] = pivot_list[j], pivot_list[p]
            drawing_list(pivot_list, False)
        return j

    def quick_sorting(quick_list, low, high):
        if low < high:
            pivot_index = get_pivot(quick_list, low, high)
            quick_sorting(quick_list, low, pivot_index - 1)
            quick_sorting(quick_list, pivot_index + 1, high)
        return quick_list

    sorted_list = quick_sorting(number_list, 0, len(number_list) - 1)
    drawing_list(sorted_list, True)


def drawing_merge_sort(number_list):

    def merge_sort(m_list):
        if len(m_list) > 1:
            left = m_list[: len(m_list) // 2]
            right = m_list[len(m_list) // 2 :]
            merge_sort(left)
            merge_sort(right)
            drawing_list(left, False)
            drawing_list(right, False)
            drawing_list(m_list, False)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    m_list[k] = left[i]
                    i += 1
                else:
                    m_list[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                m_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                m_list[k] = right[j]
                j += 1
                k += 1
        return m_list

    drawing_list(number_list, False)
    sorted_list = merge_sort(number_list)
    drawing_list(sorted_list, True)


if __name__ == "__main__":
    main()
