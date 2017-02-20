# DeepCube
Optimal Rubik's Cube Solver using neural networks

1. clone the repository.
2. Download twist.c from http://cflmath.com/Rubik/optimal_solver.html (compile with gcc -o twist.out twist.c)
3. Download optimal rubik's cube solver from http://kociemba.org/downloads/optiqtmSrc.zip (unzip and run make)
4. Ensure that twist.out and optiqtm (compiled c program) are in the same directory as your python files.
5. Run python gen-data.py making sure to change the num_cubes variable to your desired number (10 cubes takes ~20 minutes on 2015 Macbook, 1000 takes ~24 hours). This will save data to output/scrambles.json (this can and probably will be changed later and is simply an intermediate file that serves no other purpose)
6. Run python solve_cube_state.py (don't ask me about filenames, this is really hacky) making sure to change the output filenames to your desired values (currently writes to a .csv, .json, and .txt file) and let run until all cubes have been solved.
7. ???
8. Profit
