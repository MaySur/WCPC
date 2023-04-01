import java.io.IOException;
import java.util.Scanner;

public class problem1 {
    public static void main(String[] args) throws IOException {
        // Taking user input for total_income and reported_tax         
        Scanner sc = new Scanner(System.in);   
        int total_income = sc.nextInt();
        int reported_tax = sc.nextInt();

        int total_tax = (int) (total_income *.20);

        if (reported_tax < 0){
            System.out.println("Tax should be a non-negative integer.");
        } else if(total_tax > reported_tax){
            System.out.println("STACY HAS COMMITTED TAX FRAUD");

        } else{
            System.out.println("Stacy has not committed tax fraud");
        }
        
        
    }
}