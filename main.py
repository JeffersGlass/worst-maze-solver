from mazeio import load_maze, display_solved_maze
from solvemaze import export_maze, export_path, solve_maze, import_maze, import_path

#The filename and extension for the maze file
maze_name = 'worstmaze'
extension = 'jpg'

maze_file = f'{maze_name}_solved.pickle'
path_file = f'{maze_name}_path_solved.json'


try: # Used catched maze solution if it exists
    result = import_maze(maze_file)
    path = [tuple(t) for t in import_path(path_file)]
except FileNotFoundError as err:
    print(err)
    print("Solution or path not found, solving maze fresh")

    my_maze = load_maze(f'{maze_name}.{extension}', (0,0), (1000, 1000))
    result, path = solve_maze(my_maze)

    # Save solution for next time to speed up printing
    export_maze(result, maze_file)
    export_path(path, path_file)
else:
    print("Solution and path found, using solution from file")

display_solved_maze(result, path, hue_speed = 2)