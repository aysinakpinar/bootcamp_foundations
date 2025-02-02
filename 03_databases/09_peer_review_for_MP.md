# Peer review for Michal Podolak provided by Aysin Akpinar
# Databases - recipe_repository challenge

# ----------------------------------

# Challenge requirements:

# ----------------------------------

1. ## Use Single Table Design Recipe

-   Very well-organised design recipe. 
-   All steps, table name, columns are planned very well and listed clearly
-   Table was created with its column names and types of data and seed file name was provided to be used in the local database.

2. ## Create seeds/recipes.sql file

-   Seed file, single table with columns and information was created well-structured.
-   Seed file was provided to the local database which was then used in the program. 

3. ## Test-drive a Recipe class

    # Testing
-   Testing of the model (Recipe) was well done by testing its attributes (id, recipe_name, cooking_time and rating).
- __eq__ and __repr__ methods were also tested, which would be very useful for repository testing as well.

    # Coding

-   Code is well implemented with a good class structure with an initializer.
-   Recipe model was constructed with its attributes and __eql__ and __repr__ python methods were used to compare the instances of the class.

4. ## Test-drive RecipeRepository class - #all and #find method
    
     # Testing
-   Testing covers all of the implemented methods, getting the all recipe list and finding the relevant recipe for a given parameter.
-   Database connection was performed with a method for testing. 
-   Testing of the repository was performed for one column name. It could be tested for other columns, conditions as well.

    # Coding

-   Good implementation of testing conditions.
-   all() method returns a list of recipes while find() method returns one recipe of the required find() parameter with its name, cooking_time and rating as expected.
-   Both methods use correct syntax of sql to get the data from the database.
-   All required tests passed for both methods. 

5. ## Write a small program that lists recipes in the terminal

-   The app program imported all required classes to run DatabaseConnection and RecipeRepository
-   connection instance was provided to get the data from the database. 
-   recipe_directory database in DatabaseConnection was fed with the correct sql file to provide the data to the program.
-   for loop was utilised to get all of the recipes.

# ----------------------------------

# Code requirements:

# ----------------------------------

-   Code is working as expected and meets the expectations of listing all recipes and finding the desired recipe which was searched by a parameter.
-   Code doesn't cause any side-effects.


1. ## Readability and accessibility

-   It it easy to grasp the intention of the code. Code has a very good logical structure.
-   The logic of the code was implemented concisely, no need for improvement.
-   The design document shows the sql code structure and table design very clearly.

2. ## Code structure

-   The functions(methods) and classes were organised logically.
    -   Recipe class has the constructor, __eql__ and __repr__ methods to create the Recipe model and also modify it for the subsequent testing and integration with RecipeRepository class.
    -   RecipeRepository class connects to the database and uses all() and find() methods as expected. 
-   It was easy to navigate between the files to follow the code.

3. ## Testing

- Tests cover all main paths, both unit and integration tests were used as expected. 
- Some edge cases could be covered like searching every column in the table, as the search parameter changes, the data type changes and this could cause some side effects. 

4. ## Final conclusion

-   The code is well designed, tested and implemented.
-   It was easy to follow the code and its tests.
-   All Classes were costructed logically and required methods were implemented to meet the code expectations.
-   Database connection was provided in both code and tests.
-   SQL syntax was used appropriately with a well-structured dsign.
-   Only improvement needed for the code and its subsequent testing is to be able to use the find method in the RecipeRepository more versatile, to look for any parameter in all of the columns of the table.


