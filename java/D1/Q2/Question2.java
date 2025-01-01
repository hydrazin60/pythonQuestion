package java.D1.Q2;

import java.util.Scanner;

public class Question2 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to check prime number or Not : ");
        int number = sc.nextInt();
        boolean isprime = true;
        for (int i = 2; i <= 9; i++) {
            if (number % i == 0 && number != i) {
                isprime = false;
            }
        }
        if (number <= 1) {
            isprime = false;
        }
        if (isprime) {
            System.out.println("Given Number" + number + " is prime");
        } else {
            System.out.println("Given Number is " + number + "is not prime");
        }
    }
}
