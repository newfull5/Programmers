#2021.07.09
def solution(places):    
    def up_search(arg):

        if type(arg) != list:
            return

        current_r, current_c, visited = arg
        current_r -= 1

        if current_r == -1:
            return

        if place[current_r][current_c] == 'P':
            if 'X' not in visited:
                return False

        return [current_r, current_c, visited+[place[current_r][current_c]]]

    def right_search(arg):

        if type(arg) != list:
            return

        current_r, current_c, visited = arg
        current_c += 1

        if current_c == 5:
            return

        if place[current_r][current_c] == 'P':
            if 'X' not in visited:
                return False

        return [current_r, current_c, visited+[place[current_r][current_c]]]

    def left_search(arg):

        if type(arg) != list:
            return

        current_r, current_c, visited = arg
        current_c -= 1

        if current_c == -1:
            return

        if place[current_r][current_c] == 'P':
            if 'X' not in visited:
                return False

        return [current_r, current_c, visited+[place[current_r][current_c]]]

    def down_search(arg):

        if type(arg) != list:
            return

        current_r, current_c, visited = arg
        current_r += 1

        if current_r == 5:
            return

        if place[current_r][current_c] == 'P':
            if 'X' not in visited:
                return False

        return [current_r, current_c, visited+[place[current_r][current_c]]]

    def find(current_r, current_c):
        arg = [current_r, current_c, []]

        return False not in [up_search(arg),
        up_search(up_search(arg)),
        up_search(left_search(arg)),
        up_search(right_search(arg)),

        left_search(arg),
        left_search(left_search(arg)),
        left_search(up_search(arg)),
        left_search(down_search(arg)),

        right_search(arg),
        right_search(right_search(arg)),
        right_search(up_search(arg)),
        right_search(down_search(arg)),

        down_search(arg),
        down_search(down_search(arg)),
        down_search(left_search(arg)),
        down_search(right_search(arg))]
    answer = []
    
    for num in range(5):
        place = places[num]

        lists = ([find(i,j) for i in range(5) for j in range(5) if place[i][j] == 'P'])
        
        if not lists or False not in lists:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer
