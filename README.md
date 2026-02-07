# Project Title
GmE 205 - Laboratory Exercise 2

# How to set up the virtual environment
1. Create a folder on your computer and open it in your IDE (e.g., VS Code)
2. Open the terminal then create the virtual environment by running the following:
    ```
    py -m venv .venv
    .\.venv\Scripts\activate
    ```
3. Press ```Ctrl + Shift + P``` in VS Code, search for *Python: Select Interpreter*, then choose the interpreter inside the ```.venv``` folder
4. Install the required packages by running the following in the terminal:
    ```
    python -m pip install --upgrade pip
    pip install pandas matplotlib
    ```
5. (Recommended) List the installed packages via:
    ```
    pip freeze > requirements.txt
    ```

# How to run Python scripts

In the terminal, ensuring that ```(.venv)``` is present in the prompt, run the following:
    ```
    python <folder/script_name.py>
    ```

# Reflections

1. Object vs Geometry

Modeling points as objects strengthened my view of them as real-world objects (or representations thereof). Validation of rules for their attributes (e.g., range of valid lat-lon values) was easier to reason about, since I was able to add the check in the initialization of each Point object. Meanwhile, if the points were treated as simple table rows, the check will constitute a simple-to-write but largely unexplained pandas query. Much is the same for setting of expected Point behaviors. Modeling these as methods under the Point class made them easier to understand, in contrast to having an unexplained procedural chain of functions and pandas/geopandas methods.

2. Responsibility

The Point class contained the per-point attributes (id, lat-lon, name, tag), the validation of lat-lon values, and the expected behaviors (construction from rows, returning lat-lon pairs as tuples, calculating distance to another Point object). The PointSet class simply contained the collection of Point objects, the ability to construct a PointSet from a CSV (from_csv()), and its own expected behaviors (count of valid points, bounding box, filtering by tag). The runner script contained the tests for Point and PointSet creation and methods, as well as the visualization and reporting. As future improvement, the PointSet class could also have a method returning a collection of a given attribute (e.g., list of lons or lats).

3. Modeling Insight

On one hand, the separation of geometry, meaning, and behavior made it easier to understand the spatial logic from a conceptual perspective. _This_ is what a `Point` is supposed to do, while _that_ is what a `PointSet` is supposed to do. On the other hand, this new way of thinking (object-oriented) tripped me up a couple times in terms of syntax, as someone more familiar with procedural and functional thinking in coding. There is room to improve and become more familiar with OOP to better harness the smoother conceptual understanding into better computational execution.