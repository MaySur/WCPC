#  #21. Pattern Triangles

## Background
* Write a program that takes an integer n as a input and prints out a two right triangle that mirrors each other (shown below) made of asterisks * with 2n-1 rows.

* The top half of the figure should have n rows, increasing in the amount of asterisks from 1 asterisk to n asterisks, and the bottom half should have n-1 rows, decreasing in the amount of asterisks from n-1 asterisks to 1 asterisk.
***

## Description
* One input, n, is the size of the figure with 2n-1 rows. For example if n = 6, then the figure will have 11 rows (2(6)-1).

* The top half of the figure will have a loop that outputs asterisks which ranges from 1 to n making a right triangle.

* The bottom half of the figure will also have a loop that outputs asterisks which ranges from n-1 to 1 to make a mirrored right triangle.

* The input, n, is always positive and is an integer


***

## Input
* One positive integer, n that is bigger than 1.



## Output

* A figure made up of asterisks with size n. Be sure to check for any unnecessary blank lines or spaces.
***

## Sample Inputs:
### Sample Input 1:
```
2
```

### Sample Output 1:
```
*
**
*
```

### Sample Input 2:
```
5
```

### Sample Output 2:
```
*
**
***
****
*****
****
***
**
*
```

### Sample Input 3:
```
10
```

### Sample Output 3:
```
*
**
***
****
*****
******
*******
********
*********
**********
*********
********
*******
******
*****
****
***
**
*
```
***
## Code Template
Example Java Program for reading input.

```
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        // Taking user input for n
        Scanner sc = new Scanner(System.in);                                
        int n = sc.nextInt();
// Enter your code below this line
        
        
    }
}


```
Example Python Program for reading input.

```
n = int(input())

# Enter your code below this line

```
