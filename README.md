#  #19. Stacy commits Tax Fraud

## Background
* Stacy is suspected of committing tax fraud and the IRS (Internal Revenue Service) wants to investigate her. Your task is to write a program that calculates the total tax amount Stacy should have paid based on her income. The program will take two inputs the total income and the amount of tax she paid and compare it to amount she actually should have paid. If the difference between the two amounts are not equal the program needs to output a message.

***

## Description
* Given two integers (both integers), the first integer is Stacy's total income which is always bigger then 0 and the second integer amount of tax she paid. To find the amount of tax that Stacy should have paid use the below formula:

```
total_tax = (total_Income * 0.20)
```
* Compare the total_tax by the amount that Stacy reported she paid.

* If the total_tax is bigger than the amount of tax Stacy inputted then the program should output the string: 'STACY HAS COMMITTED TAX FRAUD'.

* If the total_tax is less or equal to the amount of tax Stacy inputted then the program will output the string 'Stacy has not committed tax fraud'. If the reported_tax is a negative number the program should output the string: 'Invalid input. Input should be a non-negative integer.'
***

## Input
Enter two integers:

* The first integer, total_income, should be a positive value greater than zero. This will represent the total income.

* The second integer, reported_tax, should be a value representing the reported tax amount.

## Output

* There will be a single string outputed. Either the string STACY HAS COMMITTED TAX FRAUD Or Stacy has not committed tax fraud Or Invalid input. Input should be a non-negative integer.
***

## Sample Inputs:
### Sample Input 1:
```
5000
1000
```

### Sample Output 1:
```
Stacy has not committed tax fraud
```

### Sample Input 2:
```
5000
500
```

### Sample Output 2:
```
STACY HAS COMMITTED TAX FRAUD
```

### Sample Input 3:
```
50000
-2000
```

### Sample Output 3:
```
Invalid input. Tax should be a non-negative integer.
```
***
## Code Template
Example Java Program for reading input.

```
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        // Taking user input for total_income and reported_tax         
        Scanner sc = new Scanner(System.in);   
        System.out.print("Income: ");        
        int total_income = sc.nextInt()
        System.out.print("Tax: ");         
        int reported_tax = sc.nextInt();       
        
    }
}

```
Example Python Program for reading input.

```
total_income = input('Total Income: ')
reported_tax = input('Tax: ')
```
