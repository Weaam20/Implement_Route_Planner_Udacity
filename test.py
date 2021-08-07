from helpers import load_map,show_map

MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]

def test(shortest_path_function):
    paths = []
    map_40 = load_map('map-40.pickle')
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal)
        if path == answer_path:
            correct += 1
            paths.append((start,goal,answer_path))
        else:
            print("For start:", start, 
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
        for i in range(len(paths)):
            print("Solution map ",i+1," : " )
            show_map(map_40, start=paths[i][0], goal=paths[i][1], path=paths[i][-1])
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")
    