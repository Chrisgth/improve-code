# Review and refactor the Python code in the file 'CodeToImprove_start.py'.
# Make sure your code is efficient, readable, and adheres to Python's best practices.
# Include meaningful comments where necessary.
# Implement error handling strategies to ensure the code's robustness.

class MyRange:
    def __init__(self, pos_list):
        # Ensure pos_list is not empty and all elements are valid integers
        if not pos_list:
            raise ValueError('pos_list must not be empty')
        if not all(isinstance(x, int) for x in pos_list):
            raise ValueError('All elements in pos_list must be a valid integer')

        # Ensure pos_list is sorted and unique
        self.pos_list = sorted(set(pos_list))

    @property
    def ranges(self):
        # Return a list of tuples with 2 digits representing start and end of range
        ranges = list()
        start_of_range = self.pos_list[0]

        for i in range(1, len(self.pos_list)):
            current = self.pos_list[i]
            previous = self.pos_list[i - 1]

            if current != previous + 1:
                ranges.append((start_of_range, previous))
                start_of_range = current

        # Append the last range
        ranges.append((start_of_range, self.pos_list[-1]))

        return ranges

    @property
    def formatted_ranges(self):
        # Return a list of formatted strings that represent the format of '[0:1]'
        range_strings = list()
        for start, end in self.ranges:
            if start == end:
                range_strings.append(f'[{start}]')
            else:
                range_strings.append(f'[{start}:{end}]')

        prepared_string = "".join(range_strings)
        return prepared_string

    def __repr__(self):
        return f"MyRange(pos_list={self.pos_list})"


if __name__ == '__main__':
    try:
        user_list = input('Please enter a list of integers separated by a whitespace or press enter to use default:')
        default_list = [1, 2, 3, -1, 0, 8, 98, 99]

        if user_list:
            try:
                user_list = [int(i) for i in user_list.split()]
            except ValueError:
                raise ValueError('Invalid input. Please enter a list of '
                                 'integers separated by whitespace or press enter.')
        else:
            user_list = default_list

        my_range = MyRange(user_list if user_list else default_list)
        out_list = my_range.ranges
        out_formatted_string = my_range.formatted_ranges

        print('Ranges defined as tuples:', out_list)
        print('Ranges defined as formatted strings:', out_formatted_string)
    except ValueError as e:
        print(f'ValueError: {e}')
    except Exception as e:
        print(f'An exception has occurred: {e}')

